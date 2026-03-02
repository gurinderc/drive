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

files_data.sort(key=lambda x: x['name'])

# Build the Fancy HTML
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Archive</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net">
    <style>
        body {{ max-width: 800px; margin: 20px auto; padding: 20px; }}
        table {{ width: 100%; border-collapse: collapse; }}
        .file-icon {{ margin-right: 8px; }}
        .size-tag {{ color: #888; font-size: 0.9em; }}
        tr:hover {{ background: rgba(0,0,0,0.05); }}
    </style>
</head>
<body>
    <header>
        <h1>📦 File Archive</h1>
        <p>Direct download links for hosted archives.</p>
    </header>
    <hr>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Size</th>
                <th>Last Modified</th>
            </tr>
        </thead>
        <tbody>
            {''.join(f'''
            <tr>
                <td><a href="./{f['name']}">📄 {f['name']}</a></td>
                <td><code class="size-tag">{f['size']} MB</code></td>
                <td>{f['date']}</td>
            </tr>''' for f in files_data)}
        </tbody>
    </table>
    <footer>
        <p><small>Automatically updated via Cloudflare Pages</small></p>
    </footer>
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(html_content)
