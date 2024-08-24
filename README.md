# AI_Chatbot
WhatsApp Auto-Responder with AI Integration
<br>



WhatsApp Auto-Responder with AI Integration
Overview
This Python script automates responses on WhatsApp using AI-generated replies. The script leverages the AI21 API to generate responses based on the chat history and automatically replies to messages from others. It filters out messages from the user running the script, ensuring that responses are only sent to messages from other senders. The script also handles interactions with the WhatsApp desktop application using pyautogui for GUI automation and pyperclip for clipboard management.

Features
Automated Reply: Automatically replies to new messages in WhatsApp using AI-generated responses.
AI Integration: Uses the AI21 API to generate conversational replies in an informal, English-Bengali mix.
Message Filtering: Ensures that the script does not reply to messages from the user running the script.
Clipboard Management: Retrieves chat history from WhatsApp using clipboard operations.
GUI Automation: Interacts with WhatsApp's GUI to select, copy, and paste text.
Prerequisites
Python 3.x
pyautogui
pyperclip
ai21
pygetwindow
Access to the AI21 API (API key required)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/whatsapp-auto-responder.git
Install the required Python packages:

bash
Copy code
pip install pyautogui pyperclip ai21 pygetwindow
Replace "78Qlsf3v7nK7nWydYBGPtxiYDc4S1Qfm" with your AI21 API key in the client = AI21Client(api_key="your_api_key") line in the script.

Usage
Ensure WhatsApp is open and the chat window is visible.
Run the script:
bash
Copy code
python whatsapp_auto_responder.py
The script will continuously monitor for new messages and respond accordingly.
How It Works
Active Window Check: The script verifies that WhatsApp is the active window before proceeding.
Chat History Retrieval: Uses pyautogui to select and copy chat history to the clipboard.
Message Processing: Filters out messages from the user and processes messages from other senders.
AI Response Generation: Sends the chat history to the AI21 API to generate a response.
Message Sending: Uses pyautogui to paste and send the AI-generated response.
Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.
