from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
p=Path('assets/images'); fontpath=Path(r'C:\Windows\Fonts\segoeui.ttf')
for i,(color,word,small) in enumerate([('#dedfd3','Presença.','NO PONTO DE VENDA'),('#e7c5af','Experiência.','EM CADA DESCOBERTA'),('#cad8e0','Conexão.','EM CADA DETALHE')],1):
 im=Image.new('RGB',(1200,900),color); d=ImageDraw.Draw(im)
 for k in range(4): d.rectangle((470+k*75,-200+k*75,1250+k*75,650+k*75),outline='#ffffff',width=3)
 d.text((145,240),'R / '+str(i).zfill(2),font=ImageFont.truetype(str(fontpath),25),fill='#283d37')
 d.text((140,430),word,font=ImageFont.truetype(str(fontpath),100),fill='#283d37'); d.text((145,565),small,font=ImageFont.truetype(str(fontpath),25),fill='#283d37')
 im.save(p/('projeto-'+str(i).zfill(2)+'.jpg'),quality=85,optimize=True)
p=Path('index.html'); s=p.read_text(encoding='utf-8').replace('src="assets/images/hero-romaneiro.jpg" alt="" width="1200" height="900"','src="assets/images/hero-romaneiro.jpg" alt="" width="1000" height="1080"').replace('src="assets/images/sobre-romaneiro.jpg" alt="" width="1200" height="900"','src="assets/images/sobre-romaneiro.jpg" alt="" width="1200" height="1100"');p.write_text(s,encoding='utf-8')
