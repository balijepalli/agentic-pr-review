import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    with open("pr.diff", "r") as f:
        diff = f.read()

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert GitHub pull request reviewer."},
            {"role": "user", "content": f"Review this diff and provide concise suggestions:\n\n{diff}"}
        ],
        temperature=0.4,
    )

    print("### 🤖 GPT Agent Review:\n" + response['choices'][0]['message']['content'])

if __name__ == "__main__":
    main()
