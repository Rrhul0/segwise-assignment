from huggingface_hub import InferenceClient
import os

client = InferenceClient(api_key=os.getenv("HUGGINGFACE_API_KEY"))

def getMessage(posts):
    combined_posts = "\n".join(posts)
    result = ""
    prompt = f"Create a friendly two-line LinkedIn connection message based on the user's posts: {combined_posts}"

    for message in client.chat_completion(
        model="mistralai/Mistral-Nemo-Instruct-2407",
        messages=[{"role": "user", "content": prompt,}],
        max_tokens=50,
        stream=True,
    ):
        result += message.choices[0].delta.content
    return result