# coding=utf-8
from tkinter import messagebox as msgbox

while True:
    x = input(">>> ")
    if x in globals().keys():
        print(globals()[x])
        continue
    elif x == "exit" or x == "quit":
        break
    try:
        exec(x[::-1])
    except Exception as e:
        msgbox.showerror("错误！", str(e))
        print(e)
