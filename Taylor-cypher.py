"""Taylor Herrera 9/1/2016"""
#Encrypt string by rotating then decrypt
#Python version 3.4.3

#create the cipher alphabet
cipher_alphabet = [chr(i) for i in range(10, 127)]

#ask user for word and offset
word = input("Enter a word: ")
offset = int(input("Enter offset: "))

#Encrypt the word
def encipher(offset, word):
	result = ""	

	#for every letter in the lower case word, substitue the letter with the cipher alphabet and add it to results
	for letter in word.lower():
		try:
			sub = (cipher_alphabet.index(letter) + offset)% len(cipher_alphabet)
			result+=cipher_alphabet[sub]
		except ValueError:
			result+=letter	
	#returns the encrypted word
	return result.lower()
	
#Decrypt the word
def decipher(offset, new_word):
	result = ""	

	#for every letter in the encrypted word, substitue the letter with the cipher alphabet (change it back to the original word) and add it to results
	for letter in new_word:
		try:
			sub = (cipher_alphabet.index(letter) - offset)% len(cipher_alphabet)
			result+=cipher_alphabet[sub]
		except ValueError:
			result+=letter	
	#returns the decrypted word
	return result
	
#displays the words before and after encryption
def display(word, offset):
	#calls the encipher and decipher functions
	ec = encipher(offset, word)
	dc = decipher(offset, ec)
	print ('***********************************')
	print ('\n\n\nNumber of rotation: %s' %offset)
	print ('\nWord: %s' %word) 
	print ('\nEncrypted word: %s' %ec)
	print ('\nDecrypted word: %s' %dc)
	
display(word, offset)
