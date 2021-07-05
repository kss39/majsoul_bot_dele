import pyautogui
import time
from datetime import date, datetime
from tensorflow import keras
from keras import models
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

model = keras.models.load_model('deepl/tile_model')

def int_to_tile(i):
    if i >= 35:
        i += 1
    elif i < 4:
        return ['nothing', '0m', '0p', '0s'][i]
    kind = 'mpsz'
    return str(i // 4) + kind[i % 4]

while True:
    res = pyautogui.locateOnScreen('resources/locator.png', confidence=0.8)
    print(res)

    if res:
        left, top, width, height = res
        im = pyautogui.screenshot(region=res)
        input_tiles = np.zeros((14, 105, 66, 3))

        for i in range(13):   
            now = datetime.now()
            x, y = left_shift+int(67.46153*i), top_shift
            tile = im.copy().crop(box=(x, y, x+tile_width, y+tile_height))
            input_tiles[i] = np.asarray(tile)
        x, y = left_shift+int(67.46153*13)+20, top_shift
        tile = im.copy().crop(box=(x, y, x+tile_width, y+tile_height))
        input_tiles[13] = np.asarray(tile)
        print(
            [int_to_tile(i) for i in np.argmax(model.predict(input_tiles), axis=-1)]
        )
        # pyautogui.screenshot(f'resources/hand_recog/{now.strftime("%m%d%Y%H%M")}_{14}.png', region=(left+left_shift+int(67.46153*13)+19, top+top_shift, tile_width, tile_height))

    time.sleep(3)
