def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print("Sending:", current_message)
        sent_messages.append(current_message)

# List of short text messages
text_messages = [
    "Hello, how are you?",
    "Just checking in!",
    "Don't forget our meeting tomorrow.",
    "Happy birthday! 🎉",
    "Hope you're having a great day!",
]

# List to store sent messages
sent_messages = []

# Calling the function to send and display the messages
send_messages(text_messages, sent_messages)
print("\nSent Messages:")
show_messages(sent_messages)
print("\nRemaining Messages:")
show_messages(text_messages)
