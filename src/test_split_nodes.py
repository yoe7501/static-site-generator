import unittest
from textnode import TextNode, TextType
from split_nodes import split_node_delimiter, split_nodes_images, split_nodes_link, text_to_textnodes

class TestSplitNodes(unittest.TestCase):
    def test_simple(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_node_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("This is text with a ", TextType.NORMAL),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.NORMAL),
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_no_delimiter(self):
        node = TextNode("No delimiter here", TextType.NORMAL)
        new_nodes = split_node_delimiter([node], "`", TextType.CODE)

        expected_nodes = [
            TextNode("No delimiter here", TextType.NORMAL)
        ]

        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_link_base(self):
        node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.NORMAL,
        )   
        new_nodes = split_nodes_link([node])
        expected =  [TextNode("This is text with a link ", TextType.NORMAL),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        TextNode(" and ", TextType.NORMAL),
        TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),]
        self.assertEqual(new_nodes, expected)
    
  

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
        TextNode("This is ", TextType.NORMAL),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.NORMAL),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.NORMAL),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.NORMAL),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.NORMAL),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
