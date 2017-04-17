import sys

player1 = input("what is your name?")
player2 = input("and what is yours?")

player1_answer = input("%s, do you want to choose rock, paper, or scissors?" % player1)
player2_answer = input("%s, do you want to choose rock, paper, or scissors?" % player2)

def compare(p1, p2):
    if p1 == p2:
        return ("It's a tie!")
    elif p1 == "rock":
        if p2 == "paper":
            return (player2 + " wins!")
        else:
            return (player1 + " wins!")
    elif p1 == "paper":
        if p1 == p2:
            return ("It's a tie!")
        elif p2 == "rock":
            return (player1 + " wins!")
        else:
            return (player2 + " wins!")
    elif p1 == "scissors":
        if p1 == p2:
            return ("It's a tie!")
        elif p2 == "rock":
            return (player2+ " wins!")
        else:
            return (player1+ " wins!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
    sys.exit()

print(compare(player1_answer, player2_answer))
