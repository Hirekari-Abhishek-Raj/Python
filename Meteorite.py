t=int(input())
for i in range(t):
	vertical=set()
	hori=set()
	vertical.add(1)
	hori.add(1)
	n,m,q=[int(i)for i in input().split()]
	vertical.add(n)
	hori.add(m)
	for i in range(q):
	    x,y=[int(i)for i in input().split()]
	    vertical.add(x)
	    hori.add(y)
	vertical=sorted(vertical)
	hori=sorted(hori)
	v_a=[vertical[i]-vertical[i-1]for i in range(1,len(vertical))]
	h_a=[hori[i]-hori[i-1]for i in range(1,len(hori))]
	print(len(v_a)*len(h_a),min(v_a)*min(h_a),max(v_a)*max(h_a))
