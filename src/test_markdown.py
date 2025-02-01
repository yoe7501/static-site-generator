from split_nodes import extract_markdown_images, extract_markdown_links
import unittest

class TestMarkdown(unittest.TestCase):
    def test_base_case(self):
         text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
         result = extract_markdown_images(text)
         expected = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
         self.assertEqual(result, expected)
    

if __name__ == "__main__":
     unittest.main()