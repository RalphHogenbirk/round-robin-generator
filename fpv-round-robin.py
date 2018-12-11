# usage: python fpv-round-robin.py [rounds] [pilots_per_heat] [debug]

import random
import math
import time
import sys

# configuration
pilots = "Pilot 1,Pilot 2,Pilot 3,Pilot 4,Pilot 5,Pilot 6,Pilot 7,Pilot 8,Pilot 9,Pilot 10,Pilot 11,Pilot 12".split(',')
n_rounds = 15
n_per_heat = 4
debug_info = False

# grab arguments
args = sys.argv
if len(args) >= 2:
    n_rounds = int(args[1])

if len(args) >= 3:
    n_per_heat = int(args[2])

if len(args) >= 4:
    debug_info = bool(args[3])

# global usage vars
n_heats = int(math.ceil(len(pilots) / float(n_per_heat)))
rounds = []
pilot_matches = {}
pilot_combinations = {}
pilot_last_channel = {}
pilot_i = 0
round_pilots = []

# main function
def generate():
    global pilot_i, round_pilots, rounds

    # prepare global vars
    fill_matches()

    #rounds
    for round_i in range(n_rounds):
        debug("Generating round "+str(round_i))
        debug(dict_to_sorted_list(pilot_combinations))

        # randomize pilot name list before each round
        random.shuffle(pilots)
        debug(pilots)

        round_pilots = []
        pilot_i = 0
        rounds.append([])

        #heats
        round_score = 0
        for heat_i in range(n_heats):
            rounds[round_i].append([])
            # if(round_i > 0):
            best_score = 10000
            max_score = 0
            match = None

            # genarate 4 heats, pick best one
            for i in range(4):
                match_pilots,score,max = generate_next_heat(round_pilots)
                debug("Generated match with score: "+str(score)+" (max "+str(max)+")")
                if score < best_score or (score == best_score and max < max_score):
                    match = match_pilots
                    best_score = score
                    max_score = max

            debug(match)
            if match:
                debug("picked match: "+str(score)+" / "+str(max_score))
                round_score += best_score
                if round_i > 0:
                    match = rearrange_channels(match)

                position = 0
                for m in match:
                    add_pilot_to_heat(round_i,heat_i,m,position)

                    position+=1

            store_heat(rounds[round_i][heat_i])
            i = 0
            for p in rounds[round_i][heat_i]:
                if not p:
                    rounds[round_i][heat_i][i] = "<empty>"
                i+=1

        round_score = 0
        for heat in rounds[round_i]:
            debug(heat)

    time.sleep(0.1)


def generate_next_heat(pilots_to_exclude):
    debug("Find next match")

    sorted_list = shuffle_sort(pilot_combinations) # returns a sorted list of tupels: [('name-name2',score),]
    match_score = 0
    max_score = 0
    matches = None
    for item in sorted_list:
        matched_pilots = item[0].split("-")
        if matched_pilots[0] not in pilots_to_exclude and matched_pilots[1] not in pilots_to_exclude:
            debug("Found match: "+matched_pilots[0]+" vs "+matched_pilots[1]+": "+str(item[1]))
            matches = matched_pilots
            match_score = item[1]
            max_score = match_score
            break

    if matches:
        while len(matches) < n_per_heat and len(pilots_to_exclude)+len(matches) < len(pilots):
            pilot,score = find_next_opponent(matches,pilots_to_exclude)
            match_score += score
            if score > max_score:
                max_score = score
            matches.append(pilot)

    return [matches,match_score, max_score]

def find_next_opponent(matches,exclude):
    values = {}
    max_score = 0
    for pilot in pilots:
        if not pilot in exclude and not pilot in matches:
            values[pilot] = 0
            for match in matches:
                score = pilot_matches[pilot][match]
                values[pilot] += score
                # if score > max_score:
                #     max_score = score

    # list = shuffle_dict(values)
    sorted_list = shuffle_sort(values)
    i = 0
    while i < len(sorted_list):
        p = sorted_list[i][0]
        score = sorted_list[i][1]
        debug(sorted_list)
        if p not in exclude and p not in matches:
            if score > max_score:
                max_score = score
            debug("Found pilot for this heat: "+p+" ("+str(score)+")")
            return [p,score]
        i+=1

# Add pilot to this heat
def add_pilot_to_heat(round,heat,pilot,position):
    global pilot_i, round_pilots, rounds
    rounds[round][heat].append(pilot)
    pilot_i += 1
    round_pilots.append(pilot)
    pilot_last_channel[pilot] = position

# Tries to put pilots on same positions as last heat
def rearrange_channels(heat):
    new_heat = [None] * n_per_heat

    pos = 0
    for p in heat:
        lc = pilot_last_channel[p]
        if lc and lc != pos and not new_heat[lc]:
            new_heat[lc] = p
        pos += 1

    for p in heat:
        if p not in new_heat:
            new_heat[new_heat.index(None)] = p

    return new_heat

# update globals with new heat
def store_heat(heat_list):
    for pilot in heat_list:
        for opponent in heat_list:
            if opponent != pilot and pilot and opponent:
                pilot_matches[pilot][opponent] += 1
                pilot_combinations[pilot +"-"+opponent] += 1

# pre-fill global pilot matches variables
def fill_matches():
    for pilot in pilots:
        pilot_matches[pilot] = {}
        pilot_last_channel[pilot] = None
        for opponent in pilots:
            if(opponent != pilot):
                pilot_matches[pilot][opponent] = 0
                pilot_combinations[pilot +"-"+opponent] = 0

# sorts a dict
# Returns: sorted list [('key',value),('key2',value2),]
def dict_to_sorted_list(d):
    return sorted(d.items(), key=lambda kv: kv[1])

# Shuffles and than sorts a dict
# Returns: sorted list [('key',value),('key2',value2),]
def shuffle_sort(d):
    items = d.items()
    random.shuffle(items)
    return sorted(items, key=lambda kv: kv[1])

def debug(s):
    if debug_info:
        print(s)

# Plots results
def plot():

    for i,round in enumerate(rounds):
        print("Round "+str(i+1))
        i=1
        for heat in round:
            print("Heat "+str(i)+"," + (",".join(heat)))
            i+=1

    if debug_info:
        print(pilot_matches)
        print(dict_to_sorted_list(pilot_combinations))


# start
generate()

# plot results
plot()
