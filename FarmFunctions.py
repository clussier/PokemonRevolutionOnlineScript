#Charles Lussier: Version 2.0 (7/6/2020)
import win32com.client
import time
import os
import cv2
import BattleDetect
from pynput import keyboard
from pynput.keyboard import Controller
from playsound import playsound

'''-----------INPUTS---------'''
pp = 15
stop = False
catchPokemon = []
SPATK_EVPokemon = ["gastly", "aaunter", "abra", "natu", "mareep", "gengar","budew", "magmar"]
SPD_EVPokemon = ["rattata", "spearow", "zubat", "poliwag", "raticate", "pideotto", "fearow", "poliwag"
                 "weedle", "aipom", "yanma", "eeoc"]
runPokemon = []
'''-----------INPUTS---------'''

keyboard = Controller()
shell = win32com.client.Dispatch("WScript.Shell")

def attackFirstMove():

    print("Attack")
    # Select Attack
    keyboard.press('1')
    keyboard.release('1')
    # Select First Ability
    time.sleep(.3)
    keyboard.press('1')
    keyboard.release('1')

def farmAll():
    """
    Walks back and forth (direction can be adjusted) and checks for battle between strides.
    Does not run from any pokemon and continuously uses the first attack ability
    of your pokemon when in battle (ability does not need to 1 shot).
    """
    farmAll = True
    while True:
        # Simulate A & D Key presses1a
        notInBattle = True
        while notInBattle:
            if BattleDetect.CheckIfOnLoginScreen():
                return 0
            #Start walking in specified direction
            keyboard.press('a')
            #Detect Battle on Screen
            dif = BattleDetect.Bat()
            'Adjust for # of steps'
            #time.sleep(.2)
            if dif < .1:
                print("In battle")
                notInBattle = False
                break
            keyboard.release('a')

            #Start walking in specified direction
            keyboard.press('d')
            #Detect Battle on Screen
            dif = BattleDetect.Bat()
            'Adjust for # of steps'
            #time.sleep(.2)
            if dif < .1:
                print("In battle")
                notInBattle = False
                break
            keyboard.release('d')
            ####################
        #Detect What pokemon is on screen
        BattleDetect.Cropn()
        name = BattleDetect.Read()
        print(name)

        if farmAll:
            attackFirstMove()
    return 0

def farmAndCatch(stop = False, farmAll = False, catch = [], farm = [], run = []):
    """
    This function is designed to allow the user to custimize which pokemon they want the
    program to stop for to catch, which pokemon the program should automatically kill,
    and which pokemon the user should run from.

    The program will first check if it should farm all, then which pokemon it should run from,
    then which pokemon it should catch, and hten finally which pokemon it should farm.
    If the pokemon name does not appear in any list it will default run from it.

    If global value stop is set to True, the program will stop
    :param farmAll: If true, call farmAll() function
    :param catch: a list of pokemon that the program will send an alert when found
    :param farm: a list of pokemon that the program should be farmed
    :param run: a list of pokemon that the program should run from
    """

    pokemonFound = False
    while pokemonFound == False:
        notInBattle = True
        while notInBattle:
            if BattleDetect.CheckIfOnLoginScreen():
                return 0
            i = 0
            j = 0
            keyboard.press('a')
            #Detect Battle on Screen
            dif = BattleDetect.Bat()
            time.sleep(.4)
            #print(dif)
            if dif < .1:
                notInBattle = False
                print("In battle")
                break
            keyboard.release('a')


            keyboard.press('d')
            #Detect Battle on Screen
            dif = BattleDetect.Bat()
            time.sleep(.4)
            if dif < .1:
                notInBattle = False
                print("In battle")
                break
            keyboard.release('d')


        #Detect What pokemon is on screen
        BattleDetect.Cropn()
        name = BattleDetect.Read()
        print(name)

        #Detect health of player pokemon
        BattleDetect.CropHealth()

        #Proceed to farm/run/catch pokemon
        if name in run:
            keyboard.press('4')
            keyboard.release('4')
            print("Run")
            dif = BattleDetect.Bat()
        elif farmAll:
            keyboard.press('1')
            keyboard.release('1')
            time.sleep(.3)
            keyboard.press('1')
            keyboard.release('1')
        elif name in catch:
            pokemonFound = True
            print("we fuckin got him bois")
            playsound('dialtone3.mp3')
        elif name in farm:
            keyboard.press('1')
            keyboard.release('1')
            time.sleep(.3)
            keyboard.press('1')
            keyboard.release('1')
        #If not in any list, Run from that pokemon
        else:
            keyboard.press('4')
            keyboard.release('4')
            print("Run from " + name)
            dif = BattleDetect.Bat()
    return 0