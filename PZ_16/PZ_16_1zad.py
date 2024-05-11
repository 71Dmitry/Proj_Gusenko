class Note:
    def __init__(self, text, iscomp):
        self.text = text
        self.iscompleted = iscomp
        self.count = 0
    def upcount(self, cif):
        self.count += cif

    def reset_count(self):
        self.count = 0


dict1 = Note('fffff', True)

print(dict1.text)
print(dict1.iscompleted)
print(dict1.count)
dict1.upcount(5)
print(dict1.count)
dict1.reset_count()
print(dict1.count)
print(dict1.__dict__)

