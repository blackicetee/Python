from random import randint

from machine_learing_games.Reversi.Reversi import Reversi
from machine_learing_games.tictactoe.TicTacToe import TicTacToe


def getRandomAction(possibleActionList):
    return possibleActionList[randint(0, (len(possibleActionList) - 1))]

def processTicTacToeAction(ticTacToeState):
    if not isTicTacToeStateTerminal(ticTacToeState):
        randomTicTacToeAction = getRandomAction(ticTacToeState.get_possible_moves())
        ticTacToeState.make_move(randomTicTacToeAction)

def getRandomTerminalTicTacToeState():
    ttt = TicTacToe(4)
    while not isTicTacToeStateTerminal(ttt):
        ttt.make_move(getRandomAction(ttt.get_possible_moves()))
    return ttt

def getRandomNonTerminalTicTacToeState():
    ttt = TicTacToe(4)
    randomDepth = randint(0, 15)
    for depth in range(randomDepth):
        if not ttt.is_victory():
            ttt.make_move(getRandomAction(ttt.get_possible_moves()))
    if ttt.is_victory():
        ttt.undo_move()
    return ttt

def isTicTacToeStateTerminal(ticTacToeState):
    if ticTacToeState.is_victory():
        return True
    elif not ticTacToeState.is_victory() and ticTacToeState.count_of_game_tokens_in_game() == ticTacToeState.get_maximal_amount_of_game_tokens():
        return True
    else:
        return False

def processReversiAction(reversiState=Reversi()):
    if not reversiState.is_victory():
        randomReversiAction = getRandomAction(reversiState.suggest_moves(reversiState.player_to_move()))
        reversiState.make_move(randomReversiAction[0])

def getRandomTerminalReversiState():
    reversi = Reversi()
    while not reversi.is_victory():
        playerToMove = reversi.player_to_move()
        if playerToMove != 'Game Over':
            possible_moves = reversi.suggest_moves(playerToMove)
            randomAction = getRandomAction(possible_moves)
            reversi.make_move(randomAction[0])
    return reversi

def getRandomNonTerminalReversiState():
    reversi = Reversi()
    randomDepth = randint(0, 63)
    for depth in range(randomDepth):
        playerToMove = reversi.player_to_move()
        if not reversi.is_victory():
            possible_moves = reversi.suggest_moves(playerToMove)
            randomAction = getRandomAction(possible_moves)
            reversi.make_move(randomAction[0])
    return reversi