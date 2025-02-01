import re


def parse_html(markdown: str):
    """
    Converts markdown text to HTML by replacing markdown syntax with corresponding HTML tags.

    Supported markdown elements:
    - Headings (#, ##, ###, etc.)
    - Bold (__bold__, **bold**)
    - Italic (_italic_, *italic*)
    - Inline code (`code`)
    - Links ([text](url))

    Args:
        markdown (str): The markdown text to be parsed.

    Returns:
        str: The converted HTML string.
    """
    # Convert headings (e.g., # Heading -> <h1>Heading</h1>)
    markdown = re.sub(r'^#\s+(.*)$', r'<h1>\1</h1>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^##\s+(.*)$', r'<h2>\1</h2>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^###\s+(.*)$', r'<h3>\1</h3>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^####\s+(.*)$', r'<h4>\1</h4>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^#####\s+(.*)$', r'<h5>\1</h5>', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^######\s+(.*)$', r'<h6>\1</h6>', markdown, flags=re.MULTILINE)

    # Convert bold (__bold__, **bold** -> <strong>bold</strong>)
    markdown = re.sub(r'__(.*?)__', r'<strong>\1</strong>', markdown)
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', markdown)

    # Convert italic (_italic_, *italic* -> <em>italic</em>)
    markdown = re.sub(r'_(.*?)_', r'<em>\1</em>', markdown)
    markdown = re.sub(r'\*(.*?)\*', r'<em>\1</em>', markdown)

    # Convert inline code (`code` -> <code>code</code>)
    markdown = re.sub(r'`(.*?)`', r'<code>\1</code>', markdown)

    # Convert links ([text](url) -> <a href="url">text</a>)
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

    return markdown


def parse_text(markdown: str):
    """
    Extracts plain text from a markdown string by removing all markdown syntax.

    Args:
        markdown (str): The markdown text to be processed.

    Returns:
        str: The extracted plain text.
    """
    # Remove headings (e.g., # Heading -> Heading)
    markdown = re.sub(r'^#+\s+(.*)$', r'\1', markdown, flags=re.MULTILINE)

    # Remove bold and italic syntax (e.g., **bold**, _italic_)
    markdown = re.sub(r'__([^_]+)__', r'\1', markdown)
    markdown = re.sub(r'\*\*([^*]+)\*\*', r'\1', markdown)
    markdown = re.sub(r'_([^_]+)_', r'\1', markdown)
    markdown = re.sub(r'\*([^*]+)\*', r'\1', markdown)

    # Remove inline code syntax (e.g., `code`)
    markdown = re.sub(r'`([^`]+)`', r'\1', markdown)

    # Remove links (e.g., [text](url) -> text)
    markdown = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', markdown)

    # Remove any remaining markdown symbols (e.g., *, _, `, #)
    markdown = re.sub(r'[*_`#]', '', markdown)

    # Strip leading/trailing whitespace and normalize spaces
    markdown = markdown.strip()
    markdown = re.sub(r'\s+', ' ', markdown)  # Replace multiple spaces with a single space

    return markdown


def add(a, b):
    return a + b
