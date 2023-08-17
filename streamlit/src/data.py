"""All app-specific data and disk-IO related functionality implemented here"""

import pymongo
import streamlit as st


@st.cache_resource
def __get_db():
    """Connect to MongoDB Atlas instances"""
    client = pymongo.MongoClient(st.secrets["MONGO_CONN_STR"])
    return client


def get_access_counter():
    client = __get_db()
    """Get the current access count from the database"""
    access_counter = client["mydb"]["access-counter"].find_one()
    return access_counter


def update_access_count():
    """Update the current access count by 1 in the database"""
    client = __get_db()
    access_counter = get_access_counter()
    updated_count = access_counter["current-count"] + 1
    client["mydb"]["access-counter"].update_one(
        {"_id": access_counter["_id"]},
        {"$set": {"current-count": updated_count}},
    )
    return updated_count
