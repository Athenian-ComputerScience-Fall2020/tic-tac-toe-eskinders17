# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874
# https://www.youtube.com/watch?v=_Mb04yhk48Q

# A note on style: Dictionaries can be defined before or after functions.


theBoard = {'U1': ' ' , 'U2': ' ' , 'U3': ' ' , 'M1': ' ' , 'M2': ' ' , 'M3': ' ' , 'L1': ' ' , 'L2': ' ' , 'L3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['U1'] + '|' + board['U2'] + '|' + board['U3'])
    print('-+-+-')
    print(board['M1'] + '|' + board['M2'] + '|' + board['M3'])
    print('-+-+-')
    print(board['L1'] + '|' + board['L2'] + '|' + board['L3'])

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's now your turn " + turn)
        
        print("Enter U1, U2, U3, M1, M2, M3, L1, L2, L3")
        
        move = input()        
        
        try:
            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already, try a different spot")
                continue
        except:
            print("Invalid Input, Plse try again.")
            continue

        

        
        
 
        if count >= 5:
            if theBoard['U1'] == theBoard['U2'] == theBoard['U3'] != ' ': 
                printBoard(theBoard)
                print()
                print("Game Over")                
                print(turn + " has won")                
                break
            elif theBoard['M1'] == theBoard['M2'] == theBoard['M3'] != ' ': 
                printBoard(theBoard)
                print()
                print("Game Over")                
                print(turn + " won")
                break
            elif theBoard['L1'] == theBoard['L2'] == theBoard['L3'] != ' ':
                printBoard(theBoard)
                print()
                print("Game Over")                
                print(turn + " won")
                break
            elif theBoard['L1'] == theBoard['M1'] == theBoard['U1'] != ' ':
                printBoard(theBoard)
                print()
                print("Game Over")                
                print(turn + " won")
                break
            elif theBoard['L2'] == theBoard['M2'] == theBoard['U2'] != ' ': 
                printBoard(theBoard)
                print()
                print("Game Over")                
                print(turn + " won")
                break
            elif theBoard['L3'] == theBoard['M3'] == theBoard['U3'] != ' ':
                printBoard(theBoard)
                print()
                print("Game Over")                
                print(turn + " won")
                break 
            elif theBoard['U1'] == theBoard['M2'] == theBoard['L3'] != ' ': 
                printBoard(theBoard)
                print()
                print("Game Over")                
                print(turn + " won.")
                break
            elif theBoard['L1'] == theBoard['M2'] == theBoard['U3'] != ' ':
                printBoard(theBoard)
                print()
                print("Game Over")                
                print(turn + " won.")
                break 
            

        if count == 9:
            print("Game Over")                
            print("It's a Tie!!")
            break

      
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()
    else:
        print("Good Bye")

if __name__ == "__main__":
    game()




