print('###############################')
print('wellcome to the hangman game!!')
print('###############################')

secret_word = 'abacate'
dead = False
right = False



while not dead and not right:
    print('jogando...\n')
    c = 6
    guess = input('Guess one character\n')
    index = 0
    for character in secret_word:
        if guess == character:
            print('The secret word has {} in the position: {}'.format(character, index+1))
        index = index + 1
        
        

print('Game over')