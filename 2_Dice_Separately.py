import random
import pylab

Dice_1_values = []
Dice_2_values = []
number = int(input("Please specify the number of times you want to roll the dice :"))

for i in range(number):
    The_amount_of_dice_1_rolled = random.randint(1,6)
    The_amount_of_dice_2_rolled = random.randint(1,6)
    Dice_1_values.append(The_amount_of_dice_1_rolled)
    Dice_2_values.append(The_amount_of_dice_2_rolled)

counter_of_each_number_Dice_1 =[]
counter_of_each_number_Dice_2 =[]
for item in range (0,6):
    counter_of_each_number_Dice_1.append(Dice_1_values.count(item))
    counter_of_each_number_Dice_2.append(Dice_2_values.count(item))

#print dice 2 values with probability of it
print("\nDeice 1 result:\n")

for item in range (0,6):
    print("dice roll at {} for {} times and probability of this number is : {}".format(item+1,counter_of_each_number_Dice_1[item],(counter_of_each_number_Dice_1[item]/number)))

print("\nDeice 2 result:\n")

#print dice 1 values with probability of it
for item in range (0,6):
    print("dice roll at {} for {} times and probability of this number is : {}".format(item+1,counter_of_each_number_Dice_2[item],(counter_of_each_number_Dice_2[item]/number)))

#show plots
pylab.figure(1)
pylab.hist(Dice_1_values, bins= [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
pylab.xlabel('Value')
pylab.ylabel('Count')
pylab.savefig('2_dice_separately-1_Rolled-{} times.png'.format(number))

pylab.figure(2)
pylab.hist(Dice_2_values, bins= [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
pylab.xlabel('Value')
pylab.ylabel('Count')
pylab.savefig('2_dice_separately-2_Rolled-{} times.png'.format(number))

pylab.show()
