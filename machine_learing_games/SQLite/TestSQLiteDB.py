import unittest

from machine_learing_games.SQLite.SQLiteDB import SQLiteDB


class TestInitializeDB(unittest.TestCase):
    def test_initialize_10_transitions(self):
        test_db = SQLiteDB('test.db')
        test_db.drop_transitionTable()
        test_db = SQLiteDB('test.db')
        for i in range(10):
            test_db.insert_transposition(str(i + 10000), -1, 100, -100, str((0,0)), 5, 'X')
        print test_db.get_usefulness_of_zobrist_hash_entry(str(10001))
        print test_db.get_best_move_of_zobrist_hash_entry(str(10001))


class TestDeleteDB(unittest.TestCase):
    def delete_complete_test_db(self):
        test_db = SQLiteDB('test.db')
        test_db.drop_transitionTable()