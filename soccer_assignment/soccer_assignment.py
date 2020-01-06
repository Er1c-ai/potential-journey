import argparse
import itertools
from _operator import itemgetter


class SoccerLeagueRankings:

    @staticmethod
    def open_csv_loop(input_file):
        """
        This functions opens the input file and reads the results from it
        :param input_file:
        :return: List which holds the team and goals scored
        """
        soccer_game_input = open(input_file, 'r')
        results = []
        for line in soccer_game_input:
            game = {}
            for item in line.split(','):
                item_split = item.strip().split(' ')
                name = ' '.join(item_split[:-1])
                goals = int(item_split[-1])
                game.update({name: goals})
            results.append(game)
        return results

    @staticmethod
    def scoring_update(t_scores, t_name, score):
        """
        This function is here to add the team and the score to the team_score
        :param t_scores:
        :param t_name:
        :param score:
        :return:
        """
        if t_name in t_scores:
            t_scores[t_name] += score
        else:
            t_scores.update({t_name: score})
            return t_scores

    @classmethod
    def loop_calculation(cls, g_results):
        """
        This function does the loop which works out the points for each team based on their win, loss or draw.
        :param g_results:
        :return:
        """
        team_scores = {}
        for game in g_results:
            team_list = list(game.keys())
            team_1 = team_list[0]
            team_2 = team_list[1]
            # Wining = 3 pts to winner
            if game[team_1] > game[team_2]:
                cls.scoring_update(team_scores, team_1, 3)
                cls.scoring_update(team_scores, team_2, 0)
            # draw = 1pt each
            elif game[team_1] == game[team_2]:
                cls.scoring_update(team_scores, team_1, 1)
                cls.scoring_update(team_scores, team_2, 1)
            # Losing = 0 pts to loser
            else:
                cls.scoring_update(team_scores, team_1, 0)
                cls.scoring_update(team_scores, team_2, 3)
        return team_scores
    
    @staticmethod
    def print_enumerated_file(team_scores):
        """
        This function sorts the team by most points and then alphabetically.
        It then prints out the result
        :param team_scores:
        :return:
        """
        rank = 0
        count = 0
        previous = None
        enumerated_list = sorted(team_scores.items(), key=lambda kv: (-kv[1], kv[0]))
        for index, (score, group) in enumerate(itertools.groupby(enumerated_list, itemgetter(1)), 1):
            for team, points in group:
                pts = 'pts'
                if points ==1:
                    pts="pt"
                count += 1
                if score != previous:
                    rank += count
                    previous = score
                    count = 0
                print(f'{rank}. {team}, {score} {pts}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="reading file")
    parser.add_argument('-i', '--input_file', type=str, required=True, help="reading file from input")
    args = vars(parser.parse_args())
    soccer_editor = SoccerLeagueRankings()
    game_results = soccer_editor.open_csv_loop(args['input_file'])
    team_scores = soccer_editor.loop_calculation(game_results)
    soccer_editor.print_enumerated_file(team_scores)
