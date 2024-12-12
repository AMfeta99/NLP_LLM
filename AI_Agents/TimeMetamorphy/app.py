#%% Import libraries
from transformers import load_tool, ReactCodeAgent, HfApiEngine
from PIL import Image
import torch
import numpy as np
import tempfile
import os
import uuid
import gradio as gr


#%% Methods 
# function to plot and save an AgentImage
def plot_and_save_agent_image(agent_image, save_path=None):
    # Convert AgentImage to a raw PIL Image
    pil_image = agent_image.to_raw()

    # Plot the image using PIL's show method
    pil_image.show()

    # If save_path is provided, save the image
    if save_path:
        pil_image.save(save_path)
        print(f"Image saved to {save_path}")
    else:
        print("No save path provided. Image not saved.")


def generate_prompts_for_object(object_name):
    prompts = {
        "past": f"Show an old version of a {object_name} from its early days.",
        "present": f"Show a {object_name} with from present with current features/design/technology.",
        "future": f"Show a futuristic version of a {object_name}, by predicting advanced features and futuristic design."
    }
    return prompts


# Function to generate the car industry history
def generate_object_history(object_name):
    images = []
    
    # Get prompts for the object
    prompts = generate_prompts_for_object(object_name)
    
    # Generate sequential images and display them
    for time_period, frame in prompts.items():
        print(f"Generating {time_period} frame: {frame}")
        result = agent.run(frame)  # The tool generates the image
        
        # Append the image to the list for GIF creation
        images.append(result.to_raw())  # Ensure we're using raw image for GIF

        # Save each image with the appropriate name (past, present, future)
        image_filename = f"{object_name}_{time_period}.png"
        plot_and_save_agent_image(result, save_path=image_filename)
        
        
    # Create GIF from images
    gif_path = f"{object_name}_evolution.gif"
    images[0].save(
        gif_path, 
        save_all=True, 
        append_images=images[1:], 
        duration=1000,  # Duration in milliseconds for each frame
        loop=0          # Infinite loop
    )
    
    # Return images and GIF path
    return images, gif_path


#%% Initialization of tools and AI_Agent
# Import text-to-image tool from Hub 
# m-ric/text-to-image model generates images based on textual descriptions.
image_generation_tool = load_tool("m-ric/text-to-image", cache=False) #cache=False ensures it fetches the latest tool updates directly from the Hub.

# Import search tool from LangChain
#This tool allows the agent to search for and retrieve information from the web.
from transformers.agents.search import DuckDuckGoSearchTool

search_tool = DuckDuckGoSearchTool()

# Qwen2.5-72B-Instruct is a specific, a LLM fine-tuned for instruction-following tasks.
llm_engine = HfApiEngine("Qwen/Qwen2.5-72B-Instruct") 
# Initialize the agent with both tools
agent = ReactCodeAgent(tools=[image_generation_tool, search_tool], llm_engine=llm_engine)



# Gradio interface
def create_gradio_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# Object Evolution Generator")
        
        # Add a section for instructions
        gr.Markdown("""
        ## Welcome to the Object Evolution Generator!
        This app allows you to generate visualizations of how an object, like a bicycle or a car, may have evolved over time. 
        It generates images of the object in the past, present, and future based on your input.
        
        ### Default Example: Evolution of a Car
        Below, you can see a precomputed example of a "car" evolution. Enter another object to generate its evolution.
        """)

        # Paths to the precomputed files
        default_images = [
            ("car_past.png", "Car - Past"),
            ("car_present.png", "Car - Present"),
            ("car_future.png", "Car - Future")
        ]
        default_gif_path = "car_evolution.gif"

        with gr.Row():
            with gr.Column():
                # Textbox for user to input an object name
                object_name_input = gr.Textbox(label="Enter an object name (e.g., bicycle, phone)", 
                                              placeholder="Enter an object name", 
                                              lines=1)

                # Button to trigger the generation of images and GIF
                generate_button = gr.Button("Generate Evolution")
    
                # Gradio Gallery component to display the images
                image_gallery = gr.Gallery(label="Generated Images", show_label=True, columns=3, rows=1, 
                                           value=default_images)

                # Output for the generated GIF
                gif_output = gr.Image(label="Generated GIF", show_label=True, value=default_gif_path)
         
        # Set the action when the button is clicked
        generate_button.click(fn=generate_object_history, inputs=[object_name_input], outputs=[image_gallery, gif_output])
    
    return demo

# Launch the Gradio app 
demo = create_gradio_interface()

# To make it permanent and hosted, we can use Gradio's 'share' argument or host it on a server.
demo.launch(share=True)
