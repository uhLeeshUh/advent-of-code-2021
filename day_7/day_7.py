import math
file = open("day_7_input", "r")
text = file.read()
hor_positions = [int(pos) for pos in text.split(",")]
file.close()


def get_optimal_fuel_cost(positions_list) -> int:
    sorted_list = sorted(positions_list)
    median_position = sorted_list[math.floor(len(sorted_list) / 2)]
    fuel_cost = 0
    for pos in sorted_list:
        fuel_cost += abs(pos - median_position)
    return fuel_cost


print(get_optimal_fuel_cost(hor_positions))

def get_weighted_fuel_cost(pos, des) -> int:
    distance_to_travel = abs(des - pos)
    cost = 0
    for i in range(1,distance_to_travel+1):
        cost += i
    return cost


def get_weighted_optimal_fuel_cost(positions_list) -> int:
    positions_sum = sum(positions_list)
    positions_length = len(positions_list)
    mean_pos = math.floor(positions_sum/positions_length)
    optimal_fuel_cost = 0
    for pos in positions_list:
        optimal_fuel_cost += get_weighted_fuel_cost(pos, mean_pos)
    return optimal_fuel_cost

print(get_weighted_optimal_fuel_cost(hor_positions))