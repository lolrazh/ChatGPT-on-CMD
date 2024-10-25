from openai import OpenAI

client = OpenAI()

messages = []

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting chat.")
            break  # stop the loop if the user wants to exit

        messages.append({"role": "user", "content": user_input})  # track conversation history

        print("ChatGPT: ", end="")
        assistant_response = ""  # store the full response here
        stream = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            stream=True,  # stream the response in chunks
        )
        for chunk in stream:
            content = chunk.choices[0].delta.content or ''  # handle empty chunks
            print(content, end="", flush=True)  # print each chunk immediately
            assistant_response += content  # build the complete response
        print()

        messages.append({"role": "assistant", "content": assistant_response})  # add response to history

    except KeyboardInterrupt:
        print("\nExiting chat.")  # handle manual interruption
        break
    except Exception as e:
        print(f"\nAn error occurred: {e}")  # catch and display unexpected errors
        break
