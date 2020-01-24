from ctypes  import *
height  = windll.user32.GetSystemMetrics(0) # Высота монитора 1920 px
width = windll.user32.GetSystemMetrics(1) # Ширина монитора 1080 px
