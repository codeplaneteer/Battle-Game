# BloodAlibi // 2023

from random import choice
from time import sleep
import os

GameData = [
  {"Name": "Player",
  "CurrentCard": "",
   "RemainingCards": ["2","3","4","5","6","7","8","9","10","♝","♛","♚","✻"],
   "Score": 0},
  {"Name": "Ordinateur",
  "CurrentCard": "",
   "RemainingCards": ["2","3","4","5","6","7","8","9","10","♝","♛","♚","✻"],
   "Score": 0}, ["2","3","4","5","6","7","8","9","10","♝","♛","♚","✻"]]

#-----------------------------------

def Reset():
  for user in GameData:
    if type(user) is dict:
      user["CurrentCard"] = ""
      user["RemainingCards"] = GameData[2].copy()
      user["Score"] = 0

def Clear():
  if os.name in ('nt', 'dos'):
    os.system("cls")
  else:
    os.system("clear")

def ChooseCard(plr):
  if plr == "Computer":
    card = choice(GameData[1]["RemainingCards"])
    GameData[1]["CurrentCard"] = card
    GameData[1]["RemainingCards"].remove(card)
  else:
    card = choice(GameData[0]["RemainingCards"])
    GameData[0]["CurrentCard"] = card
    GameData[0]["RemainingCards"].remove(card)

def Player():
  input("Press Enter to select card >")
  ChooseCard("Player")

def Computer():
  ChooseCard("Computer")

def Output():
  Clear()
  print("*════════════════════════*\n\n(", GameData[0]["Score"] ,") Player : [", GameData[0]["CurrentCard"], "] \n(", GameData[1]["Score"],") Computer : [", GameData[1]["CurrentCard"], "]\n\n*════════════════════════*")
  

while True:
  while len(GameData[0]["RemainingCards"]) > 0 and len(GameData[1]["RemainingCards"]) > 0:
    Output()
    sleep(1)
    Player()
    sleep(0.2)
    Computer()
    sleep(0.6)
    Output()
    sleep(0.1)
    if GameData[2].index(GameData[0]["CurrentCard"]) > GameData[2].index(GameData[1]["CurrentCard"]):
      print("Your card is stronger ! You won +1.")
      GameData[0]["Score"] += 1
    elif GameData[2].index(GameData[0]["CurrentCard"]) == GameData[2].index(GameData[1]["CurrentCard"]):
      print("You picked the same card as your opponent. You and your enemy won +1.")
      GameData[0]["Score"] += 1
      GameData[1]["Score"] += 1
    else:
      print("Your card is weaker. Your enemy won +1.")
      GameData[1]["Score"] += 1
    sleep(3)
    Output()
  #-----------
  Clear()
  if GameData[0]["Score"] > GameData[1]["Score"]:
    print("*════════════════════════*\n\nYou won !\n\n*════════════════════════*\n\nScore :", GameData[0]["Score"], "-", GameData[1]["Score"])
  elif GameData[0]["Score"] == GameData[1]["Score"]:
    print("*════════════════════════*\n\nTie ! \n\n*════════════════════════*\n\nScore :", GameData[0]["Score"], "-", GameData[1]["Score"])
  else:
    print("*════════════════════════*\n\nYou lost. Better luck next time !\n\n*════════════════════════*\n\nScore :", GameData[0]["Score"], "-", GameData[1]["Score"])
  sleep(1)
  input("\n(Press Enter to replay)")
  Reset()
