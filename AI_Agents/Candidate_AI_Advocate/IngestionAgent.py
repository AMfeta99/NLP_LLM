# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:58:37 2024

@author: zefin

Ingestion Agent
This agent gathers data from LinkedIn, GitHub, and CVs. It embeds the data using 
OpenAI embeddings and stores it in Pinecone.


"""

from langchain.embeddings import OpenAIEmbeddings
import pinecone

# Initialize Pinecone
pinecone.init(api_key="your_pinecone_api_key", environment="us-west1-gcp")
index = pinecone.Index("candidate-advocate")

class IngestionAgent:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings()

    def embed_and_store(self, data, source):
        for item in data:
            text = f"{item['name']} - {item.get('description', '')}"
            vector = self.embeddings.embed_query(text)
            index.upsert([(f"{source}-{item['name']}", vector, {"source": source})])

    def ingest_data(self, github_data, linkedin_data):
        self.embed_and_store(github_data, "GitHub")
        self.embed_and_store(linkedin_data, "LinkedIn")
        return "Data ingested successfully."
