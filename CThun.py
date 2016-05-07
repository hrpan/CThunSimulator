from random import randint

enemyHP=int(input("Enemy HP: "))
cthunATK=int(input("Attack of C'Thun: "))
numMinions=int(input("Number of minions: "))

totEHP=[enemyHP]

for i in range(0,numMinions):
    inputPrompt="Minion %d HP: " %(i+1)
    minionHP=int(input(inputPrompt))
    totEHP.append(minionHP)

iterations=int(input("Number of iterations: "))

numWin=0

for i in range(0,iterations):
    tmp=totEHP[:]
    for j in range(0,cthunATK):
        target=randint(0,len(tmp)-1)
        tmp[target]-=1
        if tmp[0]==0:
            numWin+=1
            break
        elif tmp[target]==0:
            del tmp[target]

print("Number of wins: ", numWin)

prob=numWin/iterations

print("Probability of winning is: ", prob)
