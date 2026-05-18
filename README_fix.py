with open('README.md', 'r') as f:
    content = f.read()

# Remove entire Origin section
import re
content = re.sub(r'## Origin.*?(?=\n## |\Z)', '', content, flags=re.DOTALL)

# Fix license name
content = content.replace('MIT License | Marta Zielinska 2026', 'MIT License | Marta Julia Zielinska 2026')

with open('README.md', 'w') as f:
    f.write(content)

print("Done")
