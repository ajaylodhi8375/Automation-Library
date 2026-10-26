"""Build dist/index.html: injects data/raw.json and src/model.js into src/template.html."""
from pathlib import Path
root = Path(__file__).parent
raw = (root / 'data' / 'raw.json').read_text(encoding='utf-8').replace('</', '<\\/')
model = (root / 'src' / 'model.js').read_text(encoding='utf-8')
page = (root / 'src' / 'template.html').read_text(encoding='utf-8')
out = page.replace('__RAW__', raw).replace('__MODEL__', model)
(root / 'dist').mkdir(exist_ok=True)
(root / 'dist' / 'index.html').write_text(out, encoding='utf-8')
print(f'dist/index.html written, {len(out)//1024} KB')
