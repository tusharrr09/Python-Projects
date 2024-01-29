import random

def play():                 #define function
    user = input("Choose: 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return 'It\'s a tie'                # \ is to continue in same string
    
    if is_win(user, computer):
        return 'You won!'
    
    else:
        return 'You lost!'
    
def is_win(player, opponent):

        #return true if player wins
        #r>s, s>p, p>r
        if (player == 'r' and opponent == 's') or (player =='s' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
            return True
        
print (play())