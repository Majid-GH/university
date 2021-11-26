import random

#function for simulate Penalties
def Penalty_Kick(number):

    #save the results
    Total_Score = []

    #Explanation of abbreviations
    '''
    LB = Left Bottom
    LT = Left Top
    RB = Right Bottom
    RT = Right Top
    CB = Center Bottom
    CT = Center Top
    '''
    for numbers in range(1,number+1):
        #goalkeeper could jump to this possible direction or stay in center
        Goalkeeper = random.choice(["LB", "LT", "Center", "CenterB", "CenterT", "RB", "RT"])

        #The Player can shoot the ball to any of the these possible places
        Player = random.choice(["LB", "LT", "Center", "CenterB", "CenterT", "RB", "RT", "Out"])

        #give a chance between from 1 to 3 to goalkeeper and Player
        Goalkeeper_Chance = random.randint(1,3)
        Player_Chance = random.randint(1,3)

        #Checking for the results
        if Player == 'Out':
            Total_Score.append([Goalkeeper, Player, "Saved!"])
        elif Goalkeeper == Player:
            if Player_Chance > Goalkeeper_Chance:
                Total_Score.append([Goalkeeper, Player, "Goal!"])
            elif Goalkeeper_Chance > Player_Chance:
                Total_Score.append([Goalkeeper, Player, "Saved!"])
            else:
                Total_Score.append(random.choice([[Goalkeeper, Player, "Saved!"],[Goalkeeper, Player, "Goal!"]]))
        else:
            Total_Score.append([Goalkeeper, Player, "Goal!"])

    return Total_Score

#main program

#each team have 5 shots
Team1_Penalty_Kicks = Penalty_Kick(5)
Team2_Penalty_Kicks = Penalty_Kick(5)

#variables used for counting scores and select Winner
Team1_Total_Scores = 0
Team2_Total_Scores = 0
Winner = ""

#loops for counting the scores (reminder: use .zip function later for these two for )
for item in Team1_Penalty_Kicks:
    if item[2] == "Goal!":
        Team1_Total_Scores += 1

for item in Team2_Penalty_Kicks:
    if item[2] == "Goal!":
        Team2_Total_Scores += 1

#cheack if the scores are even then go for extra shoot
while Team1_Total_Scores == Team2_Total_Scores:
    Team1_Extra_Penalty_Kicks = Penalty_Kick(1)
    Team2_Extra_Penalty_Kicks = Penalty_Kick(1)
    if Team1_Extra_Penalty_Kicks[0][2] == "Goal!":
        Team1_Total_Scores +=1
    if Team2_Extra_Penalty_Kicks[0][2] == "Goal!":
        Team2_Total_Scores +=1
#select Winner based on Total Scores
if Team1_Total_Scores > Team2_Total_Scores:
    Winner = "Team 1"
elif Team2_Total_Scores > Team1_Total_Scores:
    Winner = "Team 2"
#print the results
print("the Winner team is: {}".format(Winner))
