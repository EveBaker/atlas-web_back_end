#!/usr/bin/env python3
""" Insert document """
import pymongo

def insert_school(mongo_collection, **kwargs):
    """Inserts new doc into collection"""
    school = mongo_collection.insert_one(kwargs)
    return school.inserted_id