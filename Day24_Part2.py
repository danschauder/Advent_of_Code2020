import re, math
# txt = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew"""

txt = """nenwneswnwnwneswnenwnwsewenwsesw
swsesenwswswseseswseswneswseswsweswnese
neeswsesweneseeenwnenwnewneseewee
wseeeneseneneeeneneenweneewese
wwwwsewewsewnwwswwenewwwnww
seseneeseeswsenwswsewsewseseseneee
enesenesweseeswswswnwwnwne
swwwsenwwnwnwnwenwnenwnwsewsewwne
wnewwseeeswneneneneenweeesw
swwwswnwnwewwseswwesww
nwneswswswnweswweneeeneewwswswswne
senwseswsewseseseesesenwesesenweseesw
senesewneenwnwwesewnwesesesenewne
swwnwnwwwnwnwwewwnenwnwswsenwwnenw
swnwneseewnwnwnenwenewnwnw
swesesweswseswswnwnwsewnwseswseeswsw
nwnwnwsenwnwnwnwnwsenwwenwnwsewnwwneswnw
wwwewnwnwswwwneseeeswnwnww
swswswswseswneswseseneneswneseswswnewsw
swneseswswseseseswswswseswswse
wnewwwswnwnwwwwnwwsenww
senwsenewseneswwnene
nwseeswsesenesenwseseseseswsesenwseseswsw
wwswwswsewnewewwwwwwwwwnenesw
wwnwewenewweswnewswse
swwsenwwnwwwnwwseenwnwwnwnwnwenww
wwnenewswwewwswwwwsewwnwww
swenwnweseeseeeewe
nwewseeeesesese
nwsewesweesenwnwswseesewewswswse
wewsewwswwwnwewwwswnewwww
swswwneswwswswwwswenesene
seseseswswseswseswwseswswnesesw
newnwwwnwwwsewwnw
eswseenwseeeeeeswsenwneeeeee
swswsweswneenwneweneneneeeneesesw
swnwswesweneswswneseswswwswnw
eeeweeeesweneweneeeeeese
esesesesewnwswseswnesesesenweseseseew
nenwsenwnwnwsenenenenenwnewnenwnenesese
neenwneneneenwneneswnenwewneneeswswnenw
swseeswswswswenwswswswnwswswswsesw
nwnwswnwwenwnweneenwswnwsenwswnwsese
wenwweswseswswswswswwnwswswneenww
wswesenenwnwwenwwnwswnwnwnwnw
wnwnwnwsenwnwwnwnwnwwnwnw
ewesweeeeenenenwneswswseeeweee
nwenweeeeweeseeenwsweseeesese
senewneneneneswnenwseenwsenesewnwnenwse
senwseewewseenwseseseseswese
eeeeneswsenweeee
ewnenwnweswnwwswswnwnwnenesesewese
newnwswwnwenwwnwnwswwswnwwwwenw
nwseewwnenwnwnwnwnwnwnwsenwnwnwwenwnw
ewnenenwnenenenenwesewswwnwnenenee
seseswsesesenesewsesesenwseseewnwsese
nwswseseseeseneswnwwseeeesenweswwe
enwnwnesenwnenwnwnenenwwnenwsenwnwsenw
wewnweseeswneenenwseeeeeseee
sesesesesewseswseseseesesese
neeeeeneeswneseenwnenenwneswenwe
sewswswesweswsewseseswnwneeswnwenw
wnenenewswseneeenewseeenw
neswnwnenwwewnwnwnwnwnwseweswnwese
swnwswsewswswnenwnewsewwwwneseswse
wwswsweswwswswswswswswsw
esenewneneseweeenenew
nwswewnwsenwnwenwnwwsewwnesenwnwse
wenwweeseseswewenenweeeesew
sesenwswnwnwnenenwnwnewnesenewnenenenww
sesenesweswwesenwswnw
nwsenwswnenwnwnwsenewneswsenwwsenwnwnwne
nenenwswnwnwnenenwnwnwnwnwsenwneewnesw
nwneneeseeswsenwesewseswwseswwnesene
nwnwnwseneenwnwnwnwneswswnwsweenwnwnww
swnenesewnwseneswnwswseeseswseeenese
newneneneneneeswne
nenwnenwnewnenenenenwneswsesenwnenwnene
swwnwnwewnwnenwnwnwnw
wseenwswsenenewnwswswnwnenwnwswenwsenw
enenewnewnwnwneeneneseswswnwseneew
neneeneeneneswnenewnenwe
senewnwswsenwnenwsenwsewnwwneenwnwsw
nenwneeneeeneneeese
neswswswesewwswwswswsenesewswneswnew
wwsewwnwwwwwwnwnw
neneeeeeeeneswnewneneeseneneew
swswswswwwswswwnesw
seeneneewweenese
eswnwsweswswwnwseswswswneswseeswswne
wwnwswwwnenwnwwnww
nwseeswnwneeseswseseweseneesweseee
eseseseseeseeseseseenwsese
swesenwswseswswsewsesenesese
enesewnwswswnenenenenwneneneswsenwnenw
wnwwsesewwnewswwwwnwnwwwenwe
eswswswseswwnwnwswsweseswenwsw
enwswseswwwswnwswneswswwwseswswswsw
wsenwswswswswsweeneswwwwswwsw
esenwewwwwwwwwwwewwwww
neneneseenwsenwsenwswwwseenewnenesese
nwweswwsenwnwesweweswnwwenwenww
eseswsesesesenesesesesewewsenwnww
newesenwnenenenenwneneneswnesenenenewne
ewnwswnenwnwsenwsenwsenenwnesenwneswnwne
nwwswnwsewnenesesweenwnwnwewnenwnw
swnweswswwswswswswswnwseswswswsw
eewwswnewswewenwnwseneseenwsenwe
nenwswnwenwnenesewnenwseneswseswnwnenene
neneswnwwnwewsewenwsesw
senwseseseseseseswsenwsesesesesesesenesenw
enewsewwnwnwseswnenwswnwwnwwnenwnw
wswwwwswswnweswswwswwwwwwenwe
swswneswseseseseswswsw
wwswsenewwwwwswwswneww
wseeeewneseese
nesewwseseseswseseesw
nwenwnwswnwnwswenwswnwenwnwsenwnenenwnwnw
seswswswseswseneswseswswswneneseenesenwse
wswswwswwswswsweswnwswsweswenwewsw
sewsenwsewseneeswseeswse
eewweewneeneeeseneweeswnene
weeeenwesenweeseseewnewsenwse
nenenewneswneswneneneeneneneeeseneswe
wnwneneseenwewseswswswswneswwswnene
nweeswwwseseeseweswswnwsenwswswse
eneweenenwseweesenww
swnenewnweneseewnenwnesenenwenwnenwnesw
seseswseseswesenesesewswsesw
neeseweneeesewseeeneenwweeseee
newseneswnenwnwnesenenwnwnwenwwnwnwnw
enwnwenwnwwnwnwnwnwnenwnenwswswneese
ewwwwswwwswswwswnewswnew
sesesesenwseseseseseesese
nwnwwsewnwnwnenwwenwswseseenwnwswne
wswneneswswseswseswewwsesesweseneswnwnw
wnwsewwwwnwswwwwwwwenwew
nwnwnwnwnwnenwnwnwsww
wswswswnwswwswnwsenwseneswsweswswseswsw
nesenwneseswseswwnwneseswsesesenwswesese
nwnwnenewsenwneseenwnenwnwnwneseneswnwswne
nenesesenenenwnwswneeewnenenw
swnwswseswswwnwwwwswswnenewsewswswese
swenenwnwnwnenenwswnenwnenesweenenwnw
eeswenewenwneswneneeneenenenee
swswsweswswneswswswnenwswsweswnwsenwne
eeeesesewesenwesw
wwswswseneswsesenwseseneseeswseenwnwsw
swwwwewswwesw
wswwswwnewwseswswswswewswnwwnesw
eswsenwseswneewenweeewwwneene
wwewweswswwwswwewswwnwwwnw
swwneeenwnenwnwwswnenwnwnwweenwne
eneseneneswneneeneseneenweweswwnw
nwesesesesweeseneseesesesesesenwsenw
wwwwwwwwneswwseswwnesewwswesw
wnwesenwnwsenwwwnwwnwnwwwnewswwnw
eneewneeeneneneneneeenewese
sesesenesewsesesesesesenwsesesesenw
seswsenenwwsewseneneseeseswswswsesesese
swnenwswnwnewnwswswwnweewsesesewwne
ewneswswneswnwnwwsewneneseswseswsesee
wswswwswwnewwswwswswwewswsewe
swwnwnenenesewnenwwnwneneeweeswsene
eseswseseeseeeeneeswneneneweswee
eseseseenenesesesesewneseseseseseww
enesenenenwneneneneenenene
wswwswwwnewnwwsenewnwwnewseew
nenenenwneneeenwnwwswswnenenwenwnesw
nenenwnewswneneneneseneenenenenenesene
nenenwnwnwnwsenwnwnwnw
swwnweenwneneneeswnenenenenewswsenenenw
eswnenwswswnwwewneseesweseneenww
nenenenenwwnenwneneenenenw
sesewswneswswswseswneswswsenwswseswswse
esesweeeeneneesweeeenwwnwneee
wwwwnwwnwwsenenwwwwwnwwswseew
nweseneswnenenenenenenwnenwnenwne
wnwnwsenenewnwsewsenenenwewsenwwee
wnwseswsesesweesesenwseswswse
nwnenwwnwwneneneeswseneneeswnwnesene
neswsesesesewsesesenwswseesesesesewnesese
nwwwswwwewwww
swsweseseseseneswnwnesewseseswseseswsw
esesenwseseswwseseesenwnenesesesewsew
eseswswnwswnwsesewesesweswsw
wwwnwwwenwsenwnwnwwnw
wnwnwnwnwnwnwwnwnwnwnwnenweesenwwswnwsw
swswsesweenwnwwnene
swswswwneneneswwsesenwwswnwnwwwsee
nenwsenwenwenwsenenwnwnwnwneswnenwnww
swewwnenweswnwswwnwnwwwnwnwwwww
newneneenenenenenenenenee
swewnwswswneeswseseswnesenwenwwswsesw
wnewwswenwwwwswnwwwnewnwnwsww
nesenwswsweneseswneesesewswnenwsesesese
sewswswswwwnewswswwnwwnewwwswwsee
seeeewswneseewsesenenweseesesese
nenwneswnenenwnwnwwnwenwenenenwnwnwsw
enenwsenwwnwneswseseseenewseswsenww
newswswwswwswswwswnwwwswswneesesw
nwswswnwnwswseswswwneseenwwswe
nwwwswseneneneneneenwneneneneneenenene
senwsenwwwwwsewwwwneswnenwwww
swswwswsenwswseesesewnenenenewswsweswnw
swweneenwwsenwneneeneseneeene
nwnwnenwswenwnwwnwewnwnwsenwnenwnewnwe
eenenwneswnenenese
senwnwneseseeewswsesewsewenesesese
neswwwewwnenwwswwseswnw
wseeeneswseseeseseseseneneseseswsese
senenewesenwesenwswwwswnwsesenwenw
nweneneeeseeeeeseenwweeeswne
wswswseseswswswwnwnenwsweswswswswwsw
nenwswnwenwneswseesenenenewneee
nwnwnwnwnwnwenwswnwnwnwwnw
seseseseseneswseseseswswsw
eswswnewwswsenweswwwnwswswesenww
nenenenwwnwneenenesesenenewne
neeeswneswnweeeeeneneeswneenenew
weswswenwseswswswswsenwswsw
nwnwnwnwnwwenewwneewseseswnww
nwwsenwwswswneeneswswswsesweswswnesenee
wswwneswswswweseswnewnewnenesesesenenw
sweseseswswswsewsw
eeenewseneeweseenenewneseeneenee
seseenwnwseseseeseseeeneweseseseew
wwewnwnwwwsweew
sewnwnenwnwesenwwnenwnwwnwneswwwsew
wswwwswwsenwnwwwneswewswenwswswwsw
nwnenenenenewenenenenenwnene
sewnesewsewsewnenwwwwnewnwnwww
nwsewneeswwsewneswnwweenwnenw
eseeseseneseseweesesenwsesese
eneenenewenwswnwseswsenweeeeee
sesenwweesesesesesesenesewsesesesese
eneenwneeeewseenewewnweswseswe
swwswswswswswweswnweswswswswsesweswswnw
eewseeeenweeeenweswseseesee
nwnwneeswnwnwwnwwswswneswswnwnwenwswene
eenwnwswesenwsweswsesenweseenwee
wwnwwwewwnwwnenwwwsw
swnwnwneswenwenenenewenwswseswewse
nenwnwnenwnwnwnwnwswnwnwnwnw
nweswneeeswnweswswenwsweswneeenenwne
nwnenwneesewnewnwesenwnwnenwnewnwnwnww
ewwwwswswwenwwswswswwsesw
nwesewnenwesewseswnenweswseewseseee
nwswwsweswswseswwswswswnwswnwswswwe
wenwseewseeseneeseswswseseenwsene
seswswsesesesesesesenw
enenewenenenwnenwnenenwnenwswseswne
swwwsesewwwnwsewwsewnenwnwwwwww
wsenwwnenwnwsenwseseseseswseswneenesese
sweeeenwsenwnesenenwswswewwnwesww
swseswswswswsenwswswsw
nwswnwswnwnenwnwnwenwnwnwnenwnewnwnwnwsew
weeeeseweseweneenwsweeseenew
nwswswseswswswseswswswsw
eswsenwswsesenwswneneeenwneseswwswse
seseseseeseseseeenewsesese
swnenesweweenwneeeneneseeeeee
wwwwnwwwsewwnesewwnewse
neeenenwnenwswswnwseneeeeesweee
neenenenenenenwenewnenwswneswenwnene
wseeenesesenwneesenweeseswswswswse
esenwweswwewnenwewseenwsenwsee
newneeseeseeswewseeesesenweeesee
esewnwsenenewswnwwwsenwseswnwewnww
neneneeneenwewweneswseneneneneese
neewswnwweseswneesweswnwenwenenw
wwnwwnwwwwwwwsewewww
seseseneseswsesewseswseseswnwsee
esweeswseweseseeeenwswenwneene
sesenwwseseneseswswnwswsewseseseseseene
eeesenwsweeenwneeswswneesenewne
nenwnwnenenwnenenwwewewnwesenwswnw
nwnwnwwnwseenwenwnwnenwnwnwwnwnwwne
wneseeeenenewnwnwwneneesweswnene
wwnwwwnwsenwwewwnwsenwnwwwnew
nwnwnwnwnwwnwnwwswsesenewenwnwnwnwww
eswwsewnwwsewwnwwwwewwwenwsw
nesweswnewswnwswswewwnwsenwsenwwnwse
nwnwwwnwwweweswsenwwsewwneeww
neeenwswswnwswsweneneenwneeeneeneee
nwnwnesenwsewnwnenenwsewnwnee
eeenwesenwsesenweesweseseeswesee
eewwwwswwswswwswnewwnwnwesww
sewnenesenwnwswswnenwseneswwnenwnenwesw
ewswnwnwnwenwnwnwnwnwwswnwwenwenw
nwnwnwnwsenwnwnwnwnwnwnwnwwnw
newwwswswswswseswswswswswesw
swswswwwswwesenwswwneswswswwswsw
neeeenenweeeneneesw
seesesenwenwsewseenwsewswnweneew
swnesenesenesewsweneeswnwsesenwwese
eswnwswwswsenesenew
swneswwenwnenwsenenewwswesenenenenw
wwwwwwwwnwswneeseswneesesw
sesenwnwwnwwnesenwnwnwwnwswenwnwwene
swswswwsesweseswswwswnwswswsesesenee
nwnwswwnenenwnwwnwwnweswnwsenwnwnwnwnw"""

