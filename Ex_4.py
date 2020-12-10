import math
input = ['.#..............##....#.#.####.',
'##..........#.....##...........',
'.......#....##...........#.#...',
'.........#.#...#..........#....',
'.........#..#................##',
'..#...#..#..#...........#......',
'...................#...##..##..',
'........#.....##...#.#.#...#...',
'#..#.##......#.#..#..........#.',
'......#.#...#.#...#........##.#',
'.....#.####........#...........',
'...###..#............#.........',
'.....#.......##......#...#.....',
'#......##......................',
'......#..............#.........',
'..##...#....###.##.............',
'#...#..........#.#.........#...',
'...........#........#...#......',
'.....##.........#......#..#....',
'#..............#....#.....#....',
'.#......#....#...#............#',
'.####..........##..#.#.........',
'....#...#......................',
'....................#....#.#...',
'..........###.#...............#',
'.#...........#...##............',
'.#.#..#.....#...#....#.......#.',
'.##........#..#....#...........',
'.........#.....#......###......',
'..............#..#.......#.....',
'........#..#.#...........#..#..',
'#.........#......#.....##.#.#..',
'........#.#.#....#.............',
'........#........#.#.##........',
'#......#.#..........#..#.......',
'..#....#...##......###..#..#...',
'............#..#.#.........#...',
'....#.#...........#..........##',
'.......#.#.#..#......#...#.....',
'..#.........##.#.........#...#.',
'......#....#.#....#........#.#.',
'.#....###....#..............#..',
'.#....#.......#....#..#.....#..',
'.....#.....#...................',
'..#.....#......#......#........',
'......##.##...#...#...#...#.##.',
'##...#....#...#..#...#...#.....',
'..#.....#...#...##.##...#......',
'.....#.............##...#......',
'.....................#.##..#...',
'#...#....#....#........#.....#.',
'..#...#.........#...#..#.....#.',
'#.#......#...................#.',
'..#...........##...............',
'..#....#........#..#...........',
'...........#...................',
'.............###......#....#...',
'...........#...#....#..#....#..',
'.....##............#.#.......#.',
'.....#..#....#...#....#........',
'...............##........#.#...',
'.........#...#.#....#.......#..',
'#..#.......#.......#...#.......',
'..#...........................#',
'......#.......#..#......#......',
'.#.......#..................##.',
'..#.........#..#.##.#....#...##',
'...#..#....#...#....#.#........',
'.#...#........##..#..#.......#.',
'.....#........#....#....#..#...',
'............#...........#......',
'..###.......#..#....#......#...',
'.....#...#.......#..#..........',
'..#........##.#....##..........',
'#....#.............#..##......#',
'....#.................##.......',
'...#.......#........#....##.#.#',
'##..##..#.....#.....#..........',
'...#...............#....#..#...',
'.#...##....#....#.....#....##..',
'...#.....#......#......#.......',
'#.....#.......##.....#..#....##',
'.....#.#...##.#......##....#.#.',
'..........#....#.#...#.........',
'.#..##...#.....................',
'...........##..#...#....#......',
'...#......#........#.......#...',
'.#......#..#........#.....#..#.',
'.......#........##..#.##....#..',
'.##..........#..#...#.....#....',
'.....##...............#.#......',
'..##.....#..#......#..##.#.#...',
'....#......#.##...........#....',
'#.#..#.......#......#.#........',
'...#.#..#....#............#..#.',
'...#..........###....#....#...#',
'........##...#.......#..#....#.',
'..#...#.....#..#........##.....',
'...#..#.##.#.#.##..............',
'.......#...#.........#.....#..#',
'..#.....#.#..........#..#......',
'......#..........#......#.....#',
'.#...........#........#......##',
'..##............#......#...#..#',
'#..................#...........',
'#....#..#.........#........#..#',
'..#.#....###..#...#...##...##..',
'...#....#..#.....#.............',
'.#........##.##...#....#...#...',
'.........#.......##.#.....##...',
'#.#.....##...#........#...#...#',
'.....#.#.##...#.....#.##..#....',
'........#...##...#...#.#..#..#.',
'.##....#.##...#.......#........',
'...#..#................#..#....',
'....#.......#......#...#.##....',
'#......###..#...#......#.......',
'..#...#...##...........##......',
'.......#...#..##....##......#..',
'....#.#.............#.#...##..#',
'..........#........#...#......#',
'............#.#.#....###.......',
'#..#...#.#.####...#..#...#.....',
'.##.......#.##...#.............',
'#..#...........#.#.##.......#..',
'...#..#.#...#...###..#.#..#.#..',
'..#...#.....#..#....#....#.....',
'.........##.......#............',
'.........##.##......###........',
'.............#.#....#..#.....#.',
'...#....#.#.......#......##....',
'............#..................',
'....##...#..........#...#..#...',
'#..#....#.....#.......#.##.#..#',
'.....#.........##.............#',
'#.....#.#...#............##..##',
'..............#....#.....#.....',
'.#....###..#.#.....###.#..#....',
'.....#....##...#....#......#...',
'..........#...#....#...........',
'............#....#..#.........#',
'..##.....#.#...#.......#...#...',
'...#...#..#......##...#.....##.',
'......#.##............##.#....#',
'....#......#...##.....#.....###',
'.#.###...............#...#.#...',
'..#....................##...#..',
'.......#.....##...........#....',
'#.........#....#....#....#....#',
'..#.#..##.#.#..................',
'.....#.......#................#',
'...........#.......#........#..',
'#...#.........#.#.....#.....#..',
'..........#..#...........#.....',
'#..#.##..##..#.#.##.........#..',
'#..#..#....##..#.........#.....',
'#.#.......................#.#..',
'.##......#.#...#......#....#...',
'..#.#................#..##.....',
'.......#..................#...#',
'.....#.........##.#....#.......',
'#..........#..#.#..........#..#',
'..#..#.....#.........#...#.....',
'..............#.....#..#...#.##',
'...............................',
'...#............##......#.....#',
'.......#..#.............#.#....',
'...........#..........#........',
'...#.####..#......#...#....#...',
'##......#.##.....#.............',
'....#.........#...#...........#',
'...#........#.......#.#..#.#.#.',
'..#.......#.........#....#.....',
'................#.#.#.##...#..#',
'#.##...#...#..#.....#.....#..#.',
'...............#...........#...',
'.....##.#...............##...#.',
'.#..##.##......................',
'.......#.........#..#..#.......',
'...#......#..................#.',
'...#.#..#....#....#............',
'...........#...#..#....##......',
'.....#...#..#.#....#....#....#.',
'.......#...#...#.#.#...........',
'....#......#......#...##..#....',
'##...#.#.....#..#.##...........',
'#.#..#.....#..#................',
'...#..#.#......#.#...........##',
'##....#...#.....###..#...#....#',
'...#.....#.#.#......##...#...#.',
'............#.......#..........',
'....#..........###.......#.....',
'.................##..##....#...',
'...........#........##..#......',
'...#.#...#.....#........#...#..',
'#...#.#......#.#...........#...',
'..#..........#....#..........#.',
'..#................#...........',
'#...#.#....#.#.......#.........',
'.#...........##..#....#....#..#',
'.##........#.....#...#..#....#.',
'......#......#...#.............',
'.......#..#...#.##....#..#.#...',
'.......#......#....#....#.#.#..',
'..........##.....#....##.#.....',
'.........##..#...#.....#..#....',
'...#....#..........#..#...#..#.',
'.......#.....##.#..#.....#...#.',
'#...#......#......#...#........',
'#..#....#.#......#......#......',
'.......#.##....................',
'...##...#.....#......##......#.',
'.#...................###.......',
'....#........###...#........#..',
'...#............#.....#..#.....',
'..................#......#....#',
'..##......#..##..##......#.#...',
'........##....##.......#...#...',
'.#.#....#.....#.....#....#....#',
'...##.#.............#....##....',
'.........#.....#...#......#....',
'..#.....#............#....##...',
'..##.....#.....##.##...........',
'#....#.#.......#..#......#.....',
'##.......#.....#.....####....#.',
'##...#.......#...#.....#.......',
'#.....#..##.##...##..#.....#..#',
'..........#......#..#.#........',
'..##.#......#..............#...',
'.#...#..........#.......#....#.',
'..#....##...#...........#....#.',
'..#.........#..#......#......#.',
'.##....#......#.#.........#..##',
'.......#...#....##............#',
'.##.................#.#........',
'...#.#...#..#..#.....#.#.......',
'.#.#.......#...................',
'..#..#.....#......#.....##..##.',
'.#........#.##......#..........',
'....##...#............#.#....#.',
'.......#.#..#....##.#....#....#',
'......####...#..#.....#........',
'..........#..#.........#.#..#.#',
'..........##.........#.##......',
'.##..#.#.....#.....#....#......',
'............#..#...............',
'.....##.........#...#...##...##',
'........#.##.#...#.....#....#.#',
'#......##.#.##..........##.....',
'#..#..#........#.........#..#..',
'...............#.#..##.........',
'.#.......##.#..#....#...#....##',
'.#..##.....##......#....#...#.#',
'........#...#.........#.....#.#',
'...........#............#...#..',
'................#...........#..',
'..............##........#....#.',
'..........#.....##.....#..#....',
'#......#....###..#..#..........',
'.....#.#.....##....#.#.......#.',
'...#...#...............#.#.....',
'.............#.......#.........',
'.....#.....#..#......#.....#...',
'.........#.................#.##',
'.#.....#.##..#.................',
'..#......#.......#.....#...#..#',
'..#..#.#.#...#.......#.##......',
'..........#..#.........#.......',
'.#..........#...#....#..#...##.',
'.#.#.#.###.....#...#.#.#.......',
'....##............#............',
'.#.#.............#..#......#.#.',
'.#.#..........##..#.....#..#.#.',
'...........#.##..#...#.#.....#.',
'...........#..#....#...........',
'..#................#.#...#....#',
'...............##........##....',
'....#.............#........#...',
'...#......#.#.#........#.......',
'#..............#..##.#..##.....',
'.#.#.###................##.....',
'.............#..#.........#....',
'.......##..#............#...#..',
'...#...#...........#.....#.....',
'........#......#.#.#......#..#.',
'#.##.......#......#..#..#.#....',
'...#........#...........#...#..',
'..#...........#.........#......',
'.............#....#....#.......',
'....#.........#........#......#',
'..#............##..#.........#.',
'.#...#...#..#...#........#..#..',
'...#....##..............#......',
'...........#...#....#.#.##..###',
'..#....#......#.........#..#...',
'.......#...#...................',
'.#...#.#...................#...',
'.#.....##.#.......#.#.#...##..#',
'.....#..#.#.........#...#..##..',
'.#..#.##.#......#......#.#...#.',
'......#..#....##..#....##....##',
'#...#......##........##........',
'.#.........###................#',
'.................#..###..#.#...',
'..#.#........#..#........#...#.',
'#.#....#....#..#...#.#......#..',
'.#.#.............###.........#.',
'.....#...............##...#...#',
'..............#...#........#..#',
'...................#..#.......#',
'#......................#.....#.',
'...#.........#..##...#...#.##..',
'.....#..........#.........#....',
'.....#...#............#..#.....',
'.............#............#....',
'...#.........#.................',
'#...........#.#...............#',
'.....#...#.....#..#.##.......##',
'...#....#.#...........#........',
'.........................#.#...',
'.#..#...........#.#........#...',
'.............#.#.....#..#....#.',
'.....#...#.###...#..#........#.',
]

height=len(input)
width = len(input[0])
chars_needed = height*3
reps_needed = math.ceil(chars_needed/width)
expanded_map = [a*reps_needed for a in input]
trees=0
for i in range(height-1):
    if expanded_map[i+1][(i+1)*3]=='#':
        trees+=1
    i+=1
print(trees)