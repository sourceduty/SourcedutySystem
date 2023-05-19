#Sourceduty System V1.0
#Copyright (c) 2023, Sourceduty
#This software is free and open-source; anyone can redistribute it and/or modify it.

from colorama import *
import sys
import time
import os

def cool_print(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.010)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

        
def make():
    cls()
    cool_print(f"""
Sourceduty System V1.0
⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏

Main Menu 

    {Fore.WHITE}1 {Fore.RESET} ➝  {Fore.YELLOW}Games{Fore.RESET}
    {Fore.WHITE}2 {Fore.RESET} ➝  {Fore.YELLOW}Log{Fore.RESET}
    {Fore.WHITE}3 {Fore.RESET} ➝  {Fore.WHITE}Options{Fore.RESET}
    {Fore.WHITE}4 {Fore.RESET} ➝  {Fore.WHITE}Config{Fore.RESET}

⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏

Navigate Menus (A/B/C)
Navigate Choices (1/2/3)
Select (ENTER)
End Program (X)
Return (/) 
⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏

Selection: """)
    global response
    response = input("")
    if int(response) == 1:
       first_function()
    elif int(response) == 2:
        second_function()
    elif int(response) == 3:
         third_function()
    

def first_function():
    cls()
    cool_print(f"""
Games
⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏

    {Fore.WHITE}1 {Fore.RESET} ➝  {Fore.RED}Sky Tetris{Fore.RESET}
    {Fore.WHITE}2 {Fore.RESET} ➝  {Fore.RED}Retro Mario Airplane{Fore.RESET}

⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏

Navigate Menus (A/B/C)
Navigate Choices (1/2/3)
Select (ENTER)
End Program (X)
Return (/) 
⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏

Selection: """)
    global response
    response = input("")
    if int(response) == 1:
       first_function()
    elif int(response) == 2:
        second_function()
    make()
def second_function():
    cls()
    cool_print(f"""
Log
⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏

    {Fore.WHITE}1 {Fore.RESET} ➝  {Fore.RED}Power Time{Fore.RESET}
    {Fore.WHITE}2 {Fore.RESET} ➝  {Fore.RED}Game Time{Fore.RESET}

⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏

Navigate Menus (A/B/C)
Navigate Choices (1/2/3)
Select (ENTER)
End Program (X)
Return (/) 
⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏⸏

Selection: """)
    global response
    response = input("")
    if int(response) == 1:
       first_function()
    elif int(response) == 2:
        second_function()
    make()
def third_function():
    cls()
    cool_print(f""" Configuration
    _____________________
    
    Note
    _____________________
    
    Press enter to return
    """)
    input()
    make()
    
make()
