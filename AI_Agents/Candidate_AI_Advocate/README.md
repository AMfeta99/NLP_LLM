# Candidate AI Advocate (WIP/Draft)

<p align="center">
  <img src="https://github.com/user-attachments/assets/854cd065-3913-4c15-8ab1-951aa5ecee2f" alt="AI_lawyer" style="width:75%";>
  <br>
  <em></em>
</p>

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

<!-- https://www.linkedin.com/pulse/pros-cons-using-ai-hiring-seesy 
https://www.youtube.com/watch?v=erUfLIi9OFM

https://huggingface.co/learn/cookbook/multiagent_rag_system
-->
