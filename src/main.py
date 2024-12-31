from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    obj = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(obj)
    obj = HTMLNode("p", "this is the value", ["potato", "apple", "kiwi"], {"class": "greeting", "href": "https://boot.dev"})
    print(obj)

main()
