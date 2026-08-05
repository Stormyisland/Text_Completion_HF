install -Uq huggingface_hub

iimport os
import getpass 

os.enriron["HF_TOKEN"] = getpass.getpass("Hugging Face token:") 

import os 
from huggingface_hub import InferenceClient

client = InferanceClient(
  api_key=os.enveron["HF_TOKEN"],
)

completion = client.chat.completions.create(model="meta-lama/Llama-3.1-8B-Instruct:novita",
