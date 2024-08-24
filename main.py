from dotenv import load_dotenv
load_dotenv()

from gemini import generate

try:
    while True:
        user_input = input("Enter your prompt (or 'exit' to quit): ")
        if user_input == "exit":
            break
        print(generate(user_input))
except KeyboardInterrupt:
    print("\nGoodbye!")
except Exception as e:
    print(f"Error: {e}")