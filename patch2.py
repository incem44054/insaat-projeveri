import sys

with open('app.py', 'r', encoding='utf-8') as f:
    code = f.read()

import re
code = re.sub(r'st\.sidebar\.markdown\(\s*"""\s*<div class="student-info">.*?</div>\s*""",\s*unsafe_allow_html=True\s*\)', '', code, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(code)
