#!/usr/bin/env python3
""" List documents """
import pymongo

def list_all(mongo_collection):
    """lists all documents in MongoDB"""
    documents = []
    for doc in mongo_collection.find():
        documents.append(doc)
        return documents
