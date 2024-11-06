from huggingface_hub import InferenceClient
import os

client = InferenceClient(api_key=os.getenv("HUGGINGFACE_API_KEY"))

def getMessage(details,posts):
    userExperiences = ""
    for exp in details['experiences']:
        userExperiences += f" {exp['job_title']} at {exp['company_name']} ({exp['duration']})"
    userProfile = f"{details['name']} is a {details['about']} and have worked in the following roles:{userExperiences}"
    combined_posts = "\n".join(posts)
    result = ""
    prompt = f"Create a friendly two-line LinkedIn connection message based on the user profile: {userProfile} and user's posts (only show message result): {combined_posts}"

    for message in client.chat_completion(
        model="mistralai/Mistral-Nemo-Instruct-2407",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=60,
        stream=True,
    ):
        result += message.choices[0].delta.content
    return result