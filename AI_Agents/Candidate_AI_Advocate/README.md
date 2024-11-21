# Candidate AI Advocate Project 

This is a Supervisor-Led Multi-Agent System project fully implement with 
open-source tools like LangChain, Pinecone, and Streamlit.


## Architecture Overview

### 1. Supervisor Agent:
   - Orchestrates the workflow by delegating tasks to specialized agents and aggregating results. 
   - Ensures task dependencies are followed logically.


### 2. Ingestion Agent:
   - Gathers data from LinkedIn, GitHub, CV, and other sources.
   - Embeds the data and stores it in a vector database (e.g., Pinecone).

### 3. Knowledge Base Agent:
   - Retrieves relevant information from the vector database based on queries.

### 4. Q&A Agent:
   - Answers recruiter queries using the retrieved information.

### 5. Justification Agent:
   - Generates role-specific arguments using stored data and external sources like Google Custom Search API.
