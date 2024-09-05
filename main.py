import pygame
import random
from creatures import Creature
from predators import Predator
from environment import create_environment, Resource

# Constants for the simulation
WIDTH, HEIGHT = 600, 600  # Pygame window size
GRID_SIZE = 100           # The environment's grid size for logic
SCALE = WIDTH // GRID_SIZE  # Scale the grid to match the window size
INITIAL_CREATURES = 20
INITIAL_PREDATORS = 5
NUM_RESOURCES = 30
MUTATION_RATE = 0.1  # Chance of mutation in offspring traits
FPS = 30  # Frames per second for the simulation

# Colors
CREATURE_COLOR = (0, 255, 0)   # Green for creatures
PREDATOR_COLOR = (255, 0, 0)   # Red for predators
RESOURCE_COLOR = (0, 0, 255)   # Blue for resources
BACKGROUND_COLOR = (255, 255, 255)  # White background

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Evolution Simulation")
clock = pygame.time.Clock()

# Helper function to scale coordinates to fit the window
def scale_position(x, y):
    return int(x * SCALE), int(y * SCALE)

# Main simulation loop with Pygame graphics
def run_simulation():
    creatures, predators, resources = create_environment(GRID_SIZE, GRID_SIZE, INITIAL_CREATURES, INITIAL_PREDATORS, NUM_RESOURCES, Creature, Predator)
    
    running = True
    step = 0
    while running:
        screen.fill(BACKGROUND_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Move all creatures
        for creature in creatures:
            creature.move(GRID_SIZE, GRID_SIZE)
            # Try to eat resources
            for resource in resources:
                if creature.eat(resource):
                    resources.remove(resource)
                    resources.append(Resource(random.uniform(0, GRID_SIZE), random.uniform(0, GRID_SIZE)))  # Add new resource

            # Draw creatures
            pos_x, pos_y = scale_position(creature.x, creature.y)
            pygame.draw.circle(screen, CREATURE_COLOR, (pos_x, pos_y), int(creature.size * SCALE / 2))

        # Move all predators
        for predator in predators:
            predator.move(GRID_SIZE, GRID_SIZE)
            # Try to hunt creatures
            for creature in creatures:
                if predator.hunt(creature):
                    creatures.remove(creature)

            # Draw predators
            pos_x, pos_y = scale_position(predator.x, predator.y)
            pygame.draw.circle(screen, PREDATOR_COLOR, (pos_x, pos_y), int(3 * SCALE / 2))  # Larger size for predators

        # Draw resources
        for resource in resources:
            pos_x, pos_y = scale_position(resource.x, resource.y)
            pygame.draw.circle(screen, RESOURCE_COLOR, (pos_x, pos_y), SCALE // 4)

        # Reproduce creatures
        new_creatures = []
        for creature in creatures:
            offspring = creature.reproduce(MUTATION_RATE)
            if offspring:
                new_creatures.append(offspring)
        creatures.extend(new_creatures)

        # Output status at each step (optional)
        step += 1
        print(f"Step {step}: Creatures: {len(creatures)}, Predators: {len(predators)}, Resources: {len(resources)}")

        if len(creatures) == 0:
            print("All creatures have been eaten.")
            running = False

        # Update the display and regulate the FPS
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    run_simulation()