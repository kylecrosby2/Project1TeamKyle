#! python3

import time
import csv
import os


# Function to calculate every combination of coins in the jar. 
def dumb_sat_coins(n, jar, start):

    combinations = [[]]
    found = []
    # Iteratively finds every combination. 
    for coin in jar:
        new_combos = []
        for combo in combinations:
            # Timeout at 60 seconds
            if time.time() - start > 60:
                return ["timed out"]
            new_combos.append(combo + [coin])
            # Breaks and returns if correct combination found
            if sum(new_combos[-1]) == n: 
                found = new_combos[-1]
                break     
        combinations += new_combos

    return found # returns [] if unsatisfiable


def main():
    # Creates csv to store output
    file = open("output/output_teamkyle.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["Number of variables", "Exec Time (microseconds)", "Target", "Combo"])

    # Loops through all test files (each has different number of coins in jar)
    for input_filename in os.listdir("input"):
        input_file = open(os.path.join("input", input_filename))
        for line in input_file.readlines():

            n = int(line.split(',')[1])
            jar = list(map(int, line.split(',')[2:]))

            # Runs function on jar and target (n). Keeps start time to log total exec time. 
            start = time.time()
            combo = dumb_sat_coins(n, jar, start)
            end = time.time()
            exec_time=int((end-start)*1e6)

            # print(f"Exec time: {exec_time}μs for value {n}, jar {jar}")
            # if combo: print(f"Coin combination found: {combo}")
            # else: print("No combination found")

            # Writes result to output csv
            writer.writerow([len(jar), exec_time, n, combo])
        
        input_file.close()
            
    file.close()


if __name__ == '__main__':
    main()