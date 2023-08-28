"""All app-specific user defined configurations are defined here"""

import os
from dataclasses import dataclass

# import plotly.express as px


### define all plotting configuration here,
### should not be accessed and changed directly hence leading "__"
@dataclass
class __PlotConfig:
    """All plotting configurations are defined here"""

    # Available themes (templates):
    # ['ggplot2', 'seaborn', 'simple_white', 'plotly',
    #  'plotly_white', 'plotly_dark', 'presentation',
    #  'xgridoff', 'ygridoff', 'gridon', 'none']
    # theme = "plotly_dark"
    # cat_color_map = px.colors.qualitative.T10
    # cat_color_map_r = px.colors.qualitative.T10_r
    # cont_color_map = px.colors.sequential.amp
    # cont_color_map_r = px.colors.sequential.amp_r


### define all app-wide configuration here,
### should not be accessed and changed directly hence leading "__"
@dataclass
class __AppConfig:
    """app-wide configurations"""

    # get current working directory
    cwd = os.getcwd()
    banner_image = f"{cwd}/"
    logo_image = f"{cwd}/streamlit/assets/logo.png"
    app_title = "Text Paraphraser"
    app_icon = f"{cwd}/streamlit/assets/st_title.png"
    app_short_desc = "🤖 AI powered paraphraser"
    md_about = f"{cwd}/streamlit//artifacts/about.md"
    max_access_count = 50
    # processed_data = f"{cwd}/artifacts/"
    # model_weights = f"{cwd}/artifacts/"
    # s3_model_file_uri = ""
    # s3_data_file_uri = ""
    sidebar_state = "expanded"  # collapsed
    layout = "centered"  # wide
    icon_question = "❓"
    icon_important = "🎯"
    icon_info = "ℹ️"
    icon_stop = "⛔"
    icon_about = "👋"


### make configs available to any module that imports this module
app_config = __AppConfig()
