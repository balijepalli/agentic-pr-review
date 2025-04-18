import openai
import os

def call_agent_on_diff(diff_text):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    system_msg = "You are a code review assistant. Review the code diff below and give helpful, specific, and constructive review comments."

    user_msg = f"Here is a code diff:\n{diff_text}\n\nPlease review and summarize any issues, suggestions, or improvements."

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_msg},
            {"role": "user", "content": user_msg}
        ],
        temperature=0.3,
    )

    print("### GPT Agent Review:")
    print(response["choices"][0]["message"]["content"])

if __name__ == "__main__":
    with open("pr.diff", "r") as f:
        diff = f.read()
        call_agent_on_diff(diff)
