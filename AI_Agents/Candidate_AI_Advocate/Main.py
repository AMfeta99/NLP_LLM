# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:49:03 2024

@author: zefin
"""

import IngestionAgent
import KnowledgeBaseAgent
import QAAgent
import JustificationAgent
import SupervisorAgent


# Initialize Agents
ingestion_agent = IngestionAgent()
knowledge_base_agent = KnowledgeBaseAgent()
qa_agent = QAAgent()
justification_agent = JustificationAgent()

# Tools for Supervisor
tools = [
    Tool(name="Q&A Agent", func=qa_agent.answer_query),
    Tool(name="Justification Agent", func=justification_agent.generate_justification)
]

supervisor_agent = SupervisorAgent(tools=tools)

# Example Workflow
query = "Why is this candidate suitable for a DevOps Engineer role?"
knowledge_base_results = knowledge_base_agent.retrieve_relevant_info(query)
qa_response = qa_agent.answer_query(query, knowledge_base_results)
justification_response = justification_agent.generate_justification(query, qa_response)

print("Q&A Response:", qa_response)
print("Justification Response:", justification_response)
