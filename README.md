# Quiz-Game
This project is based on Python using GUI (Tkinter)


#Python Quiz Application
This is a Python application that presents a quiz with multiple-choice questions. The quiz consists of five questions related to Python programming. The application has several features, including a timer, hint system, review of answers, and the ability to replay the quiz.

#Features

1. Quiz Questions: The application loads the quiz questions, options, and correct answers from a JSON file.

2. Timer: A timer is implemented to keep track of the time remaining for each question. When the timer runs out, the application automatically moves to the next question.

3. Hint System: For each question, the user can access a hint by clicking the "Hint" button. The hint provides a clue to help the user find the correct answer.

4. Answer Review: After completing the quiz, the user can review their answers by clicking the "SOLUTION" button. A separate window displays all the questions, correct answers, and the user's selected answers.

5. Replay: The user has the option to replay the quiz by clicking the "RE ATTEMPT" button after completing the quiz.
Graphical User Interface (GUI): The application utilizes the Tkinter library to create a graphical user interface, making it user-friendly and visually appealing.
Modules

#The application is organized into several modules:

main.py: The main entry point of the application, responsible for creating the root window and initializing the Quiz class.

timer_module.py: This module contains the Timer class, which manages the timer functionality for each question.

hint_module.py: The Hint class in this module handles the display of hints for each question.

background_module.py: This module sets up the background image for the application window.

review_module.py: The ReviewModule class in this module is responsible for displaying the review window, which shows all the questions, correct answers, and the user's selected answers.

replay_module.py: This module contains the ReplayModule class, which handles the functionality of replaying the quiz.
Usage

To run the application, simply execute the main.py file. The quiz window will appear, and you can start answering the questions. Follow the on-screen instructions to navigate through the quiz, access hints, review answers, and replay the quiz if desired.


Requirements

Python 3.x

Tkinter library (usually included with Python installations)
