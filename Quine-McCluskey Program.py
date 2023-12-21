# Quine Mc-Cluskey using 26 Variables
# Written using Python Language

# Creating the Minterms
def comb(x, y):  # Combine 2 minterms a function called "comb" that takes two lists x and y as input.
    res = []
    for i in x:
        if i + "'" in y or (len(i) == 2 and i[0] in y):
            return []
        else:
            res.append(i)
    for i in y:
        if i not in res:
            res.append(i)
    return res
# The function essentially performs some operations related to minterms in Boolean algebra.

def combine(x, y):  # Combine 2 expressions a function that takes two input parameters x and y. 
    res = []
    for i in x:
        for j in y:
            tmp = comb(i, j)
            res.append(tmp) if len(tmp) != 0 else None
    return res
#  It then iterates through each element in x and y using nested loops, and combtiplies each pair of elements using a function called comb.

def remove(my_list, dc_list):  # Removes don't care terms from a given list and returns removed list
    res = []
    for i in my_list: #my_list = list of minterms
        if int(i) not in dc_list: #dc_list = list of don't cares
            res.append(i)
    return res
# The function then iterates over each element i in the my_list using a for loop.

def searchEPI(x):  # Function to find essential prime implicants from prime implicants chart
# searchEPI is a function that takes a dictionary x as input where the keys represent the 
# prime implicants and the values represent the minterms covered by each prime implicant.
    res = []
    for i in x:
        if len(x[i]) == 1:
            res.append(x[i][0]) if x[i][0] not in res else None
    return res
# The conditional expression checks if the minterm is already present in the res list to avoid duplicates.

def searchVariables(x, num_vars):  # Function to find variables in a meanterm.
    var_list = []
    for i in range(len(x)):
        if x[i] == '0':
            var_list.append(chr(i + 65) + "'")
        elif x[i] == '1':
            var_list.append(chr(i + 65))
    return var_list[:num_vars]
# It takes two parameters: x and num_vars. The function returns a list of variables found in the meanterm.
# Meanterm: A meanterm is an algebraic expression that represents the average value of a set of variables. 

def flatten(x):  # Flattens a list
    flattened_items = []
    for i in x:
        flattened_items.extend(x[i])
    return flattened_items
# function takes a nested list as input and returns a flattened list
# flatten() method in Python is used to return a copy of a given array 
# in such a way that it is collapsed into one dimension.

def searchMinterms(a):  # Function for finding out which minterms are merged.
    gaps = a.count('-')
    if gaps == 0:
        return [str(int(a, 2))]
    x = [bin(i)[2:].zfill(gaps) for i in range(pow(2, gaps))]
    temp = []
    for i in range(pow(2, gaps)):
        temp2, ind = a[:], -1
        for j in x[0]:
            if ind != -1:
                ind = ind + temp2[ind + 1:].find('-') + 1
            else:
                ind = temp2[ind + 1:].find('-')
            temp2 = temp2[:ind] + j + temp2[ind + 1:]
        temp.append(str(int(temp2, 2)))
        x.pop(0)
    return temp
# It takes a binary string as input and returns a list of merged minterms.

def compare(a, b):  # Function for checking if 2 minterms differ by 1 bit only
# The compare function starts by initializing a counter variable c 
# to keep track of the number of differing bits between the two minterms.
    c = 0
    for i in range(len(a)): # a loop is used to iterate over each bit of the minterms.
    #  range(len(a)) generates a sequence of numbers from 0 to the length of the minterm a.
        if a[i] != b[i]: # checks if the corresponding bits of a and b are different.
            mismatch_index = i  # indicates the position of the differing bit.
            c += 1 # c is then incremented by 1 to track of the number of differing bits
            if c > 1: # if c > 1, the function immediately returns a tuple (False, None)
                return (False, None) # indicating that the minterms differ by more than one bit.
    return (True, mismatch_index) # indicating that the minterms differ by only one bit
# Finally, if the loop completes without encountering more than one differing bit returns a tuple


def removeTerms(_chart, terms):  # Removes minterms which are already covered from chart
    for i in terms:
        for j in searchMinterms(i):
            try:
                del _chart[j]
            except KeyError:
                pass
# The _chart parameter represents the chart from which we want to remove the covered minterms, 
# The terms parameter is a list of minterms that have already been covered.

# Creating Inputs
num_vars = int(input("Enter the Number of Variables: "))
mt = [int(i) for i in input("Enter the Minterms (Minterms are Separated with Space): ").strip().split()]
dc = [int(i) for i in input("Enter the Don't Cares (Press Enter if None): ").strip().split()]
# The code prompts the user to enter the number of variables, minterms, and don't cares.
mt.sort()
minterms = mt + dc #  the minterms and don't cares are combined into a single list called minterms.
minterms.sort() # this list is then sorted in ascending order using the sort() method.
size = num_vars # size stores the number of variables,
groups, all_pi = {}, set()
# groups will store the groups of prime implicants,
# all_pi is a set that will store all the prime implicants.

# Primary grouping starts. It starts with a loop that iterates over each minterm in a given list. 
for minterm in minterms:
    try:
        groups[bin(minterm).count('1')].append(bin(minterm)[2:].zfill(size))
    except KeyError:
        groups[bin(minterm).count('1')] = [bin(minterm)[2:].zfill(size)]
# Primary grouping ends. 
# Inside the loop, the code groups the minterms based on the count of '1's in their binary representation.

# Primary group printing starts
print("\n\n\n\nGroup No.\tMinterms\tBinary of Minterms\n%s" % ('_' * 50))
for i in sorted(groups.keys()):
    print("%5d:" % i)  # Prints group number
    for j in groups[i]:
        print("\t\t    %-20d%s" % (int(j, 2), j))  # Prints minterm and its binary representation
    print('_' * 50)
