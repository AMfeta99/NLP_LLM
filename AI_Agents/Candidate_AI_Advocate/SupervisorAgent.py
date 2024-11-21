# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:56:40 2024

@author: zefin

The Supervisor Agent orchestrates the task flow. It receives a query, determines 
which agents to call, and combines their responses.
"""

from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

# Supervisor Agent
class SupervisorAgent:
    def __init__(self, tools):
        self.llm = ChatOpenAI(model="gpt-4", temperature=0)
        self.tools = tools

    def delegate_task(self, task_name, *args, **kwargs):
        # Find the correct tool by name
        for tool in self.tools:
            if tool.name == task_name:
                return tool.func(*args, **kwargs)
        raise ValueError(f"Tool '{task_name}' not found")

    def process_query(self, query):
        # Orchestrate workflow
        # Step 1: Ingestion (handled beforehand during data preprocessing)
        # Step 2: Query Handling
        qa_response = self.delegate_task("Q&A Agent", query)

        # Step 3: Justification
        justification_response = self.delegate_task("Justification Agent", query, qa_response)

        # Combine and return results
        return {
            "qa_response": qa_response,
            "justification_response": justification_response
        }