tiles = txt.splitlines()

reg1 = re.compile(r"""
                ([se|sw|nw|ne|e|w])
                """,re.VERBOSE)


parsed_tiles=[]
for tile in tiles:
    raw_tile= re.findall(reg1,tile)
    parsed_tile=[raw_tile.pop(0)]
    for i in range(len(raw_tile)):
        next_letter = raw_tile.pop(0)
        previous_letter = parsed_tile[-1]
        if previous_letter + next_letter in ('se','sw','nw','ne'):
            parsed_tile[-1] = parsed_tile[-1] + next_letter
        else:
            parsed_tile.append(next_letter)
    parsed_tiles.append(parsed_tile)


black_tiles = set()

for tile in parsed_tiles:
    # print(tile)
    pos=[0,0]
    for step in tile:
        # print(pos)
        if step == 'e':
            pos[0]+=2
        elif step== 'se':
            pos[0]+=1
            pos[1]-=1.73
        elif step=='sw':
            pos[0]-=1
            pos[1]-=1.73
        elif step=='w':
            pos[0]-=2
        elif step=='nw':
            pos[0]-=1
            pos[1]+=1.73
        else:
            pos[0]+=1
            pos[1]+=1.73
    pos_tup = tuple([round(a,2) for a in pos])
    # print(pos_tup)
    if pos_tup in black_tiles:
        black_tiles.remove(pos_tup)
    else:
        black_tiles.add(pos_tup)
    
