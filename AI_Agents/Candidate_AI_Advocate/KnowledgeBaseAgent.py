# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:59:27 2024

@author: zefin

Knowledge Base Agent

This agent retrieves relevant data from Pinecone based on the query.
"""
from langchain.embeddings import OpenAIEmbeddings

class KnowledgeBaseAgent:
    def __init__(self):
        self.index = index

    def retrieve_relevant_info(self, query):
        vector = OpenAIEmbeddings().embed_query(query)
        results = self.index.query(vector, top_k=5, include_metadata=True)
        return [result['metadata'] for result in results['matches']]


