#大作业:函数画板
#the only program
from math import *
from Tkinter import *
from tkMessageBox import *
#画主界面
def window():
    root=Tk()
    root.title('Function Drawer')
    root.geometry('500x280')
    Label(root,text='f(x)=').place(x=50,y=30,anchor=CENTER)
    global v
    v=StringVar()
    Entry(root,textvariable=v,width=30).place(x=220,y=30,anchor=CENTER)
    Button(root,text="Let's GO",command=drawy).place(x=430,y=30,anchor=CENTER)
    Button(root,text="Add Function",command=add).place(x=80,y=80,anchor=CENTER)
    Button(root,text='+',command=add1).place(x=145,y=80,anchor=CENTER)
    Button(root,text='Primitive Function',command=pf).place(x=240,y=80,anchor=CENTER)
    Button(root,text='Derivative Function',command=df).place(x=400,y=80,anchor=CENTER)
    global b1,b2
    f=Frame(root,width=110,height=140,bd=4,relief='groove')
    f.place(x=80,y=175,anchor=CENTER)
    Label(f,text='coordinate').grid()
    b1=StringVar()
    Entry(f,textvariable=b1,width=8).grid()
    b2=StringVar()
    Entry(f,textvariable=b2,width=8).grid()
    Button(root,text='   x   ',command=typex).place(x=180,y=145,anchor=CENTER)
    Button(root,text=' num ',command=num).place(x=250,y=145,anchor=CENTER)
    Button(root,text='trigonometric',command=tri).place(x=350,y=145,anchor=CENTER)
    Button(root,text='e',command=e1).place(x=430,y=145,anchor=CENTER)
    Button(root,text='pi',command=pi1).place(x=460,y=145,anchor=CENTER)
    Button(root,text='others',command=others).place(x=180,y=200,anchor=CENTER)
    Button(root,text='+-*/',command=symb).place(x=245,y=200,anchor=CENTER)
    Button(root,text='antitrigonometric',command=arc).place(x=350,y=200,anchor=CENTER)
    Button(root,text='(',command=zkh).place(x=438,y=200,anchor=CENTER)
    Button(root,text=')',command=ykh).place(x=465,y=200,anchor=CENTER)
    Button(root,text='CLEAN',command=clean).place(x=440,y=250,anchor=CENTER)
    Label(root,text='x  from:').place(x=70,y=250,anchor=CENTER)
    global v1
    v1=StringVar()
    Entry(root,textvariable=v1,width=3).place(x=120,y=250,anchor=CENTER)
    Label(root,text='to').place(x=155,y=250,anchor=CENTER)
    global v2
    v2=StringVar()
    Entry(root,textvariable=v2,width=3).place(x=190,y=250,anchor=CENTER)
    Button(root,text='clean x',command=cleanx).place(x=260,y=250,anchor=CENTER)
#点击点坐标返回模块
def callback(event):
    lx=str((event.x-750.0)/50.0)
    ly=str((500.0-event.y)/50.0)
    #print lx,ly
    b1.set('x='+lx)
    b2.set('y='+ly)
#画函数模块
def drawy():
    if v.get()=='':
        showwarning("Warning!",'You have not input any function!')
    else:
        global y
        def y(x):
            return eval(v.get())
        cell()
        draw1()
#在画布上画格子，坐标轴等
def cell():
    global t
    t=Toplevel()
    global c
    c=Canvas(t,width=1500,height=1000,bg='white')
    c.bind('<Button-1>',callback)
    c.pack()
    for i in range(1,30):
        c.create_line(50*i,0,50*i,1000,fill='gray')
    for i in range(1,20):
        c.create_line(0,50*i,1500,50*i,fill='gray')
    c.create_line(0,500,1500,500,arrow=LAST,width=4)
    c.create_line(750,0,750,1000,arrow=FIRST,width=4)
    for i in range(-14,15):
        c.create_text(50*i+748,500,text=str(i),anchor=NE)
    for i in range(9,-10,-1):
        c.create_text(748,500-50*i,text=str(i),anchor=NE)
def draw1():
    if v1.get()=='':
        sx=-15.0
    else:
        sx=float(v1.get())
    #print sx
    if v2.get()=='':
        ex=15.0
    else:
        ex=float(v2.get())
    #print ex
    tt=1
    x0=750.0+50.0*sx
    y0=500-50*y(float(x0)/50-15)
    x1=x0+tt
    y1=500-50*y(float(x1)/50-15)
    #print x0,y0,x1,y1
    c.create_line(x0,y0,x1,y1,width=3,fill='blue')
    while x1<750+50*ex:
        #print y1-y0
        x0=x1
        y0=500-50*y(float(x0)/50-15)
        x1=x0+tt
        y1=500-50*y(float(x1)/50-15)
        if abs(y1-y0)<200:
            c.create_line(x0,y0,x1,y1,width=3,fill='blue')
