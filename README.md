# Python ChatBot

## Description
Python ChatBot is a simple text-based chat program written in Python. It automatically responds to basic user inputs like greetings, questions about its well-being, and its name. This project is ideal for beginners to practice Python concepts such as **functions**, **loops**, and **conditional statements**.

## Features
- Responds to common greetings: `HI`, `HELLO`
- Answers questions like: `HOW ARE YOU`, `WHAT IS YOUR NAME`
- Handles unrecognized inputs with a default response
- Runs in a loop until the user chooses to exit
- Beginner-friendly and easy to extend

## How it Works
1. The program runs in a **while loop** until the user exits.
2. Converts user input to **uppercase** for consistent checking.
3. The `ChatBot()` function checks input and prints appropriate responses.
4. Type `1` to exit the program.

## Example Interaction
start : hi
Hey there! How can I help you.

start : how are you
I'm fine what about you?

start : what is your name
I am a basic Python ChatBot.

start : bye
Bye! Have a nice day.

start : 1
Exiting...

markdown
Copy code

## How to Run
1. Make sure Python 3.x is installed.
2. Clone or download this repository.
3. Open terminal or command prompt in the project folder.
4. Run the program:
```bash
python chatbot.py
Start chatting! Enter 1 to exit.
