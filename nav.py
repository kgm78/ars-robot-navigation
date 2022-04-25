goal_height = 182.88
goal_width = 213.36

max_height = 213.36
max_width = 213.36

current_height = 0
current_width = 0

cspace = 7.62
distance = 0

single_rotation = 20.066
def turnRight():
    #todo
    print('right')
def turnLeft():
    #todo
    print('left')
def moveForward():
    print('forward')
    

#move up
while distance != -1 and current_height < goal_height:
    distance = input('Enter distance: ')
    distance = float(distance)
    if distance <= cspace:
        while distance <= cspace:
            turnRight()
    else:
        current_height = current_height + single_rotation
        print('Move forward')
    print(current_height)

print('Goal height reached')
turnLeft()
distance = 0
#move left
while distance != -1 and current_width < goal_width:
    distance = input('Enter distance: ')
    distance = float(distance)
    if distance <= cspace:
        while distance <= cspace:
            turnRight()
            distance = 10
            current_width = current_width + distance
    else:
        print('Move forward')

print('goal reached')
exit()