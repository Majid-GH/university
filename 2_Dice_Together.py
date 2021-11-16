import random
import pylab

Dice_values = []

number = int(input("Please specify the number of times you want to roll the dices:\n"))

for i in range(number):
    The_amount_of_dice_rolled = random.randint(2,12)
    Dice_values.append(The_amount_of_dice_rolled)

counter_of_each_number =[]
for item in range (1,13):
    counter_of_each_number.append(Dice_values.count(item))

for item in range (1,12):
    print("dice roll at {} for {} times and probability of this number is : {}".format(item+1,counter_of_each_number[item],(counter_of_each_number[item]/number)))




pylab.hist(Dice_values, bins= [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5])
pylab.xlabel('Value')
pylab.ylabel('Count')
pylab.savefig('2_dice_together_Rolled-{} times.png'.format(number))
pylab.show()
