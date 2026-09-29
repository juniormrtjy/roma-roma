from pathlib import Path
from PIL import Image,ImageOps
for n in ['02','03']:
 p=Path('assets/images/hero-romaneiro-'+n+'.jpg'); source=Image.open(p); color=source.getpixel((0,0)); canvas=Image.new('RGB',(1000,1080),color); source=ImageOps.contain(source,(1000,900)); canvas.paste(source,((1000-source.width)//2,(1080-source.height)//2)); canvas.save(p,quality=88,optimize=True)
p=Path('index.html'); s=p.read_text(encoding='utf-8'); s=s.replace('src="assets/images/hero-romaneiro-02.jpg" alt="" width="1200" height="900"','src="assets/images/hero-romaneiro-02.jpg" alt="" width="1000" height="1080"').replace('src="assets/images/hero-romaneiro-03.jpg" alt="" width="1200" height="900"','src="assets/images/hero-romaneiro-03.jpg" alt="" width="1000" height="1080"'); p.write_text(s,encoding='utf-8')
