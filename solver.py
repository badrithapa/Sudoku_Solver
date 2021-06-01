board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

#print the initial board
def print_board(bo):
    for i in range(len(bo)):
        if i%3 ==0:
            print("- - - - - - - - - - - - -")
            
        for j in range(len(bo[0])):
            if j%3 == 0:
                print("| ", end="")
                
            if j==8:
                print(f'{bo[i][j]} |')
                
            else:
                print(f"{bo[i][j]} ", end="")
                
    print("- - - - - - - - - - - - -")
    
    
#check if our guess is valid compared to surroundings i.e rows and columsn and box
def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        
        if bo[pos[0]][i] == num and pos[1] != i:
            return False 
        
    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]]==num and pos[0]!=i:
            
            return False
        
    #check box
    boxX=pos[1]//3
    boxY=pos[0]//3
      
    for i in range(boxY*3, boxY*3 + 3):
        for j in range(boxX*3,boxX*3 + 3):
            
            if bo[i][j]==num and (i,j)!=pos:
                return False
    return True

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    
    else:
        row, col = find
        
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            
            #using recursion
            if solve(bo):
                return True
            
            #if above returns false we backtrack by setting previous value to 0 as below
            bo[row][col]=0
            
    return False


#we will find the empty spot for our next guess
def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j) #row, column
    return None

print_board(board)
print('#############################')
solve(board)
print_board(board)
input('press any key to exit')
