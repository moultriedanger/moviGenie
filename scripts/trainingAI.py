import openai
from openai import OpenAI
import json
import os
import time
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.config import Config

print("Loaded GPT API key:", Config.GPT_API)

# Set the API key
openai.api_key = Config.GPT_API

# Initialize the OpenAI client
client = openai.OpenAI(api_key=Config.GPT_API, timeout=40.0)

# Get the model for fine-tuning
fine_tuning_model = "gpt-3.5-turbo-0125"
print(f"Using model: {fine_tuning_model}")

# Upload the training file
with open("scripts/training.jsonl", "rb") as f:
    training_file_response = client.files.create(
        file=f,
        purpose="fine-tune"
    )
training_file_id = training_file_response.id
print("Training file uploaded successfully")
print("Training file ID:", training_file_id)

# Create a fine-tuning job
fine_tuning_response = client.fine_tuning.jobs.create(
    training_file=training_file_id,
    model=fine_tuning_model,
    seed=99
)
fine_tuning_job_id = fine_tuning_response.id

print("Fine-tuning job created successfully")
print(fine_tuning_response)

# Monitor the status of the fine-tuning job
while True:
    fine_tuning_status = client.fine_tuning.jobs.retrieve(fine_tuning_job_id)
    status = fine_tuning_status.status
    print(f"Fine-tuning job status: {status}")
    if status in ['succeeded', 'failed']:
        break
    time.sleep(120)  # Wait for 120 seconds before checking the status again

if status == 'succeeded':
    print("Fine-tuning job completed successfully")
    fine_tuned_model_id = fine_tuning_status.fine_tuned_model
    print(f"Fine-tuned model ID: {fine_tuned_model_id}")
    
    with open("app/fine_tuned_model_id.json", "w") as f:
        json.dump({"fine_tuned_model_id": fine_tuned_model_id}, f)

    # Make a call to the fine-tuned model
    response = client.chat.completions.create(
        model=fine_tuned_model_id,
        messages=[
            {"role": "system", "content": "You are my movie recommendation engine that only responds in lists of movies."},
            {"role": "user", "content": "Give me a movie with action and suspense that features Ryan Gosling."}
        ],
        max_tokens=50
    )
    print("Response from fine-tuned model:")
    print(response.choices[0].message)
else:
    print("Fine-tuning job failed")
    print(fine_tuning_status)