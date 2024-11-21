# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:00:39 2024

@author: zefin


Q&A Agent
This agent answers specific recruiter queries based on retrieved knowledge.
"""

from langchain.chat_models import ChatOpenAI

class QAAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0)

    def answer_query(self, query, knowledge_base_results):
        context = "\n".join([f"- {item['source']}: {item.get('content', '')}" for item in knowledge_base_results])
        prompt = (
            f"Context:\n{context}\n\n"
            f"Question: {query}\n\n"
            "Answer the question based on the context provided."
        )
        return self.llm.predict(prompt)