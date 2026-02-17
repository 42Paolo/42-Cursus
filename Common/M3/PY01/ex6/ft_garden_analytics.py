def ft_is_instance(obj, cls):
    current_class = obj.__class__
    while current_class is not None:
        if current_class == cls:
            return True
        current_class = current_class.__base__
    return False

class Plant():
    def __init__(self, name, color, age_d):
        self.name = name
        self.color = color
        self.age_d = age_d


class FloweringPlant(Plant):
    def __init__(self, name, color, age_d, bloom_stage, bloom_duration_days):
        super().__init__(name, color, age_d)
        self.bloom_stage = bloom_stage
        self.bloom_duration_days = bloom_duration_days


class PrizeFlower(FloweringPlant):
    def __init__(self, name, color, age_d, bloom_stage, bloom_duration_days,
                 award_name, award_year, score):
        super().__init__(name, color, age_d, bloom_stage, bloom_duration_days)
        self.award_name = award_name
        self.award_year = award_year
        self.score = score
		
class Owner:
    def __init__(self, name, age_y):
        self.name = name
        self.age_y = age_y

class Garden:
    def __init__(self, name, owner, plant):
        if not isinstance(owner, Owner):
            raise TypeError(f"owner deve essere un oggetto Owner, non {type(owner).__name__}")
        self.name = name
        self.owner = owner
        self.plant = plant
		

def main():


if __name__ == "__main__":
	main()