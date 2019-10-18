import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read, write
from numpy.fft import fft, ifft


def sig2sq(mag_spec):
    return np.log10(np.square(abs(mag_spec)))/20

FRAME_SIZE = 1024
ZP_FACTOR = 2
FFT_SIZE = FRAME_SIZE * ZP_FACTOR


################## YOUR CODE HERE ######################
def ece420ProcessFrame(frame):
    curFft = np.zeros(FFT_SIZE)
    w = np.hamming(FRAME_SIZE)
    sig_w = frame * w
    curFft = fft(sig_w, n = FFT_SIZE)
    Real = curFft[0:int(FFT_SIZE/2)]
    result = sig2sq(Real)

    return result[0:FRAME_SIZE]
################# GIVEN CODE BELOW #####################

Fs, data = read('test_vector.wav')

numFrames = int(len(data) / FRAME_SIZE)
bmp = np.zeros((numFrames, FRAME_SIZE))

for i in range(numFrames):
    frame = data[i * FRAME_SIZE : (i + 1) * FRAME_SIZE]
    curFft = ece420ProcessFrame(frame)
    bmp[i, :] = curFft

plt.figure()
plt.title('Spectrogram of the aduio')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.pcolormesh(bmp.T, vmin=0, vmax=1)
plt.axis('tight')
plt.show()