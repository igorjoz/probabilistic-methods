import math
from City import City
from TreeNode import TreeNode

NUM_CITIES_TASK1 = 6
NUM_CITIES_TASK2 = 6
COMBINATION_LENGTH = 5

cities_list = []
cities_names_list = []

permutation_results = []
temp_permutation = []

combination_results = set()
temp_combination = set()


def generate_permutations(node, remaining_items, depth):
    if depth == 0 or not remaining_items:
        return
    for item in remaining_items:
        new_node = TreeNode(item, [])
        remaining_after_selection = remaining_items.copy()
        remaining_after_selection.remove(item)
        generate_permutations(new_node, remaining_after_selection, depth - 1)
        node.children.append(new_node)
        node.children.sort()
        remaining_after_selection.add(item)


def collect_permutations(node):
    global permutation_results, temp_permutation
    if node.data != -1:
        temp_permutation.append(node.data)
    if not node.children:
        permutation_results.append(temp_permutation.copy())
        temp_permutation.clear()
        return
    collect_permutations(node.children[0])
    if node.children and not node.children[0].children:
        node.children.pop(0)


def collect_combinations(node, length):
    global combination_results, temp_combination
    combination_results = set()
    combination_results.add(tuple())
    for child in node.children:
        temp_combination = {child.data}
        new_combinations = set()
        for existing_combination in combination_results:
            extended_combination = (*existing_combination, child.data)
            new_combinations.add(extended_combination)
        combination_results.update(new_combinations)
    combination_results = {frozenset(c) for c in combination_results if len(c) == length}


def find_shortest_cycle():
    global permutation_results
    minimum_distance = math.inf
    optimal_path = []
    for path in permutation_results:
        path_distance = sum(cities_list[path[i]].distance(cities_list[path[(i + 1) % len(path)]]) for i in range(len(path)))
        if path_distance < minimum_distance:
            minimum_distance = path_distance
            optimal_path = path
    return optimal_path, minimum_distance


def find_best_partition(tree, target_population, max_depth):
    closest_match = math.inf
    best_subset = []
    subset_population_total = 0
    for depth in range(1, max_depth):
        collect_combinations(tree, depth)
        for subset in combination_results:
            current_population = sum(cities_list[city].population for city in subset)
            population_difference = abs(current_population - target_population)
            if population_difference < closest_match:
                closest_match = population_difference
                best_subset = subset
                subset_population_total = current_population
    return subset_population_total, best_subset


if __name__ == '__main__':
    print("Cities:")

    with open("italy.txt") as file:
        next(file)  # Skip header line

        for line in file:
            parts = line.strip().split()
            cities_names_list.append(parts[1])
            cities_list.append(City(parts))
            print(parts)

    root = TreeNode(-1, [])
    generate_permutations(root, set(range(NUM_CITIES_TASK1)), NUM_CITIES_TASK1)

    while root.children:
        collect_permutations(root)

    print(f"1. Permutations for N={NUM_CITIES_TASK1}: {len(permutation_results)}")
    for idx, perm in enumerate(permutation_results, 1):
        print(f"{idx}. {list(map(lambda x: cities_names_list[x], perm))}")

    path, distance = find_shortest_cycle()
    print(f"1d. Shortest cycle for N={NUM_CITIES_TASK1}: {distance} {list(map(lambda x: cities_names_list[x], path))}")

    root = TreeNode(-1, [])
    generate_permutations(root, set(range(NUM_CITIES_TASK2)), NUM_CITIES_TASK2)
    collect_combinations(root, COMBINATION_LENGTH)
    print(f"2. Combinations for N={NUM_CITIES_TASK2}, K={COMBINATION_LENGTH}: {len(combination_results)}")
    combinations_sorted = sorted([list(map(lambda y: cities_names_list[y], x)) for x in combination_results])

    for idx, combo in enumerate(combinations_sorted, 1):
        print(f"{idx}. {combo}")

    target_pop = sum(city.population for city in cities_list[:NUM_CITIES_TASK2]) // 2
    best_pop, best_combo = find_best_partition(root, target_pop, NUM_CITIES_TASK2)
    print(f"2d. Best partition for N={NUM_CITIES_TASK2} (target: {target_pop}): {best_pop} {list(map(lambda x: cities_names_list[x], best_combo))}")
