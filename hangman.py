import random
words_list = ['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard','boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon']
chosen_word = random.choice(words_list)
# print(chosen_word)

placeholder = "_" * len(chosen_word)
print(f"Word to guess : {placeholder}\n")

display = []
for char in chosen_word:
    display.append("_")

live = 6
while live != 0:
    print(f"        *************** lives : < {live} / 6 > ***************\n")

    guess = input("Guess a letter : \n").lower()

    if guess in display:
        print(f"You Have Guessed '{guess}' before. ")
    i = 0
    for letter in chosen_word:
        if guess == letter:
            display[i] = guess
        i += 1
    print("".join(map(str,display)))
    
    if guess not in chosen_word:
        live -= 1
        if live == 0:
            print("You Lose!")
    
    if list(chosen_word) == display:
        live = 0
        print("You Win!")