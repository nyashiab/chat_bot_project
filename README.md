# chat_bot_project
How to install and use program:

1. Download the python and JSON files into a folder together
2. Go into your preferred IDE (i.e: VS Code) and open the folder you made
3. Skim through description and run the program


Description:

The Chat Bot Program is a interactive chatbot designed to communicate with users while continuously expanding its knowledge base. It achieves this by learning from user interactions and saving new information for future conversations. Here's how the program works:

Key Features:

1. Knowledge Base Integration:
-- The chatbot utilizes a JSON file to store and retrieve its knowledge base.
-- It reads existing questions and answers from the file during initialization.

2. Conversational Functionality:
-- Users can type any question or statement to interact with the bot.
-- The bot attempts to provide the most relevant response by finding the closest match to the user’s input from its knowledge base.
-- If the user types "quit," the chatbot gracefully ends the session.

3. Learning Capability:
-- If the chatbot cannot find a suitable match for the user's input, it politely asks the user for the correct answer.
-- Users can teach the chatbot by providing an answer, which the bot stores in its knowledge base.
-- This new information is saved to the JSON file, enabling the bot to respond to the same question in future sessions.

4. Best Match Detection:
-- The chatbot uses string similarity algorithms to find the best match for the user’s input.
-- A customizable cutoff ensures that only sufficiently similar questions are matched.

5. User-Friendly Design:
-- The bot provides clear prompts, such as asking for clarification when it doesn’t know an answer.
-- Users can skip teaching the bot by typing "skip."

6. Persistent Knowledge:
-- All learned responses are permanently saved, ensuring that the bot evolves and becomes more intelligent with each interaction.
