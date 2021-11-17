# Author Yongdong Xi (Nov 17)
import random

# Question 1
Days = input("Which day today?")

str(Days in ['a', 'c', 'e', 'A', 'C', 'E'])
if str(Days in ['a', 'c', 'e', 'A', 'C', 'E']) == 'True':
    print('You have class today because it is {0} day.'.format(Days))
else:
    print('You do not have class today because it is {0} day.'.format(Days))

# Question 3

population2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
random.sample(population2, k=3)
guess = input("What three numbers do you get?")
anws = list(random.sample(population2, k=3))
guess1 = list.guess()
guess1.sort() = anws.sort()