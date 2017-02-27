keimeno = raw_input("Dwste to keimeno \n")

output =""
marksCount=0 # metraei !
spaceCount=0 # metraei kena

for i in range(len(keimeno)):
	if keimeno[i] is " " and marksCount is 0:
		print "keno"
		output+=" "
		continue
	elif keimeno[i] is " " and marksCount is not 0 and keimeno[i+1].isupper():
		for j in range(marksCount):
			output+="!"
		marksCount=0
		output+=" "
		continue
	elif keimeno[i] is " " and marksCount is not 0 and not keimeno[i+1].isupper():
		output+=keimeno[i]
		continue




	if keimeno[i] is not "!" and keimeno[i] is not " ":
		if keimeno[i].islower():
			marksCount=0
			output+=keimeno[i]
			continue
		if keimeno[i].isupper() or i is (len(keimeno)-1):
			if keimeno[i] is " ":
				spaceCount+=1
			for j in range(0,marksCount):
				output+="!"
			for j in range(0,spaceCount):
				output+=" "
			spaceCount=0	
			marksCount=0	
		output+=keimeno[i]
	if keimeno[i] is "!":		
		marksCount+=1
		#continue
	if keimeno[i] is "!" and i is (len(keimeno)-1):		
		for j in range(0,marksCount):
				output+="!"
		for j in range(0,spaceCount):
				output+=" "
		spaceCount=0	
		marksCount=0	

print output