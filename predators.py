import random
import math
from creatures import distance

class Predator:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed/4
        self.energy = 100
        self.target_x = random.uniform(0, 100)  # Assign a random target
        self.target_y = random.uniform(0, 100)

    def move(self, width, height):
        # If predator reaches its target, assign a new random target
        if distance(self.x, self.y, self.target_x, self.target_y) < 1:
            self.target_x = random.uniform(0, width)
            self.target_y = random.uniform(0, height)

        # Calculate direction towards target
        direction_x = self.target_x - self.x
        direction_y = self.target_y - self.y
        length = math.sqrt(direction_x ** 2 + direction_y ** 2)

        if length > 0:
            direction_x /= length
            direction_y /= length

        self.x += direction_x * self.speed
        self.y += direction_y * self.speed

        # Keep within bounds
        self.x = max(0, min(self.x, width))
        self.y = max(0, min(self.y, height))

    def hunt(self, creature):
        if distance(self.x, self.y, creature.x, creature.y) < 5:  # Catch if close enough
            self.energy += 50  # Gain energy from consuming prey
            return True
        return False
    
    def reproduce(self, mutation_rate):
        if self.energy >= 150:  # Only reproduce if enough energy
            new_speed = self.speed * (1 + random.uniform(-mutation_rate, mutation_rate))
            new_size = self.size * (1 + random.uniform(-mutation_rate, mutation_rate))
            new_vision = self.vision_range * (1 + random.uniform(-mutation_rate, mutation_rate))
            offspring = Predator(self.x, self.y, new_speed, new_size, new_vision)
            self.energy -= 50  # Cost of reproduction
            return offspring
        return None