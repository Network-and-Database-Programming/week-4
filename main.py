#!/usr/bin/env python3
import sqlite3, time, random, string
from colorama import Fore, Back, Style
import time
import UserMod, CourseMod

db_root = "./database"
home = {
  'welcome': open( db_root + "/welcome.txt", "r").read(),
  'menu':    [
    open( db_root + "/home-menu.txt").read(),
    open( db_root + "/student-menu.txt").read(),
    open( db_root + "/admin-menu.txt").read()
  ]
}

ADMIN_ACCOUNT  = "admin"
ADMIN_PASSWORD = "admin"

token  = 0
access = 0
status = 0

def main( ):
  print( home['welcome'] )
  time.sleep( 0.5 )
  print("System loading...")
  time.sleep( 0.9 )
  while True:
    menu()
def menu():
  global token, access, status
  status = access
  print("-"*17)
  print( Fore.GREEN + home['menu'][access] + Style.RESET_ALL )
  print("-"*17)
  opt = int(input("> ")[0])
  if CheckLogin( ) == False and status > 0:
    print("Sorry, you need login again")
    Logout()
    return menu( )   

  if access == 0: # default 
    if opt == 1:
      Login( )
    elif opt == 2:
      Register( )
    elif opt == 3:
      CheckLogin( True )
    elif opt == 4:
      LoginAdmin( )
  elif access == 1: # student mode
    if opt == 1:
      CourseMod.All( )
    elif opt == 2:
      CourseMod.Details()
    elif opt == 3:
      CheckLogin( True )
    elif opt == 4:
      Logout( )
  elif access == 2:
    if opt == 1:
      CourseMod.AddNewCourse( )
    elif opt == 2:
      CourseMod.All( )
    elif opt == 3:
      CourseMod.Details()
    elif opt == 4:
      CheckLogin( True )
    elif opt == 5:
      Logout()
  else:
    print(Fore.RED + 'Non-support operation' + Style.RESET_ALL)

def Logout():
  global access, token, status
  access = 0
  token  = 0
  status = 0

def Login( ):
  global token, access
  res = UserMod.Login( )
  if res:
    access = 1
    token  = time.time() + 30
  else:
    print("Nope")

def Register( ):
  res = UserMod.Register( )

def CheckLogin( info = False ):
  global access
  if info == True:
    print( "Timelamp:", token )
    print( "Access:  ", access )
    print( 
      ( 
        ( Back.GREEN + ' Still available ' )
        if time.time() < token 
        else 
        ( Back.RED + ' Invaild ') 
      ) + Style.RESET_ALL 
    )
  res = time.time() < token
  return ( res )

def LoginAdmin( ):
  global token, access
  acc = input("Account:\t")
  pwd = input("Password:\t")
  if acc == ADMIN_ACCOUNT and pwd == ADMIN_PASSWORD:
    access = 2
    token = time.time() + 30
    print("Login success")
  else:
    print("Login failed!")


if __name__ == "__main__":
  main( )
