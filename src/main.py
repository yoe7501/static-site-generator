from textnode import TextNode, TextType
from split_nodes import split_nodes_link, text_to_textnodes, split_node_delimiter, split_nodes_images

def main():
    
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        print(result)

if __name__ == "__main__":
    main()
