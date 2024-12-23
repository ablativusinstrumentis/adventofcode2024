## enter: the worst code of my life, with my original annotations

maze = [[j for j in i[:-1]] for i in open("input2.txt","r").readlines()]
d = {1: [-1,0], 2: [0,1], 3: [1,0], 0: [0,-1]} ## urdl (y,x)
placesbeento = [] ## (Y,X,direction)

## ELI. THE MAZE. IS IN THE FORM [y][x]
## BECAUSE FIRST DOWN THEN RIGHT
## PLEASE REMEMBER THIS YOU IDIOT
## new comment prettyprint was for debugging and im NOT removing it
def prettyprint(arr):
    for i in arr:
        print(i)
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][j]=="^":
            guy = [i,j,1] ## ELI. THIS IS Y,X
            placesbeento.append((i,j,1))

count = 0
allgood = True
while allgood:
    if maze[guy[0]][guy[1]] != "X":
        count+=1
        maze[guy[0]][guy[1]] = "X"
    if (guy[0]+d[guy[2]][0],guy[1]+d[guy[2]][1],guy[2]) not in placesbeento:
        placesbeento.append((guy[0],guy[1],guy[2]))
        guy[0] = guy[0]+d[guy[2]][0]
        guy[1] = guy[1]+d[guy[2]][1]
    if (guy[0]+d[guy[2]][0] not in range(len(maze))) or (guy[1]+d[guy[2]][1] not in range(len(maze[0]))):
        allgood = False
        break
    if maze[guy[0]+d[guy[2]][0]][guy[1]+d[guy[2]][1]]=="#":
        guy[2] = (guy[2]+1)%4
print(count+1)
