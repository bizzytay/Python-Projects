#Taylor Herrera 8/29/2016
'''Using recursion to find subsequence of characters and Strings'''
#python 3

seq1 = ('a', 'z', 'f', 'g', 'h', 'u', 'f', 'g', 'z')
target1 = ('f','g')

seq2 = ('azfghufgz')
target2 = ('fg')
#size of seq1 and target1
seq1_size = len(seq1)
target1_size = len(target1)
#size of seq2 and target2
seq2_size = len(seq2)
target2_size = len(target2)
#this is how the positions are stored 
position = []

def characters(seq1,target1):
	count = 0
	#iterate through the size of seq1 if fg is found then add to the postion
	for i in range(seq1_size):
		splice1 = seq1[i:i+target1_size]
		if(target1==splice1):
			position.append(i)
			count+=1

	#calculates the ratio
	ratio = float(len(position))/float(seq1_size)
		
	print("fg in characters was found at postions" ,position)
	print("The ratio was ",ratio)	
	print("Number of occurances",count)

def strings(seq2,target2):
	count = 0
	#iterate through the size of seq2 if fg is found then add to the postion
	for i in range(seq2_size):
		splice2 = seq2[i:i+target2_size]
		if(target1==splice2):
			position.append(i)
			count+=1
	
	ratio = float(len(position))/float(seq2_size)
	print("\n\nfg in a string was found at postions ",position)
	print("The ratio was ", ratio)
	print("Number of occurances",len(position))
	
characters(seq1,target1)
strings(seq2,target2)
