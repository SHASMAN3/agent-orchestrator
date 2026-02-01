BLOCKED_KEYWORDS = [
    "jailbreak",
    "bypass safety",
    "hack system"
]

def validate_prompt(prompt: str):
    for word in BLOCKED_KEYWORDS:
        if word in prompt.lower():
            raise ValueError("Prompt violates policy")
