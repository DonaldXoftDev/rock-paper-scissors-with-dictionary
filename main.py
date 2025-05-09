import random
import ascii_arts

options = {
    'rock': ascii_arts.rock,
    'paper' : ascii_arts.paper,
    'scissors': ascii_arts.scissors,
}

winning_options = {
    'rock': ascii_arts.scissors,
    'paper': ascii_arts.rock,
    'scissors':  ascii_arts.paper,
}


def game_logic():
    player_choice = input('enter a choice from either rock, paper, scissors: ').lower()
    if player_choice not in options:
        print('invalid choice chosen!')
        return game_logic()

    player_image = options[player_choice]
    computer_choice = random.choice(list(options.values()))

    print(f'player chose: \n {player_image}')
    print(f'Computer chose:\n {computer_choice}')

    for key, value in winning_options.items():
        if player_image ==  computer_choice:
            print("It's a tie!")
            break
        if player_choice == key and computer_choice == value:
            print('You win')
        elif player_choice == key and computer_choice != value:
            print('You lose')

    play_again = input('Do you want to play again'
                       '? ').lower()
    if play_again == 'yes':
        game_logic()
    elif play_again == 'no':
        print(print('Goodbye!'))


game_logic()

