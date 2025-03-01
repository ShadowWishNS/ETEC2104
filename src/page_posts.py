def get():
    return """
    <!DOCTYPE html>
    <html lang=\"en\">
    <head>
        <meta charset=\"UTF-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
        <title>Posts</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .posts-container {
                width: 400px;
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
                overflow-y: auto;
                max-height: 80vh;
            }
            .post {
                display: flex;
                align-items: center;
                padding: 10px;
                border-bottom: 1px solid #ccc;
            }
            .post:nth-child(odd) {
                background-color: #f9f9f9;
            }
            .thumbnail {
                width: 64px;
                height: 64px;
                background: gray;
                margin-right: 10px;
            }
            .post-info {
                flex: 1;
            }
            .timestamp, .views {
                font-size: 12px;
                color: gray;
            }
        </style>
    </head>
    <body>
        <div class=\"posts-container\">
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Dolphins sleep with one eye open!</strong></p><p class=\"timestamp\">3 days ago</p><p class=\"views\">Views: 12</p></div></div>
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Orcas are the largest species of dolphin.</strong></p><p class=\"timestamp\">5 days ago</p><p class=\"views\">Views: 23</p></div></div>
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Dolphins use echolocation to find food.</strong></p><p class=\"timestamp\">1 week ago</p><p class=\"views\">Views: 18</p></div></div>
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Orcas have distinct family pods.</strong></p><p class=\"timestamp\">9 days ago</p><p class=\"views\">Views: 30</p></div></div>
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Dolphins have unique whistles to communicate.</strong></p><p class=\"timestamp\">2 days ago</p><p class=\"views\">Views: 15</p></div></div>
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Orcas can live up to 90 years.</strong></p><p class=\"timestamp\">6 days ago</p><p class=\"views\">Views: 40</p></div></div>
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Dolphins have been seen helping other species.</strong></p><p class=\"timestamp\">4 days ago</p><p class=\"views\">Views: 22</p></div></div>
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Orcas can swim up to 35 mph.</strong></p><p class=\"timestamp\">7 days ago</p><p class=\"views\">Views: 33</p></div></div>
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Dolphins have incredible memories.</strong></p><p class=\"timestamp\">8 days ago</p><p class=\"views\">Views: 19</p></div></div>
            <div class=\"post\"><div class=\"thumbnail\"></div><div class=\"post-info\"><p><strong>Orcas use teamwork to hunt.</strong></p><p class=\"timestamp\">10 days ago</p><p class=\"views\">Views: 28</p></div></div>
        </div>
    </body>
    </html>
    """
