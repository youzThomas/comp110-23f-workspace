"""EX08 - River Simulation."""
__author__ = "730679279"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_bears: list[Bear] = []
        for x in self.bears:
            if x.age <= 5:
                new_bears.append(x)
        self.bears = new_bears
        new_fish: list[Fish] = []
        for y in self.fish:
            if y.age <= 3:
                new_fish.append(y)
        self.fish = new_fish        
        return None

    def bears_eating(self):
        if len(self.fish) >= 5:
            Bear().eat(3)
            self.remove_fish(3)
        return None
    
    def check_hunger(self):
        survive_bear: list[Bear] = []
        for x in self.bears:
            if x.hunger_score >= 0:
                survive_bear.append(x)
        self.bears = survive_bear
        return None
        
    def repopulate_fish(self):
        fish_offspring: int = (len(self.fish)//2)*4
        for x in range (0, fish_offspring):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        bear_offspring: int = len(self.bears)//2
        for x in range (0, bear_offspring):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        num_fish: int = len(self.fish)
        num_bear: int = len(self.bears)
        num_day: int = self.day
        print("~~~ Day " + num_day + ": ~~~\nFish population: " + num_fish + "\nBear population: " + num_bear)
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """E"""
        count: int = 0
        while count < 7:
            self.one_river_day()
            count += 1

    def remove_fish(self, amount: int):
        for x in range(0, amount):
            self.fish.pop(x)
        
        
