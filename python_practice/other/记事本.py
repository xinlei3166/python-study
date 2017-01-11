#!/usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'junxi'


from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import os


def author():
    showinfo('作者信息', '本软件由君惜完成')

def about():
    showinfo('版权信息.Copyright', '本软件版权为君惜所有')

def openfile():
    global filename
    filename = askopenfilename(defaultextension='.txt')
    if filename == '':
        filename = None
    else:
        root.title('FileName: ' + os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename,'r')
        textPad.insert(1.0, f.read())
        f.close()

def new():
    global filename
    root.title('未命名文件')
    textPad.delete(1.0, END)

def save():
    global filename
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        save_as()

def save_as():
    f = asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
    global filename
    filename = f
    fh = open(f, 'w')
    msg = textPad.get(1.0, END)
    fh.write(msg)
    fh.close()
    root.title('FileName: ' + os.path.basename(f))

def cut():
    textPad.event_generate('<<Cut>>')

def copy():
    textPad.event_generate('<<Copy>>')

def paste():
    textPad.event_generate('<<Paste>>')

def redo():     # 重做
    textPad.event_generate('<<Redo>>')

def undo():     # 撤销
    textPad.event_generate('<<Undo>>')

def select_all():
    textPad.tag_add('sel', '1.0', END)


def search():
    topsearch = Toplevel(root)
    topsearch.geometry('300x30+200+250')
    label1 = Label(topsearch, text='Find')
    label1.grid(row=0, column=0, padx=5)
    entry1 = Entry(topsearch, width=20)
    entry1.grid(row=0, column=1, padx=5)
    button1 = Button(topsearch, text='查找')
    button1.grid(row=0, column=2, padx=10)



root = Tk()
root.title('junxi note')
root.geometry("800x500+100+100")

# 创建菜单
menubar = Menu(root)
root.config(menu = menubar)

# 文件菜单
filemenu = Menu(menubar)
filemenu.add_command(label='新建', accelerator='Ctrl + N', command=new)
filemenu.add_command(label='打开', accelerator='Ctrl + O', command=openfile)
filemenu.add_command(label='保存', accelerator='Ctrl + S', command=save)
filemenu.add_command(label='另存为', accelerator='Ctrl + Shift + S', command=save_as)
menubar.add_cascade(label= '文件', menu = filemenu)       # 关联

# 编辑菜单
editmenu = Menu(menubar)
editmenu.add_command(label='撤销', accelerator='Ctrl + Z', command=undo)
editmenu.add_command(label='重做', accelerator='Ctrl + Y', command=redo)
editmenu.add_separator()
editmenu.add_command(label='剪切', accelerator='Ctrl + X', command=cut)
editmenu.add_command(label='复制', accelerator='Ctrl + C', command=copy)
editmenu.add_command(label='粘贴', accelerator='Ctrl + V', command=paste)
editmenu.add_separator()
editmenu.add_command(label='查找', accelerator='Ctrl + F', command=search)
editmenu.add_command(label='全选', accelerator='Ctrl + A', command=select_all)
menubar.add_cascade(label='编辑', menu = editmenu)

# 关于
aboutmenu = Menu(menubar)
aboutmenu.add_command(label='作者', command=author)
aboutmenu.add_command(label='版权', command=about)
menubar.add_cascade(label='关于', menu = aboutmenu)

# 工具栏
toolbar = Frame(root, height=25, bg='Light sea green')

# 按钮
shortButton = Button(toolbar, text='打开', command=openfile)
shortButton.pack(side=LEFT, padx=5, pady=5)
shortButton = Button(toolbar, text='保存', command=save)
shortButton.pack(side=LEFT)
toolbar.pack(expand=NO, fill=X)         # 显示

# 状态栏
status = Label(root, text='Ln20', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# 行号和文本编辑
linelabel = Label(root, width=2, bg='antique white')
linelabel.pack(side=LEFT, fill=Y)
textPad = Text(root, undo=True)
textPad.pack(expand=YES, fill=BOTH)

# 右边滚动下拉条
scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)


root.mainloop()