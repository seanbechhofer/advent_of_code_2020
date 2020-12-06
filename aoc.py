
def blocks(lines):
    blocks = []
    block = []
    for i in range(0,len(lines)):
        if lines[i] == "":
            blocks.append(block)
            block = []
        else:
            block.append(lines[i])
    blocks.append(block)
    return blocks
