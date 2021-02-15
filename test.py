#!/usr/bin/python3.8

import json
import re
from collections import OrderedDict

episodes = [
    "Game of thrones S2 e4",
    "Game of thrones S2 e8",
    "game of Thrones S1 e2",
    "Firefly Season 1 Episode5",
    "dexter s3 e3",
    "Firefly Season 1 Episode7",
    "Dexter Season1 Episode4",
    "Dexter Season1 Episode2",
    "dexter s4 e3",
    "game of Thrones S1 e6",
    "Game of thrones S2 e7",
    "Firefly Season 1 Episode1",
    "Dexter S5 e1",
    "game of Thrones S1 e4",
    "dexter s4 e4",
    "dexter s4 e2",
    "Game of thrones S2 e1",
    "game of Thrones S1 e9",
    "Dexter S5 e2",
    "dexter s3 e1",
    "dexter s2 e1",
    "Game of thrones S2 e6",
    "Firefly Season 1 Episode8",
    "Firefly Season 1 Episode3",
    "game of Thrones S1 e3",
    "Game of thrones S2 e3",
    "dexter s3 e4",
    "game of Thrones S1 e7",
    "Dexter S5 e3",
    "Game of thrones S2 e2",
    "Dexter S5 e4",
    "Firefly Season 1 Episode2",
    "Game of thrones S2 e5",
    "game of Thrones S1 e8",
    "Game of thrones S2 e9",
    "dexter s2 e3",
    "dexter s2 e2",
    "Firefly Season 1 Episode9",
    "Dexter Season1 Episode3",
    "Firefly Season 1 Episode6",
    "game of Thrones S1 e5",
    "dexter s2 e4",
    "Dexter Season1 Episode1",
    "dexter s4 e1",
    "Firefly Season 1 Episode4",
    "game of Thrones S1 e1",
    "dexter s3 e2"
]

# 1. List series in alphabetical order
def vod_list():
    epi = sorted(episodes)
    count = 0
    for items in epi:
        print(items.lower())
        count += 1
    print(f'Total VOD: {count}')
    print('Enf of sorted list\n')

# 2. Search for series by part of name
def grep_name():
    epi = sorted(episodes)
    new_epi = []
    for x in epi:
        new_epi.append(x.lower())

    matches = []
    name = "game"           # <--- Insert string here
    count = 0
    for match in new_epi:
        if name in match:
            count += 1
            matches.append(match)
            print(match.replace("season", "s").replace("episode", "e"))

    print(f'Total VODs: {count}')


# 3. List seasons in each series
def list_season():
    epi = sorted(episodes)
    new_epi = []
    for x in epi:
        new_epi.append(x.lower())

    matches = []
    name = "game"  # <--- Insert string here
    season_count = 0

    for match in new_epi:
        if name in match:
            season_count += 1
            matches.append(match)
            res = (match.replace("season", "s").replace("episode", "e"))
            print(res)

            season_name = []
            pattern = re.compile(r'[s]\d')
            ok = pattern.finditer(res)
            for x in ok:
                season_name.append(x)

            final = list(dict.fromkeys(season_name))
            print(final)




# 4. List episodes in each seasone


def main():
    #vod_list()     # 1. List series in alphabetical order
    #grep_name()    # 2. Search for series by part of name
    list_season()   # 3. List seasons in each series

if __name__ == "__main__":
    main()