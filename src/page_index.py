def get():
    return """
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>Index Page</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
            }
            .header {
                background-color: blue;
                color: limegreen;
                padding: 15px;
                display: flex;
                justify-content: flex-end;
                align-items: center;
                height: 50px;
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <div class=\"header\">
            Hello, NAME
        </div>
    </body>
    </html>
    """
