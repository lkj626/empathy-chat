system_prompt = "아래는 대화 내용이다."


def get_prompt(messages, eos_token):
    instruction = f"{system_prompt}\n"
    conversation = []

    for entry in messages:
        role = entry["role"]
        content = entry["content"]

        if role == "user":
            conversation.append(f"speaker: {content}")
        elif role == "assistant":
            conversation.append(f"listener: {content}{eos_token}")

    return instruction + "\n".join(conversation) + "\nlistener:"