#画两个函数图像对比次界面模块
def add():
    global at
    at=Toplevel()
    at.title('Add New Function')
    at.geometry('400x230')
    Label(at,text='f(x)=').place(x=50,y=30,anchor=CENTER)
    Label(at,text='g(x)=').place(x=50,y=70,anchor=CENTER)
    global a1
    a1=StringVar()
    Entry(at,textvariable=a1,width=30).place(x=220,y=30,anchor=CENTER)
    global a2
    a2=StringVar()
    Entry(at,textvariable=a2,width=30).place(x=220,y=70,anchor=CENTER)
    q1=v.get()
    a1.set(q1)
    Label(at,text='x  from:').place(x=70,y=120,anchor=CENTER)
    global av1,av2
    av1=StringVar()
    Entry(at,textvariable=av1,width=3).place(x=120,y=120,anchor=CENTER)
    Label(at,text='to').place(x=155,y=120,anchor=CENTER)
    av2=StringVar()
    Entry(at,textvariable=av2,width=3).place(x=190,y=120,anchor=CENTER)
    Button(at,text='clean x',command=acleanx).place(x=260,y=120,anchor=CENTER)
    Button(at,text='GO!',command=adraw,width=15).place(x=200,y=180,anchor=CENTER)
#点击加号的添加g(x)
def add1():
    q2=v.get()
    a2.set(q2)
#画出两个函数
def adraw():
    #print a1.get()
    if a1.get()=='' or a2.get()=='':
        showwarning("Warning!",'Finish The Function!')
    else:
        att=Toplevel()
        ac=Canvas(att,width=1500,height=1000,bg='white')
        ac.bind('<Button-1>',callback)
        ac.pack()
        for i in range(1,30):
            ac.create_line(50*i,0,50*i,1000,fill='gray')
        for i in range(1,20):
            ac.create_line(0,50*i,1500,50*i,fill='gray')
        ac.create_line(0,500,1500,500,arrow=LAST,width=4)
        ac.create_line(750,0,750,1000,arrow=FIRST,width=4)
        for i in range(-14,15):
            ac.create_text(50*i+748,500,text=str(i),anchor=NE)
        for i in range(9,-10,-1):
            ac.create_text(748,500-50*i,text=str(i),anchor=NE)
        #标明函数注释
        ac.create_text(1400,50,text='f(x)',anchor=E)
        ac.create_line(1420,50,1470,50,width=4,fill='blue')
        ac.create_text(1400,80,text='g(x)',anchor=E)
        ac.create_line(1420,80,1470,80,width=4,fill='green')
        def af(x):
            return eval(a1.get())
        def ag(x):
            return eval(a2.get())
        if av1.get()=='':
            sx=-15.0
        else:
            sx=float(av1.get())
        if av2.get()=='':
            ex=15.0
        else:
            ex=float(av2.get())
        tt=1
        x0=750.0+50.0*sx
        y0=500-50*af(float(x0)/50-15)
        x1=x0+tt
        y1=500-50*af(float(x1)/50-15)
        ac.create_line(x0,y0,x1,y1,width=3,fill='blue')
        while x1<750+50*ex:
            x0=x1
            y0=500-50*af(float(x0)/50-15)
            x1=x0+tt
            y1=500-50*af(float(x1)/50-15)
            if abs(y1-y0)<200:
                ac.create_line(x0,y0,x1,y1,width=3,fill='blue')
        m0=750.0+50.0*sx
        n0=500-50*ag(float(m0)/50-15)
        m1=m0+tt
        n1=500-50*ag(float(m1)/50-15)
        ac.create_line(m0,n0,m1,n1,width=3,fill='green')
        while m1<750+50*ex:
            m0=m1
            n0=500-50*ag(float(m0)/50-15)
            m1=m0+tt
            n1=500-50*ag(float(m1)/50-15)
            if abs(n1-n0)<200:
                ac.create_line(m0,n0,m1,n1,width=3,fill='green')
