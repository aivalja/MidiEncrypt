import midi

letters = ["a","b","c","d","e","f","g","h","i", "j", "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"," ",".",",","!","?", '"',"`","&","'", "-",":",";","*","(",")","[","]","{","}","+","\n","\t", "\xe2", "\x80", "\x99", "\xef", "\xbb", "\xbf"]

secret = str(midi.read_midifile("text.mid"))
teksti = ""
secretSplit = secret.split("data=[")
with open ("test.txt", "w") as file:
	file.write(str("\n".join(secretSplit)))
print secretSplit[12]
i = 1
print (len(secretSplit)-2)/2
while for i in range((len(secretSplit)-2)/2-1):
	print i
	index = secretSplit[i]
	teksti += letters[i]
	i+=2
print teksti