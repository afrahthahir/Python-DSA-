
class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
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
    
    def print_tree(self, data):
        spaces = "   " * self.get_level()
        prefix = spaces + "|---"
        tree = ""
        # print(data)
        if data == "name":
            tree = self.name
            
        elif data == "designation":
            tree = self.designation
        
        elif data == "both":
            tree = self.name + " " + "(" + self.designation + ")"
        print(prefix + tree)
        if self.children:
            for child in self.children:
                  child.print_tree(data)
                



def build_management_tree():
    root = TreeNode("Nilupul", "CEO")

    cto = TreeNode("Chinmay", "CTO")
    root.add_child(cto)

    infra = TreeNode("Vishwa","Infrastructure Head")
    cto.add_child(infra)

    cloud = TreeNode("Dhaval", "Cloud Manager")
    infra.add_child(cloud)

    app = TreeNode("Abhijit", "App Manager")
    infra.add_child(app)

    appHead = TreeNode("Aamir", "Application Head")
    cto.add_child(appHead)

    hr = TreeNode("Gels", "HR Head")
    root.add_child(hr)

    recruit = TreeNode("Peter", "Recruitment Manager")
    hr.add_child(recruit)

    policy = TreeNode("Waqas", "Policy Manager")
    hr.add_child(policy)
    

    return root


if __name__ == "__main__":
    root = build_management_tree()
    root.print_tree("both")
    root.print_tree("name")
    root.print_tree("designation")








