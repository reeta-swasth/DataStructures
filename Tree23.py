# Implementing 2-3 Binary tree

class Node23:

    key1 = None
    key2 = None
    leftnode23 = None
    rightnode23 = None
    middlenode23 = None


# Display all the values in 2-3 Tree
    def display23Tree(self):
        # Sorted display of node values

        if self.leftnode23 <> None:
            self.leftnode23.display23Tree()

        print self.key1

        if self.middlenode23 <> None:
            self.middlenode23.display23Tree()

        print self.key2

        if self.rightnode23 <> None:
            self.rightnode23.display23Tree()

# Insert new value into 2-3 Tree
    def insert(self, value):
        if self.key1 ==None:
            self.key1 = value
        elif self.key2 == None and value > self.key1:
            self.key2 = value
        elif self.key2 == None and value <= self.key1:
            self.key2 = self.key1
            self.key1 = value
        elif self.leftnode23 == None:
            self.split_node(value)
        elif  value < self.key1:
            self.leftnode23.insert(value)
        elif  value > self.key1 and value < self.key2:
            self.middlenode23.insert(value)
        elif  value > self.key2:
            self.rightnode23.insert(value)

    def split_node(self, new_value):




class Tree23:
    node23 = Node23()
    def displayNode(self):
        self.node23.display23Tree()

    def insertValue(self, value):
        self.node23.insert(value)



tree23 = Tree23()

tree23.insertValue(23)
tree23.insertValue(45)
tree23.insertValue(12)
tree23.insertValue(8)
tree23.insertValue(14)
tree23.insertValue(28)
tree23.insertValue(69)
tree23.insertValue(300)
tree23.insertValue(35)
tree23.insertValue(1)
tree23.insertValue(5)

tree23.displayNode()









