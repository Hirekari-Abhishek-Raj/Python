lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
lst2=[int(i)for i in input().split()]
dict={}
for i in range(26):
    dict[lst[i]]=lst2[i]
word=input()
high=float('-inf')
for i in word:
    if dict[i]>high:
        high=dict[i]
print(len(word)*high)
