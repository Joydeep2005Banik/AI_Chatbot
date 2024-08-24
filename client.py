from ai21 import AI21Client
from ai21.models.chat import UserMessage

client = AI21Client(api_key="<Your API Key>")

copied_text = """[10:05 pm, 22/8/2024] Sohini Bose: 🙂
[10:05 pm, 22/8/2024] Sohini Bose: Kintu ma'am i bollo khub simple na korte
[10:06 pm, 22/8/2024] Joydeep Banik: Tui bhab model ta nijei jotil....mam er kotha bad de
[10:09 pm, 22/8/2024] Sohini Bose: Haa jotil to bote
[10:09 pm, 22/8/2024] Joydeep Banik: Setai
[10:18 pm, 22/8/2024] Sohini Bose: 🙂
[11:13 pm, 22/8/2024] Joydeep Banik: reply koris na akta test korchi
[10:25 am, 23/8/2024] Sohini Bose: Holo test?
[1:04 pm, 23/8/2024] Joydeep Banik: Ha"""

def single_message_instruct(copied_text):
    """
    Generates a casual and informal response based on the copied chat history.
    """
    try:
        messages = [
            UserMessage(
                content=f'''
                You are Joydeep, a friend, and you can speak casually. You know Bengali and English. Look at the chat history below and provide a reply in an informal, English-Bengali mix. Your response should be friendly but concise. Avoid repeating words unnecessarily, and keep the language natural and conversational. Do not mention the word 'Joydeep' or the name of the sender. Chat history: {copied_text}
                '''
            )
        ]
        
        response = client.chat.completions.create(
            model="jamba-1.5-large",
            messages=messages,
            top_p=0.9,  # Slightly more focused
            temperature=0.5,  # Less creative
            max_tokens=50  # Shorter output
        )
        
        if not response or not response.choices or not response.choices[0].message:
            print("No response received from API.")
            return "No response from AI"

        # Accessing the content of the assistant's message
        output_text = response.choices[0].message.content.strip()
        if output_text:
            print(f"AI Response: {output_text}")
        else:
            print("Received an empty response.")
        return output_text

    except Exception as e:
        print(f"Error while generating response: {e}")
        return "Error generating response"

# Test the function to see what's happening
single_message_instruct(copied_text)
