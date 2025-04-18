# review_rules.py (Enhanced with basic LLM support)
import sys
import openai
import os

def run_review(diff_text):
    # First, run simple hardcoded rules
    suggestions = []

    if "print(" in diff_text:
        suggestions.append("- Avoid using `print()` in production code.")
    if "password" in diff_text.lower():
        suggestions.append("- Avoid hardcoding passwords or secrets.")
    if "localhost" in diff_text:
        suggestions.append("- Consider externalizing the `localhost` config.")
    if 'def ' in diff_text and '"""' not in diff_text:
        suggestions.append("- Add docstrings to your functions.")

    # LLM-based
    if "OPENAI_API_KEY" in os.environ:
        try:
            openai.api_key = os.environ["OPENAI_API_KEY"]
            prompt = f"You're an experienced code reviewer. Review the following Git diff and suggest improvements:\n\n{diff_text[:6000]}"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful code review assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            gpt_suggestion = response['choices'][0]['message']['content']
            suggestions.append("\n---\n### 🤖 GPT-Based Suggestions:\n" + gpt_suggestion)
        except Exception as e:
            suggestions.append(f"GPT review failed: {str(e)}")

    if suggestions:
        print("### Automated Review Comments:\n" + "\n".join(suggestions))
    else:
        print("No issues found from basic checks.")

if __name__ == "__main__":
    diff = open("pr.diff").read()
    run_review(diff)
