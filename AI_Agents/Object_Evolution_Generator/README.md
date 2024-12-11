# TimeMetamorphy

Have you ever wondered what life was like 20, 30, 40, or even 100 years ago? How did our parents communicate? What did their phones and cars look like? 
Isn’t it amazing to see how much things have changed and evolved over time? And even more mind-blowing imagining what the future might look like!

### **Unlocking the secrets of time!**

This project unveils these mysteries by offering a unique/magic lens that allows us "time travel". Powered by AI agents equipped with cutting-edge tools, it provides the superpower to explore the past, witness the present, and dream up the future like never before.  

 ### Index:
- [Setup](#Setup)
- [Usage](#Usage)
- [Methods](#Methods)
- [Results](#results)
- [Repository_files](#Repository_files)
- [Acknowledgements](#Acknowledgements)

## Application_Demo
TimeMetamorphy app was developed with Gradio. This is hosted by Hugging Face Spaces, so anyone can have access to it.
### Try the Demo : [App](https://huggingface.co/spaces/AMfeta99/Object_Evolution_Generator).

## Setup
- Create a virtual environment and install the required packages:
  
         $ python3 -m venv .venv
         $ source .venv/bin/activate
         $ pip install -r requirements.txt

## Usage
After the installation is ready, give it a try. To get started, you will be asked to enter: 
1. A Object/Concept name:
   
![image_20241211_1120271d8aed0f-3c5e-4659-b627-2c56986446d0](https://github.com/user-attachments/assets/97182213-b40a-4bee-a09b-7443f9b5b0e2)

2. Click on "Generate Evolution"
3. AI_Agent is processing, when finish it will output 3 images (past/present/future) and generate a gif. 
  

## Methods
This App is an AI_agent based system, meaning it was built around a LLM, designed to extend the capabilities of the LLM by allowing it to use specialized tools. These tools are integrated through carefully crafted prompts and structured output parsing, enabling the LLM to address tasks it wouldn’t handle effectively on its own.

Transformer Agents library was used for implementation of such system, providing building block to customized the Agent. 

### Framework
This Agent follows the **ReAct** framework combining **Reasoning + Acting (ReAct)** principles with code execution capabilities.

This type of agent operates by iteratively reasoning about the task, deciding on the necessary steps, and performing actions using external tools or executing code to achieve its goals.

  - #### 1. Code: 
      **ReactCodeAgent** can execute Python code or interact with code-related tools, allowing it to perform computational tasks, manipulate data, or even write and debug scripts as part of its workflow.

  - #### 2. Tool Integration: 
       It can integrate with tools like web search engines, calculators, APIs, or custom modules to extend its capabilities beyond language-based reasoning.

  - #### 3. Iterative Approach: 
       The agent evaluates intermediate results during execution and adapts its actions accordingly to ensure it converges on a solution effectively.


### Tools
  - #### 1. Image Generation Tool
       - This tool uses the Hugging Face Inference API (Serverless) to generate images via Stable Diffusion.
         
             image_generation_tool = load_tool("m-ric/text-to-image", cache=False)

       - The tool is loaded directly from the Hugging Face Hub, providing seamless integration and functionality.

  - #### 2. Web Search Tool
       - This is a built-in tool that allows the agent to search and retrieve information from the web.
         
             from transformers.agents.search import DuckDuckGoSearchTool
             search_tool = DuckDuckGoSearchTool()
          
       - It enables the agent to gather external knowledge to support its tasks.

### LLM & Build Agent
- #### 1. LLM Selection:
We Select a LLM fine-tuned for instruction-following tasks, Qwen2.5-72B-Instruct 

    llm_engine = HfApiEngine("Qwen/Qwen2.5-72B-Instruct") 
   
- #### 2. Initialize the agent with tools

    agent = ReactCodeAgent(tools=[image_generation_tool, search_tool], llm_engine=llm_engine)


## Results
<div style="display: flex; justify-content: center; align-items: flex-start;">
  <figure style="margin: 10px; text-align: center;">
    <img src="car_evolution.gif" alt="Car Evolution" style="width: 330px;">
  </figure>
  <figure style="margin: 10px; text-align: center;">
    <img src="phone_evolution.gif" alt="Phone Evolution" style="width: 330px;">
  </figure>
  <figure style="margin: 10px; text-align: center;">
    <img src="https://amfeta99-object-evolution-generator.hf.space/gradio_api/file=/tmp/gradio/e137e19163a0d5e9785ae84e4c8100c9ed22478e1c64a6218bd6c19a3c272bf3/Human_evolution.gif" alt="Human Evolution" style="width: 330px;">
  </figure>
</div>

## Repository_files

## Acknowledgements
- Santiago Valdarrama. (2024). [llm](https://github.com/svpino/llm/tree/main/guessing). GitHub, who contributed significantly to the idealization of the project.
- [Ollama](https://ollama.com/). Source of llm models.
- [OpenAi API](https://openai.com/index/openai-api/). Source of llm models.
- [Medium](https://medium.com/@GPTPlus/ai-in-human-robot-interaction-884ef04bdd88). repository img








[APP](https://huggingface.co/spaces/AMfeta99/Object_Evolution_Generator)

