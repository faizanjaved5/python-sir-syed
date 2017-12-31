def findOdd(upto):
	for r in range(1,upto):
		if (r %2 !=0):
			print (r)

def findPrime(upto):
	for r in range(1,upto):
		leave = 0
		for num in range(1,r):
			if(r % num == 0 and num !=1):
				leave =1
		
		if leave == 0:
			print r
				


findPrime(20)