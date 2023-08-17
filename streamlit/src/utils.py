"""App agnostic reusable utility functionality"""

from config import app_config
import streamlit as st
import s3fs


def setup_app(config):
    """Sets up all application icon, banner, title"""
    st.set_page_config(
        page_title=config.app_title,
        page_icon=app_config.app_icon,
        initial_sidebar_state=config.sidebar_state,
        layout=config.layout,
    )
    ### Logo and App title, description
    with st.container():
        app_icon_title, title, logo = st.columns([0.4, 0.6, 0.3])
        app_icon_title.image(image=app_config.app_icon, width=200)
        title.markdown(
            f"<h1 style='text-align: left; color: #03989e;'>{app_config.app_title}</h1> ",
            unsafe_allow_html=True,
        )
        title.markdown(
            f"<p style='text-align: left;'>{app_config.app_short_desc}</p>",
            unsafe_allow_html=True,
        )
        logo.image(image=app_config.logo_image)
        # st.divider()


def create_tabs(tabs):
    """Creates streamlit tabs"""
    return st.tabs(tabs)


def download_file(btn_label, data, file_name, mime_type):
    """Creates a download button for data download"""
    st.download_button(label=btn_label, data=data, file_name=file_name, mime=mime_type)


def get_class_from_name(module: str, class_name: str):
    """Instantiates and return the class given the class name and its module as str"""
    return getattr(module, class_name)


# def make_prediction(model, input_data, proba=False):
#     """
#     prediction pipeline for the model, model must have predict method and predict_proba
#     method if prediction probabilities to be returned
#     """
#     ### preprocess the input and return it in a shape suitable for this model
#     processed_input_data = data.preprocess_pred_data(input_data)
#     ### call model's predict method
#     pred = model.predict(processed_input_data)
#     ### call model's predict_proba method if required
#     pred_proba = []
#     if proba:
#         pred_proba = model.predict_proba(processed_input_data)
#     return pred, pred_proba.squeeze()


def download_from_s3(source_s3_uri, target_file):
    """connect to S3 and download file"""
    with st.spinner(
        f"Downloading trained model it may take few minutes, please be patient..."
    ):
        fs = s3fs.S3FileSystem(
            key=st.secrets["AWS_ACCESS_KEY"], secret=st.secrets["AWS_ACCESS_SECRET"]
        )
        fs.download(source_s3_uri, target_file)


def read(file) -> str:
    """read the text file and return the contents"""
    with open(file, "r") as f:
        text = f.read()
    return text
