from speech_module import recognize_speech, speak
from chatbot_module import get_chatbot_response

def chat():
    """Main chatbot loop with both speech and text input."""
    print("Chatbot is ready! Type or say something (type 'exit' to quit).")

    while True:
        choice = input("\nChoose input mode - (T)ype or (S)peak? ").strip().lower()

        if choice == "t":
            user_input = input("You: ")
        elif choice == "s":
            user_input = recognize_speech()
        else:
            print("Invalid choice! Please enter 'T' for typing or 'S' for speaking.")
            continue

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        bot_reply, mood = get_chatbot_response(user_input)

        print(f"Bot ({mood}): {bot_reply}")
        speak(bot_reply)  # Convert text response to speech

if __name__ == "__main__":
    chat()
