import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation,writers

def plotrans(xx,yy,a,*args,**kwargs):
    x2,y2=[],[]

    if kwargs.get('c',None)==None:
        c='blue'
    else:
        c=kwargs.get('c',0)
    if kwargs.get('d',None)==None:
        d=0.5
    else:
        d=kwargs.get('d',0)

    if len(xx)==len(yy):
        for i in range(len(xx)):
            x2.append(a[0][0] * xx[i] + a[0][1] * yy[i])
            y2.append(a[1][0] * xx[i] + a[1][1] * yy[i])
        if len(xx)>1:
            plt.plot(x2, y2,c,linewidth=d)
        if len(xx)==1:
            plt.plot(x2,y2,c,marker='.',markersize=d)
    else:
        print('Error:x and y must have the same dimension')

def trans(xx,yy,a):
    x2, y2 = [], []
    for i in range(len(xx)):
        x2.append(a[0][0] * xx[i] + a[0][1] * yy[i])
        y2.append(a[1][0] * xx[i] + a[1][1] * yy[i])
    return [x2,y2]

def plotax(a,*args,**kwargs):
    if kwargs.get('c',None)==None:
        c='red'
    else:
        c=kwargs.get('c',0)

    for i in range(4 * int(xl[0]) + 1, 4 * int(xl[1])):
        plotrans(trans([i, i], [4 * yl[0], 4 * yl[1]],currmat[m-1])[0],trans([i, i], [4 * yl[0], 4 * yl[1]],currmat[m-1])[1],a,c=c,d=0.2)
    for i in range(4 * int(yl[0]) + 1, 4 * int(yl[1])):
        plotrans(trans([4 * xl[0], 4 * xl[1]], [i, i],currmat[m-1])[0],trans([4 * xl[0], 4 * xl[1]], [i, i],currmat[m-1])[1],a,c=c,d=0.2)

def eigval(a):
     ev1=((a[0][0]+a[1][1])+((a[0][0]+a[1][1])**2-(4*(a[0][0]*a[1][1]-a[0][1]*a[1][0])))**0.5)/2
     ev2 = ((a[0][0] + a[1][1]) - ((a[0][0] + a[1][1]) ** 2 - (4 * (a[0][0] * a[1][1] - a[0][1] * a[1][0]))) ** 0.5)/2
     return [ev1,ev2]

def pltevec(a,*args,**kwargs):
    if kwargs.get('c',None)==None:
        c='black'
    else:
        c=kwargs.get('c',0)
    arr=eigval(a)
    xv=4*np.array(xl)
    if arr[0].imag==0:
        if (a[1][1]-arr[0]-a[0][1])==0:
            plotrans([0,0],xv, matx1, c=c, l=0.3)
        else:
            slope1=(a[0][0]-arr[0]-a[1][0])/(a[1][1]-arr[0]-a[0][1])
            plotrans(xv, slope1 * xv, matx1, c=c, l=0.3)
    if arr[1].imag == 0:
        if (a[1][1]-arr[1]-a[0][1])==0:
            plotrans([0,0],xv, matx1, c=c, l=0.3)
        else:
            slope2=(a[0][0]-arr[1]-a[1][0])/(a[1][1]-arr[1]-a[0][1])
            plotrans(xv, slope2 * xv, matx1, c=c,l=0.3)

def det(a):
   return a[0][0]*a[1][1]-a[1][0]*a[0][1]

def inv(a):
    b=det(a)
    return [[a[1][1]/b,-a[0][1]/b],[-a[1][0]/b,a[0][0]/b]]

