from textnode import TextNode, TextType
import re

def split_node_delimiter(old_nodes, delimiter, text_type):
    new_list = []  
    for node in old_nodes:
        if node.text_type is not TextType.NORMAL:
            new_list.append(node) 
            continue 

        separated_text = node.text.split(delimiter)

        # If there's no delimiter, keep as a single normal text node.
        if len(separated_text) == 1:
            new_list.append(node)
            continue

        if len(separated_text) % 2 == 0:
            raise Exception("Delimiter does not have an ending delimiter")

        for i, part in enumerate(separated_text):
            text_node_type = text_type if i % 2 else TextType.NORMAL
            new_list.append(TextNode(part, text_node_type))

    return new_list


def extract_markdown_images(text):
    """Extracts Markdown images as (alt text, image URL) pairs."""
    pattern = r"!\[([^\]]+)\]\(([^)]+)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    """Extracts Markdown links as (text, URL) pairs."""
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"
    return re.findall(pattern, text)


def split_nodes_images(old_nodes):
    pattern = r"!\[([^\]]+)\]\(([^)]+)\)"  

    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_list.append(node)
            continue
        cursor = 0
        while cursor < len(node.text):
            # Search for the next image
            match = re.search(pattern, node.text[cursor:])
            if match:
                # Normal text before the image
                if match.start() > 0:
                    normal_text = node.text[cursor:cursor + match.start()]
                    if normal_text.strip():
                        new_list.append(TextNode(normal_text, TextType.NORMAL))

                # Extract image alt and url
                alt_text, img_url = match.groups()
                new_list.append(TextNode(alt_text, TextType.IMAGE, img_url))  # Use IMAGE type for image
                cursor += match.start() + len(match.group(0))  # Move cursor past the image
            else:
                # Add the remaining normal text if no image is found
                remaining_text = node.text[cursor:]
                if remaining_text.strip():
                    new_list.append(TextNode(remaining_text, TextType.NORMAL))
                break

    return new_list


def split_nodes_link(old_nodes):
    pattern = r"\[([^\]]+)\]\(([^)]+)\)"  

    new_list = []

    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_list.append(node)
            continue
        links = extract_markdown_links(node.text)
        link_idx = 0

        cursor = 0
        while cursor < len(node.text):
            match = re.search(pattern, node.text[cursor:])
            if match:
                # Normal text before the link
                if match.start() > 0:
                    normal_text = node.text[cursor:cursor + match.start()]
                    if normal_text.strip():
                        new_list.append(TextNode(normal_text, TextType.NORMAL))

                link_text, link_url = links[link_idx]
                new_list.append(TextNode(link_text, TextType.LINK, link_url))
                cursor += match.start() + len(match.group(0))  
                link_idx += 1
            else:
                # Add the remaining normal text if no link is found
                remaining_text = node.text[cursor:]
                if remaining_text.strip():
                    new_list.append(TextNode(remaining_text, TextType.NORMAL))
                break

    return new_list


def text_to_textnodes(text):
    
    nodes = [TextNode(text, TextType.NORMAL)]

    nodes = split_node_delimiter(nodes, "**", TextType.BOLD)

    nodes = split_node_delimiter(nodes, "*", TextType.ITALIC)

    nodes = split_node_delimiter(nodes, "`", TextType.CODE)

    nodes = split_nodes_images(nodes)

    nodes = split_nodes_link(nodes)

    return nodes
