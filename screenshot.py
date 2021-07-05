import pyautogui
import time
from datetime import date, datetime
from tensorflow import keras
import numpy as np

# Locator works at 1366*768 resolution

# Each tile: width=67, height=105
# Leftmost tile position: left+(156), top+(658)

# Box(left=1070, top=433, width=1357, height=763)
# 1m: Box(left=1226, top=1091, width=67, height=105)
# 1m: Box(left=1293, top=1091, width=67, height=105)
# 1m: Box(left=1361, top=1091, width=67, height=105)
# 1m: Box(left=1428, top=1091, width=67, height=105)
# 1m: Box(left=1630, top=1091, width=67, height=105)
# 1m: Box(left=1698, top=1091, width=67, height=105)
# 1m: Box(left=1765, top=1091, width=67, height=105)
# 1m: Box(left=1833, top=1091, width=67, height=105)
# 1m: Box(left=1900, top=1091, width=67, height=105)
# 1m: Box(left=1968, top=1091, width=67, height=105)
# 1m: Box(left=2035, top=1091, width=67, height=105)
# 1m: Box(left=2103, top=1091, width=67, height=105)
# 1m: Box(left=1226, top=1091, width=67, height=105)
# 1m: Box(left=1226, top=1091, width=67, height=105)

tile_width, tile_height = 66, 105
left_shift, top_shift = 155.5, 658

while True:
    res = pyautogui.locateOnScreen('resources/locator.png', confidence=0.8)
    
    print(res)
    if res:
        left, top, width, height = res
        im = pyautogui.screenshot(region=res)
        print(im)

        for i in range(13):   
            now = datetime.now()
            x, y = left_shift+int(67.46153*i), top_shift
            im.copy().crop(box=(x, y, x+tile_width, y+tile_height)).save(f'resources/hand_recog/{now.strftime("%m%d%Y%H%M%S")}_{i}.png')
        x, y = left_shift+int(67.46153*13)+20, top_shift
        im.copy().crop(box=(x, y, x+tile_width, y+tile_height)).save(f'resources/hand_recog/{now.strftime("%m%d%Y%H%M%S")}_{13}.png')
        # pyautogui.screenshot(f'resources/hand_recog/{now.strftime("%m%d%Y%H%M")}_{14}.png', region=(left+left_shift+int(67.46153*13)+19, top+top_shift, tile_width, tile_height))

    time.sleep(3)
