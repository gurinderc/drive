import os

# Define files to exclude (like the script itself)
exclude = ['generate_index.py', 'index.html', '_redirects', 'README.md']

# Get all files in the current directory
files = [f for f in os.listdir('.') if os.path.isfile(f) and f not in exclude]
files.sort()

# Build the HTML content
html = f"""<!DOCTYPE html>
<html>
<head><title>File Index</title></head>
<body>
<h1>Index of Files</h1>
<ul>
{''.join(f'<li><a href="./{file}">{file}</a></li>' for file in files)}
</ul>
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(html)
