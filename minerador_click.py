import mouse
import time
from pyautogui import press, typewrite, hotkey

delay = 1801

def gain():
    group_eth_claim_x = 100
    group_eth_claim_y = 100

    button_claim_x = 540
    button_claim_y = 430

    mouse.move(group_eth_claim_x, group_eth_claim_y, absolute=True, duration=0.1)
    mouse.click('left')

    typewrite("/start")

    mouse.move(button_claim_x, button_claim_y, absolute=True, duration=0.1)
    mouse.click('left')

    press('enter')

while True:
    gain()
    time.sleep(1801)