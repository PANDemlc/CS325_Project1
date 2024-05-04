from xml.etree import ElementTree as ET

# HTML file creation based on example from class
def txt_to_html(txt_file, html_file):
    root = ET.Element("html")

    head = ET.SubElement(root, "head")
    title = ET.SubElement(head, "title")
    title.text = "My News Aggregation Site"
    # Added styling to website
    style = ET.SubElement(head, "style")
    style.text = """
        body {
            display: flex;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .article-container {
            max-width: 800px;
            padding: 20px;
            text-align: left;
        }
        h1 {
            font-weight: bold;
        }
        p {
            color: grey;
        }

    """
    body = ET.SubElement(root, "body")
    container = ET.SubElement(body, "div", attrib={"class": "article-container"})

    with open(txt_file, 'r') as f:
        lines = f.readlines()

        for i in range(0, len(lines), 2):
            header = lines[i].strip()
            paragraph = lines[i+1].strip()

            h1 = ET.SubElement(container, "h1")
            h1.text = header
            p = ET.SubElement(container, "p")
            p.text = paragraph

            hr = ET.SubElement(container, "hr")

    with open(html_file, 'wb') as f:
        tree = ET.ElementTree(root)
        tree.write(f, encoding='utf-8')
