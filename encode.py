import matplotlib.pyplot as plt
from scipy.signal import firwin
import sounddevice as sd
import numpy as np
import wave
import sys
import scipy.io.wavfile as wav


spf = wave.open("wavfile.wav", "r")

# Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, "Int16")


# If Stereo
if spf.getnchannels() == 2:
    print("Just mono files")
    sys.exit(0)

plt.figure(1)
plt.title("Signal Wave...")
plt.plot(signal)
plt.show()

#------------------------------------------------
# Create a FIR filter and apply it to signal.
#------------------------------------------------


sample_rate = 44100

# The Nyquist rate of the signal.
nyq_rate = sample_rate / 2.
 
# The cutoff frequency of the filter: 6KHz
cutoff_hz = 2200.0
 
# Length of the filter (number of coefficients, i.e. the filter order + 1)
numtaps = 29
 
# Use firwin to create a lowpass FIR filter
fir_coeff = firwin(numtaps, cutoff_hz/nyq_rate)
 
# Use lfilter to filter the signal with the FIR filter
filtered_signal = lfilter(fir_coeff, 1.0, signal)

sd.play(filtered_signal, sample_rate)

#---------------------------------------------------
#Modula para a portadora
#---------------------------------------------------

freq_portadora = 14000

t = (0,5,44100*5)
sinal_portadora = np.sin(freq_portadora * 2 * np.pi * t)

sinal_modulado = sinal_portadora*signal
wav.write("sinal_modulado", sample_rate , sinal_portadora)
