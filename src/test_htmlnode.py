import unittest
from htmlnode import HTMLNODE, LeafNode, ParentNode
class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        prop = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNODE("a", "Click here", None, prop)
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)
    
    def test_Leaf_Node_to_html(self):
        leaf_node_with_tag = LeafNode(value="This is a leaf node", tag="div", props={"class": "leaf"})
        expected = '<div class="leaf">This is a leaf node</div>'
        self.assertEqual(leaf_node_with_tag.to_html(), expected)

    def test_parent_node_with_leaf_nodes(self):
        # Creating leaf nodes
        leaf1 = LeafNode("Bold text", "b")
        leaf2 = LeafNode("Normal text")
        leaf3 = LeafNode("italic text", "i")

        # Creating parent node containing leaf nodes
        parent_node = ParentNode(
            "p",
            [
                leaf1,
                leaf2,
                leaf3
            ]
        )

        expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i></p>"
        self.assertEqual(parent_node.to_html(), expected_html)

    def test_parent_node_with_nested_parent_nodes(self):
        # Creating leaf nodes
        leaf1 = LeafNode("Bold text", "b")
        leaf2 = LeafNode("Normal text")
        
        # Creating a nested parent node
        nested_parent_node = ParentNode(
            "div",
            [
                LeafNode("Nested text", "span")
            ]
        )
        
        # Creating a parent node containing both leaf nodes and the nested parent node
        parent_node = ParentNode(
            "p",
            [
                leaf1,
                leaf2,
                nested_parent_node
            ]
        )

        expected_html = (
            "<p><b>Bold text</b>Normal text"
            "<div><span>Nested text</span></div></p>"
        )
        self.assertEqual(parent_node.to_html(), expected_html)




if __name__ == "__main__":
    unittest.main()

