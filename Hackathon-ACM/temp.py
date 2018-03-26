import simpleaudio as sa
import numpy as np
import copy
import math
import frequenies as fr

Bill = 
class note:
    def gen_wave(self,sample_rate):
        freq = fr.octaves[self.octave][self.major_note]
        t = np.linspace(0,self.size,self.size*sample_rate)
        data = np.sin(2*np.pi*freq*t)*self.amp
        return data.astype(np.int16)
    def __init__(self,m,o,s,a):
        self.major_note = m
        self.octave = o
        self.size = s
        self.amp = a

class scale:
# entry_time root_not  Octave  Width  Num Notes Dec
    def __init__(self,entry,root_note,octave,width,dec):
        self.entry_time = entry;
        self.dec = dec
        self.root = root_note
        self.octave = octave
        self.note_alignment = 2**width
        t = self.note_alignment/12
        self.note_list = []
        for i in range(12):
            if(dec):
                self.note_list.append(note((root_note - i) % 12,octave - math.floor(i/12),t,10000))
            else:
                self.note_list.append(note((root_note + i) % 12,octave + math.floor(i/12),t,10000))

                
    def major(self):
    #Major scale is 7 notes out of the 12
        x = self.note_list
        majorNotes = [0,2,4,5,7,9,11]
        newlist = []
        for note in majorNotes:
            newlist.append(x[note])
        self.note_list = newlist
        return newlist
         
    def minor(self):
        #Change all to the next octave level if the index jumps over 11
        all = self.note_list
        naturalMinor = []
        if (self.root + 2 > 11):
            all = fr.octaves[(self.octave+1)%9]
        nextNoteIndex = (self.root + 2) % 2 # Whole Step
        naturalMinor.append(all[nextNoteIndex])

        if (nextNoteIndex+1 > 11): # Half Step
            all = fr.octaves[(self.octave + 1)%9]
        nextNoteIndex = (nextNoteIndex + 1)%12
        naturalMinor.append(all[nextNoteIndex])
        
        for i in range(2): # 2 Whole Steps
            if (nextNoteIndex+2 > 11): # Half Step
                all = fr.octaves[(self.octave+2)%9]
            nextNoteIndex = (nextNoteIndex + 2)%12
            naturalMinor.append(all[nextNoteIndex])
        
        if (nextNoteIndex+1 > 11): # Half Step
            all = fr.octaves[(self.octave+1)%9]
        nextNoteIndex = (nextNoteIndex + 1)%12
        naturalMinor.append(all[nextNoteIndex])
        
        for i in range(2): # 2 Whole Steps
            if (nextNoteIndex+2 > 11): # Half Step
                all = fr.octaves[(self.octave+2)%9]
            nextNoteIndex = (nextNoteIndex + 2)%12
            naturalMinor.append(all[nextNoteIndex])
            
        self.note_list = naturalMinor

        
        #if (self.dec):
         #   self.note_list = naturalMinor
       # else: #Use the harmonic minor if it is ascending
        #    if (nextNoteIndex+1 > 11): # Half Step
         #       all = fr.octaves[(self.octave+1)%9]
          #  nextNoteIndex = (nextNoteIndex + 1)%12
           # naturalMinor.append(all[nextNoteIndex])
           # self.note_list = 
            
    
    def arpegio(self): # Sets the current scale to be an arpegio
    #Also returns that arpegio cause it can I guess
        x = self.note_list
        sublist = [x[0],x[2],x[4],x[6]]
        self.note_list = sublist
        return sublist
    
    def mux(self,freq):
        k = np.zeros(self.note_alignment*freq,dtype=np.int16)
        for (i,n) in enumerate(self.note_list):
            bf = n.gen_wave(freq)
            for j in range(len(bf)):
                k[i*len(bf)+j] = bf[j]
        return k

def mix_scales(scales,freq):
    muxes = []
    for s in scales:
        muxes.append(s.mux(freq))
    #find max of mux sizes
    mix_size = 0
    for i in range(len(muxes)):
        if((len(muxes[i]) + scales[i].entry_time) > mix_size):
            mix_size = len(muxes[i]) + scales[i].entry_time
    #mix em all together
    final_mix = np.zeros(mix_size,np.int16)
    for i in range(len(muxes)):
        this_scale = scales[i]
        for k in range(len(muxes[i])):
            final_mix[(k + (int)(this_scale.entry_time)) % mix_size] += muxes[i][k]
    return final_mix
