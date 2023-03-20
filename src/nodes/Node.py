from src.Type import *
from src.MIPSContext import MIPSContext

class Node:
    def __init__(self, line="unknown"):
        self.m_parent = None
        self.m_children = []
        self.linenr = line

        self.type = None    # what Type this node is/returns

        self.terminating_normal = True
        self.reachable = False

    def getValue(self):
        return None

    def setValue(self, value):
        return

    def pushChild(self, child):
        child.m_parent = self
        self.m_children.append(child)
        return child

    def replaceSelf(self, replacement):
        for child in self.m_children:
            replacement.pushChild(child)
        replacement.linenr = self.linenr
        self.m_parent.replaceChild(self, replacement)

    def getParent(self):
        return self.m_parent

    def getChild(self, i):
        return self.m_children[i]

    def getChildrenCount(self):
        return len(self.m_children)

    def getRightSiblingIfExists(self):
        i = self.getParent().m_children.index(self) + 1
        if i >= len(self.getParent().m_children):
            return None
        return self.getParent().getChild(i)

    def getLeftSiblingIfExists(self):
        i = self.getParent().m_children.index(self) - 1
        if i < 0:
            return None
        return self.getParent().getChild(i)

    def replaceChild(self, old_child, new_child):
        i = self.m_children.index(old_child)  # find old child in list of children
        self.m_children[i] = new_child  # and replace the exact node of parent
        new_child.m_parent = self  # don't forget to tell our child they have a new parent
        return new_child

    def insertChild(self, pos, child):
        self.m_children.insert(pos, child)
        child.m_parent = self

    def destroyChild(self, child):
        self.m_children.remove(child)

    def destroyChildAt(self, i):
        child = self.m_children[i]
        self.m_children.remove(child)

    def isLeaf(self):
        return len(self.m_children) == 0

    def isRoot(self):
        return self.getParent() is None 

    def isFirstChild(self):
        if self.getParent() is None:
            return False
        else:
            return self.getParent().getChild(0) == self

    # find the first node, going up the tree
    # I use it mostly to find first block
    def findFirstNode(self, typeName : type):
        if isinstance(self, typeName):
            return self
        if self.getParent() is not None:
           return self.getParent().findFirstNode(typeName)
        return None

    def getLabel(self):
        self.root = "Root"
        return self.root

    def getType(self):
        return self.type

    def setType(self, typ):
        self.type = typ

    def acceptVisitor(self, visitor):
        visitor.enterNode(self)
        for child in self.m_children:
            child.acceptVisitor(visitor)
        visitor.exitNode(self)

    def generateLLVM(self, context):
        for child in self.m_children:
            child.generateLLVM(context)

    def generateMIPS(self, context: MIPSContext):
        for child in self.m_children:
            child.generateMIPS(context)
