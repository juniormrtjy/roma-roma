from pathlib import Path
from html.parser import HTMLParser
import re,json,xml.etree.ElementTree as ET
class PrettyHTML(HTMLParser):
    void={'meta','link','img','input','br','hr','source','wbr','area','base','col','embed','param','track'}
    def __init__(self): super().__init__(convert_charrefs=False); self.depth=0; self.lines=[]; self.stack=[]
    def emit(self,s): self.lines.append('  '*self.depth+s)
    def handle_decl(self,s): self.emit('<!'+s+'>')
    def handle_comment(self,s): self.emit('<!--'+s+'-->')
    def handle_starttag(self,t,a):
        self.emit(self.get_starttag_text())
        if t not in self.void: self.depth+=1; self.stack.append(t)
    def handle_endtag(self,t):
        if not self.stack or self.stack[-1]!=t: raise ValueError('Tag mismatch '+t+' '+str(self.stack[-4:]))
        self.depth-=1; self.stack.pop(); self.emit('</'+t+'>')
    def handle_data(self,s):
        if s.strip():
            for line in s.strip().splitlines(): self.emit(line.strip())
    def handle_entityref(self,s): self.emit('&'+s+';')
    def handle_charref(self,s): self.emit('&#'+s+';')
p=Path('index.html'); parser=PrettyHTML(); parser.feed(p.read_text(encoding='utf-8')); assert not parser.stack; p.write_text('\n'.join(parser.lines)+'\n',encoding='utf-8')
p=Path('css/style.css'); s=p.read_text(encoding='utf-8')
# Remove obsolete CSS from the initial HTML-only composition; images now replace directly.
for selector in ['.visual-composition','.visual-kicker','.hero-symbol','.visual-word','.visual-index','.orbit','.orbit-two']:
    s=re.sub(re.escape(selector)+r'\s*\{[^}]*\}\s*','',s)
s=s.replace('font-size: .65rem','font-size: .75rem').replace('font-size: .68rem','font-size: .75rem').replace('font-size: .7rem','font-size: .75rem')
s=re.sub(r'\s*\{\s*',' {\n',s); s=re.sub(r';\s*',';\n',s); s=re.sub(r'\s*\}\s*','\n}\n',s)
lines=[]; depth=0
for line in s.splitlines():
    line=line.strip()
    if not line: continue
    if line.startswith('}'): depth-=1
    if line.startswith('/*') and lines: lines.append('')
    lines.append('  '*max(depth,0)+line)
    if line.endswith('{'): depth+=1
assert depth==0
p.write_text('\n'.join(lines)+'\n',encoding='utf-8')
html=Path('index.html').read_text(encoding='utf-8')
assert len(re.findall(r'<h1\b',html))==1
ids=re.findall(r'\bid="([^"]+)"',html); assert len(ids)==len(set(ids))
for src in re.findall(r'(?:src|href)="([^"]+)"',html):
    if src.startswith('#'): assert src[1:] in ids,src
    elif not re.match(r'\w+:',src): assert Path(src).exists(),src
schema=re.search(r'<script type="application/ld\+json">(.*?)</script>',html,re.S).group(1); json.loads(schema)
ET.parse('sitemap.xml')
print('HTML nesting, unique IDs, anchors, assets, JSON-LD and XML: OK')
print('Total public bytes:',sum(p.stat().st_size for p in [Path('index.html'),Path('css/style.css'),Path('js/script.js'),Path('robots.txt'),Path('sitemap.xml')])+sum(p.stat().st_size for p in Path('assets').rglob('*') if p.is_file()))
