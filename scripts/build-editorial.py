from pathlib import Path
import re,html
P=Path(__file__).resolve().parents[1]
fonts=''
for fam,stem in [('Switzer','Switzer'),('Instrument Sans','InstrumentSans'),('Mona Sans','MonaSans'),('Inter','Inter')]:
 for weight in [400,500,600]:
  name=({'400':'Regular','500':'Medium','600':'Semibold'}[str(weight)] if fam=='Switzer' else str(weight))
  fonts+=f"@font-face{{font-family:'{fam}';src:url('assets/fonts/{stem}-{name}.woff2');font-weight:{weight}}}\n"
css=fonts+'''*{box-sizing:border-box}#root{position:absolute;inset:0;width:1920px;height:1080px;overflow:hidden;background:#faf7f5;color:#202323;font-family:Switzer,sans-serif;font-weight:400}.fill{position:absolute;inset:0;width:1920px;height:1080px}.display{position:absolute;margin:0;line-height:1.08;letter-spacing:-.035em;font-weight:400}.small{font-size:27px;letter-spacing:-.01em}.brand-anchor{position:absolute;left:105px;bottom:61px;width:147px;height:auto}.ui-stage{position:absolute;inset:0;width:1920px;height:1080px;overflow:hidden}.gridline{position:absolute;background:#363e3e}.module-item{position:absolute;width:510px;height:345px;text-align:center;color:#faf7f5}.module-item img{display:block;width:140px;height:140px;margin:0 auto}.module-name{font-size:54px;line-height:1.2;letter-spacing:-.035em;margin-top:38px;font-weight:400}.module-detail{font-size:26px;color:#bfc9c5;margin-top:18px}.native-ui h1{font-weight:400!important}.native-ui{font-weight:400}.native-ui [data-ui-prompt]{white-space:normal}'''
css+=' .native-ui [class~="text-[#7c7c7c]"]{color:#707070}.native-ui [class~="text-[#c7c7c7]"]{color:#767676}.native-ui [class~="text-[#d45a08]"]{color:#b94f07}.native-ui [class~="text-[#e03e2d]"]{color:#da3c2c}.native-ui aside [class~="bg-[#f9693c]"]{color:#202323}.native-ui [class~="text-[#737373]/60"]{color:#737373}'
css+=' .native-ui [class~="text-[#737373]"]{color:#707070}.native-ui [class~="text-[#797065]"]{color:#746b60}.native-ui [class~="text-[#e7000b]"]{color:#d7000a}'
ui_css=(P/'scripts/source-ui/ui.css').read_text()
ui_css=re.sub(r'--font-sans:[^;]+;', "--font-sans: 'Instrument Sans', sans-serif;",ui_css)
ui_css=re.sub(r'--font-mono:[^;]+;', '--font-mono: monospace;',ui_css)
for unused in ['Apple Color Emoji','Segoe UI Emoji','Segoe UI Symbol','SFMono-Regular','Noto Color Emoji']:
 ui_css=ui_css.replace('"'+unused+'"','sans-serif').replace(unused,'monospace' if unused=='SFMono-Regular' else 'sans-serif')
nav=(P/'scripts/source-ui/topnav.html').read_text()
nav='<div class="native-ui" style="position:absolute;left:0;top:0;width:1920px;z-index:8;background:#fcfcfb;font-family:Instrument Sans,sans-serif">'+nav+'</div>'
# Native UI CSS is compiled from original TSX and scoped by the Hyperframes compiler.
def ui(kind):
 s=(P/f'scripts/source-ui/{kind}.html').read_text()
 s=s.replace('data-ui-prompt="true"',f'id="{kind}-prompt"')
 if kind in ('describe','request','ready','review'):s=re.sub(r'<img[^>]+src="assets/ui/crator-lockup.svg"[^>]*>','',s)
 move=('transform:translateY(200px) scale(1.16);transform-origin:50% 25%;' if kind=='request' else 'transform:translateY(-180px);' if kind in ('ready','review') else '')
 return f'<div class="ui-stage native-ui" data-layout-allow-overflow style="background:#fcfcfb"><div class="fill" data-layout-allow-overflow style="{move}">{s}</div></div>'
def comp(n,id,d,body,js='',native=False,extra=''):
 s='<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"></head><body><template><style>'+(ui_css if native else '')+css+extra+'</style><div id="root" data-composition-id="'+id+'" data-start="0" data-duration="'+str(d)+'" data-width="1920" data-height="1080">'+body+'</div><script>const tl=gsap.timeline({paused:true});'+js+'window.__timelines["'+id+'"]=tl;</script></template></body></html>'
 (P/f'compositions/frames/{n:02}-{id}.html').write_text(s)
def mark(white=False):
 return '<img class="brand-anchor" src="assets/brand/crator_logo_full_'+('white' if white else 'black')+'.svg" alt="Crator">'
# Background assets extracted from HeyGen's launch film; source recorded in ASSETS.md.
def motion_bg(id,file,start,duration):
 grading=(' data-color-grading="'+html.escape((P/'assets/backgrounds/orbit-gray-grade.json').read_text(),quote=True)+'"') if id=='orbit-grain' else ''
 return f'<video{grading} id="{id}" class="clip fill" src="assets/backgrounds/{file}" data-start="{start}" data-duration="{duration}" muted playsinline style="object-fit:cover;pointer-events:none"></video>'
def paper_bg(id):
 # Exact paper grid spacing from the reference, on Crator's cream brand color.
 return f'<div id="{id}" class="fill" aria-hidden="true" style="background-color:#faf7f5;background-image:linear-gradient(to right,rgba(90,60,10,.07) 1px,transparent 1px),linear-gradient(to bottom,rgba(90,60,10,.07) 1px,transparent 1px);background-size:40px 40px"></div>'
# Connected opening: separate file owns scenes 1–3.
exec((P/'scripts/opening-scenes.py').read_text())
exec((P/'scripts/offer-motion.py').read_text())
exec((P/'scripts/close-motion.py').read_text())
exec((P/'scripts/build-timeline.py').read_text())
