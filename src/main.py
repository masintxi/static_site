from textnode import TextNode, TextType
from htmlnode import HTMLNode
from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
import re

def main():
    # obj = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    # print(obj)
    # obj = HTMLNode("p", "this is the value", ["potato", "apple", "kiwi"], {"class": "greeting", "href": "https://boot.dev"})
    # print(obj)
    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # print(split_nodes_delimiter([node], "`", TextType.CODE))
    # text = "**This** is text with a **bolded word** and **another**"
    # text = "This ** has ** multiple ** bold ** sections"
    # node = TextNode(text, TextType.TEXT)
    # print(split_nodes_delimiter([node], "**", TextType.BOLD))
    # image = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(image))
    # link = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(link))
    
    # print(image.split(r"(!\[.*?\]\(.*?\))"))
    # print(image)
    # print(re.split(r"(!\[.*?\]\(.*?\))", image))

    node = TextNode(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)",
        TextType.TEXT,
        )
    print(split_nodes_image([node]))

    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
        )
    print(split_nodes_link([node]))
    
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    for i in text_to_textnodes(text):
        print("*", i)
    node = TextNode(text, TextType.TEXT)
    print(split_nodes_image([node]))

main()