# Primary group printing ends
# It consists of a loop that iterates over the groups dictionary and 
# prints the group number, minterms, and binary representation for each group.

# Process for creating tables and finding prime implicants starts
while True:
    tmp = groups.copy()
    groups, m, marked, should_stop = {}, 0, set(), True
    l = sorted(list(tmp.keys()))
    for i in range(len(l) - 1):
        for j in tmp[l[i]]:  # Loop which iterates through current group elements
            for k in tmp[l[i + 1]]:  # Loop which iterates through next group elements
                res = compare(j, k)  # Compare the minterms
                if res[0]:  # If the minterms differ by 1 bit only
                    try:
                        groups[m].append(
                            j[:res[1]] + '-' + j[res[1] + 1:]
                        ) if j[:res[1]] + '-' + j[res[1] + 1:] not in groups[m] else None 
                        # Put a '-' in the changing bit and add it to corresponding group
                    except KeyError:
                        groups[m] = [j[:res[1]] + '-' + j[res[1] + 1:]]  
                        # If the group doesn't exist, create the group at first and then put a '-' 
                        # in the changing bit and add it to the newly created group
                    should_stop = False
                    marked.add(j)  # Mark element j
                    marked.add(k)  # Mark element k
        m += 1
    local_unmarked = set(flatten(tmp)).difference(marked)  # Unmarked elements of each table
    all_pi = all_pi.union(local_unmarked)  # Adding Prime Implicants to the global list
    print(
        "Prime Implicants of this Table:",
        None if len(local_unmarked) == 0 else ', '.join(local_unmarked),
    )  # Printing Prime Implicants of the current table
    if should_stop:  # If the minterms cannot be combined further
        print(
            "\n\nAll Prime Implicants: ",
            None if len(all_pi) == 0 else ', '.join(all_pi),
        )  # Print all prime implicants
        break
    # Printing of all the next groups starts
    print("\n\n\n\nGroup No.\tMinterms\tBinary of Minterms\n%s" % ('_' * 50))
    for i in sorted(groups.keys()):
        print("%5d:" % i)  # Prints group number
        for j in groups[i]:
            print(
                "\t\t%-24s%s"
                % (','.join(searchMinterms(j)), j)
            )  # Prints minterms and its binary representation
        print('_' * 50)
    # Printing of all the next groups ends
# Process for creating tables and finding prime implicants ends

# Printing and processing of Prime Implicant chart starts
sz = len(str(mt[-1]))  # The number of digits of the largest minterm
chart = {}
print(
    '\n\n\nPrime Implicants Chart:\n\n    Minterms    |%s'
    % (' '.join((' ' * (sz - len(str(i)))) + str(i) for i in mt),)
    + ' ' * (len(mt) * (sz + 1) + 16)
)
for i in all_pi:
    merged_minterms, y = searchMinterms(i), 0 # finds the merged minterms covered by the current prime implicant.
    print("%-16s|" % ','.join(merged_minterms), end='') # prints the merged minterms in a formatted manner.
    for j in remove(merged_minterms, dc):
        x = mt.index(int(j)) * (sz + 1)  # The position where we should put 'X'
        print(' ' * abs(x - y) + ' ' * (sz - 1) + 'X', end='')
        y = x + sz
        try:
            chart[j].append(i) if i not in chart[j] else None  # Add minterm in chart
        except KeyError:
            chart[j] = [i] 
    print('\n' + ' ' * (len(mt) * (sz + 1) + 16))  # Updates the Prime Implicant chart 
    # by adding the prime implicant for each covered minterm.
# Printing and processing of Prime Implicant chart ends

EPI = searchEPI(chart)  # Finding essential prime implicants
print("\nEssential Prime Implicants: " + ', '.join(str(i) for i in EPI))
removeTerms(chart, EPI)  # Remove EPI related columns from chart
# This function is called to remove the columns related to the essential prime implicants from the chart.
# If there are no minterms remaining after removing the EPI related columns, the code enters the if block.
if len(chart) == 0:  # If no minterms remain after removing EPI related columns
    final_result = [
        searchVariables(i, num_vars) for i in EPI
    ]  
# If there are no minterms remaining after removing the EPI related columns, the code enters the if block.
    # Applying Petrick's Method:
else:  # Else follow Petrick's method for further simplification
    P = [[searchVariables(j, num_vars) for j in chart[i]] for i in chart]
    # The P variable is initialized as a list of lists, 
    # where each inner list represents the variables associated with a minterm in the remaining chart.
    while len(P) > 1:  # Keep combineing until we get the SOP form of P
        P[1] = combine(P[0], P[1]) 
        # Function is called to combine the first two lists in P and obtain a simplified list.
        P.pop(0) # the first list in P is removed
        # If P[0] is not empty, the code enters the if block.
    if P[0]: 
        final_result = [min(P[0], key=len)]  # Choosing the term with minimum variables from P
        final_result.extend(
            searchVariables(i, num_vars) for i in EPI
        )  # Adding the EPIs to the final solution and the result is added to the final_result list.
        # If P[0] is empty, the code enters the else block.
    else:
        final_result = [
            searchVariables(i, num_vars) for i in EPI
        ]  # Final result with only EPIs

# Display the final result
result_string = ' + '.join(''.join(i) for i in final_result)
print('\n\nAnswer: F = ' + result_string)

input("\nQuine McCluskey Program by Xtiantzyyy (Press Enter to Exit)")
# It consists of a single block of code that displays the final result.

# End of Quine Mc-Cluskey Program Code