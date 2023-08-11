import qrcode
from tkinter import *
import os
from tkinter import messagebox
import time


def create():
    t = time.localtime()
    file_name = str(t[0])+'-'+ str(t[1]) +'-'+str(t[2])+'-'+str(t[3])+'.'+str(t[4])+'.'+str(t[5])
    pic = qrcode.make(t)
    pic.save(r"C:/qrcode creater/"+file_name+'.jpg')
    messagebox.showinfo("Qrcode Creater", "成功生成C:/qrcode creater/"+file_name+'.jpg')
                        

if os.path.exists("C:/qrcode creater"):
    pass
else:
    os.mkdir("C:/qrcode creater")
    
    
tk = Tk()
tk.resizable(width=False, height=False)
tk.geometry("400x250")
tk.title("二维码生成器")

label = Label(tk, text="二维码生成器，一键生成！")
label.grid(row=0, column=0)

text = Text(tk, width=55, height=10)
text.grid(row=1, column=0)

btn1 = Button(tk, text="一键生成(图片将在C:/qrcode creater中创建)", command=create)
btn1.grid(row=3, column=0)

tk.mainloop()
