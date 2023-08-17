"""About tab rendering functionality"""

from config import app_config
import utils
import streamlit as st


###
### INTERNAL FUNCTIONS
###


###
### MAIN FLOW, entry point
###
def render():
    """Render the this page"""
    st.markdown(utils.read(app_config.md_about), unsafe_allow_html=True)
