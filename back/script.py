import pdftotext
import re

def checkWord(word):
	for i in word:
		if not i.isalpha():
			if i != " ":
				return False
	return True


if __name__ == '__main__':
	with open("example.pdf", "rb") as f:
		pdf = pdftotext.PDF(f)
	string = pdf[0]
	#for i in range(len(pdf)-1):	
		#string+=pdf[i]
	

	vals = string.split("\n")
	vals = vals[5:]
	res = []
	res2 = []	
	for val in vals:
		val = re.split(r'\s{2,}', val) 
		if len(val)>2:
			t3 = val[2].split(" ")
			if len(t3)>4:
				val.insert(3,t3.pop(0))
				val.insert(4,t3.pop(0))
				val.insert(5,t3.pop(2))
				date = []
				date.append(t3.pop(2))
				date.append(t3.pop(2))
				date.append(t3.pop(2))
				val.insert(6," ".join(date))
				val.insert(7,t3.pop(2))
				val.insert(7,t3.pop(2))
				name = []
				name.append(t3.pop(2))
				name.append(t3.pop(2))
				val.insert(8," ".join(name))
				val.pop(2)
			
			if len(val) < 4:
				pass	
			elif (len(val[2]) > 19  or len(val[3]) > 19) and val[0] != '':
				k = 2 if len(val[2]) > 19 else 3	
				t4 = val[k].split(" ")			
				del val[k]
				val.insert(k, t4.pop(0))
				val.insert(k+1, t4.pop(0))
				date = []
				date.append(t4.pop(0))
				date.append(t4.pop(0))
				val.insert(k+2, " ".join(date))

				
			for j in range(len(val)):
				if ("PM" in val[j] or "AM" in val[j]) and len(val[j]) != 17:
					t7 = val[j].split(" ")
					val.remove(val[j])
					
					
					if not t7[0][0].isdigit():
						val.insert(j, t7.pop(0))	
					if t7[-1].isdigit():
						val.insert(j+1, t7.pop())
					if len(t7) != 3:
						val.insert(j+1, t7.pop())
					val.insert(j+1, " ".join(t7))
		
						
					
			print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
			print(val)
				
		if len(val) >= 5:
			t4 = val[4].split(" ")	
			if len(t4) == 4:
				continue
			
		if len(val) >= 7:
			res.append(val)
		else:
			res2.append(val)
	res3 = []
	temp = []
	trash = []
	for i in res:
		
		t = i[3].split(" ")
		if len(t)>2:
			
			i.insert(3,t.pop(0))
			i.insert(4,t.pop(0))
			i.insert(5," ".join(t))
			i.pop(6)
		
		t2 = i[6].split(" ")
		if len(t2)>4:
			
			i.insert(6,t2.pop(0))
			i.insert(8,t2.pop(3))
			i.insert(9,t2.pop(3))
			i.insert(7," ".join(t2))
			i.pop(8)
		
			
	for r in res2:	
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		print(r)
		if len(r) < 2:
			continue
		if 'cap' not in r[1] and not r[1][-1].isdigit():
			temp.append(r)
		else:
			trash.append(r[1])
		if len(temp) == 2:
			temp[0].pop(0)
			temp[1].pop(0)
			temp2 = []
			
			temp2.append(temp[0][0]+" "+temp[1][0])
			if len(temp[0])>1:
				print("I'M HEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEERE")				
				print(temp)	
				temp2.append(temp[0][1]+" "+temp[1][1])
			if len(temp[0])>2:
				
				temp2.append(temp[0][2]+" "+temp[1][2])				
			temp = []
			res3.append(temp2)

	for i in range(len(res)):
		res[i].insert(1,res3[i][0])
	for i in res:
		for j in i:
			if j == '-':
				i.remove(j)

	
	for i in res:
		if not i[5][-1].isdigit():
			i[5]=i[5].split(" ")
			i[5] = i[5][-1]
		else:
			i.remove(i[5])
	
		if i[6][-1].isdigit():
			i[6]=i[6].split(" ")
			i.insert(7,i[6].pop())
			i[6] = " ".join(i[6])

		
			
	for i in range(len(res)):
		if len(res3[i])>1:
			res[i].insert(9, res3[i][1])
		if len(res3[i])>2:
			res[i].append(res3[i][2])

	for i in res:
		if i[8][0].isdigit():
			i[8] = i[8].split(" ")
			if len(i[8]) == 1:
				i[8] = i[8][0]
				continue
			name = i[8].pop(-2)
			surname = i[8].pop()
			
			i.insert(9, name + " " + surname )
			i[8] = i[8][0]
	for i in res:
		if len(i)<11:
			
			i.append(trash.pop(0)+" - " +trash.pop(0))
	print(trash)
	for r in res:
		print(r)
	courses = {}

	# Read all the text into one string
	#print("\n\n".join(pdf))
	