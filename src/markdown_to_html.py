from markdown_blocks import block_to_block_type, markdown_to_blocks
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_node_to_html_node, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def markdown_to_html(markdown):
    final_html = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        match block_to_block_type(block):
            case "heading":
                num_head = block.split(" ")[0].count("#")
                tag = f"h{num_head}"
                trimmed_block = block[num_head + 1:].strip()
                final_html.append(block_to_html(trimmed_block, tag))
            case "paragraph":
                tag = "p"
                final_html.append(block_to_html(block.strip(), tag))
            case "quote":
                tag = "blockquote"
                trimmed_block = trim_list(block).strip()
                final_html.append(block_to_html(trimmed_block, tag))
            case "code":
                tag = "code"
                trimmed_block = block[3:-3].strip()
                final_html.append(ParentNode("pre", [block_to_html(trimmed_block, tag)]))
            case "unordered_list":
                tag = "ul"
                trimmed_block = trim_list(block)
                final_html.append(list_to_html(trimmed_block, tag))
            case "ordered_list":
                tag = "ol"
                trimmed_block = trim_list(block)
                final_html.append(list_to_html(trimmed_block, tag))

    the_html = ParentNode("div", final_html)
    return the_html

def text_to_children(text):
    child_nodes = []
    nodes = text_to_textnodes(text)
    for node in nodes:
        child_node = text_node_to_html_node(node)
        child_nodes.append(child_node)
    return child_nodes

def block_to_html(block, tag):
    if tag != "code":
        block = " ".join(block.split("\n"))
    children = text_to_children(block)
    return ParentNode(tag, children)

def list_to_html(block, tag):
    children = []
    for line in block.split("\n"):
        child = ParentNode("li", text_to_children(line))
        children.append(child)
    return ParentNode(tag, children)

def trim_list(block):
    lines = block.split("\n")
    cleaned = []
    for line in lines:
        new_line = line.split(" ")
        cleaned.append(" ".join(new_line[1:]))
    return "\n".join(cleaned)