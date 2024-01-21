# Open the input file in read mode and output file in write mode
with open('input.txt', 'r') as infile, open('output8.txt', 'w') as outfile:
    # Read the numbers from the input file
    numbers = [int(num) for num in infile.read().split()]

    # Write the unsorted numbers to the output file
    outfile.write("Before Sorting: " + str(numbers) + "\n")

    # Sort the numbers
    numbers.sort()

    # Write the sorted numbers to the output file
    outfile.write("After Sorting: " + str(numbers) + "\n")
