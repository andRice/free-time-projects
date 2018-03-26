from appJar import gui
import main
import time
import gen_scale as gs
import random
import simpleaudio as sa


thtwo = 2**32
aScale = gs.scale(0,0,3,2,0)
aScale.major()
def press(btn):
    sa.play_buffer(main.make_bar(3,aScale,3,main.decode_config(random.randint(0,thtwo-1))),1,2,44100)
    
##def BillHiggins():
  #  return decode_config(random.randint(1,(2*32)-1)

#def get_seed():
 #   global x
  #  x = app.getEntry("seed")
   # print(x)
    #return x

    
app = gui("Robot Music!","512x512")
#app.addLabel("title","Chiptune Synthesiser")
#app.addEntry("Seed")
#app.addButton("Enter Seed",main.make_bar(1,aScale,3,main.decode_config(random.randint(1,(2*32)-1))))
app.addButton("Make Music!",press)
#app.setLabelBg("title","#FABBFB")
#x = 0
app.go()

