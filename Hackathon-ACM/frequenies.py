octaves = {}
#Notes for the 0th octave
notes = [16.35,17.32,18.35,19.45,20.60,21.83,23.12,24.50,25.96,27.50,29.14,30.87]

#1-C
#2-#
#3-D
#4-D#
#5-E
#6-F
#7-F#
#8-G
#9-G#
#10-A
#11-A#
#12-B


#The 0th octave is the 
octaves[0]=notes
#for i in range(len(notes)):
#	scales[]
#Generate the 0th octave major scale...
exponent = 0
for i in range(9):
	templist = [0]*12
	for j in range(len(notes)):
		templist[j] = notes[j]*(2**exponent)
	octaves[i] = templist
	exponent += 1
	
print(octaves[5])
