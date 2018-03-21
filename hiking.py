import fileinput


i = 0
coord_trail = []

for line in fileinput.input():
	i+=1
	if i<=1:
		huts, trails = [int(x) for x in line.split()]
	elif i<=2:
		cis = [int(x) for x in line.split()]
	else:
		p1, p2 = [int(x) for x in line.split()]
		coord_trail.append([p1,p2])


price = [0]*trails

totalprice = 0
totalupgraded = 0
upgraded = []
for i in range(trails):
	# print("Trail " + str(i))
	# print("Summit 1 : " + str(cis[coord_trail[i][0]-1]))
	# print("Summit 2 : " + str(cis[coord_trail[i][1]-1]))

	# print(upgraded)
	if cis[coord_trail[i][0]-1]>0 and cis[coord_trail[i][1]-1]>0:
		difference = cis[coord_trail[i][0]-1]
		hut = coord_trail[i][0]-1
		if cis[coord_trail[i][1]-1]<cis[coord_trail[i][0]-1]:
			difference = cis[coord_trail[i][1]-1]
			hut = coord_trail[i][1]-1
		newprice = price[i] + difference
		price[i] = newprice
		cis[coord_trail[i][0]-1] = cis[coord_trail[i][0]-1] - difference
		cis[coord_trail[i][1]-1] = cis[coord_trail[i][1]-1] - difference
		
		if (not hut in upgraded):
			upgraded.append(hut)
			totalupgraded +=1


print(totalupgraded)
print(" ".join(str(x+1) for x in upgraded))
print(" ".join(str(x) for x in price))