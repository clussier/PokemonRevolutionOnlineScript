#Charles Lussier: Version 2.0 (7/6/2020)
import win32com.client
import time
import os
import BattleDetect
from pynput import keyboard
from pynput.keyboard import Controller, Listener
from playsound import playsound
import FarmFunctions
'''--------------INPUTS--------------'''
pp = 15
farmAll = True
catchPokemon = ["ralts"]
SPATK_EVPokemon = ["gastly", "aaunter", "abra", "natu", "mareep", "gengar","budew", "magmar"]
SPD_EVPokemon = ["rattata", "spearow", "zubat", "poliwag", "raticate", "pideotto", "fearow", "poliwag"
                 "weedle", "aipom", "yanma", "eeoc"]
runPokemon = ["tangela", "onphan"]
stop = True
'''--------------INPUTS--------------'''

'''--------------LISTENER--------------'''
COMBO_farmAll = [
    {keyboard.KeyCode(char='g'), keyboard.KeyCode(char='o')}

]
COMBO_stop = [
    {keyboard.KeyCode(char='s')}
]
current = set()
log = []
controller = Controller()
def farm():
    #FarmFunctions.farmAndCatch(farmAll=True, catch=catchPokemon, run=runPokemon)
    FarmFunctions.farmAll()

def on_press(key):
    #Check for farmALL combo
    if any([key in COMBO for COMBO in COMBO_farmAll]):
        current.add(key)
        print(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBO_farmAll):
            farm()
    #log.append(key)
def on_release(key):
    #Check for farmALL combo
    if any([key in COMBO for COMBO in COMBO_farmAll]):
        current.remove(key)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
'''--------------LISTENER--------------'''
