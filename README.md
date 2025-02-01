# PyParse: Markdown Parser API

PyParse is a lightweight markdown parser that sits in front of an API, allowing users to convert markdown content into HTML or other formats via HTTP requests. It is designed to be simple, fast, and easy to integrate into your workflow. The primary interaction with PyParse is through `curl` commands, making it ideal for scripting and automation.

---

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
   - [Prerequisites](#prerequisites)
   - [Installation](#installation)
   - [Running the API](#running-the-api)
3. [Usage](#usage)
   - [Convert Markdown to HTML](#convert-markdown-to-html)
   - [Convert Markdown to Plain Text](#convert-markdown-to-plain-text)
4. [API Endpoints](#api-endpoints)
5. [Examples](#examples)
6. [Contributing](#contributing)
7. [License](#license)

---

## Features

- **Markdown to HTML**: Convert markdown content into HTML.
- **Markdown to Plain Text**: Extract plain text from markdown content.
- **Simple API**: Easy-to-use HTTP endpoints for integration.
- **Lightweight**: Minimal dependencies and fast performance.
- **Curl-Friendly**: Designed for seamless interaction via `curl`.

---

## Getting Started

### Prerequisites

- Python 3.8+
- `pip` for installing dependencies.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jaredgrxss/pyparse.git
   cd pyparse

2. Set up a virtual enviornment
   python3 -m venv venv
   source venv/bin/activate 

3. Install the required dependencies
   pip install -r requirements.txt

### Running the API 

To start the PyParseAPI, run the following command:

- python app.py

By default, the API will be avilable at http://127.0.0.1:8000


## Usage 

### Covert markdown to HTML 

To convert markdwon content to HTML, send a **POST** request to the **/markdown/to-html** endpoint with the markdown content in the request body

Example using curl:

curl -X POST http://127.0.0.1:5000/markdown/to-html \
  -H "Content-Type: text/plain" \
  -d "# Hello, World!"

Response: 

<h1>Hello, World!</h1>

### Convert markdown to plaintext

To extract plain text from markdown content, send a **POST** request to the **/markdown/to-text** endpoint with the markdown content in the request body.

Example using curl:

curl -X POST http://127.0.0.1:5000/markdown/to-text \
  -H "Content-Type: text/plain" \
  -d "# Hello, World!"

Response:

Hello, World!

## API Endpoints

Endpoint                Method                  Description
**/markdown/to-html**    POST                   Converts markdown content to HTML
**/markdown/to-text**    POST                   Extracts plain text from markdown


## Examples 

### Example 1: Convert Markdown to HTML 

curl -X POST http://127.0.0.1:5000/markdown/to-html \
  -H "Content-Type: text/plain" \
  -d "## This is a **bold** heading"

Response:
<h2>This is a <strong>bold</strong> heading</h2>

### Example 2: Convert Markdown to Plain Text

curl -X POST http://127.0.0.1:5000/markdown/to-text \
  -H "Content-Type: text/plain" \
  -d "## This is a **bold** heading"

Response:
This is a bold heading

## Contributing 

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature or bugfix 
3. Commit your changes with clear and descriptive messages
4. Submit a pull request 

## License
This project is licensed under the GNU General Public License. See the **LICENSE** file for details