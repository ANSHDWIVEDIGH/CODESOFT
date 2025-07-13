import random

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if any(greet in user_input for greet in ["hi", "hello", "hey", "good morning", "good evening"]):
        return random.choice(["Hello! How can I help you?", "Hi there! Need any assistance?", "Hey! What can I do for you today?"])

    elif any(bye in user_input for bye in ["bye", "goodbye", "see you", "take care"]):
        return random.choice(["Goodbye! Have a great day.", "See you soon!", "Take care!"])

    elif any(thank in user_input for thank in ["thanks", "thank you", "thx", "much appreciated"]):
        return random.choice(["You're welcome!", "Glad I could help!", "No problem at all."])

    elif "help" in user_input or "assist" in user_input:
        return random.choice(["Sure, I am here to assist you. Please tell me your query.", 
                              "Happy to help! Please describe your issue.", 
                              "What can I do for you?"])

    elif "your name" in user_input:
        return random.choice(["I am RuleBot, your simple chatbot.", "You can call me RuleBot.", "Just a chatbot here to help you."])

    elif "how are you" in user_input:
        return random.choice(["I'm just code, but I'm functioning perfectly!", "I'm good, thank you for asking!", "Doing great! Ready to assist you."])

    elif "what can you do" in user_input:
        return random.choice(["I can respond to basic queries based on rules.", "I am a rule-based chatbot created for learning purposes.", "My job is to answer simple questions and assist you!"])

    # Additional 5 queries:
    elif "your age" in user_input or "how old are you" in user_input:
        return random.choice(["I do not have an age. I'm just a chatbot!", "Age is just a number, and I am timeless."])

    elif "where are you from" in user_input or "your place" in user_input or "your location" in user_input:
        return random.choice(["I exist in your computer.", "I'm from the digital world!", "Location: Inside your Python code."])

    elif "hobbies" in user_input or "what do you like" in user_input:
        return random.choice(["I like helping users.", "Answering questions is my hobby!", "I enjoy chatting all day."])

    elif "creator" in user_input or "who made you" in user_input:
        return random.choice(["I was created by a BTech CSE student.", "A human programmed me using Python.", "Made as part of a computer science project."])

    elif "language" in user_input or "what language" in user_input:
        return random.choice(["I am programmed in Python.", "Python is my mother tongue!", "Python 3 is the language I understand."])

    else:
        return random.choice([
            "Sorry, I didn't understand that. Can you rephrase?",
            "I'm not sure how to respond to that.",
            "Please try asking something else."
        ])

def run_chatbot():
    print("Simple Chatbot (Type 'exit' to end)")
    while True:
        user_message = input("You: ")
        if user_message.lower() == "exit":
            print("Chatbot: Chat ended. Goodbye!")
            break
        response = chatbot_response(user_message)
        print("Chatbot:", response)

if __name__ == "__main__":
    run_chatbot()

