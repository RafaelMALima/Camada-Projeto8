import matplotlib.pyplot as plt
from filtro import LPF
import sounddevice as sd
import numpy as np
import wave
import sys
import scipy.io.wavfile as wav
import filtro as f
import soundfile as sf

sample_rate = 44100

signal = sf.read('audio.wav')[0][:, 1]

# The cutoff frequency of the filter: 6KHz
cutoff_hz = 2200

# Use lfilter to filter the signal with the FIR filter
filtered_signal = f.filtro(signal, sample_rate, cutoff_hz)


sd.play(filtered_signal, sample_rate)
sd.wait()

#---------------------------------------------------
#Modula para a portadora
#---------------------------------------------------

freq_portadora = 14_000

t = np.arange(0, len(filtered_signal)/44100, 1/44100)
sinal_portadora = np.sin(freq_portadora * 2 * np.pi * t)

sinal_modulado = sinal_portadora*filtered_signal
sinal_modulado = sinal_modulado / np.max(np.abs(sinal_modulado))
wav.write("sinal_modulado.wav", sample_rate, sinal_portadora)



# sd.play(sinal_modulado, sample_rate)
# sd.wait()