# print(sorted(black_tiles,key=lambda x: x[0]))
# print(len(black_tiles))

x_min=-500
x_max=500
y_min=-500
y_max=500

white_tiles = set()

for x in range(x_min,x_max,2):
    for y in range(y_min,y_max,2):
        t = tuple([x,round(y*1.73,2)])
        if t not in black_tiles:
            white_tiles.add(t)

for x in range(x_min+1,x_max,2):
    for y in range(y_min+1,y_max,2):
        t = tuple([x,round(y*1.73,2)])
        if t not in black_tiles:
            white_tiles.add(t)

print(f'starting with {len(black_tiles)} black tiles')
print(f'starting with {len(white_tiles)} white tiles')

def count_black_neighbor_tiles(t):
    neighbors = set()
    origin = list(t)
    e = tuple([origin[0]+2,origin[1]])
    se = tuple([origin[0]+1,round(origin[1]-1.73,2)])
    sw = tuple([origin[0]-1,round(origin[1]-1.73,2)])
    w = tuple([origin[0]-2,origin[1]])
    nw = tuple([origin[0]-1,round(origin[1]+1.73,2)])
    ne = tuple([origin[0]+1,round(origin[1]+1.73,2)])
    neighbors.add(e)
    neighbors.add(se)
    neighbors.add(sw)
    neighbors.add(w)
    neighbors.add(nw)
    neighbors.add(ne)
    cbnt=0
    for n in neighbors:
        if n in black_tiles:
            cbnt+=1
    return cbnt

day=1
day_max=100
while day<=day_max:
    flip_white = set()
    flip_black = set()
    for t in black_tiles:
        bnt = count_black_neighbor_tiles(t)
        if bnt==0 or bnt>2:
            flip_white.add(t)
    for t in white_tiles:
        bnt = count_black_neighbor_tiles(t)
        if bnt==2:
            flip_black.add(t)
    for t in flip_white:
        black_tiles.remove(t)
        white_tiles.add(t)
    for t in flip_black:
        white_tiles.remove(t)
        black_tiles.add(t)
    print(f'Day {day}: {len(black_tiles)} black tiles and {len(white_tiles)} white tiles')
    day+=1

