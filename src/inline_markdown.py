from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT and delimiter in node.text:
            start = 0
            if node.text.count(delimiter) % 2 != 0:
                raise Exception("Incorrect format, check the sytax")
            for sub_node in node.text.split(delimiter):
                if sub_node != "":
                    if start % 2 == 0:
                        new_nodes.append(TextNode(sub_node, TextType.TEXT))
                    else: 
                        new_nodes.append(TextNode(sub_node, text_type))
                start += 1

        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    try:
        return re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    except:
        raise ValueError("Incorrect syntax for image")

def extract_markdown_links(text):
    try:
        return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    except:
        raise ValueError("Incorrect syntax for link")

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            images = extract_markdown_images(node.text)
            if len(images) != 0:
                pattern = r"(!\[.*?\]\(.*?\))"
                image_index = 0
                for subnode in re.split(pattern, node.text):
                    print(subnode)
                    if subnode != "":
                        if re.match(pattern, subnode):
                            new_nodes.append(TextNode(
                                images[image_index][0],
                                TextType.IMAGE,
                                images[image_index][1])
                                )
                            image_index += 1
                        else:
                            new_nodes.append(TextNode(subnode, TextType.TEXT))    
            else:
                new_nodes.append(node)    
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links = extract_markdown_links(node.text)
            if len(links) != 0:
                pattern = r"((?<!!)\[.*?\]\(.*?\))"
                link_index = 0
                for subnode in re.split(pattern, node.text):
                    if subnode != "":
                        if re.match(pattern, subnode):
                            new_nodes.append(TextNode(
                                links[link_index][0],
                                TextType.LINK,
                                links[link_index][1])
                                )
                            link_index += 1
                        else:
                            new_nodes.append(TextNode(subnode, TextType.TEXT))    
            else:
                new_nodes.append(node)
        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    textnodes = [TextNode(text, TextType.TEXT)]
    textnodes = split_nodes_delimiter(textnodes, "**", TextType.BOLD)
    textnodes = split_nodes_delimiter(textnodes, "*", TextType.ITALIC)
    textnodes = split_nodes_delimiter(textnodes, "`", TextType.CODE)
    
    textnodes = split_nodes_link(textnodes)
    textnodes = split_nodes_image(textnodes)
    return textnodes
    