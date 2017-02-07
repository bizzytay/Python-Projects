'''Taylor Herrera 09/16/2016'''
#python version 2.7.2

#creates the alphabet to decrypt the text
alphabet = [chr(10)] + [chr(i) for i in range(32, 127)]
#gets the length of the alphabet
a_Length = len(alphabet)


#opens the file user specified
def open_file(fname):
	try:
		data = fname.read()
		return data

	except:
		return ("bad file")

#translates the message
def TranslatedMessage(message, key):

	result = ""	

	#for every letter in the encrypted word, substitue the letter with the cipher alphabet (change it back to the original word) and add it to results
	for letter in message:
		try:
			sub = (alphabet.index(letter) - key)% len(alphabet)
			result+=alphabet[sub]
		except ValueError:
			result+=letter	
	#returns the decrypted word
	return result

#cracks the ciphertext
def codecrack(ciphertext=None, keyrange=(0, 0)):
	#for every key, decrypt 30 times untill plain text is found
	for key in range(30):
		print("Key: {}\nMessage: {}\n\n".format(key,TranslatedMessage(message, key)))

f = raw_input('Enter the name of the file you want to decrypt: ')
test = open(f,'r')	
of = open_file(test)
message = of

#codecrack(message)

