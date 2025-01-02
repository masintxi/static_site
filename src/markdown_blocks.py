import re

def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split("\n\n"):
        if block != "" and block != " ":
            blocks.append(block.strip())
    return blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if re.match(r"^#{1,6} ", block):
        return "heading"    
    
    if re.match(r"^```(?!`)", lines[0]) and not re.match(r".*?````$", lines[-1]) and re.match(r".*?```$", lines[-1]):
        return "code"
    
    quote = True
    for i in lines:
        if not re.match(r"^>", i):
            quote = False
    if quote:
        return "quote"
    
    unord_list = True
    for i in lines:
        if not re.match(r"^[*-] ", i):
            unord_list = False
    if unord_list:
        return "unordered_list"
    
    ord_list = True
    for i in range(len(lines)):
        start = f"{i + 1}. "
        if lines[i][:len(start)] != start:
            ord_list = False
    if ord_list:
        return "ordered_list"
    
    return "paragraph"