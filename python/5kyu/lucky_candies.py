"""
Simple Fun #314: Lucky Candies

Task
John bought a bag of candy from the shop. Fortunately, he became the 10000000000000000000000th customer of the XXX confectionery company. Now he can choose as many candies as possible from the company's prizes. With only one condition: the sum of all the candies he chooses must be multiples of k.

Your task is to help John choose the prizes, returns the maximum possible amount of candies that John can got.

Input/Output
[input] integer array prizes

The prizes of candies. Each element is a bag of candies. John can only choose the whole bag. Open bag and take some candies is not allowed ;-)

1 ≤ prizes.length ≤ 100

1 ≤ prizes[i] ≤ 5000000

[input] integer k

A positive integer.

2 ≤ k ≤ 20

[output] an integer

The maximum amount of candies that John can got. The number should be a multiples of k. If can not find such a number, return 0 instead.

Example
For prizes = [1,2,3,4,5] and k = 5, the output should be 15

1 + 2 + 3 + 4 + 5 = 15, 15 is a multiple of 5

For prizes = [1,2,3,4,5] and k = 7, the output should be 14

2 + 3 + 4 + 5 = 14, 14 is a multiple of 7
"""
def lucky_candies(prizes, k):
    
    prizes = sorted(prizes, reverse=True)
    sumPrizes = 0
    output = 0

    for prize in prizes:
        sumPrizes += prize
    
    output = sumPrizes/k
    print ('output: ' + output)
