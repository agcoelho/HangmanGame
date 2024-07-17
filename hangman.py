print('###############################')
print('wellcome to the hangman game!!')
print('###############################')

secret_word = 'abacate'
correct = ["_", "_", "_", "_", "_", "_", "_",]
dead = False
right = False
c = 6



while not dead and not right:
    print('jogando...\n')
    
    guess = input('Guess one character\n')
    
    
    if guess in secret_word:
        
        index = 0
        for character in secret_word:
            if guess.upper() == character.upper():
                correct[index] = character
            index = index + 1
    else:
        print('theres no such character.\nTry again.')
        c = c - 1
        print('you still have {} try\n'.format(c))
        if c < 1:
            dead = True
            print('a palavra era: {}'.format(secret_word))

    if not dead:    
        print('{}\n'.format(correct))
        
        

print('Game over')