def product(a,b):
    return [[a[0][0]*b[0][0]+a[0][1]*b[1][0],a[0][0]*b[0][1]+a[0][1]*b[1][1]],
            [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

def fulfil(b):
    global m00
    global m01
    global m10
    global m11
    global currmat
    global holdmat
    global nowmat
    m00[m-1] = np.linspace(1, b[0][0], seg)
    m01[m-1] = np.linspace(0, b[0][1], seg)
    m10[m-1] = np.linspace(0, b[1][0], seg)
    m11[m-1] = np.linspace(1, b[1][1], seg)
    currmat[m-1]=holdmat[m-1]
    holdmat[m-1] = product(b, holdmat[m-1])
    nowmat[m-1]=b

xl=[-10,10]
yl=[-10,10]

seg=100
x1=np.linspace(xl[0],xl[1],seg)
y1=np.linspace(yl[0],yl[1],seg)

rows=2
columns=2

mat=[[-5,2],
     [2,-2]]

mat1=[[2,1],
     [0,-1]]

rot=[[0,-1],
     [1,0]]

squish=[[1,-1],
        [0,1]]

sp=1    #speed of the animation
n=2    #No of animations

inimat=[[1,0],[0,1]]
currmat=[inimat,inimat,inimat,inimat]
holdmat=[inimat,inimat,inimat,inimat]
nowmat=[inimat,inimat,inimat,inimat]
m00=[0,0,0,0]
m01=[0,0,0,0]
m10=[0,0,0,0]
m11=[0,0,0,0]
theetta=np.linspace(0,2*np.pi,seg)

plt.figure(facecolor='yellow',figsize=(16,9),dpi=120)


graph_ratio=2

def anim(i):
    global m
    global currmat
    global holdmat
    global matx1
    if i==0:
        holdmat=[inimat,inimat,inimat,inimat]
        currmat =[inimat,inimat,inimat,inimat]

    plt.clf()
    plt.suptitle("\u0332".join('Anandu\'s Plots'),fontsize=20)
    plt.subplots_adjust(left=0.04, right=0.99,top=0.93,bottom=0.02)
    m=2

    plt.subplot(rows,columns,m)
    if i == 1:
        fulfil(product(squish,rot))
    if sp * i == seg:
        fulfil(inimat)
    if sp * i == seg * 2:
        fulfil(inimat)
    if sp * i == seg * 3:
        fulfil(inimat)
    if sp * i == seg*4:
        fulfil(inimat)
    if sp * i == seg*5:
        fulfil(inimat)
    if sp * i == seg * 6:
        fulfil(inimat)
    if sp * i == seg * 7:
        fulfil(inimat)

    ind=sp*i-int(sp*i/seg)*seg
    if i==n*int(seg/sp)-1:
        ind=seg-1
    if i>=1:
        matx1 = [[m00[m-1][ind], m01[m-1][ind]], [m10[m-1][ind], m11[m-1][ind]]]
        plt.title('Resultant Transformation 1',fontsize=18)
        pltevec(nowmat[m-1])
        plotax(matx1)
        plotrans(trans([1.5, 2.5, 4,1.5], [1, 0, 3,1],currmat[m-1])[0],trans([1.5, 2.5, 4,1.5], [1, 0, 3,1],currmat[m-1])[1], matx1, c='green')
        plotrans(trans(np.cos(theetta),np.sin(theetta),currmat[m-1])[0],trans(np.cos(theetta),np.sin(theetta),currmat[m-1])[1],matx1)
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.set_facecolor((.8,.9,1))
        plt.xlim(graph_ratio*xl[0],graph_ratio*xl[1])
        plt.ylim(yl[0],yl[1])

    m = 1
    plt.subplot(rows, columns, m)
    if i == 1:
        fulfil(rot)
    if sp * i == seg:
        fulfil(squish)
    if sp * i == seg * 2:
        fulfil(inimat)
    if sp * i == seg * 3:
        fulfil(inimat)
    if sp * i == seg * 4:
        fulfil(inimat)
    if sp * i == seg * 5:
        fulfil(inimat)
    if sp * i == seg * 6:
        fulfil(inimat)
    if sp * i == seg * 7:
        fulfil(inimat)
    ind = sp * i - int(sp * i / seg) * seg
    if i == n * int(seg / sp) - 1:
        ind = seg - 1
    if i >= 1:
        matx1 = [[m00[m - 1][ind], m01[m - 1][ind]], [m10[m - 1][ind], m11[m - 1][ind]]]
        plt.title('Individual Transformation 1',fontsize=18)
        pltevec(nowmat[m - 1])
        plotax(matx1)
        plotrans(trans([1.5, 2.5, 4, 1.5], [1, 0, 3, 1], currmat[m - 1])[0],
                 trans([1.5, 2.5, 4, 1.5], [1, 0, 3, 1], currmat[m - 1])[1], matx1, c='green')
        plotrans(trans(np.cos(theetta), np.sin(theetta), currmat[m - 1])[0],
                 trans(np.cos(theetta), np.sin(theetta), currmat[m - 1])[1], matx1)
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.set_facecolor((.8,.9,1))
        plt.xlim(graph_ratio * xl[0],graph_ratio * xl[1])
        plt.ylim(yl[0], yl[1])

    m = 3
    plt.subplot(rows, columns, m)
    if i == 1:
        fulfil(squish)
    if sp * i == seg:
        fulfil(rot)
    if sp * i == seg * 2:
        fulfil(inimat)
    if sp * i == seg * 3:
        fulfil(inimat)
    if sp * i == seg * 4:
        fulfil(inimat)
    if sp * i == seg * 5:
        fulfil(inimat)
    if sp * i == seg * 6:
        fulfil(inimat)
    if sp * i == seg * 7:
        fulfil(inimat)
    ind = sp * i - int(sp * i / seg) * seg
    if i == n * int(seg / sp) - 1:
        ind = seg - 1
    if i >= 1:
        matx1 = [[m00[m - 1][ind], m01[m - 1][ind]], [m10[m - 1][ind], m11[m - 1][ind]]]
        plt.title('Individual Transformation 2', fontsize=18)
        pltevec(nowmat[m - 1])
        plotax(matx1)
        plotrans(trans([1.5, 2.5, 4, 1.5], [1, 0, 3, 1], currmat[m - 1])[0],
                 trans([1.5, 2.5, 4, 1.5], [1, 0, 3, 1], currmat[m - 1])[1], matx1, c='green')
        plotrans(trans(np.cos(theetta), np.sin(theetta), currmat[m - 1])[0],
                 trans(np.cos(theetta), np.sin(theetta), currmat[m - 1])[1], matx1)
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.set_facecolor((.8, .9, 1))
        plt.xlim(graph_ratio * xl[0], graph_ratio * xl[1])
        plt.ylim(yl[0], yl[1])

    m = 4
    plt.subplot(rows, columns, m)
    if i == 1:
        fulfil(product(rot,squish))
    if sp * i == seg:
        fulfil(inimat)
    if sp * i == seg * 2:
        fulfil(inimat)
    if sp * i == seg * 3:
        fulfil(inimat)
    if sp * i == seg * 4:
        fulfil(inimat)
    if sp * i == seg * 5:
        fulfil(inimat)
    if sp * i == seg * 6:
        fulfil(inimat)
    if sp * i == seg * 7:
        fulfil(inimat)
    ind = sp * i - int(sp * i / seg) * seg
    if i == n * int(seg / sp) - 1:
        ind = seg - 1
    if i >= 1:
        matx1 = [[m00[m - 1][ind], m01[m - 1][ind]], [m10[m - 1][ind], m11[m - 1][ind]]]
        plt.title('Resultant Transformation 2', fontsize=18)
        pltevec(nowmat[m - 1])
        plotax(matx1)
        plotrans(trans([1.5, 2.5, 4, 1.5], [1, 0, 3, 1], currmat[m - 1])[0],
                 trans([1.5, 2.5, 4, 1.5], [1, 0, 3, 1], currmat[m - 1])[1], matx1, c='green')
        plotrans(trans(np.cos(theetta), np.sin(theetta), currmat[m - 1])[0],
                 trans(np.cos(theetta), np.sin(theetta), currmat[m - 1])[1], matx1)
        ax = plt.gca()
        ax.set_aspect('equal')
        ax.set_facecolor((.8, .9, 1))
        plt.xlim(graph_ratio * xl[0], graph_ratio * xl[1])
        plt.ylim(yl[0], yl[1])

animation = FuncAnimation(plt.gcf(),anim,frames=n*int(seg/sp),interval=62)


#To save this animation as mp4


Writer=writers['ffmpeg']
writer=Writer(fps=16,metadata={'artist':'Me'},bitrate=5400)#bitrate=36*dpi
animation.save('Test02.mp4',writer,dpi=120)#dpi=resolution/frameheight


plt.show()