# Open the input file and read the content
with open('in.txt', 'r') as infile:
    text = infile.read()

# Extract digits from the text
digits = [char for char in text if char.isdigit()]

# Sort the digits in ascending order
sorted_digits = sorted(digits)

# Write the sorted digits to the output file
with open('out.txt', 'w+') as outfile:
    outfile.write(''.join(sorted_digits))