import sys
import os
import numpy as np

def displayHash(hash):
  os.system('cls')
  print("TIC-TAC-TOE:")
  print(" ")
  for i in range(len(hash)):
    print(end="|")
    for j in range(len(hash[0])):
      print(hash[i][j], end="" + "|")
    print()
    
def verificationWinner(hash):
  if lineCheck(hash) == True or columnCheck(hash) == True or diagonalCheck(hash) == True:
    print("You are Winner")
    question()

def lineCheck(hash):
  for i in range(len(hash)):
    if all(verification == 'X' for verification in hash[i]):
      return True
    elif all(verification == 'O' for verification in hash[i]):
      return True
    
def columnCheck(hash):
  for i in range(0,len(hash)):
    linha = [linhas[i] for linhas in hash]
    if all(verification == 'X' for verification in linha):
      return True
    elif all(verification == 'O' for verification in linha):
      return True

def diagonalCheck(hash):
  diagonal = np.diag(hash)
  diagonalInverted = np.diag(np.fliplr(hash))
  if all(verification == 'X' for verification in diagonal):
    return True
  elif all(verification == 'O'  for verification in diagonal):
    return True
  elif all(verification == 'X' for verification in diagonalInverted):
    return True
  elif all(verification == 'O'  for verification in diagonalInverted):
    return True


def verificationCases(hash):
  verification = []
  for line in hash:
    if all(word == 'X' or word == 'O' for word in line):
      verification.append(True)
    else:
      verification.append(False)
      break
  if all(verification == True for verification in verification):
    print("Game Over")
    question()
    
def options(option, hash, symbol):
  option = str(option)
  for i in range(0,len(hash)):
    for j in range(0,len(hash)):
      if hash[i][j] == option:
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
    displayHash(hash)
    verificationWinner(hash)
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
  displayHash(hash)
  menuHash(hash)

main()