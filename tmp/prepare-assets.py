from PIL import Image
from pathlib import Path
source=Path(r'C:\Users\victo\Downloads')
for src,dst,size in [('logo+texto nova preta.png','logo-romaneiro-preta.png',480),('logo+texto nova branca.png','logo-romaneiro-branca.png',480),('logo+texto nova dourada.png','logo-romaneiro-dourada.png',480),('logo nova dourada.png','simbolo-romaneiro-dourado.png',900),('logo nova branca.png','simbolo-romaneiro-branco.png',700),('logo nova preta.png','simbolo-romaneiro-preto.png',700)]:
    im=Image.open(source/src); print(src,im.mode,im.getextrema()); im.thumbnail((size,size),Image.Resampling.LANCZOS); im.save(Path('assets/images')/dst,optimize=True)
im=Image.open(source/'logo nova dourada.png'); im.thumbnail((64,64),Image.Resampling.LANCZOS); im.save('assets/icons/favicon.png')
# Neutral replacement slots; abstract design is authored in CSS, not in photos.
for name,color in [('hero-romaneiro','#172D43'),('sobre-romaneiro','#d9ded5'),('projeto-01','#dedfd3'),('projeto-02','#e7c5af'),('projeto-03','#cad8e0')]:
    Image.new('RGB',(1200,900),color).save('assets/images/'+name+'.jpg',quality=80,optimize=True)
