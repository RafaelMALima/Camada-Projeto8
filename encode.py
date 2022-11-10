import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter
from filtro import LPF
import sounddevice as sd
import numpy as np
import wave
import sys
import scipy.io.wavfile as wav


signal = wav.read("TheLick.wav")


#------------------------------------------------
# Create a FIR filter and apply it to signal.
#------------------------------------------------


sample_rate = 44100

# The Nyquist rate of the signal.
nyq_rate = sample_rate / 2.
 
# The cutoff frequency of the filter: 6KHz
cutoff_hz = 2200.0
 
numtaps = 29
# Use lfilter to filter the signal with the FIR filter
filtered_signal = LPF(signal, cutoff_hz, sample_rate)

print(filtered_signal)

sd.play(filtered_signal, sample_rate)

#---------------------------------------------------
#Modula para a portadora
#---------------------------------------------------

freq_portadora = 14000

t = (0,5,44100*5)
sinal_portadora = np.sin(freq_portadora * 2 * np.pi * t)

sinal_modulado = sinal_portadora*signal
wav.write("sinal_modulado", sample_rate , sinal_portadora)
