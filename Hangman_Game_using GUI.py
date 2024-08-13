import tkinter as tk
import random
import string
from tkinter import messagebox

# List of words to choose from
words = ['python', 'javascript', 'ruby', 'java', 'csharp', 'swift','hammad']

# Create the GUI window
root = tk.Tk()
root.title("Hangman")
root.geometry("800x600")  # Set a larger window size

# Create a frame for the game
game_frame = tk.Frame(root)
game_frame.pack(pady=20)

# Create a frame for the hangman image
hangman_frame = tk.Frame(game_frame)
hangman_frame.pack()

# Create a frame for the word
word_frame = tk.Frame(game_frame)
word_frame.pack()

# Create a frame for the guessed letters
guessed_letters_frame = tk.Frame(game_frame)
guessed_letters_frame.pack()

# Create a frame for the incorrect guesses
incorrect_guesses_frame = tk.Frame(game_frame)
incorrect_guesses_frame.pack()

# Create a frame for the buttons
button_frame = tk.Frame(game_frame)
button_frame.pack()

# Create the hangman images
hangman_images = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png', '8.png', '9.png', '10.png']

# Initialize incorrect guesses
incorrect_guesses = 0

# Load the initial hangman image
hangman_image = tk.PhotoImage(file=hangman_images[incorrect_guesses])
hangman_label = tk.Label(hangman_frame, image=hangman_image)
hangman_label.pack()

# Create the word label
word = random.choice(words)
word_label = tk.Label(word_frame, text='_ ' * len(word), font=('Helvetica', 24))  # Larger font size
word_label.pack()

# Create the guessed letters label
guessed_letters = []
guessed_letters_label = tk.Label(guessed_letters_frame, text='Guessed letters: ', font=('Helvetica', 14))
guessed_letters_label.pack()

# Create the incorrect guesses label
incorrect_guesses_label = tk.Label(incorrect_guesses_frame, text='Incorrect guesses: 0', font=('Helvetica', 14))
incorrect_guesses_label.pack()

# Create the keyboard layout
keyboard_layout = [
    'qwertyuiop',
    'asdfghjkl',
    'zxcvbnm'
]


# Function to reset the game
def reset_game():
    global word, incorrect_guesses, guessed_letters, hangman_image
    word = random.choice(words)
    incorrect_guesses = 0
    guessed_letters = []
    word_label['text'] = '_ ' * len(word)
    incorrect_guesses_label['text'] = 'Incorrect guesses: 0'
    guessed_letters_label['text'] = 'Guessed letters: '

    # Reset to initial image
    hangman_image = tk.PhotoImage(file=hangman_images[0])
    hangman_label['image'] = hangman_image
    hangman_label.image = hangman_label['image']

    create_keyboard_buttons()  # Recreate keyboard buttons
    reset_button.pack(pady=10)  # Show reset button again
    retry_button.pack_forget()  # Hide retry button
    play_again_button.pack_forget()  # Hide play again button


# Function to handle letter guesses
def guess_letter(letter):
    global word_label, guessed_letters_label, incorrect_guesses_label, hangman_image, hangman_label, hangman_images, guessed_letters, incorrect_guesses, word

    if letter in word:
        indices = [i for i, char in enumerate(word) if char == letter]
        for i in indices:
            word_label['text'] = word_label['text'][:2 * i] + letter.upper() + word_label['text'][2 * i + 1:]

        # Check for win condition
        if '_' not in word_label['text']:  # Check if there are no underscores left
            messagebox.showinfo("Congratulations!", f"Hurrah! You have guessed the correct word: {word.upper()}!",
                                icon='info')
            play_again_button.pack()  # Show play again button
            reset_button.pack_forget()  # Hide reset button
            return
    else:
        incorrect_guesses += 1  # Increment incorrect guesses
        if incorrect_guesses < len(hangman_images):  # Check if we have more images
            hangman_image = tk.PhotoImage(file=hangman_images[incorrect_guesses])
            hangman_label['image'] = hangman_image
            hangman_label.image = hangman_label['image']
            incorrect_guesses_label['text'] = 'Incorrect guesses: ' + str(incorrect_guesses)
        else:
            word_label['text'] = f'Game Over! The word was: {word}'
            hangman_label['image'] = tk.PhotoImage(file=hangman_images[-1])  # Show final hangman image
            retry_button.pack()  # Show retry button
            reset_button.pack_forget()  # Hide reset button

    guessed_letters.append(letter)
    guessed_letters_label['text'] = 'Guessed letters: ' + ', '.join(sorted(set(guessed_letters)))


# Create buttons for the keyboard layout
def create_keyboard_buttons():
    for widget in button_frame.winfo_children():
        widget.destroy()  # Clear previous buttons

    for row in keyboard_layout:
        row_frame = tk.Frame(button_frame)
        row_frame.pack(pady=5)  # Add some vertical space between rows
        for letter in row:
            button = tk.Button(row_frame, text=letter, command=lambda l=letter: guess_letter(l), width=5, height=2,
                               font=('Helvetica', 12))  # Larger buttons
            button.pack(side=tk.LEFT)


# Create Play Again, Retry, and Reset buttons
play_again_button = tk.Button(root, text="Play Again", command=lambda: [reset_game(), play_again_button.pack_forget(),
                                                                        retry_button.pack_forget()],
                              font=('Helvetica', 14))
retry_button = tk.Button(root, text="Retry",
                         command=lambda: [reset_game(), play_again_button.pack_forget(), retry_button.pack_forget()],
                         font=('Helvetica', 14))
reset_button = tk.Button(root, text="Reset", command=reset_game, font=('Helvetica', 14))
reset_button.pack(pady=10)  # Always show the reset button

# Start the GUI
create_keyboard_buttons()  # Create the keyboard buttons for the first time
root.mainloop()