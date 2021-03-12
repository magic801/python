# from pymouse import PyMouse

# m = PyMouse()
# a = m.position()    #获取当前坐标的位置
# print(a)

# m.move(31, 223)   #鼠标移动到(x,y)位置
# a = m.position()
# print(a)

# m.click(31, 223)  #移动并且在(x,y)位置左击

import pyautogui
from pymouse import PyMouse

class MouseClick:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def startclick(self):
        pyautogui.click(self.x, self.y, clicks=2, interval=0.0, button='right')

    def autoclick(self):
        m = PyMouse()
        m.click(self.x, self.y,button=1,n=2)

    def printXY(self):
        print('123123123')

if __name__ == '__main__':
    ob = MouseClick(400, 380)
    ob.startclick()

    #img1 = pyautogui.screenshot()
    #img1.save('first_shot.png')
    # pyautogui.typewrite(message="hahah,", interval=0.5)
