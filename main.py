import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

def processAudio():
    fs=44100
    duration = 5  # seconds
    myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
    print ("Recording Audio")
    sd.wait()
    print ("Audio recording complete , Play Audio")
    sd.play(myrecording, fs)
    sd.wait()
    print ("Play Audio Complete")   


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
