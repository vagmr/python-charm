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
root.title('�󹦵�ϵͳ')

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
        ������ť
        :param master: �����Ĵ���
        :param canvas: ����
        :param x1: ��ť���϶��������
        :param y1: ��ť���϶���������
        :param x2: ��ť���¶��������
        :param y2: ��ť���¶���������
        :param str1: ��ť�ϵ�����
        :param fontsize: ��ť�ϵ������С
        '''
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
        self.str=str1
        self.root=master
        self.canvas=canvas
        self.fontsize=fontsize
        self.r1 = self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, width=2, outline='white')  # ��ť���
        self.r2 = self.canvas.create_rectangle(self.x1 + 3, self.y1 + 3, self.x2 - 3, self.y2 - 3, width=2,
                                     outline='white')  # ��ť�ڿ�
        self.t = self.canvas.create_text((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, text=self.str,
                               font=('����', self.fontsize, 'bold'), fill='white')  # ��ť��ʾ�ı�
        self.SetBuuton()

    def bind_1(self,event=None):# �����Ӧ����
        pass

    def bind_2(self,event):# ��꾭����Ӧ����
        if self.x1<=event.x<=self.x2 and self.y1<=event.y<=self.y2:# ��Ӧ��λ��
            self.canvas.itemconfigure(self.r1,outline='gold')# ���������ɫ
            self.canvas.itemconfigure(self.r2,outline='gold')# �����ڿ���ɫ
            self.canvas.itemconfigure(self.t,fill='gold')# ������ʾ�ı���ɫ
        else:
            self.canvas.itemconfigure(self.r1,outline='white')# �ָ����Ĭ����ɫ
            self.canvas.itemconfigure(self.r2,outline='white')# �ָ��ڿ�Ĭ����ɫ
            self.canvas.itemconfigure(self.t,fill='white')# �ָ���ʾ�ı�Ĭ����ɫ
    def SetBuuton(self):
        self.canvas.bind('<Button-1>',lambda event:self.bind_1(event))# ����������¼�
        self.canvas.bind('<Motion>',lambda event:self.bind_2(event))# ������꾭���¼�
flag=0
class LoginPage(object):
    def __init__(self, master=None):
        self.flag=0
        self.root = master  # �����ڲ�����root
        self.root.title('��¼����')
        self.root.geometry('%dx%d' % (300, 200))  # ���ô��ڴ�С
        self.username = StringVar()
        self.username.set('vagmr')
        self.password = StringVar()

    def fun(self):#ִ�к���
        self.createPage()


    def createPage(self):#���ý��溯��
        self.page = Frame(self.root)  # ����Frame
        self.page.pack()

        Label(self.page).grid(row=0, stick=W)
        Label(self.page, text='�˻�: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        Label(self.page, text='����: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        Button(self.page, text='��½', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='ע��', command=self.sign).grid(row=3, column=1, stick=W)
        Button(self.page, text='�˳�', command=self.page.quit).grid(row=3, column=1, stick=E)

    def sign(self):#ע�ắ��
        def sign_up_admin():
            np = new_psd.get()
            npf = new_psd_confirm.get()
            nn = new_name.get()

            with open('usrs_info.pickle', 'rb') as user_file:
                exit_user_info = pickle.load(user_file)
            if np != npf:
                tk.messagebox.showerror(title="Error", message='������������벻һ�£�')
            elif len(np)==0:
                tk.messagebox.showerror(title="Error", message='���벻��Ϊ�գ�')
            elif nn in exit_user_info:
                tk.messagebox.showerror(title="Error", message='����û����Ѿ���ע���ˣ�')
            else:
                exit_user_info[nn] = np
                with open('usrs_info.pickle', 'wb') as user_file:
                    pickle.dump(exit_user_info, user_file)
                tk.messagebox.showinfo(title='Welcome', message="ע��ɹ���")
                root_sign_up.destroy()

        root_sign_up = tk.Toplevel(self.root)
        root_sign_up.geometry('350x200')
        root_sign_up.title('ע�����')

        new_name = tk.StringVar()
        new_name.set('vagmr')
        tk.Label(root_sign_up, text="�û�����").place(x=10, y=10)
        entry_new_name = tk.Entry(root_sign_up, textvariable=new_name).place(x=120, y=10)

        new_psd = tk.StringVar()
        new_psd.set('')
        tk.Label(root_sign_up, text="���룺").place(x=10, y=60)
        entry_new_psd = tk.Entry(root_sign_up, textvariable=new_psd, show='*').place(x=120, y=60)

        new_psd_confirm = tk.StringVar()
        new_psd_confirm.set('')
        tk.Label(root_sign_up, text="��ȷ�����룺").place(x=10, y=110)
        entry_new_psd_confirm = tk.Entry(root_sign_up, textvariable=new_psd_confirm, show='*').place(x=120, y=110)

        btn_comfirm_sign_up = tk.Button(root_sign_up, text='ע��', command=sign_up_admin)
        btn_comfirm_sign_up.place(x=170, y=160)

    def loginCheck(self):#��¼����
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
                tk.messagebox.showinfo(title="��¼�ɹ�", message='��ã�' + name+'��\n���ٴε�����밴ť������������ϵͳ~')
                global flag
                flag=1
                self.root.destroy()

            else:
                tk.messagebox.showerror(message="�������")
        else:
            is_sign_up = tk.messagebox.askyesno(title='Hi', message='�㻹û��ע�ᣬҪ����ǰ��ע����')

            if is_sign_up:
                self.sign()
money=20
class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # �����ڲ�����root
        self.root.title('�󹦵�ϵͳ')
        self.root.geometry('%dx%d' % (900, 600))  # ���ô��ڴ�С
        self.money=0
        self.volume=0.5
        self.count=0
        self.funcPage()

    def funcPage(self):#��������

        def Load1():#����-10����
            global texty1, count1
            if texty1 > 340:
                new2 = self.canvans_main.create_text(380, texty1, anchor='nw', text='����-10',
                                          font=('����', 40), fill='black')
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
        def Load():#����+1����
            global texty, count
            if texty > 340:
                new1 = self.canvans_main.create_text(380, texty, anchor='nw', text='����+1',
                                          font=('����', 40), fill='black')
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



        def Laugh(evnet=None):#����Ц����
            '''
            ��һ��������Ц
            :return:
            '''

            def UpDate():
                self.canvans_main.update()
            if self.money<10:
                tk.messagebox.showerror(message='���²��㣡')

            else:
                Load1()
                mu1=pygame.mixer.Sound('fozu.mp3')
                mu1.play()
                self.canvans_main.update()
                self.root.update_idletasks()
                self.root.after(1,UpDate)
                for i in levallist:
                    self.canvans_main.delete(i)
                new = self.canvans_main.create_text(10, 10, anchor='nw', text='����:%d' % (self.money-10),
                                                    font=('����', 50), fill='white')
                self.money = self.money - 10
                levallist.append(new)

                self.root.update_idletasks()
        #��1��������Ц
        self.root.bind('1', Laugh)

        levallist=[]

        def Knock():#��ľ��
            self.canvans_main.delete(la3)
            Load()
            print('����+1')
            self.money=self.money+1
            new=self.canvans_main.create_text(10, 10, anchor='nw',text='����:%d' % (self.money),font=('����',50),fill='white')
            self.count+=1
            mu2=pygame.mixer.Sound('muyu.mp3')
            mu2.play()
            for i in levallist:
                self.canvans_main.delete(i)
            levallist.append(new)
            for i in range(self.count-1):
                self.canvans_main.delete(levallist[i])
            self.root.update_idletasks()
        self.canvans_main = Canvas(self.root, width=900, height=600, highlightthickness=0)  #������Ļ���
        self.chick = self.canvans_main.create_image(0, 0, anchor='nw', image=root_img1)
        self.canvans_main.pack()
        la3 = self.canvans_main.create_text(10, 10, anchor='nw',text='����:0' ,font=('����',50),fill='white')

        def Helptip():#����ҳ
            helptop = tk.Toplevel()
            helptop.title('����')
            helptop.geometry('400x250')
            helptext = '����\n��ӭ����󹦵�ϵͳ\n����·���ť�û�ľ����ܹ���\n����Ե���·���ť���Ĺ����÷�������Ц\nҲ���Կ�\'1\'�����÷�������Ц\n���๦�����ڿ��������ᣩ'
            tk.Label(helptop, text=helptext,font=('����',15)).pack()
        b02 = Button(self.root, bg='white', bd=0, font=('����', 30), fg='gold', text='����', command=Helptip)
        b02.place(width=120, height=50, x=560, y=10)  # ������ť

        def Setpage():#����ҳ
            settop = tk.Toplevel()
            settop.title('����')
            settop.geometry('400x350')
            abouttext = '   ����'
            def tip():
                tk.messagebox.showinfo(message='����')
            la01=tk.Label(settop,text='����',font=('����',20))
            la01.place(x=110,y=85)
            la02 = tk.Label(settop, text='����', font=('����', 20))
            la02.place(x=110, y=175)
            la03 = tk.Label(settop, text='����', font=('����', 20))
            la03.place(x=110, y=255)
            b05=tk.Button(settop,text='��������',font=('����',20),command=tip)
            b05.place(x=210,y=85)
            b06 = tk.Button(settop, text='����', font=('����', 20),command=tip)
            b06.place(x=210, y=165)
            b07 = tk.Button(settop, text='�ر�', font=('����', 20),command=tip)
            b07.place(x=210, y=245)
            tk.Label(settop, text=abouttext,font=('����',25)).pack()


        b01 = Button(self.root, bg='white', bd=0, font=('����', 30), fg='gold', text='����', command=Setpage)
        b01.place(width=120, height=50, x=700, y=10)  # ���ð�ť
        #���ڰ�ť
        class About(CreateButton):
            def __init__(self, master=None, canvas=None, x1=None, y1=None, x2=None, y2=None, str1=None, fontsize=30):
                '''
                ������ť
                :param master: �����Ĵ���
                :param canvas: ����
                :param x1: ��ť���϶��������
                :param y1: ��ť���϶���������
                :param x2: ��ť���¶��������
                :param y2: ��ť���¶���������
                :param str1: ��ť�ϵ�����
                :param fontsize: ��ť�ϵ������С
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
                                                       outline='white')  # ��ť���
                self.r2 = self.canvas.create_oval(self.x1 + 3, self.y1 + 3, self.x2 - 3, self.y2 - 3, width=2,
                                                       outline='white')  # ��ť�ڿ�
                self.t = self.canvas.create_text((self.x1 + self.x2) / 2, (self.y1 + self.y2) / 2, text=self.str,
                                                 font=('����', self.fontsize, 'bold'), fill='white')  # ��ť��ʾ�ı�
                self.SetBuuton()
            def Abouttip(self):
                abouttop = tk.Toplevel()
                abouttop.title('����')
                abouttop.geometry('500x320')
                abouttext = '*************************\n\n����ϵͳV0.0.1\n\nĳ\nĳ\n���ߣ�vagmr\n\n*************************'
                tk.Label(abouttop, text=abouttext,font=('����',15)).pack()

            def bind_1(self, event=None):  # �����Ӧ����
                if self.x1 <= event.x <= self.x2 and self.y1 <= event.y <= self.y2:  # ��Ӧ��λ��
                    self.Abouttip()  # ����
        About(self.root, self.canvans_main, 830, 10, 880, 60, '?')


        #��ľ�㰴ť
        b03=Button(self.root,text='����˴��û�ľ��',bd=4,bg='gold',font=('����',30),command=Knock)
        b03.place(x=50,y=510)

        # ����Ц��ť
        b04 = Button(self.root, text='��1��������Ц', bd=4, bg='gold', font=('����', 30), command=Laugh)
        b04.place(x=500, y=510)


        def Recharge():#��ֵ��ť
            chargetop=Toplevel(self.root)
            chargetop.title('������')
            chargetop.geometry('400x400')
            tk.Label(chargetop,text='���Ӱ�ȫ����ʹ��΢�Ż������ɨһɨ',font=('����',15)).pack()
            tk.Label(chargetop,image=root_img2).pack()

        b06 = Button(self.root, bg='red', bd=0, font=('����', 30), fg='gold', text='������', command=Recharge)
        b06.place(width=120, height=50, x=780, y=400)  # ���ð�ť
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
            i.bind('<Leave>', leave1)  # ��ť�����������¼�
        for i in [b03, b04]:
            i.bind('<Enter>', enter2)
            i.bind('<Leave>', leave2)
        b06.bind('<Enter>', enter3)
        b06.bind('<Leave>', leave3)

def login(*args, **kwargs):#��¼
    top = Toplevel()
    LoginPage(top).fun()
    while flag == 1:
        top.destroy()
        canvans_login.destroy()
        MainPage(root)
        break

class LoginButton(CreateButton):#��¼��ť
    def bind_1(self, event=None):  # �����Ӧ����
        if self.x1 <= event.x <= self.x2 and self.y1 <= event.y <= self.y2:  # ��Ӧ��λ��
            login()
##��д����
LoginButton(root,canvans_login,380-50,520-20,520+50,570+20,'�� ��',60)#���밴ť

def main():#������
    '''
    ������
    :return: ��
    '''
    root.mainloop()  # ���͵�whileѭ��

if __name__ == '__main__':
     main()

