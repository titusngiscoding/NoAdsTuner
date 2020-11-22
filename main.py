import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def processAudio():
    fs=44100
    duration = 0.01  # seconds
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1,dtype='float64')
    print ("Recording Audio")
    sd.wait()
    print ("Audio recording complete , Play Audio")
    print(myrecording)
    sd.play(myrecording, fs)
    sd.wait()
    print ("Play Audio Complete")


def main():
    processAudio()

if __name__ == "__main__":
    main()
