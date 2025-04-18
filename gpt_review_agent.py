from openai import OpenAI
import os
import json

def main():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    with open("pr.diff", "r") as f:
        diff = f.read()

    prompt = (
        "You are a senior software engineer doing code review. "
        "Provide a brief review for the following pull request diff:\n\n"
        f"{diff}"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful code reviewer."},
            {"role": "user", "content": prompt},
        ],
    )

    print("### GPT PR Review:")
    print(response.choices[0].message.content.strip())

if __name__ == "__main__":
    main()
