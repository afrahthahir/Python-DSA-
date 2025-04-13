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
          


    def print_tree(self):
        spaces = "  " * self.get_level() 
        prefix = spaces + "|---" if self.parent else ""
        print(prefix + self.data) #printing nodes here

        if self.children:
            for child in self.children:
                # print(child.data)
                child.print_tree()   # recursively calling to print child nodes


def build_tree():
    root = TreeNode("Electronics")

    tv = TreeNode("TV")
    root.add_child(tv)

    phone = TreeNode("phone")
    root.add_child(phone)

    laptop = TreeNode("laptop")
    root.add_child(laptop)

    led = TreeNode("LED")
    tv.add_child(led)

    lcd = TreeNode("LCD")
    tv.add_child(lcd)

    plasma = TreeNode("Plasma")
    tv.add_child(plasma)

    nokia = TreeNode("Nokia")
    phone.add_child(nokia)

    blackberry = TreeNode("blackberry")
    phone.add_child(blackberry)

    samsungFlip = TreeNode("samsungFlip")
    phone.add_child(samsungFlip)

    lenovo = TreeNode("lenovo")
    laptop.add_child(lenovo)

    acer = TreeNode("acer")
    laptop.add_child(acer)

    # print(acer.get_level())

    return root

if __name__ == "__main__":
    root = build_tree()
    root.print_tree()