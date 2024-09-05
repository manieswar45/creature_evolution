import random

class Resource:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Function to create the environment with initial creatures, predators, and resources
def create_environment(width, height, num_creatures, num_predators, num_resources, Creature, Predator):
    creatures = [Creature(random.uniform(0, width), random.uniform(0, height),
                          random.uniform(1, 3), random.uniform(1, 3), random.uniform(10, 20))
                 for _ in range(num_creatures)]
    
    predators = [Predator(random.uniform(0, width), random.uniform(0, height), random.uniform(2, 4))
                 for _ in range(num_predators)]
    
    resources = [Resource(random.uniform(0, width), random.uniform(0, height)) for _ in range(num_resources)]
    
    return creatures, predators, resources