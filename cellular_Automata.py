import time,os
import curses
import random


def Rule():
    return True
def cell(n):
    cell =[]
    for i in range(n):
        cell.append([])
        for j in range(n):
            if (i%3==2 or j%3==1):
                cell[i].append("*")
            else:
                cell[i].append(" ")
    print(cell)
    time.sleep(0.5)
    return cell

def cell_out(cell):
    n = len(cell)
    cell_out = []
    for k in range(n):
        prin_out = ""
        for i in range(n):
            prin_out += cell[k][i]
        cell_out.append(prin_out)
    return cell_out

def alive(cell,x,y):
    count = 0
    n = len(cell)
    for i in range(-1,2):
        for j in range(-1,2):
            x1 = x+i
            y1 = y+j
            if x1<0 or y1<0 or x1>n-1 or y1>n-1 or (i == j and i==0):
                continue
            elif cell[x1][y1]=="*":
                count += 1
#    print(count)
    if cell[x][y]=="*":
        if count<2:
            return False
        elif count==2 or count<=3:
            return True
        elif count>3:
            return False
    elif count==3:
        return True

def evolve(cell):
    n = len(cell)
    for i in range(n):
        for j in range(n):
            if(alive(cell,i,j)):
                cell[i][j] ="*"
            else:
                cell[i][j] =" "
    return cell
    

n = int(input("size"))
cell1 = cell(n)
cell_o = cell_out(cell1)

while(True):
    os.system('clear')
    celln = evolve(cell1) 
    cell_o = cell_out(celln)
    for i in range(n):
        print(cell_o[i])
    time.sleep(0.1)
