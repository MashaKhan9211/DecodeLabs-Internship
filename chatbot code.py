while True:

    user = input("You: ").lower()

    if user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine.")

    elif user == "your name":
        print("Bot: My name is AI Bot.")

    elif user == "bye" or user == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")