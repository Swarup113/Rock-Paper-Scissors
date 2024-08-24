def player(prev_play, opponent_history=[], play_order={}):
    # Track the opponent's moves
    if prev_play:
        opponent_history.append(prev_play)

    # Default play
    guess = "R"

    if len(opponent_history) >= 2:
        # Build play_order if not already done
        if len(opponent_history) == 2:
            for i in ["R", "P", "S"]:
                for j in ["R", "P", "S"]:
                    play_order[i + j] = 0

        # Update the play_order dictionary with the latest pair of moves
        last_two = "".join(opponent_history[-2:])
        play_order[last_two] += 1

        # Predict the opponent's next move
        potential_plays = [opponent_history[-1] + "R",
                           opponent_history[-1] + "P", opponent_history[-1] + "S"]
        
        # Find the most likely next move based on history
        prediction = max(potential_plays, key=lambda x: play_order[x])

        # Counter the predicted move
        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        guess = ideal_response[prediction[-1]]

    return guess
