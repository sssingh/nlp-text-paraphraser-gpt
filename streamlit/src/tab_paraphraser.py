"""About tab rendering functionality"""

from config import app_config
import data
import requests
import streamlit as st


###
### INTERNAL FUNCTIONS
###
def __paraphrase(text):
    ### Invoke the lambda function via REST api call to paraphrase the text
    url = st.secrets["API_ENDPOINT"]
    headers = {"Content-Type": "application/json"}
    payload = {"text": text}
    response = requests.request(method="POST", url=url, headers=headers, json=payload)
    response = response.json()
    paraphrased_text = response["paraphrased_text"]
    return paraphrased_text


def __refresh_access_cnt_stats(curr_count, access_stats):
    access_cnt_stats = f"""
    |Maximum allowed requests|Requests made so far|Requests available|
    |:---: |:---: |:---:|
    |{app_config.max_access_count}|{curr_count}|{app_config.max_access_count - curr_count}
    """
    access_stats.empty()
    access_stats.container().markdown(access_cnt_stats)


###
### MAIN FLOW, entry point
###
def render():
    ### show the current and available number of requests
    st.success(
        "Due to cost constraints the total number of paraphrasing requests are "
        + "restricted, as shown below..."
    )
    access_stats = st.empty()
    access_counter = data.get_access_counter()
    curr_count = access_counter["current-count"]
    __refresh_access_cnt_stats(curr_count, access_stats)
    st.divider()

    ### if maximum number of requests are exhausted then throw and error and abort
    if curr_count >= app_config.max_access_count:
        st.error(
            "SORRY! the maximum number of allowed requests are exhausted, please ping me via "
            + "`Contact Me` section in `About` tab if you see this message."
        )
    else:
        ### render the UI
        output_text = "Paraphrased text will appear here"
        input_text = st.text_area(
            "Input Text:",
            placeholder="Enter the text you want to paraphrase",
            help="Maximum of 100 words are allowed",
            height=250,
        )
        with st.expander("Important Note...", expanded=True):
            st.warning(
                "***Please note that when you try first time, app may return an "
                + "`Internal Error`, this is expected and is due to the AWS hosted hardware"
                + " taking some time to warm-up first time. After couple of trials you "
                + "should be able to see the results.***",
                icon=app_config.icon_important,
            )

        if st.button("Paraphrase ✒️"):
            ## if max word length breached throw and error
            if len(input_text.split(" ")) > 100:
                st.error(
                    "In this demo app, a maximum of 100 words are allowed in input text, "
                    + "please reduce the text length and try again",
                    icon=app_config.icon_stop,
                )
            ## all good, proceed to process now
            else:
                with st.spinner("Processing..."):
                    output_text = __paraphrase(input_text)

                    # update the access-count in DB and refresh the stats display
                    curr_count = data.update_access_count()
                    __refresh_access_cnt_stats(curr_count, access_stats)
                    # show the original and paraphrased text
                    st.divider()
                    st.subheader("Original Text")
                    st.write(input_text)
                    st.subheader("Paraphrased Text")
                    st.write(output_text)
                    st.divider()
