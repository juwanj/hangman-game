import random

def mask_word(word):
    return ''.join('*' if c.isalpha() else c for c in word)

def uncover_word(answer_word, masked_word, guessed_letter):
    guessed_letter = guessed_letter.lower()
    result = ''
    for a_char, m_char in zip(answer_word, masked_word):
        if a_char.lower() == guessed_letter:
            result += a_char
        else:
            result += m_char
    return result

def get_random_word(word_list):
    return random.choice(word_list)

def start_new_game(word_list):
    word, hint = get_random_word(word_list)
    return {
        'answer_word': word,
        'hint': hint,
        'masked_word': mask_word(word),
        'previous_guesses': []
    }

def guess(game, letter):
    letter = letter.lower()
    if letter in game['previous_guesses']:
        print(f"You already guessed '{letter}'. Try a different letter.")
        return
    game['previous_guesses'].append(letter)
    if letter in game['answer_word'].lower():
        game['masked_word'] = uncover_word(game['answer_word'], game['masked_word'], letter)
        print(f"Nice! '{letter}' is in the word.")
    else:
        print(f"Oops! '{letter}' is NOT in the word.")

def play_game():
    words = [
        ('Juwan', "It's my name!"),
        ('Orange juice', "A popular breakfast drink"),
        ('Running', "A form of exercise or sport")
    ]
    game = start_new_game(words)

    print("Welcome to Hangman! Try to guess the word letter by letter.")
    print(f"Hint: {game['hint']}")
    print(f"Word to guess: {game['masked_word']}")

    while '*' in game['masked_word']:
        guess_letter = input("Guess a letter (or type 'hint' to see the hint): ").strip()
        if guess_letter.lower() == 'hint':
            print(f"Hint: {game['hint']}")
            continue
        if len(guess_letter) != 1 or not guess_letter.isalpha():
            print("Please enter a single alphabetical letter.")
            continue

        guess(game, guess_letter)
        print("Current word:", game['masked_word'])
        print("Previous guesses:", ', '.join(game['previous_guesses']))

    print(f"Congrats! You guessed it: {game['answer_word']}")

if __name__ == "__main__":
    play_game()