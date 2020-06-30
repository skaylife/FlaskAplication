from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title('Test Monitor')

my_img1 = ImageTk.PhotoImage(Image.open("slideShow/1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("slideShow/2.png"))

image_list = [my_img1, my_img2]

image_list[1]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(window, text="<<")
button_exit = Button(window, text="exit programm", command=window.quit)
button_forward = Button(window, text=">>")


button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


window.mainloop()