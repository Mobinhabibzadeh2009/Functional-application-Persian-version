#فراخوانی کتابخانه ها
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import Label, Tk 
import time
import pygame
import random
import calendar
from tkinter import filedialog
import tkinter as tk
from  PIL import Image, ImageTk
import os
#ساخت صفحه اصلی
def home():
    home=Tk()
    home.title("صفحه اصلی")
    home.geometry("300x470")
    home.resizable(False,False)
    home.configure(bg="gray",cursor="circle")
    Label(home,text="سلام خوش آمدید",font=("B titr",12),bg="black",fg="yellow").pack()
    Label(home,text="یکی از قسمت هارا برای ادامه انتخاب کنید",font=("B titr",12),bg="black",fg="yellow").pack()
    Label(home,text="سازنده:مبین حبیب زاده",font=("B titr",12),bg="black",fg="red").pack()

    


    
    def winn():
        win=Tk()
        win.title("کاربردی")
        win.geometry("300x470")
        win.configure(bg="pink",cursor="circle")
        win.resizable(False,False)
        lb=Label(win,text="قسمت  برنامه های کاربردی",font=("B titr",12),bg="pink",fg="black")
        lb.pack()
        lp=Label(win,text="برنامه نویسی: مبین حبیب زاده",font=("B titr",11),bg="pink",fg="blue")
        lp.pack()
        #قسمت ماشین حساب
        def clacu():
                #یک صفحه درست میکنیم
                class Calculator:




                    def __init__(self, master):

                        '''
                        DOCSTRING: Define what to do on initialization
                        '''
                        
                        #Assign reference to the main window of the application
                        self.master = master

                        #افزدون نام
                        master.title("ماشین حساب")
                        
                        #افزدون صفحه نمایش
                        self.equation=Entry(master, width=25,border=3, borderwidth=7,font=("Baloo",10))

                        #افزدون اپ گرید
                        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

                        #ساخت دکمه
                        self.createButton()




                    def createButton(self):
                        
                        #ساختن دکمه ها
                        b0 = self.addButton(0)
                        b1 = self.addButton(1)
                        b2 = self.addButton(2)
                        b3 = self.addButton(3)
                        b4 = self.addButton(4)
                        b5 = self.addButton(5)
                        b6 = self.addButton(6)
                        b7 = self.addButton(7)
                        b8 = self.addButton(8)
                        b9 =  self.addButton(9)
                        b_add = self.addButton('+')
                        b_sub = self.addButton('-')
                        b_mult = self.addButton('*')
                        b_div = self.addButton('÷')
                        b_clear = self.addButton('c')
                        b_equal = self.addButton('=')

                        #ترتیب بندی
                        row1=[b7,b8,b9,b_add]
                        row2=[b4,b5,b6,b_sub]
                        row3=[b1,b2,b3,b_mult]
                        row4=[b_clear,b0,b_equal,b_div]

                        #گرافیکی کردن دکمه
                        r=1
                        for row in [row1, row2, row3, row4]:
                            c=0
                            for buttn in row:
                                buttn.grid(row=r, column=c, columnspan=1)
                                c+=1
                            r+=1




                    def addButton(self,value):

                            return Button(self.master, text=value, width=9, command = lambda: self.clickButton(str(value)))
                    



                    def clickButton(self, value):
                        
                        
                        #Get the equation that's entered by the user
                        current_equation=str(self.equation.get())
                        
                        #تعریف دکمه پاک کردن
                        if value == 'c':
                            self.equation.delete(-1, END)
                        
                        #=تعریف
                        elif value == '=':
                            answer = str(eval(current_equation))
                            self.equation.delete(-1, END)
                            self.equation.insert(0, answer)
                        
                        #تعریف کیلک بروی ان
                        else:
                            self.equation.delete(0, END)
                            self.equation.insert(-1, current_equation+value)




                #Execution
                if __name__=='__main__':
                    
                    #ایجاد صفحه ظاهری
                    root = Tk()
                    root.title("ماشین حساب")
                    root.configure(bg="light green",cursor="circle")
                    root.resizable(False,False)
                    root.geometry("310x160") 
                    menubar=Menu(root)
                    feilemenu=Menu(menubar , tearoff=0)
                    #افزدون منو
                    menubar.add_command(label="بستن" , command=root.destroy)
                    root.config(menu=menubar)
                    
                    my_gui = Calculator(root)
                    
                    
                    root.mainloop() 
        #قسمت نوت پد
        def txt():
            #ایجاد بدنه 
            txt_my=Tk()
            txt_my.title("دفتر یادداشت")
            txt_my.geometry("310x300")
            txt_my.configure(bg="yellow",cursor="circle")
            op_txt=Text(txt_my,width=40,height=10,font=("B titr",12))
            op_txt.pack()
            #تعیرف امکان سیو
            def save_text():
                with open("output.txt","w") as f:
                    f.write(op_txt.get(1.0,END))
            def load_text():
                with open("output.txt") as f: 
                    date=f.read()
                op_txt.insert(INSERT,date)
            #تعریف منو
            menubar=Menu(txt_my)
            filemenuyy=Menu(menubar , tearoff=0)
            menubar.add_cascade(label="منو",menu=filemenuyy)
            filemenuyy.add_command(label="ذخیره",command=save_text)
            filemenuyy.add_command(label="بارگذاری از حافظه" , command=load_text)
            txt_my.config(menu=menubar)
            def maxmize_txt():
                txt_my.geometry("310x300")
            def minmize_txt():
                txt_my.geometry("1x1")
            filemenuy=Menu(menubar , tearoff=0)
            menubar.add_command(label="خروج" , command=txt_my.destroy)
            txt_my.config(menu=menubar)
            txt_my.mainloop()
        #قسمت ساعت دیجیتال
        def clock():
            #تعیرف بدنه
            root = Tk()
            root.title("ساعت دیجیتال")
            width = 700
            height = 200
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            x = (screen_width/2)- (width/2)
            y = (screen_height/2)- (height/2)
            root.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root.config(bg="green",cursor="circle")
            #تعریف تنظیمات ظاهری
            def Edit_clock():
                edc=Tk()
                edc.title("تنظیمات")
                edc.geometry("250x230")
                Label(edc,text="تنظیمات ظاهری",font=("b titr",12)).pack()
                scale_c=Scale(edc,from_=1,to=10,orient=HORIZONTAL)
                scale_c.pack()
                def get_clock():
                    scale_clock=scale_c.get()
                    if scale_clock==1:
                        root.config(bg="black")
                    elif scale_clock==2:
                        root.config(bg="white")
                    elif scale_clock==3:
                        root.config(bg="red")  
                    elif scale_clock==4:
                        root.config(bg="blue")
                    elif scale_clock==5:
                        root.config(bg="yellow")
                    elif scale_clock==6:
                        root.config(bg="green")
                    elif scale_clock==7:
                        root.config(bg="pink")
                    elif scale_clock==8:
                        root.config(bg="purple")
                    elif scale_clock==9:
                        root.config(bg="orange")
                    elif scale_clock==10:
                        root.config(bg="light green")         
                def returnn():
                    root.config(bg="green")        
                Button(edc,text="ذخیره ویرایش",width=15,command=get_clock,font=("b titr",11),bg="green").pack()
                Button(edc,text="بستن",command=edc.destroy,width=15,font=("b titr",11),bg="red").pack()
                Button(edc,text="بازگشت به حالت اول",command=returnn,width=15,font=("b titr",11),bg="orange").pack()
                edc.mainloop()
            #تعیرف منو    
            menubar=Menu(root)      
            filemen=Menu(menubar , tearoff=0)
            menubar.add_command(label="تنظیمات ظاهری",command=Edit_clock)
            menubar.add_command(label="بستن" , command=root.destroy)
            root.config(menu=menubar) 
            #تعریف بدست اوری زمان
            def tick():
                setTime=time.strftime('Time: %I %M %S %p')
                clock.config(text=setTime)
                clock.after(200,tick)
            Top = Frame(root, width=1000, bd=1, relief=SOLID)
            Top.pack(side=TOP)
            Mid = Frame(root, width=1000)
            Mid.pack(side=TOP, expand=1)
            lbl_title = Label(Top, text="برنامه نویسی : مبین حبیب زاده", width=1000, font=("B titr", 20))
            lbl_title.pack(fill=X)
            clock= Label(Mid, font=('Baloo', 50 , 'bold'), fg="blue", bg="light blue")
            clock.pack()
            if __name__=='__main__':
                tick()
            root.mainloop()    
        #قسمت پخش موسیقی
        def Music_pleyer():
                    #فراخوانی کتابخانه 
                    import pygame
                    import tkinter as tkr
                    from tkinter.filedialog import askdirectory
                    import os
                    music_player = tkr.Tk()
                    music_player.title("پخش کننده موسیقی")
                    music_player.geometry("450x500")
                    music_player.configure(cursor="circle")
                    menubar=Menu(music_player)
                    filemenuq=Menu(menubar , tearoff=0)
                    menubar.add_cascade(label="سایز ",menu=filemenuq)
                    filemenuq.add_command(label="بستن" , command=music_player.destroy)
                    music_player.config(menu=menubar)
                    directory = askdirectory()
                    os.chdir(directory)
                    song_list = os.listdir()

                    play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='white',fg="black", selectmode=tkr.SINGLE)
                    for item in song_list:
                        pos = 0
                        play_list.insert(pos, item)
                        pos += 1
                    pygame.init()
                    pygame.mixer.init()

                    def play():
                        pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
                        var.set(play_list.get(tkr.ACTIVE))
                        pygame.mixer.music.play()
                    def stop():
                        pygame.mixer.music.stop()
                    def pause():
                        pygame.mixer.music.pause()
                    def unpause():
                        pygame.mixer.music.unpause()
                    Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 13 bold", text="پخش",command=play, bg="gray", fg="black")
                    Button2 = tkr.Button(music_player, width=2, height=3, font="Helvetica 13 bold", text="بستن آهنگ", command=stop, bg="black", fg="white")
                    Button3 = tkr.Button(music_player, width=2, height=3, font="Helvetica 13 bold", text="توقف", command=pause, bg="gray", fg="black")
                    Button4 = tkr.Button(music_player, width=2, height=3, font="Helvetica 13 bold", text="ادامه پخش", command=unpause, bg="black", fg="white")
                    
                    

                    var = tkr.StringVar() 
                    song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

                    song_title.pack()
                    Button1.pack(fill="x")
                    Button2.pack(fill="x")
                    Button3.pack(fill="x")
                    Button4.pack(fill="x")
                    play_list.pack(fill="both", expand="yes")
                    music_player.mainloop()
        #قسمت صفحه راهنما
        def help_page():    
            help=Tk()
            help.title("راهنما")
            help.geometry("450x150")
            help.configure(bg="light blue",cursor="circle")
            help.resizable(False,False)   
            Label(help,text="در این قسمت برنامه های کاربردی قرار دارند ",font=("B titr",10),fg="black",bg="light blue").pack()
            Label(help,text="برای استفاده از پخش کننده موسیقی پس از باز کردن آن",font=("B titr",10),bg="red",fg="blue").pack()
            Label(help,text="پوشه حاوی موسیقی را انتخاب و سپس باز کنید",font=("B titr",10),bg="red",fg="blue").pack()
            Label(help,text="طراحی و برنامه نویسی : مبین حبیب زاده ",font=("B titr",10),bg="green",fg="black").pack()
            help.mainloop()  
        
        #قسمت درباره
        def about():
            about=Tk()
            about.title("درباره")   
            about.geometry("320x350") 
            about.configure(bg="brown",cursor="circle")
            Label(about,text="طراحی و برنامه نویسی: مبین حبیب زاده",font=("B koodak",14),bg="brown",fg="white").pack()
            Label(about,text="هدف از ساخت این برنامه استفاده راحتتر و یکجا",font=("B koodak",14),bg="brown",fg="white").pack()
            Label(about,text="از برنامه های کاربردی برای دانش آموزان است",font=("B koodak",14),bg="brown",fg="white").pack()
            about.mainloop()
        #قسمت تقویم
        def calender():
            calen=Tk()
            calen.title("calender")
            calen.resizable(False,False)
            calen.configure(cursor="circle")
            calen.geometry("300x350")
            Label(calen,text="سال ",font=("B koodak",12),bg="light green").pack()
            fir1=Entry(calen,width=20,font=("Black ops one",10))
            fir1.pack()
            Label(calen,text="ماه",font=("B koodak",12),bg="light green").pack()
            fir2=Entry(calen,width=20,font=("Black ops one",10))
            fir2.pack()
            def geting():
                import calendar
                aa=fir1.get()
                bb=fir2.get()

                mobin=calendar.month(int(aa),int(bb))
                Label(calen,text=mobin,font=("Arial",12),bg="light green").pack()
            Button(calen,text="نمایش تقویم ",font=("B Koodak",13),bg="orange",width=11,command=geting).pack()
            menubar=Menu(calen)
            calenmenu=Menu(menubar , tearoff=0)
            #افزدون منو
            menubar.add_command(label="بستن" , command=calen.destroy)
            calen.config(menu=menubar)
            
            calen.mainloop()

        #افزدون دکمه های اصلی
        Button(win,text="ماشین حساب",font=("B Koodak",13),bg="red",width=11,command=clacu).pack()
        Button(win,text="ساعت دیجیتال",font=("B Koodak",13),bg="orange",width=11,command=clock).pack()
        Button(win,text="دفتر یادداشت",font=("B Koodak",13),bg="yellow",width=11,command=txt).pack()
        Button(win,text="تقویم میلادی",font=("B Koodak",13),bg="green",width=11,command=calender).pack()
        Button(win,text="پخش کننده موسیقی",font=("B Koodak",13),bg="light blue",width=11,command=Music_pleyer).pack()
        Button(win,text="درباره",font=("B Koodak",13),bg="blue",width=11,command=about).pack()
        lc=Label(win,text=":راهنمای برنامه",font=("B titr",11),bg="pink",fg="black")
        lc.pack()
        Button(win,text="راهنما",font=("B Koodak",13),bg="purple",width=11,command=help_page).pack()


        #قسمت تنظیمات
        def Edit():
            edit=Tk()
            edit.title("تنظیمات")
            edit.geometry("250x230")
            edit.resizable(False,False)
            edit.configure(cursor="circle")
            Label(edit,text="تنظیمات ظاهری",font=("b titr",12)).pack()
            scale=Scale(edit,from_=1,to=11,orient=HORIZONTAL)
            scale.pack()
            def get_scale():
                scale_1=scale.get()
                if scale_1==11:
                    win.configure(bg="black")
                    lb.config(bg="black",fg="white")
                    lc.config(bg="black",fg="white")
                    lp.config(bg="black",fg="white")
                elif scale_1==1:
                    win.configure(bg="light green")
                    lb.config(bg="light green",fg="black")
                    lc.config(bg="light green",fg="black")
                    lp.config(bg="light green",fg="blue")
                elif scale_1==2:
                    win.configure(bg="pink")
                    lb.config(bg="pink",fg="black")
                    lc.config(bg="pink",fg="black")
                    lp.config(bg="pink",fg="blue")
                elif scale_1==3:
                    win.configure(bg="red") 
                    lb.config(bg="red",fg="white")
                    lc.config(bg="red",fg="white")
                    lp.config(bg="red",fg="white")   
                elif scale_1==4:
                    win.configure(bg="blue")
                    lb.config(bg="blue",fg="white")
                    lc.config(bg="blue",fg="white")
                    lp.config(bg="blue",fg="white") 
                elif scale_1==5:
                    win.configure(bg="light blue")  
                    lc.config(bg="light blue",fg="black")
                    lp.config(bg="light blue",fg="black") 
                    lb.config(bg="light blue",fg="blue")
                elif scale_1==6:
                    win.configure(bg="dark blue")  
                    lb.config(bg="dark blue",fg="white")
                    lc.config(bg="dark blue",fg="white")
                    lp.config(bg="dark blue",fg="white") 
                elif scale_1==7:
                    win.configure(bg="orange") 
                    lb.config(bg="orange",fg="black")
                    lc.config(bg="orange",fg="black")
                    lp.config(bg="orange",fg="blue")      
                elif scale_1==8:
                    win.configure(bg="yellow")
                    lb.config(bg="yellow",fg="black")
                    lc.config(bg="yellow",fg="black")
                    lp.config(bg="yellow",fg="blue") 
                elif scale_1==9:
                    win.configure(bg="purple")
                    lb.config(bg="purple",fg="white")
                    lc.config(bg="purple",fg="white")
                    lp.config(bg="purple",fg="blue") 
                elif scale_1==10:
                    win.configure(bg="white")
                    lb.config(bg="white",fg="black")
                    lc.config(bg="white",fg="black")
                    lp.config(bg="white",fg="blue") 
            def return_default():
                win.config(bg="pink")    
                lb.config(bg="pink",fg="black")
                lc.config(bg="pink",fg="black")
                lp.config(bg="pink",fg="blue")
            Button(edit,text="ذخیره",command=get_scale , font=("B titr",11),bg="green",width=15).pack()
            Button(edit,text="بستن",command=edit.destroy,font=("B titr",11),bg="red",width=15).pack()
            Button(edit,text="بازگشت به حالت اول",command=return_default,font=("B titr",11),bg="orange",width=15).pack()
            edit.mainloop()    


        menubar=Menu(win)      
        filemenue=Menu(menubar , tearoff=0)
        menubar.add_cascade(label="منو",menu=filemenue)
        filemenue.add_command(label="فایل جدید" , command=txt)
        filemenue.add_command(label="تنظیمات ظاهری" , command=Edit)
        filemenue.add_command(label="راهنما" , command=help_page)
        win.config(menu=menubar)    
        filemenu=Menu(menubar , tearoff=0)
        menubar.add_command(label="خروج" , command=win.destroy)
        win.config(menu=menubar)
        
        
        


        win.mainloop()
    def win2():
        win2=Tk()
        win2.title("سرگرمی")
        win2.geometry("300x360")
        win2.resizable(False,False)
        win2.configure(bg="light green",cursor="circle")
        lb=Label(win2,text="قسمت بازی و سرگرمی ",font=("B titr",12),bg="light green",fg="black")
        lb.pack()
        lp=Label(win2,text="برنامه نویسی :مبین حبیب زاده",font=("B titr",11),bg="light green",fg="blue")
        lp.pack()

        #صفحه  بازی ها
        def Game_page():
        
            #ساخت بدنه بازی
            game=Tk()
            game.geometry("200x200")
            game.title("صفحه بازی")
            game.resizable(False,False)
            game.configure(bg="blue",cursor="circle")
            #snake game
            def snake_game():
                #فراخوانی کتاب خانه ها
                import pygame
                import time
                import random
                
                pygame.init()
                
                white = (255, 255, 255)
                yellow = (255, 255, 102)
                black = (0, 0, 0)
                red = (213, 50, 80)
                green = (0, 255, 32)
                blue = (50, 153, 213)
                
                dis_width = 600
                dis_height = 400
                
                dis = pygame.display.set_mode((dis_width, dis_height))
                pygame.display.set_caption('Snake Game ')
                
                clock = pygame.time.Clock()
                
                snake_block = 10
                snake_speed = 8
                
                font_style = pygame.font.SysFont("bahnschrift", 25)
                score_font = pygame.font.SysFont("comicsansms", 35)
                
                
                def Your_score(score):
                    value = score_font.render("Your Score: " + str(score), True, yellow)
                    dis.blit(value, [0, 0])
                
                
                
                def our_snake(snake_block, snake_list):
                    for x in snake_list:
                        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
                
                
                def message(msg, color):
                    mesg = font_style.render(msg, True, color)
                    dis.blit(mesg, [dis_width / 6, dis_height / 3])
                
                
                def gameLoop():
                    game_over = False
                    game_close = False
                
                    x1 = dis_width / 2
                    y1 = dis_height / 2
                
                    x1_change = 0
                    y1_change = 0
                
                    snake_List = []
                    Length_of_snake = 1
                
                    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                
                    while not game_over:
                
                        while game_close == True:
                            dis.fill(yellow)
                            message(" Lost! Press C-Play Again or Q-Quit", red)
                            Your_score(Length_of_snake - 1)
                            pygame.display.update()
                
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_q:
                                        game_over = True
                                        game_close = False
                                    if event.key == pygame.K_c:
                                        gameLoop()
                
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                game_over = True
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_LEFT:
                                    x1_change = -snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_RIGHT:
                                    x1_change = snake_block
                                    y1_change = 0
                                elif event.key == pygame.K_UP:
                                    y1_change = -snake_block
                                    x1_change = 0
                                elif event.key == pygame.K_DOWN:
                                    y1_change = snake_block
                                    x1_change = 0
                
                        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                            game_close = True
                        x1 += x1_change
                        y1 += y1_change
                        dis.fill(blue)
                        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
                        snake_Head = []
                        snake_Head.append(x1)
                        snake_Head.append(y1)
                        snake_List.append(snake_Head)
                        if len(snake_List) > Length_of_snake:
                            del snake_List[0]
                
                        for x in snake_List[:-1]:
                            if x == snake_Head:
                                game_close = True
                
                        our_snake(snake_block, snake_List)
                        Your_score(Length_of_snake - 1)
                
                        pygame.display.update()
                
                        if x1 == foodx and y1 == foody:
                            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                            Length_of_snake += 1
                
                        clock.tick(snake_speed)
                
                    pygame.quit()
                    quit()
                
                gameLoop()
            #tik-tok-teo
            def teo():

                root = Tk()
                root.title('Tic-Tac-Toe')

                #root.geometry("1200x710")

                # X starts so true
                clicked = True
                count = 0




                # دیزان دکمه ها
                def disable_all_buttons():
                    b1.config(state=DISABLED)
                    b2.config(state=DISABLED)
                    b3.config(state=DISABLED)
                    b4.config(state=DISABLED)
                    b5.config(state=DISABLED)
                    b6.config(state=DISABLED)
                    b7.config(state=DISABLED)
                    b8.config(state=DISABLED)
                    b9.config(state=DISABLED)

                #تعریف برنده شدن ایکس
                def checkifwon():
                    global winner
                    winner = False

                    if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
                        b1.config(bg="red")
                        b2.config(bg="red")
                        b3.config(bg="red")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  X بازیکن")
                        disable_all_buttons()
                    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
                        b4.config(bg="red")
                        b5.config(bg="red")
                        b6.config(bg="red")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  X بازیکن")
                        disable_all_buttons()

                    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
                        b7.config(bg="red")
                        b8.config(bg="red")
                        b9.config(bg="red")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe","برنده شد  X بازیکن")
                        disable_all_buttons()

                    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
                        b1.config(bg="red")
                        b4.config(bg="red")
                        b7.config(bg="red")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  X بازیکن")
                        disable_all_buttons()

                    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
                        b2.config(bg="red")
                        b5.config(bg="red")
                        b8.config(bg="red")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  X بازیکن")
                        disable_all_buttons()

                    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
                        b3.config(bg="red")
                        b6.config(bg="red")
                        b9.config(bg="red")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  X بازیکن")
                        disable_all_buttons()

                    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
                        b1.config(bg="red")
                        b5.config(bg="red")
                        b9.config(bg="red")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  X بازیکن")
                        disable_all_buttons()

                    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
                        b3.config(bg="red")
                        b5.config(bg="red")
                        b7.config(bg="red")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe","برنده شد  X بازیکن")
                        disable_all_buttons()

                    #تعریف برنده شدن او
                    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
                        b1.config(bg="blue")
                        b2.config(bg="blue")
                        b3.config(bg="blue")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  O بازیکن")
                        disable_all_buttons()
                    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
                        b4.config(bg="blue")
                        b5.config(bg="blue")
                        b6.config(bg="blue")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  O بازیکن")
                        disable_all_buttons()

                    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
                        b7.config(bg="blue")
                        b8.config(bg="blue")
                        b9.config(bg="blue")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  O بازیکن")
                        disable_all_buttons()

                    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
                        b1.config(bg="blue")
                        b4.config(bg="blue")
                        b7.config(bg="blue")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  O بازیکن")
                        disable_all_buttons()

                    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
                        b2.config(bg="blue")
                        b5.config(bg="blue")
                        b8.config(bg="blue")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  O بازیکن")
                        disable_all_buttons()

                    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
                        b3.config(bg="blue")
                        b6.config(bg="blue")
                        b9.config(bg="blue")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  O بازیکن")
                        disable_all_buttons()

                    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
                        b1.config(bg="blue")
                        b5.config(bg="blue")
                        b9.config(bg="blue")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  O بازیکن")
                        disable_all_buttons()

                    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
                        b3.config(bg="blue")
                        b5.config(bg="blue")
                        b7.config(bg="blue")
                        winner = True
                        messagebox.showinfo("Tic Tac Toe", "برنده شد  O بازیکن")
                        disable_all_buttons()

                    # Check if tie
                    if count == 9 and winner == False:
                        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
                        disable_all_buttons()
                                
                # تابع کلیک
                def b_click(b):
                    global clicked, count

                    if b["text"] == " " and clicked == True:
                        b["text"] = "X"
                        clicked = False
                        count += 1
                        checkifwon()
                    elif b["text"] == " " and clicked == False:
                        b["text"] = "O"
                        clicked = True
                        count += 1
                        checkifwon()
                    else:
                        messagebox.showerror("Tic Tac Toe", "اونجا قبلا پر شده یک خانه دیگر رو انتخاب کن" )

                # شروع مجدد بازی
                def reset():
                    global b1, b2, b3, b4, b5, b6, b7, b8, b9
                    global clicked, count
                    clicked = True
                    count = 0

                    # دکمه ها
                    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
                    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
                    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

                    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
                    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
                    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

                    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
                    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
                    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

                    # ساخت شطرنجی صفحه
                    b1.grid(row=0, column=0)
                    b2.grid(row=0, column=1)
                    b3.grid(row=0, column=2)

                    b4.grid(row=1, column=0)
                    b5.grid(row=1, column=1)
                    b6.grid(row=1, column=2)

                    b7.grid(row=2, column=0)
                    b8.grid(row=2, column=1)
                    b9.grid(row=2, column=2)


                # ساخت بدنه منو
                my_menu = Menu(root)
                root.config(menu=my_menu)

                # ساخت منو
                options_menu = Menu(my_menu, tearoff=False)
                my_menu.add_command(label="شروع مجدد", command=reset)
                my_menu.add_command(label="خارج شدن", command=root.destroy)

                reset()

                root.mainloop()   
            

            Label(game,text="قسمت بازی های رایانه ای",font=("B titr",12),bg="blue",fg="light blue").pack()     
            Label(game,text="برنامه نویسی : مبین حبیب زاده",font=("B titr",11),bg="blue",fg="red").pack()     
            Button(game,text="Snake Game",command=snake_game,bg="yellow",font=("Baloo",12),width=17).pack()
            Button(game,text="Tik Tok Teo",command=teo,bg="pink",font=("Baloo",12),width=17).pack()
            game.mainloop()    
            Button(home,text="راهنما",font=("B Koodak",13),bg="orange",width=11,command=home_about).pack() 
        #عدد شانسی
        def adad_shans():
            shans=Tk()
            shans.title("عدد شانسی")
            shans.geometry("300x600")
            shans.resizable(False,False)
            shans.configure(bg="blue")
            Label(shans,text="قسمت عدد شانسی",font=("B titr",13),bg="blue",fg="yellow").pack()
            Label(shans,text="عدد اول",font=("B titr",11),bg="blue",fg="red").pack()
            one=Entry(shans,width=20,font=("Baloo",10))
            one.pack()
            Label(shans,text="عدد دوم",font=("B titr",11),bg="blue",fg="red").pack()
            two=Entry(shans,width=20,font=("Baloo",10))
            two.pack()
            Label(shans,text="عدد سوم",font=("B titr",11),bg="blue",fg="red").pack()
            three=Entry(shans,width=20,font=("Baloo",10))
            three.pack()
            Label(shans,text="عدد چهارم",font=("B titr",11),bg="blue",fg="red").pack()
            four=Entry(shans,width=20,font=("Baloo",10))
            four.pack()
            Label(shans,text="عدد پنجم",font=("B titr",11),bg="blue",fg="red").pack()
            five=Entry(shans,width=20,font=("Baloo",10))
            five.pack()
            def get_shans():
                choos=[]
                one1=one.get()
                choos.append(one1)
                two2=two.get()
                choos.append(two2)
                three3=three.get()
                choos.append(three3)
                four4=four.get()
                choos.append(four4)
                five5=five.get()
                choos.append(five5)
                choice=random.choice(choos)
                Label(shans,text=choice,font=("B titr",12),bg="blue",fg="white").pack()
            Button(shans,text="انتخاب شانسی",font=("B Koodak",13),bg="orange",width=11,command=get_shans).pack() 
            def reset():
                shans.destroy()
                adad_shans()
            menubar=Menu(shans)
            shansmenu=Menu(menubar , tearoff=0)
            #افزدون منو
            menubar.add_command(label="شروع مجدد" , command=reset)
            menubar.add_command(label="بستن" , command=shans.destroy)
            shans.config(menu=menubar)
            shans.mainloop()
        #قسمت راهنما 
        def sargarmi_about():
            help=Tk()
            help.title("راهنما")
            help.geometry("450x150")
            help.configure(bg="light blue",cursor="circle")
            help.resizable(False,False)   
            Label(help,text="در این قسمت برنامه و بازی هایی در قسمت سرگرمی وجود دارند",font=("B titr",10),fg="black",bg="light blue").pack()
            Label(help,text="بازی دوز و بازی مار که به صورت گرافیکی قرار دارند",font=("B titr",10),bg="red",fg="blue").pack()
            Label(help,text="طراحی و برنامه نویسی : مبین حبیب زاده ",font=("B titr",10),bg="green",fg="black").pack()
            help.mainloop()  
        #قسمت ساخت پسورد
        def make_pass():
            password=Tk()
            password.title("پسورد ساز")
            password.geometry("300x420")
            password.resizable(False,False)
            password.configure(bg="gray",cursor="circle")
            list_number=["0","2","1","3","4","5","6","7","8","9"]
            list_horof=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
            Label(password,text=":ساخت پسورد",font=("B titr",11),bg="gray",fg="red").pack()
            scale=Scale(password,from_=4,to=6,orient=HORIZONTAL)
            scale.pack()
            #قسمت چهار کاراکتری
            def four_pass():
                num=""
                a=random.choice(list_horof)
                b=random.choice(list_number)
                c=random.choice(list_horof)
                d=random.choice(list_number)
                num+=a
                num+=b
                num+=c
                num+=d
                Label(password,text=num,font=("Baloo",13),bg="gray",fg="black").pack()
            #قسمت پنج کاراکتری    
            def five_pass():
                num=""
                a=random.choice(list_horof)
                b=random.choice(list_number)
                c=random.choice(list_number)
                d=random.choice(list_horof)
                e=random.choice(list_number)
                num+=a
                num+=b
                num+=c
                num+=d
                num+=e
                Label(password,text=num,font=("Baloo",13),bg="gray",fg="black").pack()
            #قسمت شش کاراکتری
            def six_pass():
                num=""
                a=random.choice(list_number)
                b=random.choice(list_number)
                c=random.choice(list_horof)
                d=random.choice(list_number)
                e=random.choice(list_horof)
                f=random.choice(list_number)
                num+=a
                num+=b
                num+=c
                num+=d
                num+=e
                num+=f
                Label(password,text=num,font=("Baloo",13),bg="gray",fg="black").pack()  
            #قسمت چهار کاراکتری عددی
            def four_male():
                num=""
                a=random.choice(list_number)
                b=random.choice(list_number)
                c=random.choice(list_number)
                d=random.choice(list_number)
                num+=a
                num+=b
                num+=c
                num+=d
                Label(password,text=num,font=("Baloo",13),bg="gray",fg="black").pack()
            #قسمت پنچ کاراکتری عددی
            def five_male():
                num=""
                a=random.choice(list_number)
                b=random.choice(list_number)
                c=random.choice(list_number)
                d=random.choice(list_number)
                e=random.choice(list_number)
                num+=a
                num+=b
                num+=c
                num+=d
                num+=e
                Label(password,text=num,font=("Baloo",13),bg="gray",fg="black").pack()
            #قسمت شش کاراکتری عددی
            def six_male():
                num=""
                a=random.choice(list_number)
                b=random.choice(list_number)
                c=random.choice(list_number)
                d=random.choice(list_number)
                e=random.choice(list_number)
                f=random.choice(list_number)
                num+=a
                num+=b
                num+=c
                num+=d
                num+=e
                num+=f
                Label(password,text=num,font=("Baloo",13),bg="gray",fg="black").pack()
            #قسمت چهار کاراکتری حروفی
            def four_A():
                num=""
                a=random.choice(list_horof)
                b=random.choice(list_horof)
                c=random.choice(list_horof)
                d=random.choice(list_horof)
                num+=a
                num+=b
                num+=c
                num+=d
                Label(password,text=num,font=("Baloo",13),bg="gray",fg="black").pack()
            #قسمت پنج کاراکتری حروفی
            def five_A():
                num=""
                a=random.choice(list_horof)
                b=random.choice(list_horof)
                c=random.choice(list_horof)
                d=random.choice(list_horof)
                e=random.choice(list_horof)
                num+=a
                num+=e
                num+=b
                num+=c
                num+=d
                Label(password,text=num,font=("Baloo",13),bg="gray",fg="black").pack()
            #قسمت شش کاراکتری حروفی
            def six_A():
                num=""
                a=random.choice(list_horof)
                b=random.choice(list_horof)
                c=random.choice(list_horof)
                d=random.choice(list_horof)
                e=random.choice(list_horof)
                f=random.choice(list_horof)
                num+=a
                num+=b
                num+=c
                num+=d
                num+=e
                num+=f
                Label(password,text=num,font=("Baloo",13),bg="gray",fg="black").pack()
            #تعریف شرط بار    
            def get_scale():
                scale_1=scale.get()
                if scale_1==4:
                    four_pass()
                elif scale_1==5:
                    five_pass()
                elif scale_1==6:
                    six_pass()
            #تعریف شرط بار عددی        
            def get_scale_male():
                scale_12=scale.get()
                if scale_12==4:
                    four_male()
                elif scale_12==5:
                    five_male()
                elif scale_12==6:
                    six_male()        
            #تعریف شرط بار حروفی
            def get_scale_A():
                scale_2=scale.get()
                if scale_2==4:
                    four_A()
                elif scale_2==5:
                    five_A()
                elif scale_2==6:
                    six_A()         

            Button(password,text="ساخت پسورد",font=("B Koodak",13),bg="red",width=12,command=get_scale).pack()    
            Button(password,text="ساخت فقط با عدد",font=("B Koodak",13),bg="orange",width=12,command=get_scale_male).pack()    
            Button(password,text="ساخت فقط با حروف",font=("B Koodak",13),bg="yellow",width=12,command=get_scale_A).pack()    
            def reset():
                password.destroy()
                make_pass()
            menubar=Menu(password)
            passmenu=Menu(menubar , tearoff=0)
            #افزدون منو
            menubar.add_command(label="شروع مجدد" , command=reset)
            menubar.add_command(label="بستن" , command=password.destroy)
            password.config(menu=menubar)


        Button(win2,text="بازی",font=("B Koodak",13),bg="red",width=11,command=Game_page).pack() 
        Button(win2,text="عدد شانسی",command=adad_shans,bg="orange",font=("b koodak",13),width=11).pack()
        Button(win2,text="پسورد ساز",command=make_pass,bg="yellow",font=("b koodak",13),width=11).pack()
        lc=Label(win2,text=":راهنمای  برنامه ",font=("B titr",11),bg="light green",fg="black")
        lc.pack()
        Button(win2,text="راهنما",command=sargarmi_about,bg="green",font=("b koodak",13),width=11).pack()

        #قسمت تنظیمات
        def Edit_win2():
            edit=Tk()
            edit.title("تنظیمات")
            edit.geometry("250x230")
            edit.resizable(False,False)
            edit.configure(cursor="circle")
            Label(edit,text="تنظیمات ظاهری",font=("b titr",12)).pack()
            scale=Scale(edit,from_=1,to=11,orient=HORIZONTAL)
            scale.pack()
            def get_scale():
                scale_1=scale.get()
                if scale_1==11:
                    win2.configure(bg="black")
                    lb.config(bg="black",fg="white")
                    lc.config(bg="black",fg="white")
                    lp.config(bg="black",fg="white")
                elif scale_1==5:
                    win2.configure(bg="light green")
                    lb.config(bg="light green",fg="black")
                    lc.config(bg="light green",fg="black")
                    lp.config(bg="light green",fg="blue")
                elif scale_1==2:
                    win2.configure(bg="pink")
                    lb.config(bg="pink",fg="black")
                    lc.config(bg="pink",fg="black")
                    lp.config(bg="pink",fg="blue")
                elif scale_1==3:
                    win2.configure(bg="red") 
                    lb.config(bg="red",fg="white")
                    lc.config(bg="red",fg="white")
                    lp.config(bg="red",fg="white")   
                elif scale_1==4:
                    win2.configure(bg="blue")
                    lb.config(bg="blue",fg="white")
                    lc.config(bg="blue",fg="white")
                    lp.config(bg="blue",fg="white") 
                elif scale_1==1:
                    win2.configure(bg="light blue")  
                    lb.config(bg="light blue",fg="black")
                    lc.config(bg="light blue",fg="black") 
                    lp.config(bg="light blue",fg="blue")
                elif scale_1==6:
                    win2.configure(bg="dark blue")  
                    lb.config(bg="dark blue",fg="white")
                    lc.config(bg="dark blue",fg="white")
                    lp.config(bg="dark blue",fg="white") 
                elif scale_1==7:
                    win2.configure(bg="orange") 
                    lb.config(bg="orange",fg="black")
                    lc.config(bg="orange",fg="black")
                    lp.config(bg="orange",fg="blue")      
                elif scale_1==8:
                    win2.configure(bg="yellow")
                    lb.config(bg="yellow",fg="black")
                    lc.config(bg="yellow",fg="black")
                    lp.config(bg="yellow",fg="blue") 
                elif scale_1==9:
                    win2.configure(bg="purple")
                    lb.config(bg="purple",fg="white")
                    lc.config(bg="purple",fg="white")
                    lp.config(bg="purple",fg="blue") 
                elif scale_1==10:
                    win2.configure(bg="white")
                    lb.config(bg="white",fg="black")
                    lc.config(bg="white",fg="black")
                    lp.config(bg="white",fg="blue") 
            def return_default():
                win2.config(bg="light green")    
                lb.config(bg="light green",fg="black")
                lc.config(bg="light green",fg="black")
                lp.config(bg="light green",fg="blue")
            Button(edit,text="ذخیره",command=get_scale , font=("B titr",11),bg="green",width=15).pack()
            Button(edit,text="بستن",command=edit.destroy,font=("B titr",11),bg="red",width=15).pack()
            Button(edit,text="بازگشت به حالت اول",command=return_default,font=("B titr",11),bg="orange",width=15).pack()
            edit.mainloop()    



        #ساخت منو 
        menubar=Menu(win2)
        win2menu=Menu(menubar , tearoff=0)
        #افزدون منو
        menubar.add_command(label="تنظیمات ظاهری" , command=Edit_win2)
        menubar.add_command(label="بستن" , command=win2.destroy)
        win2.config(menu=menubar)

        win2.mainloop()
    def home_about():
        ahome=Tk()
        ahome.title("راهنما")
        ahome.geometry("400x200")
        ahome.resizable(False,False)
        ahome.configure(bg="light blue")
        Label(ahome,text="برنامه به دو بخش تقسیم شده است",font=("B titr",12),bg="light blue",fg="blue").pack()
        Label(ahome,text="بخش کاربردی که برنامه های کاربردی و مفیدی قرار دارد",font=("B titr",12),bg="light blue",fg="red").pack()
        Label(ahome,text="بخش سرگرمی که برنامه و بازی های سرگرم کننده ای قرار دارد",font=("B titr",12),bg="light blue",fg="green").pack()
        Label(ahome,text="برای راحتی شما در تمامی قسمت برنامه راهنما  قرار داده شده است",font=("B titr",11),bg="red",fg="black").pack()
        Label(ahome,text="طراح و برنامه نویس : مبین حبیب زاده",font=("B titr",11),bg="yellow",fg="black").pack()

        ahome.mainloop()
    Button(home,text="کاربردی",font=("B Koodak",13),bg="light green",width=11,height=4,command=winn).pack()
    Button(home,text="سرگرمی",font=("B Koodak",13),bg="light blue",width=11,height=4,command=win2).pack()  
    Label(home,text=":راهنمای برنامه",font=("B titr",12),bg="gray",fg="black").pack()
    Button(home,text="راهنما",font=("B Koodak",13),bg="orange",width=11,command=home_about).pack() 
     
    home.mainloop()
home()    