import pyautogui

# im = pyautogui.screenshot()
# im.save('1.png')

btm = pyautogui.locateOnScreen('checkbox.png')
print(btm)

# btmList = pyautogui.locateAllOnScreen('checkbox.png')
# btm = list(btmList)[0]
# print(list(btmList))

# center = pyautogui.center((
#   btm.left,
#   btm.top,
#   btm.width,
#   btm.height
# ))
# pyautogui.click(center)

# print('click done')
