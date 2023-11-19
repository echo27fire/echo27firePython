'''
Author: Taylor Goodspeed
Date: 11-4-2023
Program: lab11b - Capital Quiz
'''
import random


def load_capital_file(filename):
    """
    Loads a file containing country-capital pairs and returns a dictionary with the data.

    Args:
        filename (str): The name of the file to load.

    Returns:
        dict: A dictionary containing the state-capital pairs.
    """
    with open(filename, 'r') as file:
        return dict(line.strip().split(',') for line in file)


def quiz_the_user(state_capitals):
    """
    This function quizzes the user on state capitals. It randomly selects a state from the dictionary of state capitals,
    prompts the user to enter the capital of that state, and checks if the user's answer is correct. If the user's answer
    is correct, it prints "That's correct!" and increments the number of correct answers. If the user's answer is incorrect,
    it prints the correct answer and moves on to the next question. The function returns the number of correct answers.
    
    Args:
    state_capitals (dict): A dictionary containing the names of states as keys and their corresponding capitals as values.
    
    Returns:
    int: The number of correct answers.
    """
    correct = 0
    total = len(state_capitals)
    for question in range(total):
        state = random.choice(list(state_capitals.keys()))
        capital = state_capitals.pop(state)
        user_answer = input(f"What is the capital of {state}? ").strip()
        if user_answer.lower() == capital.lower():
            print("That's correct!")
            correct += 1
        else:
            print(f"Incorrect! The capital of {state} is {capital}.")
    return correct


def save_quiz_results(username, difficulty, score, total, filename):
    """
    Saves the quiz results to a file.

    Args:
        username (str): The username of the quiz taker.
        difficulty (str): The difficulty level of the quiz.
        score (int): The number of questions answered correctly.
        total (int): The total number of questions in the quiz.
        filename (str): The name of the file to save the results to.

    Returns:
        None
    """
    with open(filename, 'a') as file:
        file.write(f"{username}, {difficulty}, {score}/{total} correct, {score/total:.2%}\n")


def main():
    """
    This function loads a state capitals quiz file based on user input, prompts the user to take the quiz,
    saves the user's score to a file, and displays the user's score to the console.
    """
    easy_mode = 'easy_state_capitals.txt'
    med_mode = 'medium_state_capitals.txt'
    hard_mode = 'hard_state_capitals.txt'

    records_file = 'capitals_quiz_results.txt'

    while True:
        difficulty = input("Load Easy, Medium, or Hard mode file? (press 'q' to quit): ").upper()
        if difficulty == 'Q':
            print("Exiting the quiz.")
            return
        elif difficulty == 'EASY':
            filename = easy_mode
        elif difficulty == 'MEDIUM':
            filename = med_mode
        elif difficulty == 'HARD':
            filename = hard_mode
        else:
            print("Invalid difficulty, please try again.")
            continue

        states_capitals = load_capital_file(filename)
        total = len(states_capitals)  # Set total before the quiz starts and states are popped

        username = input("Enter your name: ")
        score = quiz_the_user(states_capitals)

        total_questions = total  # Use total directly instead of subtracting len(states_capitals)
        print(f"{username}, you have achieved a score of {score} out of {total_questions} correct responses.")
        save_quiz_results(username, difficulty, score, total_questions, records_file)
        break

if __name__ == "__main__":
    main()
