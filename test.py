from collections import defaultdict

class simple_component():
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "simple_component at {}".format(self.id)

component = simple_component(0)
component2 = simple_component(1)

components = defaultdict(dict)

components[type(component)][0] = component
components[type(component2)][0] = component2

components[type(component)][1] = component
components[type(component)][2] = component

components[type(component2)][3] = component2

print("--- List ---")
print(components)
print("--- Type ---")
print(components[type(component2)].get(1))