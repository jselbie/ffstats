import math

angry_faces = [
    135.78,
    106.96,
    136.12,
    82.80,
    87.74,
    98.30,
    99.72,
    107.72,
    122.80,
    74.00,
    131.38,
    151.92,
    99.42,
    158.78,
]
ocsi_clean = [
    89.98,
    110.68,
    112.76,
    119.48,
    92.26,
    130.00,
    90.68,
    83.10,
    98.52,
    89.12,
    103.08,
    121.62,
    105.08,
    108.80,
]
blitz = [
    84.20,
    115.10,
    86.42,
    127.58,
    121.80,
    127.80,
    115.50,
    96.60,
    104.00,
    92.24,
    90.22,
    108.86,
    115.50,
    118.00,
]
backups_and_running_backs = [
    123.72,
    95.70,
    95.98,
    119.30,
    127.06,
    126.90,
    113.16,
    132.60,
    124.80,
    84.34,
    140.66,
    108.30,
    103.80,
    166.78,
]
puckachu_i_choose_you = [
    80.16,
    103.22,
    96.26,
    88.74,
    147.88,
    86.62,
    84.88,
    129.58,
    94.82,
    121.64,
    133.74,
    89.96,
    136.04,
    142.02,
]
hock_tua = [
    102.22,
    66.48,
    107.08,
    98.94,
    125.12,
    84.22,
    87.94,
    86.86,
    108.80,
    123.70,
    120.68,
    123.08,
    112.28,
    60.98,
]
aria_read_for_some_football = [
    101.94,
    128.84,
    96.90,
    79.30,
    108.54,
    126.14,
    95.06,
    118.68,
    121.84,
    73.14,
    108.34,
    68.36,
    75.94,
    103.00,
]
kamara_sutra = [
    87.38,
    146.34,
    95.48,
    110.38,
    115.90,
    99.66,
    111.80,
    145.70,
    102.46,
    113.04,
    96.40,
    92.10,
    92.90,
    109.66,
]
cincinnati_harambes = [
    75.52,
    95.62,
    110.34,
    111.62,
    92.76,
    65.16,
    99.86,
    128.84,
    91.40,
    97.08,
    112.14,
    96.86,
    120.72,
    89.62,
]
guess_who_fumbles = [
    102.96,
    101.36,
    99.26,
    111.68,
    97.86,
    99.72,
    92.54,
    120.16,
    124.62,
    115.42,
    100.74,
    79.98,
    109.56,
    152.36,
]
to_infinity_and_bijan = [
    129.78,
    106.86,
    89.08,
    112.92,
    103.92,
    110.76,
    105.14,
    117.34,
    86.26,
    124.08,
    94.24,
    111.70,
    158.14,
    128.80,
]
sofa_king_awesome = [
    81.66,
    119.80,
    105.70,
    139.58,
    87.94,
    126.28,
    104.94,
    81.60,
    95.52,
    92.40,
    125.48,
    82.42,
    79.46,
    71.12,
]


def get_initial_team_table() ->dict[str,list[int]] :
    team_table = {}
    team_table["angry_faces"] = angry_faces
    team_table["osci_clean"] = ocsi_clean
    team_table["blitz"] = blitz
    team_table["backups_and_running_backs"] = backups_and_running_backs
    team_table["puckachu_i_choose_you"] = puckachu_i_choose_you
    team_table["hock_tua"] = hock_tua
    team_table["aria_read_for_some_football"] = aria_read_for_some_football
    team_table["kamara_sutra"] = kamara_sutra
    team_table["cincinnati_harambes"] = cincinnati_harambes
    team_table["guess_who_fumbles"] = guess_who_fumbles
    team_table["to_infinity_and_bijan"] = to_infinity_and_bijan
    team_table["sofa_king_awesome"] = sofa_king_awesome
    return team_table

def factorial(n):
    return math.factorial(n)

def get_list_perumtation(l,p):
    result = l[:] # copy
    index = len(result)
    for i in range(len(result)):
        swap_index = i + p % index
        result[i],result[swap_index] = result[swap_index],result[i]
        p  = p // index
        index -= 1
    return result

def get_opponent_list(team_name, tt):
    result = []
    for team in tt:
        if (team != team_name):
            result.append(team)
    return result

def run_analysis():
    team_table = get_initial_team_table()
    for team in team_table:
        opponents = get_opponent_list(team, team_table)
        assert(len(opponents) == 11)
        max_permutations = math.factorial(len(opponents))
        highest_wins = -1
        lowest_wins = 999999
        highest_wins_counts = 0
        lowest_wins_counts = 0
        winning_seasons = 0
        tied_seasons = 0
        losing_seaons = 0
        for p in range(max_permutations):
            # if (p % 100000 == 0):
            #    print(p)
            schedule_list = get_list_perumtation(opponents, p)
            schedule_list.extend(schedule_list[0:3])  # add the first three opponents to the end
            assert(len(schedule_list) == 14)
            wins = 0
            losses = 0
            weeks = len(schedule_list)
            for week in range(weeks):
                this_team_score = team_table[team][week]
                other_team_score = team_table[schedule_list[week]][week]
                if (this_team_score > other_team_score):
                    wins += 1
                else:
                    losses += 1
            if (wins == highest_wins):
                highest_wins_counts += 1
            elif (wins > highest_wins):
                highest_wins = wins
                highest_wins_counts = 1

            if (wins == lowest_wins)           :
                lowest_wins_counts += 1
            elif  (wins < lowest_wins):
                lowest_wins = wins
                lowest_wins_counts = 1

            if (wins > losses):
                winning_seasons += 1
            elif (wins == losses):
                tied_seasons += 1
            else:
                losing_seaons += 1
        print("team: ", team)
        print("winning season percentage: ", (100*winning_seasons)/max_permutations)
        print("non-losing season percentage: ", (100*(winning_seasons+tied_seasons))/max_permutations)
        print("losing season percentage: ", (100*(losing_seaons))/max_permutations)
        print("best record: ", highest_wins, "wins  percentage:", (100*highest_wins_counts)/max_permutations)
        print("worst record: ", lowest_wins, "wins  percentage:", (100*lowest_wins_counts)/max_permutations)
        print("\n\n")


def dump_stats():
    team_table = get_initial_team_table()
    for team in team_table:
        scores = team_table[team]
        total_points = sum(scores)
        print(team, total_points)


run_analysis()
