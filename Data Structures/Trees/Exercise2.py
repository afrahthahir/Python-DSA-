class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent

        while p:
            level += 1
            p = p.parent

        return level
    
    def print_tree(self, level):
        spaces = "   " * self.get_level()
        prefix = spaces + "|---"
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                if child.get_level() <= level:
                  child.print_tree(level)
                



def build_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    root.add_child(india)

    gujarat = TreeNode("Gujarat")
    india.add_child(gujarat)

    ahmedabad = TreeNode("Ahmedabad")
    gujarat.add_child(ahmedabad)

    baroda = TreeNode("Baroda")
    gujarat.add_child(baroda)

    karnataka = TreeNode("Karnataka")
    india.add_child(karnataka)

    bangaluru = TreeNode("Bangluru")
    karnataka.add_child(bangaluru)

    mysuru = TreeNode("Mysuru")
    karnataka.add_child(mysuru)

    usa = TreeNode("USA")
    root.add_child(usa)

    newJersey = TreeNode("New Jersey")
    usa.add_child(newJersey)

    princeton = TreeNode("Princeton")
    newJersey.add_child(princeton)

    trenton = TreeNode("Trenton")
    newJersey.add_child(trenton)

    california = TreeNode("California")
    usa.add_child(california)

    sanFransisco = TreeNode("SanFransisco")
    california.add_child(sanFransisco)

    mountainView = TreeNode("MountainView")
    california.add_child(mountainView)

    paloAlto = TreeNode("Palo Alto")
    california.add_child(paloAlto)
    

    return root


if __name__ == "__main__":
    root = build_tree()
    root.print_tree(0)
    root.print_tree(1)
    root.print_tree(2)
    root.print_tree(3)