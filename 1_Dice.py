import random
import pylab

Dice_values = []

number = int(input("Please specify the number of times you want to roll the dice:\n"))

for i in range(number):
    The_amount_of_dice_rolled = random.randint(1,6)
    Dice_values.append(The_amount_of_dice_rolled)

counter_of_each_number =[]
for item in range (1,7):
    counter_of_each_number.append(Dice_values.count(item))


#print dice values with probability of it
for item in range (0,6):
    print("dice roll at {} for {} times and probability of this number is : {}".format(item+1,counter_of_each_number[item],(counter_of_each_number[item]/number)))

#show plot
pylab.hist(Dice_values, bins= [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5])
pylab.xlabel('Value')
pylab.ylabel('Count')
pylab.savefig('1_Dice_Rolled-{} times.png'.format(number))
pylab.show()
