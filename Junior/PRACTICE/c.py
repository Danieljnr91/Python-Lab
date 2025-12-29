# letters = [
#     'A','b','C','D','E','F','G','H','i','_','k','l','n','M','N','O','P','Q','R','S','T','U','v','w','x','y','z'
# ]

# v = input("Enter letter:")

# for i in range(len(letters)):
#     if letters[i] == '_':
#         letters[i] = v

# print(letters)

# dicts ={}
# date = "25th december 25"
# subject = "physics"
# topic = "Forces"
# time = "3hrs"

# lists=[]
# l=[1,2,3]
# v=lists +l
# dicts[date] = [subject , topic ,time]
# print(dicts)
# print(v)

g={
    "o":[1,2,3],
    "f":[4,5,6]
}
for i,x in g.items():
    u = sum(x)
    avg = u/len(x)
    g[i]=avg
print(g)

# h={}
# for i in g:
#     g[i]=[]
# for x in g:
#     h[x]=[]
# print(h)
