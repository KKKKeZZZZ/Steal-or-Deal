#
# File:      26852_game.py
# Author:    Ke Zhang
# SAIBT Id:  26852
# Version:   1.0  26 March 2017
# Description: Assignment part I
#   This is my own work as defined by the University's
#   Academic Misconduct policy.
#
import random
# set the list
titlesList = ['Steal','Deal', 'Comp steal', 'Comp deal']
countsList = [0, 0, 0, 0]
#basic setting
S = "Steal"
D = "Deal"
Q = "Quit"
index = 0
times = 0
wins = 0
loses = 0
drawns = 0
totalMan = 0
totalCom = 0
stealsKeep = 0
y = 'y'

ask = input("Would you like to play Steal or Deal [y|n]? ")
# input check 
while ask != 'y' and ask != 'n':
    print("Please enter either 'y' or 'n'.\n")
    ask = input("Would you like to play Steal or Deal [y|n]? ")
    
if ask == 'n':
    print("\nNo worries... another time perhaps... :)\n\n")
elif ask == "y":
    print("\n1. Always steal\n2. Always deal\n3. Random\n")
    
    # choose level of computer
    level = input("Which strategy for the computer [1,2,3]? ")
    while level != '1' and level != '2' and level != '3':
        print("Please enter either 1, 2, or 3.")
        level = input("Which strategy for the computer [1,2,3]? ")
        
# computer level 1
if ask == "y" and level == '1':
    chooseCom = "S"
#the while loop to play 10 times game
    while times <= 10:
# reach the game limited
        if times == 10:
            print("\nGame limit reached.\n")
            print("\nGame Result")
            print("============")
            print("\nYou played",times,"games:")
            print("  |--> Won:     ",wins)
            print("  |--> Lost:    ",loses)
            print("  |--> Drawn:   ",drawns)
            print("  |--> Winnings:",totalMan)
            print("\n\nGame Statistics: ")
            print("\nChoice        Frequency")
            
            #for loop to show the frequency
            for title in titlesList:
                print(format((title+":"),'<14s'),("*" * countsList[index]),sep = "")
                index += 1
            print("\nThanks for playing!\n\n")
            times = 11
            
        # different situation 
        else:
            print("\n\nJackppot: 200")
            chooseMan = input("Steal, Deal or Quit [S|D|Q]? ")
            while chooseMan != 'S' and chooseMan != 'D' and chooseMan !='Q':
                print("Please enter either 'S', 'D' or 'Q'.\n")
                chooseMan = input("Steal, Deal or Quit [S|D|Q]? ")

            if chooseMan == "D"and chooseCom == "S":
                print("     You     |    Computer ")
                print("--------------------------")
                print("C:   Deal    |    Steal")
                print("S:   0       |    200")
                print("         You lose!")
                print("     You get nothing! \n\n")
                totalMan += 0
                totalCom += 200
                print("     You     |    Computer ")
                print("---------- Total ----------")
                print(format(totalMan, '>6d'),"      |   ",format(totalCom, '>6d'))
                times += 1
                loses += 1
                countsList[1] += 1
                countsList[2] += 1
                stealsKeep = 0

            elif chooseMan == "S"and chooseCom == "S":
                stealsKeep += 1
                print("     You     |    Computer ")
                print("--------------------------")
                print("C:   Steal   |    Steal")
                print("S:   0       |    0   ")
                print("        Too greedy!")
                print("     You get nothing! ")
                totalMan += 0
                totalCom += 0
                
                #user keep stealing waring & punishment
                if stealsKeep == 2:
                    print("\nCareful… one more steal and you lose it ALL!")
                if stealsKeep == 3:
                    print("\nI told you so... you lose all of your winnings!")
                    totalMan = 0
                    stealsKeep = 0
                    
                print("\n\n     You     |    Computer ")
                print("---------- Total ----------")
                print(format(totalMan, '>6d'),"     |   ",format(totalCom, '>6d') ) 
                times +=1
                drawns += 1
                countsList[0] += 1
                countsList[2] += 1
                
            #use Q to quit and time equal to 0
            elif times == 0 and chooseMan == 'Q':
                print("\nNo worries... another time perhaps... :)\n\n")
                times = 11

            # user input Q to quit the game
            else:
                print("\nGame Result")
                print("============")
                if times == 1:
                    print("\nYou played",times,"game:")
                else:
                    print("\nYou played",times,"games:")
                print("  |--> Won:     ",wins)
                print("  |--> Lost:    ",loses)
                print("  |--> Drawn:   ",drawns)
                print("  |--> Winnings:",totalMan)
                print("\n\nGame Statistics: ")
                print("\nChoice        Frequency")

                for title in titlesList:
                    print(format((title+":"),'<14s'),("*" * countsList[index]),sep = "")
                    index += 1
                print("\nThanks for playing!\n\n")
                times = 11
                
