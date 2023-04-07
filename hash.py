import sys
import os

def displayhash(hash):
  os.system('cls')
  print("TIC-TAC-TOE:")
  print(" ")
  for i in range(len(hash)):
    print(end="|")
    for j in range(len(hash[0])):
      print(hash[i][j], end="" + "|")
    print()
    
def verificationWinner(hash, symbol):
    if hash[0][0] == symbol and hash[1][0] == symbol and hash[2][0] == symbol:
        print("You are Winner!")
        question()
    elif hash[0][0] == symbol and hash[0][1] == symbol and hash[0][2] == symbol:
        print("You are Winner!")
        question()
    elif hash[0][2] == symbol and hash[1][2] == symbol and hash[2][2] == symbol:
        print("You are Winner!")
        question()
    elif hash[2][0] == symbol and hash[2][1] == symbol and hash[2][2] == symbol:
        print("You are Winner!")
        question()
    elif hash[0][0] == symbol and hash[1][1] == symbol and hash[2][2] == symbol:
        print("You are Winner!")
        question()
    elif hash[0][2] == symbol and hash[1][1] == symbol and hash[2][0] == symbol:
        print("You are Winner!")
        question()
    elif hash[0][1] == symbol and hash[1][1] == symbol and hash[2][1] == symbol:
        print("You are Winner!")
        question()
    elif hash[1][0] == symbol and hash[1][1] == symbol and hash[1][2] == symbol:
        print("You are Winner!")
        question()
    
def verificationCases(hash):
  verification = 0
  for line in hash:
    for word in line:
      if word == 'X' or word == 'O':
        verification = verification + 1
      else:
        break
  if verification == 9:
    print("Game Over")
    question()
    
def options(option, hash, symbol):
    option = str(option)
    for i in range(0,len(hash)):
        for j in range(0,len(hash)):
            if hash[i][j] == option:
                print("teste")
                if symbol == "X":
                    symbol = "O"
                    hash[i][j] = symbol
                else:
                    symbol = "X"
                    hash[i][j] = symbol
    return symbol

def menuHash(hash):
  symbol = "O"
  option = int(1)
  while option != 0:
    option = input("\nChoose a number to put the symbol: ")
    symbol = options(option, hash, symbol)
    displayhash(hash)
    verificationWinner(hash, symbol)
    verificationCases(hash)
    
def question():
  option = input("would you like to play again?" + " Yes or Not? ").upper()
  if option == "YES":
    os.system('cls')
    main()
  else:
    os.system('cls')
    sys.exit()

def main():
  hash = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
  displayhash(hash)
  menuHash(hash)

main()