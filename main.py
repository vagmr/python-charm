#coding=gbk

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from PIL import Image,ImageTk
import tkinter.messagebox
import pickle
from PIL import Image as imim
import pygame

root = Tk()
root.title('大功德系统')

root_img=ImageTk.PhotoImage(imim.open("bp.png"))
root_img1=ImageTk.PhotoImage(imim.open('bp1.png'))
root_img2=ImageTk.PhotoImage(imim.open('QR.png'))

canvans_login=Canvas(root,width=900,height=600,highlightthickness=0)#

chick=canvans_login.create_image(0,0,anchor='nw',image=root_img)
canvans_login.pack()


texty = 400
levallist1 = []
count = 0
texty1 = 400
levallist2 = []
count1 = 0

pygame.mixer.init()
pygame.mixer.music.load('dabeizhou.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

class CreateButton(object):
    def __init__(self,master=None,canvas=None,x1=None,y1=None,x2=None,y2=None,str1=None,fontsize=30):
        '''
        创建按钮
        :param master: 建立的窗口
        :param canvas: 画布
        :param x1: 按钮左上顶点横坐标
        :param y1: 按钮左上顶点纵坐标
        :param x2: 按钮右下顶点横坐标
        :param y2: 按钮右下顶点纵坐标
        :param str1: 按钮上的文字
        :param fontsize: 按钮上的字体大小
        '''
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.str=str1
        self.root=master
        self.canvas=canvas
        self.fontsize=fontsize
        self.r1 = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, width=2, outline='white')  # 按钮外框
        self.r2 = self.canvas.create_rectangle(self.x1 + 3, self.y1 + 3, self.x2 - 3, self.y2 - 3, width=2,
                                     outline='white')  # 按钮内框
        self.t = self.canvas.create_text((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, text=self.str,
                               font=('楷体', self.fontsize, 'bold'), fill='white')  # 按钮显示文本
        self.SetBuuton()

    def bind_1(self,event=None):# 点击响应函数
        pass

    def bind_2(self,event):# 鼠标经过响应函数
        if self.x1<=event.x<=self.x2 and self.y1<=event.y<=self.y2:# 响应的位置
            self.canvas.itemconfigure(self.r1,outline='gold')# 重设外框颜色
            self.canvas.itemconfigure(self.r2,outline='gold')# 重设内框颜色
            self.canvas.itemconfigure(self.t,fill='gold')# 重设显示文本颜色
        else:
            self.canvas.itemconfigure(self.r1,outline='white')# 恢复外框默认颜色
            self.canvas.itemconfigure(self.r2,outline='white')# 恢复内框默认颜色
            self.canvas.itemconfigure(self.t,fill='white')# 恢复显示文本默认颜色
    def SetBuuton(self):
        self.canvas.bind('<Button-1>',lambda event:self.bind_1(event))# 关联鼠标点击事件
        self.canvas.bind('<Motion>',lambda event:self.bind_2(event))# 关联鼠标经过事件
flag=0
class LoginPage(object):
    def __init__(self, master=None):
        self.flag=0
        self.root = master  # 定义内部变量root
        self.root.title('登录界面')
        self.root.geometry('%dx%d' % (300, 200))  # 设置窗口大小
        self.username = StringVar()
        self.username.set('vagmr')
        self.password = StringVar()

    def fun(self):#执行函数
        self.createPage()


    def createPage(self):#设置界面函数
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()

        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='账户: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='注册', command=self.sign).grid(row=3, column=1, stick=W)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

    def sign(self):#注册函数
        def sign_up_admin():
            np = new_psd.get()
            npf = new_psd_confirm.get()
            nn = new_name.get()

            with open('usrs_info.pickle', 'rb') as user_file:
                exit_user_info = pickle.load(user_file)
            if np != npf:
                tk.messagebox.showerror(title="Error", message='两次输入的密码不一致！')
            elif len(np)==0:
                tk.messagebox.showerror(title="Error", message='密码不能为空！')
            elif nn in exit_user_info:
                tk.messagebox.showerror(title="Error", message='这个用户名已经被注册了！')
            else:
                exit_user_info[nn] = np
                with open('usrs_info.pickle', 'wb') as user_file:
                    pickle.dump(exit_user_info, user_file)
                tk.messagebox.showinfo(title='Welcome', message="注册成功！")
                root_sign_up.destroy()

        root_sign_up = tk.Toplevel(self.root)
        root_sign_up.geometry('350x200')
        root_sign_up.title('注册界面')

        new_name = tk.StringVar()
        new_name.set('vagmr')
        tk.Label(root_sign_up, text="用户名：").place(x=10, y=10)
        entry_new_name = tk.Entry(root_sign_up, textvariable=new_name).place(x=120, y=10)

        new_psd = tk.StringVar()
        new_psd.set('')
        tk.Label(root_sign_up, text="密码：").place(x=10, y=60)
        entry_new_psd = tk.Entry(root_sign_up, textvariable=new_psd, show='*').place(x=120, y=60)

        new_psd_confirm = tk.StringVar()
        new_psd_confirm.set('')
        tk.Label(root_sign_up, text="请确认密码：").place(x=10, y=110)
        entry_new_psd_confirm = tk.Entry(root_sign_up, textvariable=new_psd_confirm, show='*').place(x=120, y=110)

        btn_comfirm_sign_up = tk.Button(root_sign_up, text='注册', command=sign_up_admin)
        btn_comfirm_sign_up.place(x=170, y=160)

    def loginCheck(self):#登录函数
        name = self.username.get()
        secret = self.password.get()
        try:
            with open("usrs_info.pickle", 'rb') as user_file:
                usrs_info = pickle.load(user_file)
        except FileNotFoundError:
            with open('usrs_info.pickle', 'wb') as user_file:
                usrs_info = {'admin': 'admin'}
                pickle.dump(usrs_info, user_file)

        if name in usrs_info:
            if secret == usrs_info[name]:
                tk.messagebox.showinfo(title="登录成功", message='你好，' + name+'！\n请再次点击进入按钮进入赛博功德系统~')
                global flag
                flag=1
                self.root.destroy()

            else:
                tk.messagebox.showerror(message="密码错误！")
        else:
            is_sign_up = tk.messagebox.askyesno(title='Hi', message='你还没有注册，要现在前往注册吗？')

            if is_sign_up:
                self.sign()
money=20
class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('大功德系统')
        self.root.geometry('%dx%d' % (900, 600))  # 设置窗口大小
        self.money=0
        self.volume=0.5
        self.count=0
        self.funcPage()

    def funcPage(self):#各个功能

        def Load1():#功德-10函数
            global texty1, count1
            if texty1 > 340:
                new2 = self.canvans_main.create_text(380, texty1, anchor='nw', text='功德-10',
                                          font=('楷体', 40), fill='black')
                levallist2.append(new2)
                self.root.after(5, Load1)
                if count1 >0:
                    self.canvans_main.delete(levallist2[count1 - 1])
            if texty1 == 340:
                for i in levallist2:
                    self.canvans_main.delete(i)
                levallist2.clear()
                texty1=400
                count1=-1

            texty1 -= 1
            count1 += 1
        def Load():#功德+1函数
            global texty, count
            if texty > 340:
                new1 = self.canvans_main.create_text(380, texty, anchor='nw', text='功德+1',
                                          font=('楷体', 40), fill='black')
                levallist1.append(new1)
                self.root.after(5, Load)
                if count >0:
                    self.canvans_main.delete(levallist1[count - 1])
            if texty == 340:
                for i in levallist1:
                    self.canvans_main.delete(i)
                levallist1.clear()
                texty=400
                count=-1

            texty -= 1
            count += 1



        def Laugh(evnet=None):#佛祖笑函数
            '''
            扣一佛祖陪你笑
            :return:
            '''

            def UpDate():
                self.canvans_main.update()
            if self.money<10:
                tk.messagebox.showerror(message='功德不足！')

            else:
                Load1()
                mu1=pygame.mixer.Sound('fozu.mp3')
                mu1.play()
                self.canvans_main.update()
                self.root.update_idletasks()
                self.root.after(1,UpDate)
                for i in levallist:
                    self.canvans_main.delete(i)
                new = self.canvans_main.create_text(10, 10, anchor='nw', text='功德:%d' % (self.money-10),
                                                    font=('楷体', 50), fill='white')
                self.money = self.money - 10
                levallist.append(new)

                self.root.update_idletasks()
        #扣1佛祖陪你笑
        self.root.bind('1', Laugh)

        levallist=[]

        def Knock():#敲木鱼
            self.canvans_main.delete(la3)
            Load()
            print('功德+1')
            self.money=self.money+1
            new=self.canvans_main.create_text(10, 10, anchor='nw',text='功德:%d' % (self.money),font=('楷体',50),fill='white')
            self.count+=1
            mu2=pygame.mixer.Sound('muyu.mp3')
            mu2.play()
            for i in levallist:
                self.canvans_main.delete(i)
            levallist.append(new)
            for i in range(self.count-1):
                self.canvans_main.delete(levallist[i])
            self.root.update_idletasks()
        self.canvans_main = Canvas(self.root, width=900, height=600, highlightthickness=0)  #主界面的画布
        self.chick = self.canvans_main.create_image(0, 0, anchor='nw', image=root_img1)
        self.canvans_main.pack()
        la3 = self.canvans_main.create_text(10, 10, anchor='nw',text='功德:0' ,font=('楷体',50),fill='white')

        def Helptip():#帮助页
            helptop = tk.Toplevel()
            helptop.title('帮助')
            helptop.geometry('400x250')
            helptext = '帮助\n欢迎进入大功德系统\n点击下方按钮敲击木鱼积攒功德\n你可以点击下方按钮消耗功德让佛祖陪你笑\n也可以扣\'1\'快速让佛祖陪你笑\n更多功能正在开发（不会）'
            tk.Label(helptop, text=helptext,font=('楷体',15)).pack()
        b02 = Button(self.root, bg='white', bd=0, font=('楷体', 30), fg='gold', text='帮助', command=Helptip)
        b02.place(width=120, height=50, x=560, y=10)  # 帮助按钮

        def Setpage():#设置页
            settop = tk.Toplevel()
            settop.title('设置')
            settop.geometry('400x350')
            abouttext = '   设置'
            def tip():
                tk.messagebox.showinfo(message='不会')
            la01=tk.Label(settop,text='语言',font=('楷体',20))
            la01.place(x=110,y=85)
            la02 = tk.Label(settop, text='字体', font=('楷体', 20))
            la02.place(x=110, y=175)
            la03 = tk.Label(settop, text='音乐', font=('楷体', 20))
            la03.place(x=110, y=255)
            b05=tk.Button(settop,text='简体中文',font=('楷体',20),command=tip)
            b05.place(x=210,y=85)
            b06 = tk.Button(settop, text='楷体', font=('楷体', 20),command=tip)
            b06.place(x=210, y=165)
            b07 = tk.Button(settop, text='关闭', font=('楷体', 20),command=tip)
            b07.place(x=210, y=245)
            tk.Label(settop, text=abouttext,font=('楷体',25)).pack()


        b01 = Button(self.root, bg='white', bd=0, font=('楷体', 30), fg='gold', text='设置', command=Setpage)
        b01.place(width=120, height=50, x=700, y=10)  # 设置按钮
        #关于按钮
        class About(CreateButton):
            def __init__(self, master=None, canvas=None, x1=None, y1=None, x2=None, y2=None, str1=None, fontsize=30):
                '''
                创建按钮
                :param master: 建立的窗口
                :param canvas: 画布
                :param x1: 按钮左上顶点横坐标
                :param y1: 按钮左上顶点纵坐标
                :param x2: 按钮右下顶点横坐标
                :param y2: 按钮右下顶点纵坐标
                :param str1: 按钮上的文字
                :param fontsize: 按钮上的字体大小
                '''
                self.x1 = x1
                self.x2 = x2
                self.y1 = y1
                self.y2 = y2
                self.str = str1
                self.root = master
                self.canvas = canvas
                self.fontsize = fontsize
                self.r1 = self.canvas.create_oval(self.x1, self.y1, self.x2, self.y2, width=2,
                                                       outline='white')  # 按钮外框
                self.r2 = self.canvas.create_oval(self.x1 + 3, self.y1 + 3, self.x2 - 3, self.y2 - 3, width=2,
                                                       outline='white')  # 按钮内框
                self.t = self.canvas.create_text((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, text=self.str,
                                                 font=('楷体', self.fontsize, 'bold'), fill='white')  # 按钮显示文本
                self.SetBuuton()
            def Abouttip(self):
                abouttop = tk.Toplevel()
                abouttop.title('关于')
                abouttop.geometry('500x320')
                abouttext = '*************************\n\n功德系统V0.0.1\n\n某\n某\n作者：vagmr\n\n*************************'
                tk.Label(abouttop, text=abouttext,font=('楷体',15)).pack()

            def bind_1(self, event=None):  # 点击响应函数
                if self.x1 <= event.x <= self.x2 and self.y1 <= event.y <= self.y2:  # 响应的位置
                    self.Abouttip()  # 弹窗
        About(self.root, self.canvans_main, 830, 10, 880, 60, '?')


        #敲木鱼按钮
        b03=Button(self.root,text='点击此处敲击木鱼',bd=4,bg='gold',font=('楷体',30),command=Knock)
        b03.place(x=50,y=510)

        # 佛祖笑按钮
        b04 = Button(self.root, text='扣1佛祖陪你笑', bd=4, bg='gold', font=('楷体', 30), command=Laugh)
        b04.place(x=500, y=510)


        def Recharge():#充值按钮
            chargetop=Toplevel(self.root)
            chargetop.title('功德箱')
            chargetop.geometry('400x400')
            tk.Label(chargetop,text='链接安全，请使用微信或浏览器扫一扫',font=('楷体',15)).pack()
            tk.Label(chargetop,image=root_img2).pack()

        b06 = Button(self.root, bg='red', bd=0, font=('楷体', 30), fg='gold', text='功德箱', command=Recharge)
        b06.place(width=120, height=50, x=780, y=400)  # 设置按钮
        def enter1(event):
            event.widget['fg'] = 'yellow';event.widget['bg'] = 'dimgray'
        def leave1(event):
            event.widget['fg'] = 'orange';event.widget['bg'] = 'white'
        def enter2(event):
            event.widget['fg'] = 'yellow';event.widget['bg'] = 'dimgray'
        def leave2(event):
            event.widget['fg'] = 'black';event.widget['bg'] = 'gold'
        def enter3(event):
            event.widget['fg'] = 'yellow';event.widget['bg'] = 'dimgray'
        def leave3(event):
            event.widget['fg'] = 'black';event.widget['bg'] = 'red'
        for i in [b01, b02]:
            i.bind('<Enter>', enter1)
            i.bind('<Leave>', leave1)  # 按钮关联鼠标进入事件
        for i in [b03, b04]:
            i.bind('<Enter>', enter2)
            i.bind('<Leave>', leave2)
        b06.bind('<Enter>', enter3)
        b06.bind('<Leave>', leave3)

def login(*args, **kwargs):#登录
    top = Toplevel()
    LoginPage(top).fun()
    while flag == 1:
        top.destroy()
        canvans_login.destroy()
        MainPage(root)
        break

class LoginButton(CreateButton):#登录按钮
    def bind_1(self, event=None):  # 点击响应函数
        if self.x1 <= event.x <= self.x2 and self.y1 <= event.y <= self.y2:  # 响应的位置
            login()
##重写父类
LoginButton(root,canvans_login,380-50,520-20,520+50,570+20,'进 入',60)#进入按钮

def main():#主函数
    '''
    主函数
    :return: 无
    '''
    root.mainloop()  # 大型的while循环

if __name__ == '__main__':
     main()

