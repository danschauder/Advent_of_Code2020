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

##count number of rows and columns in the input
input_rows = len(parsed_input)
input_cols = len(parsed_input[0])

#each coordinate can only expand by a max of 2 units per cycle.
#calculate the max dimensions of the coordinate space after n cycles (6 in this case)
cycles=6
max_row_units = input_rows+(cycles*2)
max_col_units = input_cols+(cycles*2)
max_z_units = 1+(cycles*2)+6
max_w_units = 1+(cycles*2)+6

##create a numpy matrix to store the max 4D space
initial_state = np.zeros((max_z_units,max_w_units,max_row_units,max_col_units))

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
            initial_state[initial_layer,initial_layer,i+initial_row_offset,j+initial_col_offset]=conversion_map[parsed_input[i][j]]

#define a function to update the state of the system using the rules defined in the puzzle
def update_state(s1):
    #copy the input state into a new matrix
    s2 = s1.copy()

    #store the dimensions of the state to make referencing easier
    z_range = np.shape(s1)[0]
    w_range = np.shape(s1)[1]
    rows = np.shape(s1)[2]
    cols = np.shape(s1)[3]

    #iterate over every element of the matrix
    for z in range(z_range):
        for w in range(w_range):
            for i in range(rows):
                for j in range(cols):
                    #get the current value of the element
                    x_zwij = s1[z,w,i,j]

                    #define the indexes of two bounding points of the neighborhood hypercube
                    bottom_left_front = [z-1 if z>0 else 0, w-1 if 2>0 else 0, i-1 if i>0 else 0, j-1 if j>0 else 0]
                    up_right_back = [z+2 if z<z_range else z_range, w+2 if w<w_range else w_range, i+2 if i<rows else rows, j+2 if j<cols else cols]

                    #Grab the slice of the matrix bounded by the corners above
                    a = s1[bottom_left_front[0]:up_right_back[0],bottom_left_front[1]:up_right_back[1],bottom_left_front[2]:up_right_back[2],bottom_left_front[3]:up_right_back[3]]

                    #flatten the neighborhood matrix into a 1D array
                    a_flat = np.reshape(a, a.size)

                    #find the sum of the activated states in the neighborhood (not including the current element)
                    neighbor_sum = np.nansum(a_flat) - x_zwij

                    #apply the logic for whether to change the element state
                    if x_zwij==0 and neighbor_sum==3:
                        s2[z,w,i,j]=1
                    elif x_zwij==1 and not neighbor_sum in (2,3):
                        s2[z,w,i,j]=0
                    else:
                        pass
    
    #return the updated copy of the matrix as the new state
    return s2

#Current cycle counter
k=0

#Initialize the system with the cleaned input state
current_state=initial_state


#Perform iterations until the cycle counter hits the # of cycles
while k<cycles:
    current_state = update_state(current_state)
    k+=1

#flatten out the final state and print the answer (sum of the activated states)
final_state_flat = np.reshape(current_state,current_state.size)
print(np.nansum(current_state))
