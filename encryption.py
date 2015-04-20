import midi

def note(track, tick, length, velocity, pitch):
	track.append(midi.NoteOnEvent(tick = tick, velocity = velocity, pitch = pitch))
	track.append(midi.NoteOffEvent(tick = tick+length, pitch = pitch))
	return track

def encrypt(textName, midiName):

    with open (textName + ".txt", "r") as file:
        text = file.read().lower()

    pattern = midi.Pattern()
    track=midi.Track()
    pattern.append(track)
    letters = ["a","b","c","d","e","f","g","h","i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"," ",".",",","!","?", '"',"`","&","'", "-",":",";","*","(",")","[","]","{","}","+","\n","\t", "\xe2", "\x80", "\x99", "\xef", "\xbb", "\xbf"]

    for i in range(len(text)):
        x = letters.index(text[i])
        track = note(track, i, 1000, 100, x)

    track.append(midi.EndOfTrackEvent(tick=1))
    midi.write_midifile(midiName + ".mid",pattern)
    
    with open("midi.txt", "w") as file:
        file.write(str(pattern))

encrypt(text, text)
"""
secret = str(midi.read_midifile("text.mid"))
#print str(midi.parse_track(midi.read_midifile("text.mid"), track))

secretSplit = secret.split(",    ")
print secret
"""