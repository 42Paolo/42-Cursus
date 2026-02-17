def ft_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def ft_append(lst, element):
    new_list = []
    for i in range(ft_len(lst)):
        new_list += [lst[i]]
    new_list += [element]
    return new_list

class Plant:

    category = "regular"

    def __init__(self, name, color, age_d, height_cm):
        self.name = name
        self.color = color
        self.age_d = age_d
        self.height_cm = height_cm

    def grow(self):
        self.height_cm += 1
        print(self.name + " grew 1cm")

    def get_info(self):
        return "- " + self.name + ": " + str(self.height_cm) + "cm"


class FloweringPlant(Plant):

    category = "flowering"

    def __init__(self, name, color, age_d, height_cm, bloom_stage, bloom_duration_days):
        super().__init__(name, color, age_d, height_cm)
        self.bloom_stage = bloom_stage
        self.bloom_duration_days = bloom_duration_days

    def get_info(self):
        if self.bloom_stage:
            blooming = "blooming"
        else:
            blooming = "not blooming"

        return "- " + self.name + ": " + str(self.height_cm) + "cm, " + self.color + " flowers (" + blooming + ")"


class PrizeFlower(FloweringPlant):

    category = "prize"

    def __init__(self, name, color, age_d, height_cm, bloom_stage,
                 bloom_duration_days, award_name, award_year, score):
        super().__init__(name, color, age_d, height_cm,
                         bloom_stage, bloom_duration_days)
        self.award_name = award_name
        self.award_year = award_year
        self.score = score

    def get_info(self):
        if self.bloom_stage:
            blooming = "blooming"
        else:
            blooming = "not blooming"

        return "- " + self.name + ": " + str(self.height_cm) + \
               "cm, " + self.color + " flowers (" + blooming + \
               "), Prize points: " + str(self.score)


class Owner:

    def __init__(self, name, age_y):
        self.name = name
        self.age_y = age_y


class Garden:

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.plants = []
        self._total_growth = 0
        self._plants_added = 0

    def add_plant(self, plant):
        self.plants = ft_append(self.plants, plant)
        self._plants_added += 1
        print("Added " + plant.name + " to " + self.owner.name + "'s garden")

    def grow_all(self):
        print(self.owner.name + " is helping all plants grow...")

        for i in range(ft_len(self.plants)):
            self.plants[i].grow()
            self._total_growth += 1

    def get_score(self):
        total = 0

        for i in range(ft_len(self.plants)):
            plant = self.plants[i]

            if plant.category == "prize":
                total += plant.score

        return total

    def get_report(self):

        regular = 0
        flowering = 0
        prize = 0

        for i in range(ft_len(self.plants)):
            plant = self.plants[i]

            if plant.category == "regular":
                regular += 1
            elif plant.category == "flowering":
                flowering += 1
            elif plant.category == "prize":
                prize += 1

        print("\n=== " + self.owner.name + "'s Garden Report ===")
        print("Plants in garden:")

        for i in range(ft_len(self.plants)):
            print("  " + self.plants[i].get_info())

        print("Plants added: " + str(self._plants_added) +
              ", Total growth: " + str(self._total_growth) + "cm")

        print("Plant types: " + str(regular) + " regular, " +
              str(flowering) + " flowering, " +
              str(prize) + " prize flowers")


class GardenManager:

    def __init__(self, gardens=None):
        self.gardens = []

        if gardens is not None:
            for i in range(ft_len(gardens)):
                self.gardens = ft_append(self.gardens, gardens[i])

    def add_garden(self, garden):
        self.gardens = ft_append(self.gardens, garden)

    def get_info(self):

        print("=== Garden Management System Demo ===")

        for i in range(ft_len(self.gardens)):
            self.gardens[i].grow_all()

        for i in range(ft_len(self.gardens)):
            self.gardens[i].get_report()

        has_tall = False

        for i in range(ft_len(self.gardens)):
            garden = self.gardens[i]

            for j in range(ft_len(garden.plants)):
                if garden.plants[j].height_cm > 100:
                    has_tall = True

        print("\nHeight validation test: " + str(has_tall))

        print("Garden scores -")

        for i in range(ft_len(self.gardens)):
            garden = self.gardens[i]
            print(garden.owner.name + ": " + str(garden.get_score()))

        print("Total gardens managed: " + str(ft_len(self.gardens)))

def main():

    alice = Owner("Alice", 35)
    bob = Owner("Bob", 42)

    alice_garden = Garden("Alice's Garden", alice)
    alice_garden.add_plant(Plant("Oak Tree", "green", 3650, 100))
    alice_garden.add_plant(FloweringPlant("Rose", "red", 25, 25, True, 30))
    alice_garden.add_plant(PrizeFlower("Sunflower", "yellow", 50, 50,
                                       True, 60, "Best Flower", 2023, 10))

    bob_garden = Garden("Bob's Garden", bob)
    bob_garden.add_plant(PrizeFlower("Orchid", "purple", 100, 80,
                                     True, 90, "Rare Bloom", 2022, 92))

    manager = GardenManager([alice_garden, bob_garden])
    manager.get_info()


if __name__ == "__main__":
    main()