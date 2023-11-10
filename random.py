import random
import xml.etree.ElementTree as ET

def load_config():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

def play_game(x1, x2, n):
    target_number = random.randint(x1, x2)
    
    for _ in range(n):
        guess = int(input(f"Guess a number between {x1} and {x2}: "))
        
        if guess < target_number:
            print("Too low. Try again.")
        elif guess > target_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the correct number: {target_number}")
            break
    else:
        print(f"Sorry, you've reached the maximum number of guesses. The correct number was {target_number}")

if __name__ == "__main__":
    x1, x2, n = load_config()
    play_game(x1, x2, n)
