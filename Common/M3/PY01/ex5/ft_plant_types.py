class Plant:
    def __init__(self, name, height_cm, age_d):
        self.name = name
        self.height_cm = height_cm
        self.age_d = age_d


class Flower(Plant):
    def __init__(self, name, height_cm, age_d, color):
        super().__init__(name, height_cm, age_d)
        self.color = color

    def get_info(self):
        print(
            f"{
                self.name} (Flower): {
                self.height_cm}, {
                self.age_d} days, {
                    self.color} color")

    def get_info_v2(self):
        print(f"{self.name} is in its: ", end="")
        if 0 <= self.age_d <= 7:
            print("Bud Formation")
        elif 8 <= self.age_d <= 14:
            print("Bud Development")
        elif 15 <= self.age_d <= 21:
            print("Blooming")
        elif self.age_d >= 22:
            print("Wilting")
        print()


class Tree(Plant):
    def __init__(self, name, height_cm, age_d, diameter_cm):
        super().__init__(name, height_cm, age_d)
        self.diameter_cm = diameter_cm

    def get_info_v2(self):
        growth_factor = self.age_d / 30
        shade = self.diameter_cm * growth_factor
        print(f"{self.name} provides {shade:.0f} square meters of shade\n")

    def get_info(self):
        print(
            f"{
                self.name} (Tree): {
                self.height_cm}cm, {
                self.age_d} days, {
                    self.diameter_cm}cm diameter")


class Vegetable(Plant):
    def __init__(
            self,
            name,
            height_cm,
            age_d,
            harvest_season,
            nutritional_value):
        super().__init__(name, height_cm, age_d)
        self.harvest_season = harvest_season
        self.nutrinational_value = nutritional_value

    def get_info(self):
        print(
            f"{
                self.name} (Vegetable): {
                self.height_cm}cm, {
                self.age_d} days, {
                    self.harvest_season} harvest")

    def get_info_v2(self):
        print(f"{self.name} is rich in vitamin {self.nutrinational_value}\n")


def main():

    p1 = Flower("Rose", 30, 10, "red")
    p2 = Flower("Tulip", 25, 5, "yellow")
    p3 = Tree("Oak", 500, 20, 200)
    p4 = Tree("Pine", 450, 15, 150)
    p5 = Vegetable("Carrot", 20, 40, "Spring", "High in Vitamin A")
    p6 = Vegetable("Lettuce", 15, 25, "Summer", "Rich in Fiber")

    plants = [p1, p2, p3, p4, p5, p6]

    print("=== Garden Plant Types ===\n")
    for p in plants:
        p.get_info()
        p.get_info_v2()


if __name__ == "__main__":
    main()
