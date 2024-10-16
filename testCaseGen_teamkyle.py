#! python3

import argparse
import random
from datetime import datetime
import textwrap

def generate(num_vars, size):
  # Handle arguments
  # parser = argparse.ArgumentParser(
  #   prog='knapsackTestCaseGen',
  #   formatter_class=argparse.RawDescriptionHelpFormatter,
  #   description='Creates a given number each of small, medium, and large test cases for the knapsack problem.',
  #   epilog=textwrap.dedent('''
  #       The range for total value, number of coins, and coin size can be configured within the code.
  #       The cases are in format "casetype, totalvalue, coin1value, coin2value, coin3value,...'''))
  
  # parser.add_argument("--file", "-f", required=True, type=argparse.FileType('w'),
  #                     help="File to print test cases to (Will overwrite data).")
  # parser.add_argument("--size", "-s", required=True, type=int,
  #                     help="Number of test cases to generate.")
  
  # args = parser.parse_args()

  # # If something went wrong and the file cannot be opened, exit with error
  # if (not args.file):
  #   print("Error opening file.")
  #   return
  
  # Otherwise, print test cases to file

  # Set the total value range for the small, medium, and large test cases
  # Format: [[easy min val, easy max val], [med min, med max], [large min, large max]]
  # testcaseTotalValueRange = [[1e2, 1e3], [1e4, 1e5], [1e6, 1e7]]

  file = open(f"input/{num_vars}_coins.txt", "w")

  testcaseTotalValueRange = [[0, 100], [100, 1000], [1000, 10000]]
  # convert float values to ints
  testcaseTotalValueRange = [[int(x[0]), int(x[1])] for x in testcaseTotalValueRange]
  
  # Set the maximum coin value for the small, medium, and large test cases
  # Default is [25, 25, 25] to make them all 25 cents, but could be changed
  testcaseMaxCoinValue = [25, 25, 25]

  # Set the number of coin values to generate (default is 4)
  numCoins = num_vars

  # Set the case types
  testcaseTypes = ["Small", "Medium", "Large"]

  # Set randomization seed
  random.seed(datetime.now().timestamp())
  for testSize, vals in enumerate(testcaseTotalValueRange):
    for _testcase in range(size):
      file.write(f"{testcaseTypes[testSize]}")
      file.write(f", {random.randint(testcaseTotalValueRange[testSize][0], testcaseTotalValueRange[testSize][1])}")
      for coin in range(numCoins):
        file.write(f", {random.randint(1, testcaseMaxCoinValue[testSize])}")
      file.write("\n")

  # Close the file once we are done
  file.close()


def main():

  for i in range(1, 21):
    generate(i, 100)


if __name__ == '__main__':
  main()