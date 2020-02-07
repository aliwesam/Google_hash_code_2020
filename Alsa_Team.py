# More Pizza Practice round
# Google Hash Code 2020
# By Ali Wissam
# Team : ALSA / Iraq
##############************#################
# Import file then split first & secound lines

def Devteam(filename, output):  # filename : input file | output : give name for output file
    with open(filename) as fin:
        Pizza, diff_type = [int(lines) for lines in next(fin).split()]  # this to make first line readable
        "Pizza, for Maximum number of pizzas slices"
        array = []  # To handle rest lines
        for line in fin:  # this to read secound line
            array.append([int(lines) for lines in line.split()])
        arrays = []  # to store types that reach the maximun number or closer
        sum_of_types = 0  # Store result of sum each value that reach the maximun number or closer
        opparray = reversed(array[0])  # reverse array to start in opposite way
        counter = len(array[0]) - 1    # Here we can store the Indexing to use with output file
        for i in opparray:             # Loop that start from last value to first one
            # Check if sum the current value with previous sum result less than or equal maximum number given
            if (sum_of_types + i) <= Pizza:
                sum_of_types += i
                arrays.append(counter)  # Still less ? store it then
            counter = counter - 1

    result_array = []                    # Store with this array to prepare output file writing
    for n in arrays:
        result_array.append(str(n))
    print(result_array)
    open('' + output + '.out', 'w').write(str(len(result_array)) + '\n')  # here set the type of Pizza used
    for i in list(reversed(result_array)):
        open('' + output + '.out', 'a').write(i + ' ')                     # Insert the Indexes chosen
    print(sum_of_types)


files = [
    "a_example.in",
    "b_small.in",
    "c_medium.in",
    "d_quite_big.in",
    "e_also_big.in"
]
for file in files:
    fileout = file[:-3]
    Devteam("INPUT/"+file, "OUTPUT/"+fileout)
