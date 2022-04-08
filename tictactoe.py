board = ["-", "-", "-",
          "-", "-", "-",              
          "-", "-", "-"]

current_player = "X"
winner = None
gameRunning = True

# Print Board
def printBoard(board):
  print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ")
  print("-----------")
  print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
  print("-----------")
  print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")

# Get Player Input
def playerInput(board):
  finalInput = " "
  
  while finalInput == " ":
    inputUser = int(input("Enter a number 1-9: "))
    if inputUser >= 1 and inputUser <= 9 and board[inputUser-1] == "-":
      board[inputUser-1] = current_player
      break
    else: 
      print("You need to answer a number between 1-9")
      finalInput == " "

while gameRunning:
  printBoard(board)
  playerInput(board)