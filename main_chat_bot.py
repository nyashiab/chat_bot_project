# main_chat_bot.py
# Description: This program has a chat bot that learns from the user.

import json
from difflib import get_close_matches

# Load the knowledge base from a JSON file
def load_knowledge_path(file_path: str) -> dict:
    with open(file_path, 'r') as file: # open the file path in read mode as file
        data: dict = json.load(file) # The data of type dictionary is going to equal json.load
    return data

# Function that saves the knowledge or save the dictionary to the knowledge base so 
# that the next time we start the program we will have the old responses also in the memory
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent = 2)
# ^^ insert that data into the Json this is going to put our Json or our dictionary of responses back into the Json file so
# that we can load it later once again

# Function that finds the best match from the dictionary
def find_best_match(user_question: str, questions: list[str]) -> str | None: # there's a chance that what it's looking for inside the
# knowledge base might not exist then we need to create some matches which is going to be of type list 
    matches: list = get_close_matches(user_question, questions, n = 1, cutoff= 0.6)
    return matches[0] if matches else None

# Function that gets the answer for each question 
def get_answer_for_question(question : str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        
def chat_bot(): #function for the chat_bot to learn from its user
    knowledge_base: dict = load_knowledge_path('knowledge_base.json')

    while True:
        user_input: str = input ("You: ") #user input to chat with the bot

        if user_input.lower() == "quit": #checks for all ways user could type "quit"
            print (f"Leaving chat bot...") 
            break #breaks off of program

        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]]) #within arguments there's a list comprehension

        if best_match: #if statement for when there's a best match
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print (f"Bot: {answer}")
        else:
            print (f"Bot: I don\'t know the answer. Can you teach me, please?")
            new_answer: str = input (f"Type the answer or 'skip' to skip: ")

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                print (f"Bot: Thank you! I learned a new response!")

if __name__ == '__main__':
    chat_bot()