#Have a board of 3x3
#Each place in the board can hold either an x or o
#Players take turn placing one of their designated symbol in one of the places
#Each time they place it, check to see if there's 3 in a row in any direction

def createBoard():
  return [[" ", " ", " "],[" ", " ", " "],[" "," "," "]]

def playerMove(symbol, row, column, board):
  if checkIsValidMove(row, column, board) == True:
    board[row][column] = symbol
    return board
  else:
    return False

def checkIsValidMove(row, column, board):
  if board[row][column] == " ":
    return True
  else:
    return False


def hasWon(symbol, row, column, board):
  if isRow(symbol, row, board) == True:
    return True
  if isColumn(symbol, column, board) == True:
    return True
  if isDiagonal(symbol, board) == True:
    return True
  else:
    return False


def isRow(symbol, row, board):
  if board[row][0] == symbol and board[row][1] == symbol and board[row][2] == symbol:
    return True
  else:
    return False

def isColumn(symbol, column, board):
  if board[0][column] == symbol and board[1][column] == symbol and board[2][column] == symbol:
    return True
  else:
    return False

def isDiagonal(symbol, board):
  if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
    return True
  if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
    return True
  else:
    return False

def drawBoard(board):
  for i in range(0,2):
    printRow(i, board)
    print "___________"
  printRow(2, board)

def printRow(rowNum, board):
  row = ""
  for i in range(0,2):
    row = row + " " + board[rowNum][i] + " |"
  row = row + board[rowNum][2]
  print row

def swapPlayer(player):
  if player == 'x':
    return 'o'
  else:
    return 'x'


#Create board
#draw board
#prompt correct player
#receives input from player
#checks if is valid, if valid, plays the move
#if not, player goes again
#prompts player 2
#draws board after each play
#after each move, checks if player has won
#if won, then restart game

def ticTacToe():
  board = createBoard()
  drawBoard(board)

  #set player
  player = 'x'
  gameEnd = False

  while not gameEnd:
    try:
      row = int(raw_input("Player " + player + ": What row? "))
      column = int(raw_input("Player " + player + ": What column? "))
    except Exception:
      row = None
      column = None
    if row in [0, 1, 2] and column in [0, 1, 2]:
      valid = playerMove(player, row, column, board)
      if valid:
        drawBoard(valid)
        gameEnd = hasWon(player, row, column, board)
        if not gameEnd:
          player = swapPlayer(player)
      else:
        print "Invalid move. Please try again."
    else:
      print "Invalid position."

  print "Congratulations player " + player + "! You won!"

  playAgain = raw_input("Would you like to play again? Y/N: ")
  if playAgain == "Y":
    ticTacToe()


ticTacToe()


#Use 'curses' to have control over screen. Can redraw existing board
#Variable board sizes


