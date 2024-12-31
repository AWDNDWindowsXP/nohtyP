# coding=utf-8
from tkinter import messagebox as msgbox

while True:
    c = input("Enter a code: ")
    if c == "exit" or c == "quit":
        break
    else:
        print(c[::-1])
        msgbox.showinfo("执行成功！代码：", "执行成功！代码：" + c[::-1])
