import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node = TextNode("This", TextType.NORMAL)
        node2 = TextNode("This", TextType.NORMAL)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("that", TextType.BOLD)
        node2 = TextNode("This", TextType.NORMAL)
        self.assertNotEqual(node, node2)
        node = TextNode("This", TextType.BOLD)
        node2 = TextNode("This", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_text(self):
        text_node = TextNode("Just some text", TextType.NORMAL)
        result = text_node_to_html_node(text_node)
        expected = LeafNode(value="Just some text")
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_bold(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        result = text_node_to_html_node(text_node)
        expected = LeafNode(value="Bold text", tag="b")
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_italic(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        result = text_node_to_html_node(text_node)
        expected = LeafNode(value="Italic text", tag="i")
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_code(self):
        text_node = TextNode("Code snippet", TextType.CODE)
        result = text_node_to_html_node(text_node)
        expected = LeafNode(value="Code snippet", tag="code")
        self.assertEqual(result.to_html(), expected.to_html())

    def test_text_node_to_html_node_link(self):
        text_node = TextNode("Click here", TextType.LINK, url="https://www.example.com")
        result = text_node_to_html_node(text_node)
        expected = LeafNode(value="Click here", tag="a", props={"href": "https://www.example.com"})
        self.assertEqual(result.to_html(), expected.to_html())


    def test_link_missing_href(self):
        text_node = TextNode("Invalid link", TextType.LINK)
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

    def test_image_missing_src_or_alt(self):
        text_node = TextNode("", TextType.IMAGE, alt="An image")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)
        
        text_node = TextNode("", TextType.IMAGE, url="https://www.example.com/image.jpg")
        with self.assertRaises(ValueError):
            text_node_to_html_node(text_node)

if __name__ == "__main__":
    unittest.main()
