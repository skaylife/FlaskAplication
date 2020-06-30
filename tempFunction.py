from ctypes  import *
import copy

height  = windll.user32.GetSystemMetrics(0) # Высота монитора 1920 px
width = windll.user32.GetSystemMetrics(1) # Ширина монитора 1080 px

from screeninfo import get_monitors
print("------1-------")

global data
data = []
for im in get_monitors():
    # print(im)
    data.append(im)
    print(data)




print("------Gl-------")


print("------G2-------")
# L1 = L2[:]
#Копируем
dataTemp = [] # Временный кортеж
dataTemp = data # Сохраняем временный кортеж
data2 = copy.deepcopy(dataTemp) # Копируем сохраненый временно кортеж в data2
print(data2)
print("------G3-------")


display = ()
display2 = []
display = data2[0]
display2 = data2[1]

print("------Первый монитор-------")
print(display)
print("------Второй монитор-------")

twomon = []

twomon.append(display2)

print(display2)


print("---------------------------------")
print(type(twomon))
print(type(display2))


print(data2)

print("------G4-------")





print(type(display2))


# >>> a = [1, 2, 3]
# >>> b = a
# >>>
# >>> a[0] = 'ffff'
# >>> b
# ['ffff', 2, 3]
# >>> import copy
# >>> c = copy.deepcopy(b)
# >>> c
# ['ffff', 2, 3]
# >>> c[0] = 1
# >>> c
# [1, 2, 3]
# >>> b
# ['ffff', 2, 3]






# import wx
#
# print("------2-------")
#
# app = wx.App(False) # the wx.App object must be created first.
# print(wx.GetDisplaySize())  # returns a tuple



import tkinter as tk

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print("------3-------")

print(screen_height)
print(screen_width)

print("------4-------")

import tkinter as tk
root = tk.Tk()

width_px = root.winfo_screenwidth()
height_px = root.winfo_screenheight()
width_mm = root.winfo_screenmmwidth()
height_mm = root.winfo_screenmmheight()
# 2.54 cm = in
width_in = width_mm / 25.4
height_in = height_mm / 25.4
width_dpi = width_px/width_in
height_dpi = height_px/height_in

print('Width: %i px, Height: %i px' % (width_px, height_px))
print('Width: %i mm, Height: %i mm' % (width_mm, height_mm))
print('Width: %f in, Height: %f in' % (width_in, height_in))
print('Width: %f dpi, Height: %f dpi' % (width_dpi, height_dpi))

import ctypes
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

print("-------5------")
print('Size is %f %f' % (w, h))

curr_dpi = w*96/width_px
print("-------6------")
print('Current DPI is %f' % (curr_dpi))



from PyQt5 import QtWidgets
import sys

MyApp = QtWidgets.QApplication(sys.argv)
V = MyApp.desktop().screenGeometry()
h = V.height()
w = V.width()
print("-------7------")
print("The screen resolution (width X height) is the following:")
print(str(w) + "X" + str(h))


import ctypes
user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32

screensize = (user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
print("-------8------")
print("screensize =%s"%(str(screensize)))
dc = user32.GetDC(None);

screensize = (gdi32.GetDeviceCaps(dc,8), gdi32.GetDeviceCaps(dc,10), gdi32.GetDeviceCaps(dc,12))
print("screensize =%s"%(str(screensize)))
screensize = (gdi32.GetDeviceCaps(dc,118), gdi32.GetDeviceCaps(dc,117), gdi32.GetDeviceCaps(dc,12))
print("screensize =%s"%(str(screensize)))

print("-------9------")
import pyautogui
resolution = pyautogui.size()
print(resolution)


print("-------10------")



height  = windll.user32.GetSystemMetrics(0) # Высота монитора 1920 px
width = windll.user32.GetSystemMetrics(1) # Ширина монитора 1080 px

