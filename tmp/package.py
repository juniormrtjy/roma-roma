from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import json,re,xml.etree.ElementTree as ET
root=Path.cwd(); html=(root/'index.html').read_text(encoding='utf-8'); json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',html,re.S).group(1)); ET.parse('sitemap.xml')
with ZipFile('romaneiro-site.zip','w',ZIP_DEFLATED) as archive:
 for name in ['index.html','README.md','robots.txt','sitemap.xml']: 
  if Path(name).is_file(): archive.write(name,name)
 for folder in ['css','js','assets','docs']:
  for p in Path(folder).rglob('*'):
   if p.is_file(): archive.write(p,p.as_posix())
print('ZIP:',Path('romaneiro-site.zip').stat().st_size,'bytes')
print('Files:',len(ZipFile('romaneiro-site.zip').namelist()))
