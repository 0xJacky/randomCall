#!/usr/bin/env python
#-*- coding:utf-8 -*-

import random
import os
from Tkinter import *
from tkFont import Font
from ttk import *
#Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
from tkMessageBox import *

ABS_PATH = os.path.split(os.path.realpath(__file__))[0]
version = '1.0'
font_family = '宋体'

class Application_ui(Frame):
    # UI 部分
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('点名器')
        self.master.geometry('490x216+438+295')
        self.master.resizable(0,0)
        self.master.iconbitmap(default=os.path.join(ABS_PATH,'randomCall.ico'))
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TCommand.TButton', font=(font_family,12))
        self.button_label = StringVar()
        self.button_label.set('抽取')
        self.Command = Button(self.top, textvariable=self.button_label, command=self.control, style='TCommand.TButton')
        self.Command.place(relx=0.784, rely=0.37, relwidth=0.149, relheight=0.264)

        self.style.configure('TFrame.TLabelframe', font=(font_family,9))
        self.style.configure('TFrame.TLabelframe.Label', font=(font_family,9))
        self.Frame = LabelFrame(self.top, text='抽取框', style='TFrame.TLabelframe')
        self.Frame.place(relx=0.327, rely=0.333, relwidth=0.41, relheight=0.412)

        self.Text1Var = IntVar(value='')
        self.Text1 = Entry(self.top, textvariable=self.Text1Var, font=(font_family,9))
        self.Text1.place(relx=0.18, rely=0.37, relwidth=0.1, relheight=0.083)

        self.Text2Var = IntVar(value='')
        self.Text2 = Entry(self.top, textvariable=self.Text2Var, font=(font_family,9))
        self.Text2.place(relx=0.18, rely=0.519, relwidth=0.1, relheight=0.083)

        self.style.configure('TLabel1.TLabel', anchor='w', font=(font_family,9))
        self.Label1 = Label(self.top, text='起始学号', style='TLabel1.TLabel')
        self.Label1.place(relx=0.065, rely=0.37, relwidth=0.115, relheight=0.079)

        self.style.configure('TLabel2.TLabel', anchor='w', font=(font_family,9))
        self.Label2 = Label(self.top, text='终止学号', style='TLabel2.TLabel')
        self.Label2.place(relx=0.065, rely=0.519, relwidth=0.115, relheight=0.079)

        self.style.configure('Title.Label', anchor='w', font=(font_family,22))
        self.Title = Label(self.top, text='点名器', style='Title.Label', justify='center')
        self.Title.pack(ipady=20)

        self.p = StringVar()
        self.style.configure('TLabel5.TLabel', anchor='w', font=(font_family,10))
        self.Label5 = Label(self.top, textvariable=self.p, style='TLabel5.TLabel')
        self.Label5.place(relx=0.78, rely=0.704)

        self.style.configure('TLabel6.TLabel', anchor='w', font=(font_family,9))
        self.Label6 = Label(self.top, text='Version:'+version, style='TLabel6.TLabel')
        self.Label6.place(relx=0.8, rely=0.889, relwidth=0.182, relheight=0.079)

        self.current = IntVar()
        self.style.configure('TLabel4.TLabel', anchor='w', font=(font_family,30))
        self.Label4 = Label(self.Frame, textvariable=self.current, style='TLabel4.TLabel', justify='center')
        self.Label4.pack(ipady=13)


class Application(Application_ui):
    # 处理部分
    def __init__(self, master=None):
        Application_ui.__init__(self, master)
        self.msec = 5
        self._startnum = int(self.Text1.get()) if self.Text1.get() else ''
        self._t  = list()
        self._chosen = 0
        self._running = False

    def control(self, event=None):
        self._startnum = int(self.Text1.get()) if self.Text1.get() else ''
        stopnum = int(self.Text2.get()) + 1 if self.Text2.get() else ''
        if not self._running:
            try:
                if self._startnum and stopnum:
                    if 0 < self._startnum < stopnum:
                        self._t  = list(range(self._startnum, stopnum))
                        print 'Student number pool:'
                        print self._t
                        self._update()
                        p = format(1/float(stopnum - self._startnum), '.3f')
                        self.p.set('当前概率: ' + str(p))
                        self.button_label.set('停止')
                        self._running = True
                    else:
                        showerror('错误', '学号填写范围：0 ≤ 起始学号 ≤ 终止学号')
                else:
                    showerror('错误', '您还未输入学号')
            except Exception as e:
                showerror('System error', e)

        elif self._running:
            self.after_cancel(self._thread)
            self._running = False
            print 'No.' + str(self._chosen) + ' was selected.'
            self.current.set(self._chosen)
            self.button_label.set('开始')
            self._t = list()


    def _update(self):
        self._chosen = random.choice(self._t)
        self.current.set(self._chosen)
        self._thread = self.after(self.msec, self._update)

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
