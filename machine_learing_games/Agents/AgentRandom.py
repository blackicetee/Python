from random import randint

from machine_learing_games.tictactoe.TicTacToe import TicTacToe


def getRandomAction(possibleActionList):
    return possibleActionList[randint(0, (len(possibleActionList) - 1))]

def getRandomTerminalTicTacToeState():
    ttt = TicTacToe(4)
    while not isTerminal(ttt):
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

def isTerminal(s):
    if s.is_victory():
        return True
    elif not s.is_victory() and s.count_of_game_tokens_in_game() == s.get_maximal_amount_of_game_tokens():
        return True
    else:
        return False