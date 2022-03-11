import random
import constants
from ladders import ldrStartPotistion
from snakes import snake

n  = ldrStartPotistion()

s = snake()

def gameplay():
    Target = 100
    score = 0
    count=0
    while True:
        if score==Target:
            print("WOW GREATE JOB YOU WIN THE GAME")
            break
        x=input("PLAY ")
        if x=='D':
            dice = random.randint(1,6)
            if (score+dice)>Target:
                print('Over Input Dice')
                print('Dice:',dice)
                print('NOW SCORE:',score,"\n")
                print('Needed Dice: ',Target-score,"\n")
            else:
                print('Dice:',dice)
                score =score+dice
                print('NOW SCORE',score,"\n")
                if score==1:
                    print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+n[0], "\n")
                    score=score+n[0]
                    print('NOW SCORE:',score,"\n")
                elif score==4:
                    print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+n[1], "\n")
                    score=score+n[1]
                    print('NOW SCORE:',score,"\n")
                elif score==9:
                    print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+n[2], "\n")
                    score=score+n[2]
                    print('NOW SCORE:',score,"\n")
                elif score==21:
                    print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+n[3], "\n")
                    score=score+n[3]
                    print('NOW SCORE:',score,"\n")
                elif score==28:
                    print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+n[4], "\n")
                    score=score+n[4]
                    print('NOW SCORE:',score,"\n")
                elif score==51:
                    print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+n[5], "\n")
                    score=score+n[5]
                    print('NOW SCORE:',score,"\n")
                elif score==72:
                    print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+n[6], "\n")
                    score=score+n[6]
                    print('NOW SCORE:',score,"\n")
                elif score==80:
                    print("**LUCKKY YOU GOT LADDER** LADDER STARTS AT" ,score, "AND LADDER END AT" ,score+n[7], "\n")
                    score=score+n[7]
                    print('NOW SCORE:',score,"\n")

                    #snake cammends
                elif score==17:
                    print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-s[0], "\n")
                    score=score-s[0]
                    print('NOW SCORE:',score)
                elif score==54:
                    print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-s[1], "\n")
                    score=score-s[1]
                    print('NOW SCORE:',score)
                elif score==62:
                    print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-s[2], "\n")
                    score=score-s[2]
                    print('NOW SCORE:',score)
                elif score==64:
                    print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-s[3], "\n")
                    score=score-s[3]
                    print('NOW SCORE:',score)
                elif score==87:
                    print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-s[4], "\n")
                    score=score-s[4]
                    print('NOW SCORE:',score)
                elif score==93:
                    print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-s[5], "\n")
                    score=score-s[5]
                    print('NOW SCORE:',score)
                elif score==95:
                    print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-s[6], "\n")
                    score=score-s[6]
                    print('NOW SCORE:',score)
                elif score==98:
                    print("**UNLUCKKY SNAKE SWALLOWED** SNAKE HEAD",score," AND SNAKE TAIL" ,score-s[7], "\n")
                    score=score-s[7]
                    print('NOW SCORE:',score)
        else:
                print("Wrong Input..Please Press 'D' \n")
        count+=1
    print("NO.OF DICE ROLLED:",count,"\n")      
    print("                            ##  THE GAME END  ##                        \n") 

    x=input() #it will help  when run in idle to see winner messege