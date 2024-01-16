# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():
    # Ensure correct usage -- checking # of command line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    teams = []  # list of teams

    # TODO: Read teams into memory from file
    file = open(
        sys.argv[1], "r"
    )  # Read file which will be the second command line argument sys.argv[1]
    reader = csv.DictReader(file)  # Convert file into dictionary

    for row in reader:
        team_name = row["team"]
        team_rating = int(row["rating"])  # cast ratings from string to int value
        teams.append(
            {"team": team_name, "rating": team_rating}
        )  # add items to teams list - create new dictionary because ratings are now int values

    # print(simulate_tournament(teams)) - test simulate_tournaments() func, pass in teams[]
    file.close()

    counts = {}  # team names with the # of times team won simulated tournament

    # TODO: Simulate N tournaments and keep track of win counts

    for i in range(N):
        winner_team = simulate_tournament(teams)
        if winner_team in counts:
            counts[
                winner_team
            ] += 1  # if the winning team is in counts, this means they have won a tournament and we increment counts if they win again
        else:
            counts[winner_team] = 1  # first time team has won

    # Print each team's chances of winning, according to simulation
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    # TODO
    while len(teams) > 1:  # there should only be one team remaining - winner
        teams = simulate_round(teams)
    return teams[0]["team"]  # return name of team that won tournament


if __name__ == "__main__":
    main()
