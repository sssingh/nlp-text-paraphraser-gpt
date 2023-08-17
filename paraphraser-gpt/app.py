import os
import json
import requests
import spacy
import concurrent.futures

gpt3_url = "https://api.openai.com/v1/completions"
gpt3_api_key = os.environ["OPENAI_KEY"]
gpt3_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {gpt3_api_key}",
}


def paraphrase(sent):
    gpt3_payload = {
        "model": "text-davinci-003",
        "prompt": "Following is an original sentence followed by paraphrased version "
        + "of it with diverse choice of words:\n\noriginal: Once upon a time a group of "
        + "rats in forest were searching for water\n\nparaphrase: long ago in a jungle "
        + "a pack of rats were thirsty looking for drinking water\n###\noriginal: "
        + "{0}\nparaphrase:".format(sent),
        "max_tokens": 256,
        "temperature": 0.85,
        "top_p": 1,
        "frequency_penalty": 0.72,
        "presence_penalty": 0.72,
        "stop": ["###"],
    }

    response = requests.request(
        method="POST", url=gpt3_url, headers=gpt3_headers, json=gpt3_payload
    )
    response = response.json()
    paraphrase_sent = response["choices"][0]["text"]
    return paraphrase_sent.strip()


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    raw_text = r"{0}".format(event["body"])
    json_payload = json.loads(raw_text)
    input_text = json_payload["text"]
    ### break text into sentences
    nlp = spacy.load(
        "en_core_web_sm", disable=["ner", "tagger", "lemmatizer", "textcat"]
    )
    sentences = nlp(input_text).sents
    ### get each sentence paraphrased, use concurrency for speed
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(paraphrase, sent.text.strip())
            for sent in sentences
            if sent.text.strip() != ""
        ]
    paraphrased_sentences = [future.result() for future in futures]
    output = {"paraphrased_text": " ".join(paraphrased_sentences)}
    ### join the paraphrased sentences and return as full paraphrased text
    return {
        "statusCode": 200,
        "body": json.dumps(output),
    }
