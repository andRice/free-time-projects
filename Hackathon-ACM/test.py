import gen_scale as gs
import main
import simpleaudio as sa
import random
#******   CONFIG     ******


def main():
john = random.randint(0,(2**32)-1)
print(john)
aScale = gs.scale(0,0,4,3,0)
aScale.major()

#bScale = main.next_scale(aScale, 1,main.decode_config(random.randint(0,(2**32)-1)),1)



#bScale = gs.scale(0,0,4,2,0)
#cScale = gs.scale(0,0,5,2,7,1)

#out = gs.mix_scales([aScale,bScale],44100)
#a.play_buffer(main.make_bar(3,aScale,3,main.decode_config(john)),1,2,44100)
#sa.play_buffer(out,1,2,44100)


def Testy(num):
    john = random.randint(0,2**32-1)
    print(bin(john))
    for i in range(num):
        try:
            sa.play_buffer(main.make_bar(i,aScale,3,main.decode_config(john)),1,2,44100)
        except:
            continue