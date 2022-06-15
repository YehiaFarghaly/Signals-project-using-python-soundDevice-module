#First we imported the needed libraries :-
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.fftpack import fft
#Then we made a list of integers representing the time starting from 0 to 3:-
t = np.linspace(0,3,12*1024)
#Then lists of left hand and right hand frequencies were made.
# we chose the frequencies of the music ladder:-
freqLeft = [440,493,554,587,659,739,830,880,440]
freqRiht = [440,493,554,587,659,739,830,880,440]
#Here we made list 'ti' to represent the starting time of the frequency at index i :-
ti = [0,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.6]
#While for the list 'T' it shows the period of the frequency at index i:-
T=[0.3,0.3,0.3,0.3,0.3,0.3,0.3,0.5,0.4]
#Now to define the given parameter we made a variable x to sum the signals:-
x=0
#The function unit step defines the unit step signal to be used in the summation:-
def unitStep(t) :
    return 1*(t>=0)
#Using the for loop the signals are summed to the variable x:-
for  i in range(9):
   x = x+((np.sin(2*np.pi*freqLeft[i]*t)+np.sin(2*np.pi*freqRiht[i]*t))*(unitStep(t-ti[i])-unitStep(t-ti[i]-T[i]) ))
#Here we plot the graph of the song frequencies:-   
#plt.plot(t,x)  
#Finally the song is played:-
sd.play(x,3*1024)

N = 3*1024
f = np. linspace(0 , 512 , int(N/2))
xf = fft(x)
xf = 2/N * np.abs(xf [0:int(N/2)])
f1 = np.random.randint(0, 512)
f2 = np.random.randint(0, 512)
n = np.sin(2*np.pi*f1*t)+np.sin(2*np.pi*f2*t)
xn = x+n

xnf = fft(xn)
xnf = 2/N * np.abs(xnf [0:int(N/2)])

randomNoise = np.where(xnf>np.ceil(np.max(x)))
peek1 = randomNoise[0][0]
peek2 = randomNoise[0][1]
filteredX = xn - (np.sin(2*np.pi*int(f[peek1])*t)+np.sin(2*np.pi*int(f[peek2])*t))

#sd.play(filteredX, 3*1024)

fftFilteredX = fft(filteredX)
fftFilteredX = 2/N * np.abs(fftFilteredX [0:int(N/2)])

plt.figure()
plt.subplot(3,1,1)
plt.plot(t,x)
plt.subplot(3,1,2)
plt.plot(t,xn)
plt.subplot(3,1,3)
plt.plot(t,filteredX)

plt.figure()
plt.subplot(3,1,1)
plt.plot(f,xf)
plt.subplot(3,1,2)
plt.plot(f,xnf)
plt.subplot(3,1,3)
plt.plot(f,fftFilteredX)
