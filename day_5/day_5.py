file = open("day_5_input", "r")
text = file.read()
coor_pairs = []
for line in text.split("\n"):
    str_pairs = line.split(" -> ")
    coor_pair = []
    for pair in str_pairs:
        str_pair = pair.split(",")
        coor_pair.append(str_pair)
    coor_pairs.append(coor_pair)
file.close()

def upsert_coordinate_count_dict(x_coor, y_coor, coordinate_count_dict):
    dict_tuple_key = (x_coor, y_coor)
    coordinate_count_dict[dict_tuple_key] = coordinate_count_dict[dict_tuple_key] + 1 if coordinate_count_dict.get(dict_tuple_key) else 1


def get_coor_range(first_val, second_val):
    return range(first_val, second_val + 1) if second_val > first_val else range(first_val, second_val - 1, -1)


def get_intersecting_vent_count(coordinates) -> int:
    coordinate_count_dict = {}
    for coor_pair in coordinates:
        pair_start = [int(coor_pair[0][0]), int(coor_pair[0][1])]
        pair_end = [int(coor_pair[1][0]), int(coor_pair[1][1])]
        # determine if is horizontal, vertical or neither
        if coor_pair[0][0] == coor_pair[1][0]:
            # vertical
            shared_x_coor = pair_start[0]
            for y_coor in get_coor_range(pair_start[1], pair_end[1]):
                upsert_coordinate_count_dict(shared_x_coor, y_coor, coordinate_count_dict)
        elif coor_pair[0][1] == coor_pair[1][1]:   
            # horizontal
            shared_y_coor = pair_start[1]
            for x_coor in get_coor_range(pair_start[0], pair_end[0]):
                upsert_coordinate_count_dict(x_coor, shared_y_coor, coordinate_count_dict)
        else:
            # neither
            pass
    
    return sum(1 for val in coordinate_count_dict.values() if val > 1)


print(get_intersecting_vent_count(coor_pairs))


def get_full_intersecting_vent_count(coordinates) -> int:
    coordinate_count_dict = {}
    for coor_pair in coordinates:
        pair_start = [int(coor_pair[0][0]), int(coor_pair[0][1])]
        pair_end = [int(coor_pair[1][0]), int(coor_pair[1][1])]
        if coor_pair[0][0] == coor_pair[1][0]:
            # vertical
            shared_x_coor = pair_start[0]
            for y_coor in get_coor_range(pair_start[1], pair_end[1]):
                upsert_coordinate_count_dict(shared_x_coor, y_coor, coordinate_count_dict)
        elif coor_pair[0][1] == coor_pair[1][1]:   
            # horizontal
            shared_y_coor = pair_start[1]
            for x_coor in get_coor_range(pair_start[0], pair_end[0]):
                upsert_coordinate_count_dict(x_coor, shared_y_coor, coordinate_count_dict)
        else:
            # diagonal
            x_range = get_coor_range(pair_start[0], pair_end[0])
            y_range = get_coor_range(pair_start[1], pair_end[1])
            for i in range(0, len(x_range)):
                x_coor = x_range[i]
                y_coor = y_range[i]
                upsert_coordinate_count_dict(x_coor, y_coor, coordinate_count_dict)

    return sum(1 for val in coordinate_count_dict.values() if val > 1)  

print(get_full_intersecting_vent_count(coor_pairs))