# computer level 2
elif  ask == "y" and level == '2':

    while times <= 10:
        #result when limit reach
        if times == 10:
            print("\nGame limit reached.\n")
            print("\nGame Result")
            print("============")
            print("\nYou played",times,"games:")
            print("  |--> Won:     ",wins)
            print("  |--> Lost:    ",loses)
            print("  |--> Drawn:   ",drawns)
            print("  |--> Winnings:",totalMan)
            print("\n\nGame Statistics: ")
            print("\nChoice        Frequency")

            for title in titlesList:
                print(format((title+":"),'<14s'),("*" * countsList[index]),sep = "")
                index += 1
            print("\nThanks for playing!\n\n")
            times = 11
            
        else:
            print("\n\nJackppot: 200")
            chooseCom = "D"
            chooseMan = input("Steal, Deal or Quit [S|D|Q]? ")

            while chooseMan != 'S' and chooseMan != 'D' and chooseMan !='Q':
                print("Please enter either 'S', 'D' or 'Q'.")
                print("")
                chooseMan = input("Steal, Deal or Quit [S|D|Q]? ")
            #draw situation
            if chooseMan == "D"and chooseCom == "D":
                print("     You     |    Computer ")
                print("--------------------------")
                print("C:   Deal    |    Deal")
                print("S:   100     |    100   ")
                print("           Draw!")
                print("       Split pot!\n\n")
           
                totalMan += 100
                totalCom += 100
                print("     You     |    Computer ")
                print("---------- Total ----------")
                print(format(totalMan, '>8d',),"    |",format(totalCom, '>9d'))
                
                times +=1
                drawns += 1
                stealsKeep = 0
                countsList[1] += 1
                countsList[3] += 1
            # win situation    
            elif chooseMan == "S"and chooseCom == "D":
                stealsKeep += 1
                print("     You     |    Computer ")
                print("--------------------------")
                print("C:   Steal   |    Deal")
                print("S:   200     |    0   ")
                print("         You win!")
                print("         Jackpot! ")
                
                totalMan += 200
                totalCom += 0

                if stealsKeep == 2:
                    print("\nCareful… one more steal and you lose it ALL!")
                if stealsKeep == 3:
                    print("\nI told you so... you lose all of your winnings!")
                    totalMan = 0
                    stealsKeep = 0
                print("\n\n     You     |    Computer ")
                print("---------- Total ----------")
                print(format(totalMan, '>8d'),"    |",format(totalCom, '>9d'))
                times +=1
                wins += 1
                countsList[0] += 1
                countsList[3] += 1
            # no game then Q
            elif times == 0 and chooseMan == 'Q':
                print("\nNo worries... another time perhaps... :)\n\n")
                times = 11
            # result when enter Q
            else:
                print("\nGame Result")
                print("============")
                if times == 1:
                    print("\nYou played",times,"game:")
                else:
                    print("\nYou played",times,"games:")
                print("  |--> Won:     ",wins)
                print("  |--> Lost:    ",loses)
                print("  |--> Drawn:   ",drawns)
                print("  |--> Winnings:",totalMan)
                print("\n\nGame Statistics: ")
                print("\nChoice        Frequency")

                for title in titlesList:
                    print(format((title+":"),'<14s'),("*" * countsList[index]),sep = "")
                    index += 1
                print("\nThanks for playing!\n\n")
                times = 11                  

