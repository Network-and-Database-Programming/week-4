#!/usr/bin/env python3
import sqlite3, time, random, string
from colorama import Fore, Back, Style
import time
import UserMod
import os
#db_root = "./database"
dir = os.path.dirname(os.path.abspath(__file__))
dir = os.path.join(dir, "database")
home = {
  'welcome': open(os.path.join(dir, "welcome.txt") , "r").read(),
  'menu':    open( os.path.join(dir, "home-menu.txt")).read()
}

access = 0

def main( ):
  print( home['welcome'] )
  time.sleep( 0.5 )
  print("System loading...")
  time.sleep( 0.9 )
  while True:
    print("-"*17)
    print( Fore.GREEN + home['menu'] + Style.RESET_ALL )
    print("-"*17)
    opt = int(input("> ")[0])
    if opt == 1:
      Login( )
    elif opt == 2:
      Register( )
    elif opt == 3:
      res = CheckLogin( True )
    else:
      print(Fore.RED + 'Non-support operation' + Style.RESET_ALL)

def Login( ):
  global access
  res = UserMod.Login( )
  if res:
    access = time.time() + 30
  else:
    print("Nope")

def Register( ):
  res = UserMod.Register( )

def CheckLogin( info = False ):
  if info == True:
    print( "Timelamp: ", access )
    print( 
      ( 
        ( Back.GREEN + ' Still available ' )
        if time.time() < access 
        else 
        ( Back.RED + ' Invaild ') 
      ) + Style.RESET_ALL 
    )
  return ( time.time() < access )

if __name__ == "__main__":
  main( )