#画原函数模块
def pf():
    if v.get()=='':
        showwarning("Warning!",'You have not input any function!')
    else:
        pt=Toplevel()
        pt.title('Primitive Function')
        pc=Canvas(pt,width=1500,height=1000,bg='white')
        pc.bind('<Button-1>',callback)
        pc.pack()
        for i in range(1,30):
            pc.create_line(50*i,0,50*i,1000,fill='gray')
        for i in range(1,20):
            pc.create_line(0,50*i,1500,50*i,fill='gray')
        pc.create_line(0,500,1500,500,arrow=LAST,width=4)
        pc.create_line(750,0,750,1000,arrow=FIRST,width=4)
        for i in range(-14,15):
            pc.create_text(50*i+748,500,text=str(i),anchor=NE)
        for i in range(9,-10,-1):
            pc.create_text(748,500-50*i,text=str(i),anchor=NE)
        if v1.get()=='':
            sx=0.0
        else:
            sx=float(v1.get())
        if v2.get()=='':
            ex=15.0
        else:
            ex=float(v2.get())
        def y(x):
            return eval(v.get())
        tt=1
        x0=750.0+50.0*sx
        y0=500-50*y(float(x0)/50-15)
        yy0=500
        x1=x0+tt
        y1=500-50*y(float(x1)/50-15)
        yy1=500-((500-yy0)+y(float(x1)/50-15))
        #print yy1
        pc.create_line(x0,yy0,x1,yy1,width=3,fill='blue')
        while x1<750+50*ex:
        #print y1-y0
            x0=x1
            y0=500-50*y(float(x0)/50-15)
            yy0=yy1
            x1=x0+tt
            y1=500-50*y(float(x1)/50-15)
            yy1=500-((500-yy0)+y(float(x1)/50-15))
            pc.create_line(x0,yy0,x1,yy1,width=3,fill='blue')
#画导函数模块
def df():
    if v.get()=='':
        showwarning("Warning!",'You have not input any function!')
    else:
        dt=Toplevel()
        dt.title('Derivative Function')
        dc=Canvas(dt,width=1500,height=1000,bg='white')
        dc.bind('<Button-1>',callback)
        dc.pack()
        for i in range(1,30):
            dc.create_line(50*i,0,50*i,1000,fill='gray')
        for i in range(1,20):
            dc.create_line(0,50*i,1500,50*i,fill='gray')
        dc.create_line(0,500,1500,500,arrow=LAST,width=4)
        dc.create_line(750,0,750,1000,arrow=FIRST,width=4)
        for i in range(-14,15):
            dc.create_text(50*i+748,500,text=str(i),anchor=NE)
        for i in range(9,-10,-1):
            dc.create_text(748,500-50*i,text=str(i),anchor=NE)
        if v1.get()=='':
            sx=-15.0
        else:
            sx=float(v1.get())
        if v2.get()=='':
            ex=15.0
        else:
            ex=float(v2.get())
        def y(x):
            return eval(v.get())
        tt=1
        x0=750.0+50.0*sx
        y0=500-50*y(float(x0)/50-15)
        x1=x0+tt
        y1=500-50*y(float(x1)/50-15)
        dy1=500-50*(y0-y1)
        while x1<750+50*ex:
            x0=x1
            y0=500-50*y(float(x0)/50-15)
            dy0=dy1
            x1=x0+tt
            y1=500-50*y(float(x1)/50-15)
            dy1=500-50*(y0-y1)
            dc.create_line(x0,dy0,x1,dy1,width=3,fill='blue')
#以下都是定义一些输入键的模块
def typex():
    v.set(v.get()+'x')
def num():
    l=Toplevel()
    l.title('numbers')
    l.geometry('305x300')
    Label(l,text='f(x)').grid()
    e=Entry(l,textvariable=v,width=30)
    e.grid(row=0,column=1)
    Button(l,text='1',width=6,command=num1).place(x=50,y=70,anchor=CENTER)
    Button(l,text='2',width=6,command=num2).place(x=150,y=70,anchor=CENTER)
    Button(l,text='3',width=6,command=num3).place(x=250,y=70,anchor=CENTER)
    Button(l,text='4',width=6,command=num4).place(x=50,y=130,anchor=CENTER)
    Button(l,text='5',width=6,command=num5).place(x=150,y=130,anchor=CENTER)
    Button(l,text='6',width=6,command=num6).place(x=250,y=130,anchor=CENTER)
    Button(l,text='7',width=6,command=num7).place(x=50,y=190,anchor=CENTER)
    Button(l,text='8',width=6,command=num8).place(x=150,y=190,anchor=CENTER)
    Button(l,text='9',width=6,command=num9).place(x=250,y=190,anchor=CENTER)
    Button(l,text='0',width=6,command=num0).place(x=150,y=250,anchor=CENTER)
    Button(l,text='.',width=6,command=num_).place(x=250,y=250,anchor=CENTER)
    Button(l,text='C',width=6,command=clean).place(x=50,y=250,anchor=CENTER)
