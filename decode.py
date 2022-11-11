import matplotlib.pyplot as plt
from filtro import LPF
import sounddevice as sd
import numpy as np
import wave
import sys
import scipy.io.wavfile as wav
from suaBibSignal import signalMeu
import soundfile as sf
import filtro


signal = signalMeu()
sd.default.samplerate = 44100
sd.default.channels = 2

audio, f = sf.read('sinal_modulado.wav')
print(audio)

# Decodificação
tempo = np.arange(0, len(audio)/44100, 1/44100)
portadora = np.sin(2*np.pi*14_000*tempo)
sinal_demodulado = audio*portadora
sinal_demodulado = sinal_demodulado.astype(np.float32)
sinal_demodulado = sinal_demodulado / np.max(np.abs(sinal_demodulado))


# filtrada = filtro.filtro(sinal_demodulado, 44100, 2200)
print('tocando')
sd.play(sinal_demodulado, 44100)
sd.wait()

plt.figure(0)
plt.plot(tempo, sinal_demodulado)
plt.title('Sinal demodulado')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')

plt.figure(1)
signal.plotFFT(sinal_demodulado, 44100)
plt.title('Frequencia demodulada')
plt.xlabel('Frequencia')
plt.ylabel('Amplitude')

# plt.figure(2)
# signal.plotFFT(filtrada, 44100)
# plt.title('Frequencia filtrada')
# plt.xlabel('Frequencia')
# plt.ylabel('Amplitude')

plt.show()
