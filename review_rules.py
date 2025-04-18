import sys

def run_review(diff_text):
    suggestions = []

    if "print(" in diff_text:
        suggestions.append("- Avoid using `print()` in production code.")
    if "password" in diff_text.lower():
        suggestions.append("- Avoid hardcoding passwords or secrets.")
    if "localhost" in diff_text:
        suggestions.append("- Consider externalizing the `localhost` config.")
    if 'def ' in diff_text and '"""' not in diff_text:
        suggestions.append("- Add docstrings to your functions.")

    if suggestions:
        print("### 🤖 Automated Review Comments:\n" + "\n".join(suggestions))
    else:
        print("No issues found from basic checks.")

if __name__ == "__main__":
    diff = open("pr.diff").read()
    run_review(diff)
