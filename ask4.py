import numpy

print "Dwste toulaxiston 5 ari8mous xwrismenous me kena"
ari8moi = map(float, raw_input().split())

# parnei orisma enan ari8mo kai kai thn list ari8mwn tou xrhsth.
#An brei ton ari8mo pou pairnei ws orisma ton diagrafei.
def removeNumber(todelete,ari8moi):
	for i in range(len(ari8moi)):
		if ari8moi[i] is todelete:
			del(ari8moi[i])
			break

def upologismosMO(ari8moi):
	mo=0
	for i in range(len(ari8moi)):
		mo = mo + ari8moi[i]
	return mo/len(ari8moi)

def upologismosDiaforas(ari8moi,mo):
	test = 0
	for i in range(len(ari8moi)):
		test = test + (ari8moi[i]-mo)**2
	return test

if len(ari8moi)<5:  #  an de dwsei swsto input na mhn trejei
	print "Dwste toulaxiston 5 ari8mous"
else:
	min1 = min(ari8moi) # briskw ton prwto mikrotero
	removeNumber(min1,ari8moi) # ton diagrafw
	min2 = min(ari8moi)   # briskw ton deutero mikrotero
	removeNumber(min2,ari8moi) # ton diagrafw
	max1 = max(ari8moi)
	removeNumber(max1,ari8moi)
	max2=max(ari8moi)
	removeNumber(max2,ari8moi)

	#Pleon h list ari8moi einai xwris tous 2 megaluterous kai tous dio 
	#mikroterous pou zhthtai na agnoh8oun

	#Ypologismos tupikhs apoklishs

	mo = upologismosMO(ari8moi) # mesos oros
	# twra afairoume apo ka8e ari8mo ton mo kai to upsonoume sto tetragwnw
	diafora = upologismosDiaforas(ari8moi,mo)

	print 'Tupikh apoklish =',numpy.sqrt(diafora/len(ari8moi))