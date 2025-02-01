from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from . import parser

app = FastAPI()


def create_response(status_code: int, success: bool, message: str, data=None):
    """
    Creates a standardized JSON response for API endpoints.

    Args:
        status_code (int): The HTTP status code for the response.
        success (bool): Indicates whether the request was successful.
        message (str): A message describing the result of the request.
        data (Optional[dict]): Additional data to include in the response. Defaults to None.

    Returns:
        JSONResponse: A JSON response with the provided status code and content.
    """
    response = {
        'status_code': status_code,
        'success': success,
        'message': message
    }
    if data is not None:
        response['data'] = data
    return JSONResponse(content=response, status_code=status_code)


async def get_plaintext_body(request: Request) -> str:
    """
    Extracts and validates plaintext content from the request body.

    Args:
        request (Request): The incoming FastAPI request object.

    Returns:
        str: The decoded and stripped plaintext content from the request body.

    Raises:
        HTTPException: If the request body is empty or contains only whitespace.
    """
    body = await request.body()
    content = body.decode('utf-8').strip()
    if not content:
        raise HTTPException(
            status_code=400,
            detail='Input cannot be empty'
        )
    return content


@app.post('/markdown/to-html', response_model=dict)
async def markdown_to_html(request: Request):
    """
    Converts plaintext markdown content to HTML.

    Args:
        request (Request): The incoming FastAPI request object containing the plaintext markdown content.

    Returns:
        JSONResponse: A JSON response containing the converted HTML content.

    Example:
        Request:
            POST /markdown/to-html
            Content-Type: text/plain
            Body: "Hello, World!"

        Response:
            {
                "status_code": 200,
                "success": true,
                "message": "Markdown successfully converted to HTML",
                "data": {
                    "html": "Hello, World!"
                }
            }
    """
    content = await get_plaintext_body(request)
    html_content = parser.parse_html(content)
    return create_response(
        status_code=200,
        success=True,
        message='Markdown successfully converted to HTML',
        data={
            'html': html_content
        }
    )


@app.post('/markdown/to-text', response_model=dict)
async def markdown_to_text(request: Request):
    """
    Converts plaintext markdown content to plain text.

    Args:
        request (Request): The incoming FastAPI request object containing the plaintext markdown content.

    Returns:
        JSONResponse: A JSON response containing the converted plain text.

    Example:
        Request:
            POST /markdown/to-text
            Content-Type: text/plain
            Body: "Hello, World!"

        Response:
            {
                "status_code": 200,
                "success": true,
                "message": "Markdown successfully converted to plain text",
                "data": {
                    "text": "Hello, World!"
                }
            }
    """
    content = await get_plaintext_body(request)
    plain_text = parser.parse_text(content)
    return create_response(
        status_code=200,
        success=True,
        message='Markdown successfully converted to plain text',
        data={
            'text': plain_text
        }
    )


# Customer excpetion handler for FastAPI HTTPException
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handles HTTP exceptions and returns a standardized JSON response.

    Args:
        request (Request): The incoming FastAPI request object.
        exc (HTTPException): The exception raised by FastAPI.

    Returns:
        JSONResponse: A JSON response with the error details.
    """
    return create_response(
        status_code=exc.status_code,
        success=False,
        message=exc.detail
    )


@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    """
    Handles 404 Not Found errors and returns a list of supported routes.

    Args:
        request (Request): The incoming FastAPI request object.
        exc (HTTPException): The exception raised by FastAPI.

    Returns:
        JSONResponse: A JSON response with the error details and a list of supported routes.
    """
    return create_response(
        status_code=404,
        success=False,
        message='Route not supported',
        data={'supported_routes': ['/markdown/to-html', '/markdown/to-text']}
    )
