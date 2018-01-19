from scipy.fftpack import fft
import numpy as np
sig = [[],[],[],[]]

file = open("smoke.text","r")

for x in range(0,22000):
    sig[0].append(float(file.readline()))
    sig[1].append(float(file.readline()))
    sig[2].append(float(file.readline()))
    sig[3].append(float(file.readline()))

N=22000
T=1.0/200.0
x=np.linspace(0.0,N*T,N)
y0=sig[0]
yf0= fft(y0)
y1=sig[1]
yf1= fft(y1)
y2= sig[2]
yf2=fft(y2)
y3=sig[3]
yf3=fft(y3)

xf=np.linspace(0.0,1.0/(2.0*T),N/2)
import matplotlib.pyplot as plt
plt.plot(xf,2.0/N*np.abs(yf0[0:N/2]),'b')
plt.plot(xf,2.0/N*np.abs(yf1[0:N/2]),'r')
plt.plot(xf,2.0/N*np.abs(yf2[0:N/2]),'y')
plt.plot(xf,2.0/N*np.abs(yf3[0:N/2]),'g')

plt.grid()
plt.show()
