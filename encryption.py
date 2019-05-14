import midi


def note(track, tick, length, velocity, pitch):
    track.append(midi.NoteOnEvent(tick=tick, velocity=velocity, pitch=pitch))
    track.append(midi.NoteOffEvent(tick=tick + length, pitch=pitch))
    return track


def encrypt(textName, midiName):
    note_length = 25
    note_pause = 25
    intensity = 50
    scale_length = 12
    # Original notes = [43, 45, 46, 48, 50, 51, 53, 55]
    notes = [7, 9, 10, 12, 14, 15, 17]
    with open(textName + ".txt", "r") as file:
        text = file.read().lower()

    pattern = midi.Pattern()
    track = midi.Track()
    pattern.append(track)
    letters = ["a","b","c","d","e","f","g","h","i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"," ",".",",","!","?", '"',"`","&","'", "-",":",";","*","(",")","[","]","{","}","+","\r", "\x93", "\n","\t", "\xe2", "\x80", "\x99", "\xef", "\xbb", "\xbf", "\xc3", "\xa4", "\xf6", "\xe4", "_","=","/","%","<",">","$",":","|","@","\\","\xb6", "#","\xc2"]
    # track = note(track, 100, note_length*5, intensity, midi.G_2)
    # track = note(track, 100, note_length*5, intensity, midi.G_2)
    # track = note(track, 100, note_length*5, intensity, midi.G_2)
    
    for i in range(len(text)):
        x = letters.index(text[i])
        pitch = notes[x % len(notes)] + (x // len(notes))*scale_length + scale_length*3
        # x = i + 30
        tick = (note_length + note_pause)
        track = note(track, tick, note_length, intensity, pitch)
    
    track.append(midi.EndOfTrackEvent(tick=1))
    midi.write_midifile(midiName + ".mid", pattern)
    with open("midi.txt", "w") as file:
        file.write(str(pattern))
    print pattern
encrypt("teksti", "text")
"""
secret = str(midi.read_midifile("text.mid"))
#print str(midi.parse_track(midi.read_midifile("text.mid"), track))

secretSplit = secret.split(",    ")
print secret
"""
