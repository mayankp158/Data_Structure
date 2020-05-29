# with open('camelot.txt','r') as f:
#     print(f.read(2))
#     print(f.read(8))
#     print(f.read())


camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)