"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload

from isolation import Board
from sample_players import RandomPlayer, GreedyPlayer


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    """
    Test: 1. minimax to return any legal move and that minimax() 
    Test: 3. raises SearchTimeout when the timer expires
    """

    def test_minimax_any_legal_move(self):
        best_moves = (0, 0)
        minimax_player = game_agent.MinimaxPlayer()
        minimax_move = minimax_player.get_move(self.game, lambda: 150)
        self.assertEqual(best_moves, minimax_move)

    """Test: 2. functionality of MinimaxPlayer.minimax() 

    Failed Test: 2. Test functionality of MinimaxPlayer.minimax() 
    ---------------------------------------------------------------------- AssertionError: False is not true : Your 
    MinimaxAgent.minimax function did not visit every node in the game tree as player 1.  First check for off-by-one 
    errors in your handling of the depth limiting. Then, especially if the number of nodes explored by your agent is too 
    low, check everywhere you call to game.get_legal_moves() to make sure you are getting the legal moves for the 
    appropriate player at each level of the game tree.  Finally, you may be using non-standard search optimizations that 
    are not supported by the test cases.  The range of expansions accepted will vary slightly within the range indicated 
    based on your termination condition. 
    
    Expected number of visited nodes -- min: 7 max: 7
    Number of nodes your agent explored: 281
    
    Test Case Details:
    ------------------
    Heuristic: open_move_score
    Depth limit: 1
    Initial Board State:
         0   1   2   3   4   5   6   7   8
    0  |   |   |   |   |   |   |   |   |   | 
    1  |   |   |   |   |   |   |   |   |   | 
    2  |   |   |   | 2 | - | - |   |   |   | 
    3  |   |   |   |   |   |   | - |   |   | 
    4  |   |   | - |   |   | - | - |   |   | 
    5  |   |   |   | - |   | - |   |   |   | 
    6  |   |   |   | - | 1 | - |   |   |   | 
    7  |   |   |   |   |   |   |   |   |   | 
    8  |   |   |   |   |   |   |   |   |   | 
    
    game._board_state: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 
    1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 29, 42] 

    """

    def test_minimax_visit_every_node_as_player_1(self):
        best_moves = (0, 0)
        minimax_player = game_agent.MinimaxPlayer()
        minimax_move = minimax_player.get_move(self.game, lambda: 150)
        self.assertEqual(best_moves, minimax_move)


    """
    Test: 4. Test that MinimaxPlayer successfully plays a full game
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    IndexError: list index out of range
    
    During handling of the above exception, another exception occurred:
    
    AssertionError: Your agent raised an error while attempting to play a complete game against another agent.  Make sure 
    that your agent can play an entire game -- including selecting initial moves on an empty board. Exception: list index 
    out of range 
    
    """

    def test_minimax_play_game_success(self):
        best_moves = (0, 0)
        minimax_player = game_agent.MinimaxPlayer()
        minimax_move = minimax_player.get_move(self.game, lambda: 150)
        self.assertEqual(best_moves, minimax_move)

    def test_alphabeta_7(self):
        player1 = game_agent.AlphaBetaPlayer()
        player2 = game_agent.AlphaBetaPlayer()
        game = Board(player1, player2)
        game.apply_move(game.get_legal_moves(player1)[0])
        winner, history, outcome = game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(game.to_string())
        print("Move history:\n{!s}".format(history))

if __name__ == '__main__':
    unittest.main()
