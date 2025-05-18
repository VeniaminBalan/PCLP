
def read_file():
    with open("in.txt", "r") as infile:
        text = infile.readline()
    return text


def process(text :str):
    values = []

    for i in range( len(text), 0, -8 ):
        begin = i - 8 if i - 8 >= 0 else 0
        end = i
        values.append(text[begin:end])
    
    values[-1] = ((8 - len(values[-1])) * "0") + values[-1]

    return reversed(values)

def write_file(values):
    with open("out.txt", "w+") as outfile:
        for value in values:
            outfile.write(value + "-" + str(int(value, 2)) + "\n")

text = read_file()
write_file(process(text))