def run_quiz():
    # Initialize score
    score = 0
    
    # Quiz questions
    questions = [
        {
            "question": "What is the output of print('Hello'[0]) in Python?",
            "options": ["Hello", "H", "Error", "0"],
            "correct": 1
        },
        {
            "question": "Which actor played Neo in The Matrix?",
            "options": ["Tom Hanks", "Keanu Reeves", "Leonardo DiCaprio", "Johnny Depp"],
            "correct": 1
        },
        {
            "question": "What is the result of 5 % 2 in Python?",
            "options": ["2", "1", "3", "0"],
            "correct": 1
        },
        {
            "question": "In what year was the first Star Wars movie released?",
            "options": ["1975", "1977", "1980", "1983"],
            "correct": 1
        },
        {
            "question": "What does the Python function len() do?",
            "options": ["Calculates the square root", "Returns the length", "Sorts a list", "Reverses a string"],
            "correct": 1
        }
    ]
    
    # Ask each question
    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for j, option in enumerate(q['options']):
            print(f"{j + 1}. {option}")
        
        # Get user's answer
        while True:
            try:
                answer = int(input("\nEnter your answer (1-4): ")) - 1
                if 0 <= answer <= 3:
                    break
                print("Please enter a number between 1 and 4")
            except ValueError:
                print("Please enter a valid number")
        
        # Check if correct
        if answer == q['correct']:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {q['options'][q['correct']]}")
    
    # Display final score
    print(f"\nQuiz complete! Your final score is {score} out of {len(questions)}")
    return score

def main():
    while True:
        run_quiz()
        
        # Ask to play again
        while True:
            play_again = input("\nWould you like to play again? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            print("Please enter 'yes' or 'no'")
        
        if play_again == 'no':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    print("Welcome to the Python & Movies Quiz!")
    main()
