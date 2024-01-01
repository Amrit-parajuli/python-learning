import random
item_list=["rock","paper","scissor"]
user_score=0
comp_score=0
round=3
for _ in range (round):
    user_choice=input("enter your choice: (rock, paper, scissor): ")
    comp_choice= random.choice(item_list)
    print(f"user choice:{user_choice} and computer choice:{comp_choice}")

    if user_choice==comp_choice:
        print("match tie")
    elif user_choice=="rock":
        if comp_choice=="paper":
            print("paper cover rock: computer wins")
            comp_score+=1
        else:
            print("rock smashes scissor: you wins")
            user_score+=1
    elif user_choice=="paper":
        if comp_choice=="rock":
            print("paper cover the rock: you wins")
            user_score+=1
        else:
            print("scissor cut the paper: computer wins")
            comp_score+=1
    elif user_choice=="scissor":
        if comp_choice=="paper":
            print("scisssor cut the paper: you win")
            user_score+=1
        else:
            print ("rock smashes the scissor: computer wins")
            comp_score+=1
print(f"user score:{user_score} computer choice:{comp_score}")
if user_score > comp_score:
    print("user win")
elif user_score==comp_score:
    print("match tie")
else:
    print("computer wins")
            