import numpy as np
# input=""".#.
# ..#
# ###"""

input="""..##.##.
#.#..###
##.#.#.#
#.#.##.#
###..#..
.#.#..##
#.##.###
#.#..##."""

##split each line into an array
parsed_input=input.splitlines()

##count number of rows and cols in the input
input_rows = len(parsed_input)
input_cols = len(parsed_input[0])

#each coordinate can only expand by a max of 2 units per cycle.
#calculate the max dimensions of the coordinate plane after n cycles (6 in this case)
cycles=6
max_row_units = input_rows+(cycles*2)
max_col_units = input_cols+(cycles*2)
max_z_units = 1+(cycles*2)+2

##create a numpy matrix to store the max 3d space
initial_state = np.zeros((max_z_units,max_row_units,max_col_units))

##Find the 'middle' layer of the matrix where the input values will be initialized
initial_layer = int((max_z_units+1)/2)

##Find the offsets needed so we can center the input grid in the middle layer
initial_row_offset = int((max_row_units-input_rows) / 2)
initial_col_offset = int((max_col_units-input_cols) / 2)

##Convert the textual cube representations to 0 for inactive, 1 for active
conversion_map={'.':0,'#':1}

# iterate through each entry of each line, converting the text to 0's or 1's and storing in the initial state
for i in range(len(parsed_input)):
    for j in range(len(parsed_input[i])):
        if parsed_input[i][j] in conversion_map.keys():
            initial_state[initial_layer,i+initial_row_offset,j+initial_col_offset]=conversion_map[parsed_input[i][j]]







#define a function to update the state of the system using the rules defined in the puzzle
def update_state(s1):
    #copy the input state into a new matrix
    s2 = s1.copy()

    #store the dimensions of the state to make referencing easier
    z_range = np.shape(s1)[0]
    rows = np.shape(s1)[1]
    cols = np.shape(s1)[2]

    #iterate over every element of the matrix
    for z in range(z_range):
        for i in range(rows):
            for j in range(cols):
                #store the current value of the element
                x_zij = s1[z,i,j]

                #define the indexes of two bounding points of the cube
                # up_left_back = [z+2 if z<z_range else z_range, i-1 if i>0 else 0, j-1 if j>0 else 0]
                # bottom_down_right = [z-1 if z>0 else 0, i+2 if i<rows else rows, j+2 if j<cols else cols]
                bottom_left_front = [z-1 if z>0 else 0, i-1 if i>0 else 0, j-1 if j>0 else 0]
                up_right_back = [z+2 if z<z_range else z_range, i+2 if i<rows else rows, j+2 if j<cols else cols]

                #Grab the slice of the matrix bounded by the corners above
                a = s1[bottom_left_front[0]:up_right_back[0],bottom_left_front[1]:up_right_back[1],bottom_left_front[2]:up_right_back[2]]

                #flatten the neighborhood matrix into a 1D array
                a_flat = np.reshape(a, a.size)

                #find the sum of the occupied seats (not including the current element)
                neighbor_sum = np.nansum(a_flat) - x_zij

                #apply the logic for whether to change the element state
                if x_zij==0 and neighbor_sum==3:
                    s2[z,i,j]=1
                elif x_zij==1 and neighbor_sum in (2,3):
                    pass
                elif x_zij==1:
                    s2[z,i,j]=0
                # elif x_zij==1 and not neighbor_sum in (2,3):
                #     s2[z,i,j]=0
                else:
                    pass
    
    #return the updated copy of the matrix as the new state
    return s2

#Current cycle counter
k=0

#Initialize the system with the cleaned input state
current_state=initial_state

# print(current_state[7])

#Perform iterations until the cycle counter hits the # of cycles
while k<cycles:
    # new_state=update_state(current_state)
    # if np.array_equal(current_state, new_state, equal_nan=True):
    #     print(f"solved in {k} iterations")
    #     print(new_state)
    #     new_state_flat = np.reshape(new_state,new_state.size)
    #     print(np.nansum(new_state_flat))
    #     done=True
    # else:
    #     current_state=new_state
    #     k+=1
    current_state = update_state(current_state)
    #print(current_state[8])
    k+=1


final_state_flat = np.reshape(current_state,current_state.size)
print(current_state.shape)
print(len(final_state_flat))
print(np.nansum(current_state))
