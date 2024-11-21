# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 17:01:21 2024

@author: zefin

Justification Agent
This agent builds a compelling argument for the candidate’s suitability for the role.
"""

class JustificationAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0)

    def generate_justification(self, query, qa_response):
        prompt = (
            f"The following is a recruiter question and the candidate's response:\n"
            f"Question: {query}\n"
            f"Response: {qa_response}\n\n"
            f"Based on this response and industry trends, provide a detailed justification for the candidate's suitability."
        )
        return self.llm.predict(prompt)
