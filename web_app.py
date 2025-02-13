"""This file contains the code for the web deployment of the doodle-recognizer model"""

import gradio as gr
import numpy as np
import torch

from PIL import Image
from torchvision.transforms import Resize
from model_module.predict import setup, make_prediction

CANVAS_SIZE = 840  # 28 * 30. It is a multiple of 30 to make the downscaling process return better results. 
CATEGORIES = ["Clock", "Boomerang", "Airplane", "Snail", "Parachute", "Tree", "Fish", "Diamond", "Helicopter", "T-Shirt"]

# Set up the prediction model
setup()

# Initialize the image resizer
resizer = Resize([28, 28])

def sketchToNumpy(image):
    img_array = image['composite']  # This is a numpy array of size (CANVAS_SIZE, CANVAS_SIZE)

    tensor_image = torch.tensor(img_array).unsqueeze(0)  # Add an extra batch dimension
    resized_image = resizer(tensor_image)  # Resize for visualization

    # Process image
    _, class_probs = make_prediction(resized_image.numpy(), convolutional=True)
    class_probs = class_probs.numpy()

    # Convert numpy array to PIL image and back to original size to show the low-res version to the user in the UI
    img = Image.fromarray(resized_image.squeeze().numpy())
    img = img.resize((CANVAS_SIZE, CANVAS_SIZE), resample=Image.Resampling.NEAREST)
    
    # Add a checkmark to the class that has the highest probability in the model outputs
    icons = ["✅" if maximum else "❌" for maximum in class_probs == np.max(class_probs)]

    # Create the text that each label will display
    text_labels = [f"Probability: {prob:.2f} {icon}" for prob, icon in zip(class_probs, icons)]

    # Return probabilities and image
    return text_labels + [img]

with gr.Blocks() as demo:
    gr.Markdown("# Doodle Recognizer ✏️🤖 ")
    gr.Markdown("Welcome to the webb application for the google recognizer. To start, please draw a shape")
    with gr.Row():
        with gr.Column():
            custom_brush = gr.Brush(default_color="white", default_size=20)  # Define a custom brush for the canvas
            sketchpad = gr.Sketchpad(canvas_size=(CANVAS_SIZE, CANVAS_SIZE), image_mode='L', brush=custom_brush, label="Draw here! ✒️")
            
        with gr.Column():
            outputs_2 = [gr.Image(type="pil", label="Pre-Processed Sketch 🧮🖼️")]
    
    with gr.Row():
        outputs_1_1 = [gr.Text(label=label) for label in CATEGORIES[:5]]
        
    with gr.Row():
        outputs_1_2 = [gr.Text(label=label) for label in CATEGORIES[5:]]
    
    outputs_1 = outputs_1_1 + outputs_1_2

    btn = gr.Button("Analyze 🧠⚡")
    btn.click(sketchToNumpy, inputs=sketchpad, outputs=outputs_1+outputs_2)

demo.launch()



