class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        txt = ""
        for key, value in self.props.items():
            txt += f' {key}="{value}"'
        return txt
    
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Need something here!!. Value must not be empty")
        if self.tag == None:
            return self.value
        if self.props == None:
            start = f'<{self.tag}>'
        else:
            start = f'<{self.tag}{self.props_to_html()}>'
        end = f'</{self.tag}>'
        return f'{start}{self.value}{end}'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("The tag is not oprional")
        if self.children == None:
            raise ValueError("No children, no fun")
        text = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            text += child.to_html()
        text += f'</{self.tag}>'
        return text
