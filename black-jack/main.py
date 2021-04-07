from new_game import Game

def evaluateScore(player):
    hand = player[0]
    hand_value = player[1]
    if not hand:
        return
    for i in hand:
        if i == 'A':
            hand_value
        # TODO: Handle Ace Logic
        elif i in ['J', 'Q', 'K']:
            hand_value += 10
        else:
            hand_value += int(i)
    if hand_value <= 21:
        return True
    return False

def turn(game_state, player):
    print(f"It is Player {player}s turn. What would you like to do?")
    while True:
        prompt = input("Would you like to: 1) Hit or 2) Stay? [1/2] : ")
        if prompt in ['1', '2']:
            break
    if prompt == '1': # deal a card
        game_state.dealCard(player)
        if evaluateScore(game_state.players[player]): 
            turn(game_state, player)
        else:
            return
    elif prompt == '2': # don't deal a card
        return


def main ():
    game = Game()
    print("Welcome")
    number_of_players = int(input("Input the number of players: "))
    game.addPlayers(number_of_players)
    for player in game.players:
        turn(game, player)
    print(game.players)

if __name__ == "__main__":
    main()