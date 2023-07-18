def parse_file(file):
    titles = {}
    lines = file.readlines()
    index = 0
    
    while index < len(lines):
        title = lines[index]
        if title not in titles:
            titles[lines[index]] = title
        index += 1
        while not lines[index].startswith("==="):
            text = lines[index]
            titles[title] += text
            index += 1
        titles[title] += "\n"
        index += 1
    return titles


def new_file(titles):
    file = open("new_clippings.txt", "w")
    for title in titles:
        file.write(title)
        file.write(titles[title])
        file.write("==========\n")
    file.close()

def main():
    file = open("My Clippings.txt", "r")
    print("OK")
    titles = parse_file(file)
    
    new_file(titles)

main()