import random

# List of jokes - mixing programming and general humor
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "What's a programmer's favorite place? The foo bar!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "What do you call a bear with no teeth? A gummy bear!",
    "Why did the programmer quit his job? Because he didn't get arrays!",
    "What's the best thing about Switzerland? I don't know, but their flag is a big plus!",
    "Why do programmers always mix up Halloween and Christmas? Because Oct 31 = Dec 25!",
    "What did the Zen master say to the hot dog vendor? Make me one with everything!",
    "Why did the variable go to therapy? It was feeling a little undefined!",
    "What's a programmer's favorite snack? Cookies!"
]

def get_random_joke():
    """Returns a random joke from the list"""
    return random.choice(jokes)

def main():
    print("🎭 Welcome to the Joke Generator! 🎭")
    print("Here's your random joke:")
    print("\n" + get_random_joke())
    print("\nHope that made you laugh! 😄")

if __name__ == "__main__":
    main()
