class House:

    def __init__(self, household_type, total_area, furniture, remaining_area=0):
        self.household_type = household_type
        self.total_area = total_area
        self.furniture = furniture
        self.remaining_area = remaining_area
        self.name_furniture()
        
    def __str__(self):
        return f'Household_Type: {self.household_type}, Total_area: {self.total_area}, Remaining_area: {self.total_area - self.furniture_area}, List of furnitures: {self.furniture.keys()}'

    def name_furniture(self):
        self.furniture_area = 0
        for item in self.furniture.values():
            self.furniture_area += item
        return self.furniture_area
        


house = House('House', 100,{'bed': 4,  'wardrobe': 2, 'table': 1.5})
print(house)
        