def get():
    return """
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>Sign Up</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f4f4f4;
            }
            .signup-container {
                background: white;
                padding: 25px;
                border-radius: 8px;
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
                width: 350px;
                text-align: center;
            }
            .signup-container input {
                width: 90%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
            .signup-container button {
                width: 90%;
                padding: 10px;
                background: blue;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class=\"signup-container\">
            <h2>Sign Up</h2>
            <input type=\"email\" placeholder=\"Email\">
            <input type=\"text\" placeholder=\"Real Name\">
            <input type=\"password\" placeholder=\"Password\">
            <input type=\"date\">
            <button>Sign Up</button>
        </div>
    </body>
    </html>
    """
