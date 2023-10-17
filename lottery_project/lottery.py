import random

class Lottery:
    def __init__(self):
        self.list_rewards = [
            "Gold necklace",
            "Labrador puppy",
            "12 chocolate bars",
            "A free vacation to anywhere",
            "100$"
        ]
    
    def get_reward(self):
        random_number = random.randint(0, self.list_rewards.len())
        return self.list_rewards[random_number]