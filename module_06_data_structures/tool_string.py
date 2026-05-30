class Tool:
    def __init__(self, name, od, id_, length, weight, pressure_rating):
        self.name = name
        self.od = od
        self.id = id_
        self.length = length
        self.weight = weight
        self.pressure_rating = pressure_rating

class ToolString:
    def __init__(self, name, tools):
        self.name = name
        self.tools = tools

    def total_length(self):
        total = 0
        for tool in self.tools:
            total += tool.length
        return total

    def total_weight(self):
        total = 0
        for tool in self.tools:
            total += tool.weight
        return total

    def max_od(self):
        largest = 0
        for tool in self.tools:
            if tool.od > largest:
                largest = tool.od
        return largest

    def min_pressure_rating(self):
        smallest = self.tools[0].pressure_rating
        for tool in self.tools:
            if tool.pressure_rating < smallest:
                smallest = tool.pressure_rating
        return smallest

#create tool objects
packer = Tool("Production Packer", 5.5, 2.875, 8.0, 250, 10000)
screen = Tool("Wirewrap Screen", 4.5, 2.5, 40, 400, 7500)
sleeve = Tool("Frac Sleeve", 4.75, 2.375, 6.5, 175, 10000)

# put tools into a list
tools = [packer, screen, sleeve]

# create a toolstring object
my_string = ToolString("Lower Completion String", tools)

#test total_length()
print(my_string.total_length())
print(my_string.total_weight())
print(my_string.max_od())
print(my_string.min_pressure_rating())