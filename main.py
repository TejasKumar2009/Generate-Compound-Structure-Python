import webbrowser
import pyautogui
import time

name = input("Enter the name of the organic compound / hydrocarbon (Please enter correct name) : ")

webbrowser.open(f'https://pubchem.ncbi.nlm.nih.gov/compound/{name}#section=3D-Conformer&fullscreen=true') 

time.sleep(7)

for i in range(0,13):
    if i==12:
        pyautogui.press("Enter")
    pyautogui.press("Tab")

pyautogui.press("enter")

