import random

def initialize_population(pop_size, gene_length):
    population = []
    for _ in range(pop_size):
        individual = ''.join(random.choice('01') for _ in range(gene_length))
        population.append(individual)
    return population

def calculate_fitness(individual):
    return individual.count('1')

def select_parents(population, fitness_values):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    parent1 = population[roulette_wheel_selection(probabilities)]
    parent2 = population[roulette_wheel_selection(probabilities)]
    return parent1, parent2

def roulette_wheel_selection(probabilities):
    random_choice = random.random()
    cumulative_probability = 0.0
    for i, prob in enumerate(probabilities):
        cumulative_probability += prob
        if cumulative_probability > random_choice:
            return i

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate(individual, mutation_rate):
    mutated_individual = list(individual)
    for i in range(len(mutated_individual)):
        if random.random() < mutation_rate:
            mutated_individual[i] = '1' if mutated_individual[i] == '0' else '0'
    return ''.join(mutated_individual)

def genetic_algorithm(pop_size, gene_length, generations, mutation_rate):
    population = initialize_population(pop_size, gene_length)
    for generation in range(generations):
        print(f"Generation {generation}:")
        
        fitness_values = [calculate_fitness(individual) for individual in population]
        
        if max(fitness_values) == gene_length:
            print("Optimal solution found!")
            break
        
        parent1, parent2 = select_parents(population, fitness_values)
        offspring1, offspring2 = crossover(parent1, parent2)
        
        offspring1 = mutate(offspring1, mutation_rate)
        offspring2 = mutate(offspring2, mutation_rate)
        
        population[fitness_values.index(min(fitness_values))] = offspring1
        population[fitness_values.index(min(fitness_values))] = offspring2
        
        best_individual = population[fitness_values.index(max(fitness_values))]
        print(f"Best individual: {best_individual}, Fitness: {max(fitness_values)}")

if __name__ == "__main__":
    pop_size = 10
    gene_length = 8 
    generations = 20 
    mutation_rate = 0.01

    genetic_algorithm(pop_size, gene_length, generations, mutation_rate)
