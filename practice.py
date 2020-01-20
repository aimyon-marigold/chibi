n=[0]*101
while 1:
    try:n[int(input())]+=1
    except:break
m_n=max(n)
for i in range(n.count(m_n)):
    print(n.index(m_n)+i)
    n.remove(m_n)
    