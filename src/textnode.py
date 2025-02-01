from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None, alt=None):
        self.text = text
        self.text_type = text_type
        self.url = url
        self.alt = alt
    
    def __eq__(self, other):
        if self.text == other.text and self.text_type == other.text_type and self.url == other.url and self.alt == other.alt:
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}, {self.alt})"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(value=text_node.text, tag="b")
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(value=text_node.text, tag="i")
    elif text_node.text_type == TextType.CODE:
        return LeafNode(value=text_node.text, tag="code")
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("Link must have a 'url' attribute.")
        return LeafNode(value=text_node.text, tag="a", props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url or not text_node.alt:
            raise ValueError("Image must have 'url' (src) and 'alt' attributes.")
        return LeafNode(value="", tag="img", props={"src": text_node.url, "alt": text_node.alt})
    else:
        raise ValueError(f"Unknown text type: {text_node.text_type}")
