import simpleaudio as sa
import chippy
import audioop
import time
from numpy import *

# tone synthesis
def note(freq, len, amp=1, rate=44100):
	t = linspace(0,len,len*rate)
	data = sin(2*pi*freq*t)*amp
	return data.astype(int16) # two byte integers


interval = .5
#synth = chippy.Synthesizer(framerate=44100)

#y = synth.sine_pcm(length = 1, frequency = 261)
#x = synth.sine_pcm(length = 1, frequency = 350)
#z = synth.sine_pcm(length=1,frequency = 200)
x = note(261,2,amp=10000)
y = note(293,2,amp=10000)
z = note(250,2,amp=10000)
notes = [x,y,z]

noteSpeed = interval/len(notes)

for i in notes:
	obj = sa.play_buffer(i,1,2,44100)
	obj.wait_done()
	#time.sleep(noteSpeed)
	

for i in range(len(notes)):
	i += 1
	obj = sa.play_buffer(notes[i*-1],1,2,44100)
	obj.wait_done()
#	obj.stop
#	time.sleep(1)
	
	
	
