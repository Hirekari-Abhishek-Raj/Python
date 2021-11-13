dict={"a":".-","b":"-...","c":"-.-.","d":"-..","e":".","f":"..-.","g":"--.","h":"....","i":"..","j":".---","k":"-.-","l":".-..","m":"--","n":"-.","o":"---","p":".--.","q":"--.-","r":".-.","s":"...","t":"-","u":"..-","v":"...-","w":".--","x":"-..-","y":"-.--","z":"--.."}
for i in range(int(input())):
    lst=[str(i)for i in input().split()]
    for i in range(len(lst)):
        conc=""
        for let in lst[i]:
            conc=conc+dict[let]
        lst[i]=conc
	lst2=[]
 for i in lst:
            if i not in lst2:
                lst2.append(i)
    print(len(lst2))
