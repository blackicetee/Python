def depth_search(state):
    evaluations = []
    for action in actions(state):
        state.make_move(action)
        evaluations.append((evaluate(state), action))
        state.undo_move()
    if state.count_of_game_tokens_in_game() % 2 == 0:
        evaluations = sorted(evaluations, reverse=True)
    elif state.count_of_game_tokens_in_game() % 2 == 1:
        evaluations = sorted(evaluations)
    return evaluations