def num1():
    v.set(v.get()+'1')
def num2():
    v.set(v.get()+'2')
def num3():
    v.set(v.get()+'3')
def num4():
    v.set(v.get()+'4')
def num5():
    v.set(v.get()+'5')
def num6():
    v.set(v.get()+'6')
def num7():
    v.set(v.get()+'7')
def num8():
    v.set(v.get()+'8')
def num9():
    v.set(v.get()+'9')
def num0():
    v.set(v.get()+'0')
def num_():
    v.set(v.get()+'.')
def tri():
    l=Toplevel()
    l.title('trigonometric')
    l.geometry('305x240')
    Label(l,text='f(x)').grid()
    e=Entry(l,textvariable=v,width=30)
    e.grid(row=0,column=1)
    Button(l,text='sin',width=6,command=sin1).place(x=150,y=70,anchor=CENTER)
    Button(l,text='tan',width=6,command=tan1).place(x=50,y=130,anchor=CENTER)
    Button(l,text='C',width=6,command=clean).place(x=250,y=130,anchor=CENTER)
    Button(l,text='cos',width=6,command=cos1).place(x=150,y=190,anchor=CENTER)
def sin1():
    v.set(v.get()+'sin(')
def cos1():
    v.set(v.get()+'cos(')
def tan1():
    v.set(v.get()+'tan(')
def others():
    l=Toplevel()
    l.title('others')
    l.geometry('305x240')
    Label(l,text='f(x)').grid()
    e=Entry(l,textvariable=v,width=30)
    e.grid(row=0,column=1)
    Button(l,text='sqrt',width=6,command=sqrt1).place(x=150,y=70,anchor=CENTER)
    Button(l,text='^',width=6,command=index1).place(x=50,y=130,anchor=CENTER)
    Button(l,text='abs',width=6,command=abs1).place(x=250,y=130,anchor=CENTER)
    Button(l,text='ln',width=6,command=ln).place(x=150,y=190,anchor=CENTER)
    Button(l,text='C',width=6,command=clean).place(x=150,y=130,anchor=CENTER)
def sqrt1():
    v.set(v.get()+'sqrt(')
def index1():
    v.set(v.get()+'**')
def abs1():
    v.set(v.get()+'abs(')
def ln():
    v.set(v.get()+'log(,e)')
def symb():
    l=Toplevel()
    l.title('symbol')
    l.geometry('305x240')
    Label(l,text='f(x)').grid()
    e=Entry(l,textvariable=v,width=30)
    e.grid(row=0,column=1)
    Button(l,text='+',width=6,command=plus).place(x=150,y=70,anchor=CENTER)
    Button(l,text='-',width=6,command=minus).place(x=50,y=130,anchor=CENTER)
    Button(l,text='*',width=6,command=multiply).place(x=250,y=130,anchor=CENTER)
    Button(l,text='/',width=6,command=divide).place(x=150,y=190,anchor=CENTER)
    Button(l,text='C',width=6,command=clean).place(x=150,y=130,anchor=CENTER)
def plus():
    v.set(v.get()+'+')
def minus():
    v.set(v.get()+'-')
def multiply():
    v.set(v.get()+'*')
def divide():
    v.set(v.get()+'/')
def arc():
    l=Toplevel()
    l.title('antitrigonometric')
    l.geometry('305x240')
    Label(l,text='f(x)').grid()
    e=Entry(l,textvariable=v,width=30)
    e.grid(row=0,column=1)
    Button(l,text='arcsin',width=6,command=arcsin1).place(x=150,y=70,anchor=CENTER)
    Button(l,text='arctan',width=6,command=arctan1).place(x=50,y=130,anchor=CENTER)
    Button(l,text='C',width=6,command=clean).place(x=250,y=130,anchor=CENTER)
    Button(l,text='arcos',width=6,command=arcos1).place(x=150,y=190,anchor=CENTER)
def arcsin1():
    v.set(v.get()+'asin(')
def arcos1():
    v.set(v.get()+'acos(')
def arctan1():
    v.set(v.get()+'atan(')
def e1():
    v.set(v.get()+'e')
def pi1():
    v.set(v.get()+'pi')
def zkh():
    v.set(v.get()+'(')
def ykh():
    v.set(v.get()+')')
def clean():
    v.set('')
def cleanx():
    v1.set('')
    v2.set('')
def acleanx():
    av1.set('')
    av2.set('')
def main():
    window()
    mainloop()
main()
