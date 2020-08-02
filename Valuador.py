import	math	
def factrial(n):
	if n==0:
		return 1
	else:
		return n*factrial(n-1)
		pass
	pass
def Trianguloloco(S,K,r,sigma,t,n):
	dt=t/n
	u=math.exp(sigma*math.sqrt(3*dt))
	d=1/u
	Pu=math.sqrt(dt/(12*sigma**2))*(r-((sigma**2)/2))+(1/6)
	Pd=-math.sqrt(dt/(12*sigma**2))*(r-((sigma**2)/2))+(1/6)
	Pm=1-Pu-Pd
	Su=[]
	for x in range(0,n):
		Su.append(S*(u**(n-x)))
		pass
	Sd=[]
	for x in range(1,n+1):
		Sd.append(S*(d**(x)))
		pass
	Cb=[]
	for x in range(0,n):
		Cb.append(max(Su[x]-K,0))
		pass
	Cb.append(max(S-K,0))
	for x in range(0,n):
		Cb.append(max(Sd[x]-K,0))
		pass
	C=[Cb]
	for y in range(0,n):
		Cn=[]
		for x in range(0,2*(n-y)-1):
			Cn.append(((Pu*C[y][x])+(Pm*C[y][x+1])+(Pd*C[y][x+2]))*(math.exp(-r*dt)))
			pass
		C.append(Cn)
		pass
	print (C[n-1][0])
	pass
Trianguloloco(20,21,.05,.3,10,10)

