print("epic battle of rock paper scissors")
print("==================================")
print()
print("Please enter your name: ")
print()
player1=input("player1:")
player2=input("player2:")
print()
print("let the battle begin between",player1,"and",player2)
print("==================================")
print()
counter1=0
counter2=0
while counter1<3 or counter2<3:
    print(player1,"and",player2,"be ready")
    print()
    print("choose r for rock, p for paper, s for scissors")
    print()
    print()
    from getpass import getpass as input
    print(player1,"choose")
    choice1=input("player1:")
    print(player2,"choose")
    choice2=input("player2:")
    print()
    if choice1=="s" and choice2=="p":
        counter1+=1
        print(player1+"s","scissor tore",player2+"s","paper")
        print(player1,"wins")
        print(player2,"loses")
    elif choice1=="r" and choice2=="s":
        counter1+=1
        print(player1+"s","rock broke",player2+"s","scissor")
        print(player1,"wins this round")
        print(player2,"loses this round")
    elif choice1=="p" and choice2=="r":
        print(player1+"s","paper captured",player2+"s","rock")
        counter1+=1
        print(player1,"wins this round")
        print(player2,"loses this round")
    elif choice1=="p" and choice2=="p":
        print("draw")
        print("you both chose paper")
    elif choice1=="r" and choice2=="r":
        print("draw")
        print("you both chose rock")
    elif choice1=="s" and choice2=="s":
        print("draw")
        print("you both chose scissor")
    elif choice1=="" and choice2=="":
        print("you nutty boys")
    elif choice2=="r" and choice1=="s":
        counter2+=1
        print(player2+"s","rock broke",player1+"s","scissor")
        print(player2,"wins this round")
    elif choice2=="p" and choice1=="r":
        print(player2+"s","paper captured",player1+"s","rock")
        counter2+=1
        print(player2,"wins this round")
        print(player1,"loses this round")
    elif choice2=="s" and choice1=="p":
        counter2+=1
        print(player2+"s","scissor tore",player1+"s","paper")
        print(player2,"wins")
        print(player1,"loses") 
    if counter1==3:
        print(player1,"won the game")
        print("ending the game")
        exit()
    elif counter2==3:
        print(player2,"won all rounds")
        print("ending the game")
        exit()
    else:
        continue
    
