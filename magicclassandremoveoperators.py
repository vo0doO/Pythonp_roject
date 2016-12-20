class Quen:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Quen({})".format(self._hiddenlist)

quen = Quen([1, 2, 3])
print(quen)
print("=================")
quen.push(4)
quen.push(0)
print("================")
print(quen)
quen.pop()
print(quen)
