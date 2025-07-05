import random

def get_response(message):
    message = message.lower()

    responses = {
        "hello": "Hi Sir!",
        "how are you": "I'm Fine, What's About you?!",
        "what's your name": "I'm AI Chatbot.",
        "bye": "See You!",
        "default": "I'm sorry, I don't understand that."
    }

    if "hello" in message:
        return responses["hello"]
    elif "how are you" in message:
        return responses["how are you"]
    elif "what's your name" in message or "your name" in message:
        return responses["what's your name"]
    elif "bye" in message:
        return responses["bye"]
    else:
        return responses["default"]

# Main loop to run the chatbot
def chat():
    print("Hello! I'm a simple rule-based chatbot. You can start chatting with me. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

# Lets cht with chatbot
chat()