#computer level 3
elif ask == "y" and level == '3':
    while times <= 10:

        #result when limit reached
        if times == 10:
            print("\nGame limit reached.\n")
            print("\nGame Result")
            print("============")
            print("\nYou played",times,"games:")
            print("  |--> Won:     ",wins)
            print("  |--> Lost:    ",loses)
            print("  |--> Drawn:   ",drawns)
            print("  |--> Winnings:",totalMan)
            print("\n\nGame Statistics: ")
            print("\nChoice        Frequency")
            for title in titlesList:
                print(format((title+":"),'<14s'),("*" * countsList[index]),sep = "")
                index += 1
            print("\nThanks for playing!\n\n")
            times = 11 
             
        else:
            print("\n\nJackppot: 200")
            chooseCom = random.choice("SD")
            chooseMan = input("Steal, Deal or Quit [S|D|Q]? ")

            while chooseMan != 'S' and chooseMan != 'D' and chooseMan !='Q':
                print("Please enter either 'S', 'D' or 'Q'.")
                print("")
                chooseMan = input("Steal, Deal or Quit [S|D|Q]? ")
                
            #draw situation
            if chooseMan == "D"and chooseCom == "D" :
                print("     You     |    Computer ")
                print("--------------------------")
                print("C:   Deal    |    Deal")
                print("S:   100     |    100   ")
                print("           Draw!")
                print("       Split pot!\n\n")
              
                totalMan += 100
                totalCom += 100
                print("     You     |    Computer ")
                print("---------- Total ----------")
                print(format(totalMan, '>8d'),"    |",format(totalCom, '>9d'))
                
                times +=1
                drawns += 1
                countsList[1] += 1
                countsList[3] += 1
                stealsKeep = 0
                chooseCom = random.choice("SD")

            #lose situation
            elif chooseMan == "D"and chooseCom == "S":
                print("     You     |    Computer ")
                print("--------------------------")
                print("C:   Deal    |    Steal")
                print("S:   0       |    200")
                print("         You lose!")
                print("     You get nothing! \n\n")
               
                totalMan += 0
                totalCom += 200

                print("     You     |    Computer ")
                print("---------- Total ----------")
                print(format(totalMan, '>8d'),"    |",format(totalCom, '>9d'))
               
                times += 1
                loses += 1
                stealsKeep = 0
                countsList[1] += 1
                countsList[2] += 1
                chooseCom = random.choice("SD")

            #draw situation
            elif chooseMan == "S"and chooseCom == "S":
                stealsKeep += 1
                print("     You     |    Computer ")
                print("--------------------------")
                print("C:   Steal   |    Steal")
                print("S:   0       |    0   ")
                print("        Too greedy!")
                print("     You get nothing! ")
               
                totalMan += 0
                totalCom += 0

                if stealsKeep == 2:
                    print("\nCareful… one more steal and you lose it ALL!")
                if stealsKeep == 3:
                    print("\nI told you so... you lose all of your winnings!")
                    totalMan = 0
                    stealsKeep = 0
                    

                print("\n\n     You     |    Computer ")
                print("---------- Total ----------")
                print(format(totalMan, '>8d'),"    |",format(totalCom, '>9d'))
                
                times +=1
                drawns += 1
                countsList[0] += 1
                countsList[2] += 1
                chooseCom = random.choice("SD")

            #win situation
            elif chooseMan == "S"and chooseCom == "D":
                stealsKeep += 1
                print("     You     |    Computer ")
                print("--------------------------")
                print("C:   Steal   |    Deal")
                print("S:   200     |    0   ")
                print("         You win!")
                print("         Jackpot! ")
            
                totalMan += 200
                totalCom += 0

                if stealsKeep == 2:
                    print("\nCareful… one more steal and you lose it ALL!")
                if stealsKeep == 3:
                    print("\nI told you so... you lose all of your winnings!")
                    totalMan = 0
                    stealsKeep = 0

                print("\n\n     You     |    Computer ")
                print("---------- Total ----------")
                print(format(totalMan, '>8d'),"    |",format(totalCom, '>9d'))
                times +=1
                wins += 1
                countsList[0] += 1
                countsList[3] += 1
                chooseCom = random.choice("SD")

            #when 0 game is played enter Q
            elif times == 0 and chooseMan == 'Q':
                print("\nNo worries... another time perhaps... :)\n\n")
                times = 11

            #result when enter Q
            else:    
                print("\nGame Result")
                print("============")
                if times == 1:
                    print("\nYou played",times,"game:")
                else:
                    print("\nYou played",times,"games:")
                print("  |--> Won:     ",wins)
                print("  |--> Lost:    ",loses)
                print("  |--> Drawn:   ",drawns)
                print("  |--> Winnings:",totalMan)
                print("\n\nGame Statistics: ")
                print("\nChoice        Frequency")

                for title in titlesList:
                    print(format((title+":"),'<14s'),("*" * countsList[index]),sep = "")
                    index += 1
                print("\nThanks for playing!\n\n")
                times = 11  
        
            
