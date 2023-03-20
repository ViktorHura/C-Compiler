class SymbolTable:
    def __init__(self, block=None):
        self.data = {}
        self.block = block
        self.parent = None

    def isRoot(self):
        return self.parent is None

    def declare(self, name, node):
        if self.data.get(name) is not None:  # check if node not already declared in this scope
            return False
        self.data[name] = node    # points to declarator node
        return True

    def redeclare(self, name, node):
        self.data[name] = node

    def lookUp(self, name):
        rtn = self.data.get(name)   # find node in current scope
        if rtn is None and self.parent is not None:     # go up the scope if possible
            return self.parent.lookUp(name)
        return rtn

    def lookUpAndGet(self, name):
        rtn = self.data.get(name)
        if rtn or self.parent is None:
            return rtn, self
        else:
            return self.parent.lookUpAndGet(name)

    def lookUpDeclarator(self, name):
        return self.lookUp(name)

    def lookUpType(self, name):
        return self.lookUp(name).getType()

    def remove(self, name):
        return self.data.pop(name, None)

    def toDot(self):
        row1 = "{Symbol|"
        row2 = "{Data|"

        for key in self.data.keys():
            row1 += key + "|"
            row2 += str(self.lookUpType(key)) + " "
            row2 += '|'

        row1 = row1[:-1]
        row1 += "}"

        row2 = row2[:-1]
        row2 += "}"

        return row1 + "|" + row2