import unittest

from soccer_assignment import SoccerLeagueRankings


class TestSoccerAssignment(unittest.TestCase):

    def setUp(self):
        self.sort = SoccerLeagueRankings()
        self.team_score = {'Lions': 5, 'Snakes': 1, 'Tarantulas': 6, 'FC_Awesome': 1, 'Grouches': 0}
        self.dic_data = [{'Lions': 3, 'Snakes': 3}, {'Tarantulas': 1, 'FC_Awesome': 0}, {'Lions': 1, 'FC_Awesome': 1},
                         {'Tarantulas': 3, 'Snakes': 1}, {'Lions': 4, 'Grouches': 0}]

    def test_equal_loop_func(self):
        new_output = self.sort.loop_calculation(self.dic_data)
        self.assertEqual(self.team_score, new_output)

    def test_not_equal_enumerate_func(self):
        new_output = self.sort.loop_calculation(self.dic_data)
        self.assertNotEqual(self.dic_data, new_output)

    def test_equal_enumerate_file(self):
        final_print = "1. Tarantulas, 6 pts 2. Lions, 5 pts 3. FC_Awesome, 1 pt 3. Snakes, 1 pt 5. Grouches, 0 pt"
        new_output = self.sort.print_enumerated_file(self.team_score)
        self.assertTrue(final_print, new_output)

    def test_not_equal_enumerate_file(self):
        new_output = self.sort.print_enumerated_file(self.team_score)
        self.assertNotEqual(self.team_score, new_output)

    def test_loop_non_string_should_fail(self):
        self.assertRaises(TypeError, self.sort.loop_calculation, 234)

    def test_loop_none_should_fail(self):
        self.assertRaises(TypeError, self.sort.loop_calculation, None)

    def test_enumerate_non_string_should_fail(self):
        self.assertRaises(AttributeError, self.sort.print_enumerated_file, 234)

    def test_enumerate_non_should_fail(self):
        self.assertRaises(AttributeError, self.sort.print_enumerated_file, None)


if __name__ == "__main__":
    unittest.main()
