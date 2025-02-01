class HTMLNODE:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        if not self.props:
            return ""
        for key, value in self.props.items():
            result += f" {key}=\"{value}\""
        return result
    def __repr__(self):
        return f"HTMLNODE(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNODE):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, children=None, props=props)
        if not value:
            raise ValueError("LeafNode must have a value")
    
    def to_html(self):
        if not self.value:
            raise ValueError("Value must be present")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"
    

class ParentNode(HTMLNODE):
    def __init__(self, tag, children, props = None, value=None):
        super().__init__(tag, value, children, props)
        if not tag or not children:
            raise ValueError("Must have tag and children")
        
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        
        # Opening tag
        opening_tag = f"<{self.tag}{self.props_to_html()}>"
        
        # Recursively call to_html() on each child, whether it's a LeafNode or another ParentNode
        children_html = "".join([child.to_html() for child in self.children])
        
        # Closing tag
        closing_tag = f"</{self.tag}>"
        
        
        return f"{opening_tag}{children_html}{closing_tag}"
    
    def __repr__(self):
        return f"ParentNode(tag={self.tag}, children={self.children}, props={self.props})"
        