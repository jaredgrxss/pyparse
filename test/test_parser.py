from pyparse.parser import parse_html, parse_text


# Test cases for parse_html
def test_parse_html_headings():
    markdown = "# Heading 1\n## Heading 2\n### Heading 3"
    expected = "<h1>Heading 1</h1>\n<h2>Heading 2</h2>\n<h3>Heading 3</h3>"
    assert parse_html(markdown) == expected


def test_parse_html_bold():
    markdown = "This is **bold text** and __also bold__."
    expected = "This is <strong>bold text</strong> and <strong>also bold</strong>."
    assert parse_html(markdown) == expected


def test_parse_html_italic():
    markdown = "This is *italic text* and _also italic_."
    expected = "This is <em>italic text</em> and <em>also italic</em>."
    assert parse_html(markdown) == expected


def test_parse_html_inline_code():
    markdown = "Here is some `inline code`."
    expected = "Here is some <code>inline code</code>."
    assert parse_html(markdown) == expected


def test_parse_html_links():
    markdown = "Check out this [link](https://www.google.com)."
    expected = 'Check out this <a href="https://www.google.com">link</a>.'
    assert parse_html(markdown) == expected


def test_parse_html_mixed_elements():
    markdown = "# Heading\nThis is **bold** and _italic_ with `code` and a [link](https://example.com)."
    expected = "<h1>Heading</h1>\nThis is <strong>bold</strong> and <em>italic</em> with <code>code</code> and a <a href=\"https://example.com\">link</a>."
    assert parse_html(markdown) == expected


# Test cases for parse_text
def test_parse_text_headings():
    markdown = "# Heading 1\n## Heading 2\n### Heading 3"
    expected = "Heading 1 Heading 2 Heading 3"
    assert parse_text(markdown) == expected


def test_parse_text_bold_and_italic():
    markdown = "This is **bold text** and _italic text_."
    expected = "This is bold text and italic text."
    assert parse_text(markdown) == expected


def test_parse_text_inline_code():
    markdown = "Here is some `inline code`."
    expected = "Here is some inline code."
    assert parse_text(markdown) == expected


def test_parse_text_links():
    markdown = "Check out this [link](https://www.google.com)."
    expected = "Check out this link."
    assert parse_text(markdown) == expected


def test_parse_text_mixed_elements():
    markdown = "# Heading\nThis is **bold** and _italic_ with `code` and a [link](https://example.com)."
    expected = "Heading This is bold and italic with code and a link."
    assert parse_text(markdown) == expected
