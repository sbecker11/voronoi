import os

markdown = "# Random Voronoi Images\n\n"

# Get all files in the current directory
files = os.listdir()

# Filter out the .png files
png_files = [f for f in files if f.endswith('.png')]

# Generate markdown for each image
for file in png_files:
    markdown += f'<img src="./{file}" alt="{file}" width="500"/>\n\n'

# Write the markdown to README.md
with open('README.md', 'w') as f:
    f.write(markdown)