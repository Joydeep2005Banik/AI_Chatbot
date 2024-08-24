import re
import pyautogui
import pyperclip
import time
from ai21 import AI21Client
from ai21.models.chat import UserMessage
import pygetwindow as gw

def is_whatsapp_active():
    """
    Checks if the active window is WhatsApp.
    """
    active_window = gw.getActiveWindow()
    return "WhatsApp" in (active_window.title if active_window else "")

client = AI21Client(api_key="78Qlsf3v7nK7nWydYBGPtxiYDc4S1Qfm")

def analyze_and_reply(output_text):
    """
    Clicks on the specified position and types the response.
    """
    try:
        # Click on the input field (ensure this is within the WhatsApp window)
        print("Clicking on input field...")
        pyautogui.click(1131, 954)#to paste the response in the chat
        time.sleep(0.5)  # Ensure the click is registered
        pyautogui.typewrite(output_text)
        pyautogui.press('enter')#to send the response to user
        print(f"Replied with: {output_text}")
    except Exception as e:
        print(f"Error while sending reply: {e}")

def single_message_instruct(copied_text):
    """
    Generates a casual and informal response based on the copied chat history,ensuring the AI responds as Joydeep Banik:.
    """
    try:
        # Filter out messages from "Joydeep" and prepare chat history for AI processing
        filtered_text = "\n".join(line for line in copied_text.split('\n') if "Joydeep Banik" not in line)
        
        messages = [
            UserMessage(
                content=f'''
                You are Joydeep Banik:, a friend, and you can speak casually. You know Bengali and English. Look at the chat history below and provide a reply in an informal, English-Bengali mix. Your response should be friendly but concise. Avoid repeating words unnecessarily, and keep the language natural and conversational. Do not mention the word 'Joydeep' or the name of the sender. Reply only when the sender responds. Do not respond to messages by Joydeep.Do not start like this [21:02, 12/6/2024] Sohini Bose: . Chat history: {filtered_text}
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
        print(f"AI Response: {output_text}")
        return output_text

    except Exception as e:
        print(f"Error while generating response: {e}")
        return "Error generating response"


def get_copied_text():
    """
    Retrieves and returns the text from the clipboard after copying.
    """
    try:
        # Click and drag to select the text in WhatsApp (adjust these coordinates)
        print("Selecting chat text...")
        pyautogui.moveTo(730, 218)  # Start point of chat history
        pyautogui.dragTo(1105, 960, duration=1, button='left')  # End point of chat history

        # Copy the selected text to the clipboard
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)  # Short delay to ensure the text is copied
        # Simulate a click somewhere outside the selection area to deselect
        pyautogui.click(1223, 591)  # Click on a location outside the chat area

        # Retrieve the text from the clipboard
        copied_text = pyperclip.paste().strip()
        print(f"Copied Text: {copied_text}")
        return copied_text
    except Exception as e:
        print(f"Error while copying text: {e}")
        return ""

def is_new_message(copied_text, previous_text):
    """
    Checks if there is a new message by comparing the copied text with the previous text.
    If previous text is equal to copied text, skip the processing.
    """
    # Compare copied text with previous text
    if copied_text != previous_text:
        return True  # There is new content

    return False  # No new message detected


def get_last_sender_message(copied_text):
    """
    Extracts and returns the last message sent by Sohini Bose if the last message is from Sohini Bose.
    """
    # Split the copied text into lines
    messages = copied_text.split('\n')

    # Iterate over messages in reverse to find the last one from Sohini Bose
    for message in reversed(messages):
        if re.match(r"\[\d{1,2}:\d{2} (am|pm), \d{1,2}/\d{1,2}/\d{4}\]", message):
            if "Sohini Bose:" in message:
                return message.split("] ")[1]  # Extract the message text after the timestamp and sender name
            elif "Joydeep Banik:" in message:
                return ""  # Return an empty string if the message is from Joydeep Banik

    return ""  # Return an empty string if no suitable message is found


def main():
    previous_text = ""

    while True:
        try:
            # Check if WhatsApp is the active window
            if is_whatsapp_active():
                print("WhatsApp is active.")
                # Click on the WhatsApp window to ensure it's focused
                time.sleep(0.5)  # Ensure the click is registered

                # Retrieve the chat history
                copied_text = get_copied_text()

                # Check if there is a new message
                if is_new_message(copied_text, previous_text):
                    # Get the last message from Sohini Bose
                    last_sender_message = get_last_sender_message(copied_text)

                    if last_sender_message:  # If there's a message to reply to
                        # Get the AI-generated response based on the last sender message
                        ai_response = single_message_instruct(copied_text)

                        # Check if the AI response is valid (not empty or not default)
                        if ai_response.strip() and ai_response.lower() != "no response from ai":
                            # Send the AI-generated response
                            analyze_and_reply(ai_response)

                    # Update the previous text with the latest chat history
                    previous_text = copied_text
                else:
                    print("No new message detected.")
            else:
                print("WhatsApp is not active.")

            # Wait before the next iteration
            time.sleep(10)  # Adjust the sleep time as needed

        except Exception as e:
            print(f"Error in main loop: {e}")
            time.sleep(10)  # Wait before retrying

if __name__ == "__main__":
    main()

