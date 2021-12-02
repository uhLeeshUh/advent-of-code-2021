file = open("day_2_input", "r")
text = file.read()
dirs = [ line.split(" ") for line in text.split("\n") ]
# dirs is a list of lists[2, str] where arg 1 is action and 2 is amount

def get_position(dirs_list) -> int:
    # keep track of horizontal and depth positions
    # iterate over outer list and update relevant position
    # return product of horizontal and depth
    horizontal_position = 0
    depth_position = 0
    for dir_pair in dirs_list:
        action = dir_pair[0]
        amount = int(dir_pair[1])
        if action == 'forward':
            horizontal_position += amount
        elif action == 'down':
            depth_position += amount
        else:
            depth_position -= amount
    
    return horizontal_position * depth_position

print(get_position(dirs))

def get_position_with_aim(dirs_list) -> int:
    # now include "aim", which also starts at 0
    # now "down" and "up" increase and decrease "aim" respectively
    # forward increases horizonal_position by X and increases depth by aim * X
    horizontal_position = 0
    depth_position = 0
    aim = 0
    for dir_pair in dirs_list:
        action = dir_pair[0]
        amount = int(dir_pair[1])
        if action == "down":
            aim += amount
        elif action == "up":
            aim -= amount
        else:
            horizontal_position += amount
            depth_position += (amount * aim)
    return horizontal_position * depth_position

print(get_position_with_aim(dirs))
