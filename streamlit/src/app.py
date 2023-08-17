"""Application entry point, global configuration, application structure"""

from config import app_config
import utils
import tab_about
import tab_paraphraser
import streamlit as st
import os


def init():
    """setup app-wide configuration and download data only once"""
    utils.setup_app(app_config)

    ### Download model/data

    ### setup app tab structure
    about, paraphraser = utils.create_tabs(["ABOUT 👋", "TEXT PARAPHRASER ✒️"])
    with about:
        tab_about.render()
    with paraphraser:
        tab_paraphraser.render()


### Application entry point
if __name__ == "__main__":
    init()
