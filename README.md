---
title: Nlp Text Paraphraser Gpt
emoji: 📝
colorFrom: pink
colorTo: red
sdk: streamlit
sdk_version: 1.27.1
app_file: streamlit/src/app.py
pinned: false
license: mit
---

<a href="https://huggingface.co/spaces/sssingh/nlp-text-paraphraser-gpt"  target="_blank"><img src="https://img.shields.io/badge/click_here_to_open_streamlit_app-f63366?style=for-the-badge&logo=streamlit&logoColor=black" /></a>

<img src="https://github.com/sssingh/nlp-text-paraphraser-gpt/blob/main/streamlit/assets/title.png?raw=true" width="1000" height="350"/><br><br> 

# Introduction  
***This App demonstrates the `text paraphrasing` NLP functionality.***
>Although this app focuses on `text-paraphrasing`, the design philosophy and architecture used in this app can easily be extended to include other NLP functionalities such as 'FAQ Generation from a text context', 'Question Answering', 'Document Summarization', 'Language Translation', and so on.

# App Details
The app contains two tabs: "ABOUT" and "TEXT PARAPHRASER". 

## ABOUT 
This page, describes the app usage and architecture
    
## TEXT PARAPHRASER
Input a text paragraph in the provided text-area and then click the 'Paraphrase' button. The app will analyse the input text and generate a 'paraphrased' version of the input text paragraph while keeping the sense of the paragraph unaltered. Below is an example of input and output... 

#### Input
<img src="https://github.com/sssingh/nlp-text-paraphraser-gpt/blob/main/streamlit/assets/input-texts.png?raw=true" width="1000" height="700"/><br>

#### Output
<img src="https://github.com/sssingh/nlp-text-paraphraser-gpt/blob/main/streamlit/assets/result-text.png?raw=true" width="1000" height="500"/><br>

* Please keep in mind that this sample demo app is hosted utilizing the free tiers of'streamlit community cloud' and 'Amazon Web Services,' making it useable but somewhat lacking in speed and quality of paraphrasing. 
* Due to cost and resource limits, the App currently only supports a maximum of 100 words per paraphrase request.
* Please also keep in mind that while using it for the first time or after a lengthy interval (more than 1 hour), the app may throw an "Internal Error" message. This is to be expected, as the free tier of AWS services is configured for 'cold-start,' and it may take a few minutes to warm up before serving the request. Having said that the performance appears to be fairly satisfactory for demo and testing purposes; but, if we had dedicated premium AWS resources provisioned, there will be no wait..

## Technical details

### App Architecture:

<img src="https://github.com/sssingh/nlp-text-paraphraser-gpt/blob/main/streamlit/assets/architecture.png?raw=true"/><br>

The app has three main components:
1. **Streamlit cloud hosted UI**: 
* The user enters the text to be paraphrased and initiates the paraphrasing request. 
* Before beginning to handle the request, the App conducts the following validations:
  * Verifies that the maximum number of authorized requests has not been reached. Because each request to OpenAI costs tokens (i.e. money), I have limited the usage to reduce the cost incurred.
  * if the aforementioned check passes, it checks to see whether the amount of words in the input text is fewer than the set limit (now 100). If both checks pass, the App proceeds to the next step; otherwise, the app displays an error message and aborts.  
* For data durability, the app additionally connects to a 'MongoDB' database housed on a `MongoDB Atlas` cluster. At the moment, the only data that is saved/updated is the number of queries made via the app. It should be noted that the capability of the same DB connection app may be easily expanded to: 
  * Store/manage user sign up/sign
  * Store user data such as the original text and then matching paraphrased text, etc. 
2. **AWS hosted API Gateway & Lambda Function**: 
* 'API Gateway' accepts the REST Request from the app and forwards it to the 'Lambda' function for processing. 
* The Lambda function extracts and prepares the data before launching a 'REST API Request' to 'OpenAI'. When a response from OpenAI is received, it is formatted and sent to the App through AWS API Gateway. 
3. **GPT-3 LLM Hosted by OpenAI**: 
* 'OpenAI API' takes requests from Lambda functions, talks with 'GPT-3.5' to complete the request, and sends the results to Lambda. 
* The app is set up to utilize the 'text-davinci-003' LLM. This may easily be changed to utilize any other more powerful LLM for better results, but the charges to be paid to OpenAI will most likely increase proportionally. 

# Project Source
[👉 Visit GitHub Repo](https://github.com/sssingh/nlp-text-paraphraser-gpt)

# Contact Me
[![email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sunil@sunilssingh.me)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/@thesssingh)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sssingh/)
[![website](https://img.shields.io/badge/web_site-8B5BE8?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sunilssingh.me)

