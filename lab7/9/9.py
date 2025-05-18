def read_file():
    with open("in.txt", "r") as infile:
        text = infile.readline()
    return text

def write_file(text):
    newline = False
    for i in range(1, len(text)):
        if text[i] == "1":
            newline = True
            continue
        if newline:
            lines += "\n" + text[i]
            newline = False
        else:
            lines += text[i]

    with open("out.txt", "w+") as outfile:
        lines = str()
        outfile.write(lines)


def write_file2(text:str):
    lines = [line for line in text.split("1") if line.strip()]
    with open("out.txt", "w+") as outfile:
        outfile.write("\n".join(lines))


txt = read_file()
write_file2(txt)