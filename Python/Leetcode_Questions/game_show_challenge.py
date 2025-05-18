from numpy import random

def runGame(n:int, pick_new: bool):
    
    wins = 0
    plays = 0
 
    for i in range(n):
        prize_list = ['g', 'g', 'g']
        ranIntCar = random.randint(0,3)
        prize_list[ranIntCar] = 'c'

        randIntPick = random.randint(0,3)
        openedDoor = 0
        for i in range(len(prize_list)):
            if i != randIntPick and prize_list[i] == 'g':
                openedDoor = i
                break

        new_pick = 3 -(openedDoor+randIntPick)
        #print(f'new pick: {new_pick} OD: {openedDoor}  ranPick: {randIntPick}')
        if pick_new == False and prize_list[randIntPick] == 'c':
            wins += 1
        elif pick_new == True and prize_list[new_pick] == 'c':
            wins += 1
        
        plays += 1
    
    percent = (wins*100)/plays
    print(f"Wins: {wins}  Plays: {plays}  Win %: {percent}")
        

        

def main():
    n =100000
    runGame(n,True)
    runGame(n,False)

if __name__ == '__main__':
    main()

