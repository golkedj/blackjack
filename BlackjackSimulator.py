from BlackjackGame import *

def main():
    print("Blackjack Simulator")

    for x in range(1, 11):
        print("Starting game " + str(x) + " of 10")
        current_game = BlackjackGame()
        while not current_game.game_done:
            current_game.take_turn()

if __name__ == "__main__":
    main()