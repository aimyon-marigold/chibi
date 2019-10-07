class Counter(object):
    def __init__(self): #コンストラクタ
        self.cut = 0
    
    def count(self):
        self.cut += 1

    def doublecount(self):
        self.cut += 2
    
    def reset(self):
        self.cut = 0
    
    def show(self):
        print(self.cut)

    def __repr__(self): #文字列を返すと表示される
        return str(self.cut)

c = Counter()
c.show()
c.doublecount()
c.show()
print(type(c))
print(c)
