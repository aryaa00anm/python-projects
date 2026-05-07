#START

print("HELLO PLAYER\n")

#DIFFICULTY

print("SET DIFFICULTY")
diff = int(input("Enter max range : "))

#GENERATING NUMBER

import random
gen = random.randint(0,diff)

#SETTING VALUES FOR "ATTEMPTS" "HIGHSCORE"

attempts = 0
highscore = float('inf')

#GAME LOOP
flagADMIN = 0
while True :
             

             #GUESS LOOP
             while True :
                         #ASKING FOR GUESS

                         inp = int(input("TAKE A GUESS : "))

                         #ATTEMPTS COUNTER

                         attempts += 1

                         #CHECKING RANGE

                         if inp in range(0,(diff+1)) :
                                 
                                 #IF CORRECT

                                 if inp == gen :
                                         print("YOU WIN !!\n")
                                         print("ATTEMPTS TAKEN : ",attempts," \n")
                                         if attempts < highscore :
                                                 highscore = attempts
                                         print("HIGHSCORE:", highscore, "ATTEMPTS")
                                         flag = 0
                                         while True:
                                                 op = int(input("ENTER 1 TO PLAY AGAIN \nENTER 2 TO EXIT: "))
                                                 if op == 1:
                                                         flag = 1
                                                         break
                                                 elif op == 2:
                                                         flag = 2
                                                         break
                                                 else :
                                                         print("WRONG INPUT\n     ")
                                                         pass
                                         if flag == 1 :
                                                 flagADMIN = 1 #RE-RUN MAIN GAME LOOP
                                                 break
                                         if flag == 2 :
                                                 flagADMIN = 2 #EXIT MAIN GAME LOOP
                                                 break
                                         
                                 #IF WRONG

                                 else :
                                         print("OOPS ! WRONG ")
                                         flag = 0
                                         while True:
                                                 op = int(input("ENTER 1 FOR MORE GUESSES \nENTER 2 TO EXIT: "))
                                                 if op == 1:
                                                         flag = 1
                                                         break
                                                 elif op == 2:
                                                         flag = 2
                                                         print("YOU LOOSE !\nNUMBER WAS-",gen)
                                                         if highscore == float('inf'):
                                                                 print("HIGHSCORE: No wins yet")
                                                         else :
                                                                 print("HIGHSCORE:", highscore, "ATTEMPTS")
                                                         break
                                                 else :
                                                         print("WRONG INPUT\n     ")
                                                         pass
                                         if flag == 1 :
                                                 pass
                                         if flag == 2 :
                                                 flagADMIN = 2
                                                 break
                         else :
                                 print("NUMBER NOT IN RANGE")
                                 pass
                         
             # DECISION FOR MAIN GAME LOOP
             if flagADMIN == 1 :
               attempts = 0
               gen = random.randint(0,diff)
               pass
                        
             elif flagADMIN == 2 :
                print("BYE")
                break
                         


                                        

                                                
                                    

           

