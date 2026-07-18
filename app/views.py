from django.http import HttpResponse

def home(request):
    features = ["User Authentication", "Database Syncing", "AI Dashboard Analytics", "API Integrations"]
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Tech Exercise Part 2</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f4f4f9; }}
            h1 {{ color: #333; }}
            ul {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 300px; }}
            li {{ padding: 10px 0; border-bottom: 1px solid #eee; }}
            li:last-child {{ border-bottom: none; }}
            .status {{ color: green; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>Framework Status: <span class="status">Partially Running</span></h1>
        <p>Demonstrating hard-coded application features:</p>
        <ul>
            {"".join([f"<li>{feature}</li>" for feature in features])}
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content)