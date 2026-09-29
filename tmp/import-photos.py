from pathlib import Path
from PIL import Image, ImageOps
import shutil,json
source=Path(r'C:\Users\victo\AppData\Local\Temp')
received=Path('tmp/fotos-recebidas'); received.mkdir(parents=True,exist_ok=True)
photos=[
 ('codex-clipboard-f8820971-89ff-420a-afaa-98ab4fc0cdd4.png',['hero-romaneiro.jpg','projeto-02.jpg']),
 ('codex-clipboard-524a08ba-29dc-4481-9f44-17c20500e286.png',['sobre-romaneiro.jpg']),
 ('codex-clipboard-ac928fc2-a567-4bcd-b7b0-4969eea74c04.png',['hero-romaneiro-02.jpg']),
 ('codex-clipboard-66570c73-d290-46cd-b974-cd0a839bc4a5.png',['projeto-01.jpg']),
 ('codex-clipboard-c7c073c6-9db9-4189-ab06-cbdece2dcebf.png',['gondola-azeites-lateral.jpg']),
 ('codex-clipboard-91b4b20d-0546-450d-8149-52a078cf8b77.png',['hero-romaneiro-03.jpg','projeto-03.jpg']),
 ('codex-clipboard-13d3ff48-8e85-4ed6-b28c-460245337eb4.png',['gondola-azeites-frontal.jpg']),
 ('codex-clipboard-b0346f29-fa37-44b3-954c-588174fad7f5.png',['weber-haus-registro-pdv.jpg'])]
report=[]
for i,(name,targets) in enumerate(photos,1):
 original=source/name
 assert original.exists(),original
 shutil.copy2(original,received/('foto-'+str(i).zfill(2)+'.png'))
 image=ImageOps.exif_transpose(Image.open(original)).convert('RGB')
 # Apenas exportação web: manter composição, pessoas, produtos e inscrições originais.
 for target in targets:
  output=Path('assets/images')/target
  image.save(output,quality=86,optimize=True,progressive=True)
  report.append({'file':target,'width':image.width,'height':image.height,'bytes':output.stat().st_size})
print(json.dumps(report,ensure_ascii=False,indent=2))
Path('tmp/fotos-recebidas/manifesto.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
