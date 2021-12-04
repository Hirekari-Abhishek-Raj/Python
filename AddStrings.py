def addStrings(num1, num2):     
	if len(num1)<len(num2):
		num1,num2=num2,num1
	num1=num1[::-1]
	num2=num2[::-1]
	num3=[]
	carry=0
	for i in range(len(num2)):
		x=int(num1[i])+int(num2[i])+carry
		carry=x//10
		num3.append(x%10)
	for i in range(len(num2),len(num1)):
		x=int(num1[i])+carry
		carry=x//10
		num3.append(x%10)
	if carry!=0:
		num3.append(carry)
	num3=num3[::-1]
	return "".join(map(str,num3))

## Do not change anything below this line:

for _ in range(int(input())):
    n1, n2 = input().split()
    print(addStrings(n1,n2))
