#!/usr/bin/env python3
""" Update School """
import pymongo
from typing import List

def update_topics(mango_collection, name, topics):
    """changes school topics"""
    mango_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )