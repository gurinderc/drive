import os
from datetime import datetime

# Files to exclude from the list
exclude = ['generate_index.py', 'index.html', 'README.md', '_redirects', '.git', '.github']

# Get files with metadata
files_data = []
for f in os.listdir('.'):
    if os.path.isfile(f) and f not in exclude:
        stats = os.stat(f)
        size = round(stats.st_size / (1024 * 1024), 2)  # Size in MB
        date = datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M')
        files_data.append({'name': f, 'size': size, 'date': date})

# Sort files alphabetically
files_data.sort(key=lambda x: x['name'])

# Build the Minimalistic Mono HTML
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Index of /</title>
    <style>
        :root {{
            --bg: #ffffff;
            --text: #1a1a1a;
            --border: #e0e0e0;
            --hover: #f5f5f5;
        }}
        body {{ 
            font-family: "Courier New", Courier, monospace; 
            background: var(--bg);
            color: var(--text);
            max-width: 900px; 
            margin: 40px auto; 
            padding: 0 20px;
            line-height: 1.5;
        }}
        h1 {{ 
            font-size: 1.2rem; 
            font-weight: bold;
            margin-bottom: 2rem;
            border-bottom: 1px solid var(--text);
            display: inline-block;
        }}
        table {{ 
            width: 100%; 
            border-collapse: collapse; 
            margin-top: 10px;
        }}
        th {{ 
            text-align: left; 
            border-bottom: 2px solid var(--text);
            padding: 10px 5px;
            font-size: 0.9rem;
        }}
        td {{ 
            padding: 8px 5px; 
            border-bottom: 1px solid var(--border);
            font-size: 0.9rem;
        }}
        tr:hover {{ background: var(--hover); }}
        a {{ 
            color: var(--text); 
            text-decoration: none; 
        }}
        a:hover {{ text-decoration: underline; }}
        .size-col {{ text-align: right; width: 100px; }}
        .date-col {{ text-align: right; width: 180px; color: #666; }}
    </style>
</head>
<body>
    <h1>INDEX OF ARCHIVES</h1>
    <table>
        <thead>
            <tr>
                <th>FILE NAME</th>
                <th class="size-col">SIZE</th>
                <th class="date-col">LAST MODIFIED</th>
            </tr>
        </thead>
        <tbody>
            {''.join(f'''
            <tr>
                <td><a href="./{f['name']}">{f['name']}</a></td>
                <td class="size-col">{f['size']} MB</td>
                <td class="date-col">{f['date']}</td>
            </tr>''' for f in files_data)}
        </tbody>
    </table>
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(html_content)

print("index.html generated successfully.")
