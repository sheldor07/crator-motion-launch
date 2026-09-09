# v4 opening: continuous product demonstration. Uses original composer and ERP rail.
def element_at(s, start):
 tag=re.match(r'<([\w-]+)',s[start:]).group(1)
 depth=0
 for m in re.finditer(r'</?'+tag+r'\b[^>]*>',s[start:]):
  depth+=-1 if m.group().startswith('</') else 1
  if depth==0:return s[start:start+m.end()]
 raise ValueError('Unclosed '+tag)
source=(P/'scripts/source-ui/describe.html').read_text()
pos=source.index('<div class="relative z-10 flex min-h-[144px]')
composer=element_at(source,pos)
composer=re.sub(r'<span data-ui-prompt="true">.*?</span>','<span data-ui-prompt="true">I run a manufacturing business. We make furniture. Set up inventory, production and accounting.</span>',composer)
composer=composer.replace('GPT-5.6 Sol','GPT-6 Astra')
# Native cursor is retained, but all surrounding app chrome is removed.
def input_ui(prefix):return '<div class="native-ui" style="width:800px;font-family:Instrument Sans,sans-serif">'+composer.replace('data-ui-prompt="true"',f'id="{prefix}-prompt"')+'</div>'
# v40: recognizable Lovable lockup from frame one, then the existing complete analogy and ERP modules.
mods=[('Inventory','stock.svg'),('Manufacturing','manufacturing.svg'),('Accounting','accounting.svg'),('Sales','selling.svg'),('Purchasing','buying.svg'),('CRM','crm.svg')]
hook=paper_bg('hook-paper').replace('background-color:', 'opacity:0;background-color:')
hook+='<div id="erp-lens" class="fill" data-layout-allow-overflow style="transform-origin:0 0"><div id="hook-camera" class="fill" data-layout-allow-overflow style="z-index:2"><div id="hook-pan" class="fill" data-layout-allow-overflow><div id="hook-line" style="position:absolute;left:120px;top:432px;width:1680px;height:210px;display:flex;align-items:center;justify-content:center;gap:24px;white-space:nowrap;letter-spacing:-.055em;font-size:140px;font-weight:600"><span id="hook-meet">Meet</span><span id="hook-brand" style="position:relative;display:flex;align-items:center;gap:24px"><img id="hook-lovable" src="assets/brand/lovable.svg" alt="Lovable" style="width:110px;height:110px;flex-shrink:0"><span id="hook-name">Lovable</span></span><span id="hook-for">for</span><span id="hook-erp">ERP</span></div></div></div>'
for i,(label,icon) in enumerate(mods):
 hook+=f'<div id="map-module-{i}" class="map-module" data-layout-allow-overflow><div id="satellite-{i}" class="satellite"><img src="assets/erpnext/pastel/{icon}" alt=""><span>{label}</span></div></div>'
hook+='<div id="intro-next" class="display" data-layout-allow-overflow style="left:4360px;top:478px;width:1600px;text-align:center;font-size:112px;visibility:hidden">Describe your business.</div></div>'
js='''
gsap.set('#erp-lens,.map-module,.satellite',{force3D:false});
const lens={cx:960,cy:540,zoom:1};
function placeLens(){gsap.set('#erp-lens',{x:960-lens.cx*lens.zoom,y:540-lens.cy*lens.zoom,scale:lens.zoom});}
// Tighten the entire orbit around the same optical center.
tl.to(lens,{zoom:1.18,duration:.5,ease:'power3.inOut',onUpdate:placeLens},1.25);
// Center the complete lockup using the settled native wordmark geometry.
const brand=document.querySelector('#hook-brand');
const brandX=960-(120+brand.offsetLeft+brand.offsetWidth/2);
gsap.set('#hook-meet,#hook-for,#hook-erp',{autoAlpha:0});
tl.fromTo('#hook-brand',{x:brandX,y:3,scale:1.65},{x:brandX,y:3,scale:1.5,duration:.24,ease:'power2.out'},0);
tl.fromTo('#hook-lovable',{scale:1.18,rotation:-16},{scale:1,rotation:0,duration:.24,ease:'power2.out'},0);
tl.to('#hook-brand',{x:0,y:0,scale:1,duration:.36,ease:'sine.inOut'},.26);
tl.fromTo('#hook-meet,#hook-for,#hook-erp',{y:28,autoAlpha:0},{y:0,autoAlpha:1,duration:.3,stagger:.035,ease:'sine.out'},.42);
tl.to('#hook-meet,#hook-lovable,#hook-name,#hook-for',{opacity:0,duration:.18,ease:'power2.in'},1.2);
tl.to('#hook-erp',{x:-567.32,y:-1.5,scale:1.5,duration:.45,ease:'power3.inOut'},1.2);
const arrangement={line:0,orbit:0};
function placeModules(){
 for(let i=0;i<6;i++){
  const a=(i*60+200)*Math.PI/180+arrangement.orbit;
  const ox=Math.cos(a)*710,oy=Math.sin(a)*310,tilt=-Math.PI/18;
  const sx=960+ox*Math.cos(tilt)-oy*Math.sin(tilt);
  const sy=540+ox*Math.sin(tilt)+oy*Math.cos(tilt);
  const tx=960+i*540,ty=540,f=arrangement.line,u=1-f;
  const x=u*u*sx+2*u*f*(sx+(tx-sx)*.65)+f*f*tx;
  const y=u*u*sy+2*u*f*(sy+(sy<540?-90:90))+f*f*ty;
  const depth=(Math.sin(a)+1)/2;
  gsap.set('#map-module-'+i,{x:x-960,y:y-540,scale:(.9+.16*depth)*(1-f)+f,zIndex:depth>.5||f>.1?4:1});
 }
}
placeModules();
tl.to(arrangement,{orbit:.28,duration:.85,ease:'none',onUpdate:placeModules},1.45);
// The same icons peel off the orbit into a horizontal path past the lens.
tl.to('#hook-erp',{opacity:0,duration:.15},2.23);
tl.to(arrangement,{line:1,duration:.36,ease:'power3.inOut',onUpdate:placeModules},2.27);
tl.to(lens,{zoom:2.3,duration:.3,ease:'power3.inOut',onUpdate:placeLens},2.35);
// Ease into the first icon, then accelerate along the line instead of a constant-speed sweep.
tl.to(lens,{cx:3660,duration:.83,ease:'power1.in',onUpdate:placeLens},2.65);
tl.set('#intro-next',{autoAlpha:1},3.48);
// Continue at almost the same world velocity, then brake as the headline fills the frame.
tl.to(lens,{cx:5160,duration:.46,ease:'power1.out',onUpdate:placeLens},3.48);
tl.to(lens,{zoom:1,duration:.46,ease:'power1.inOut',onUpdate:placeLens},3.48);
tl.to('#hook-paper',{opacity:1,duration:.24,ease:'sine.inOut'},3.7);
'''
for i,_ in enumerate(mods):
 js+=f"tl.fromTo('#satellite-{i}',{{opacity:0,y:90,rotation:-9,scale:.55}},{{opacity:1,y:0,rotation:0,scale:1,duration:.3,ease:'power3.out'}},{1.45+i*.025});\n"
comp(1,'hook',4,hook,js,extra='''
#root{background:#fcfcfb}.map-module{position:absolute;left:830px;top:425px;width:260px;height:230px;transform-origin:50% 50%}
.satellite{display:flex;flex-direction:column;align-items:center;gap:20px;font-size:36px;letter-spacing:-.025em;opacity:0}
.satellite img{width:168px;height:168px;object-fit:contain;border-radius:46px;box-shadow:0 7px 0 #0000000d,0 17px 22px #20232312}
''')
# Build after fonts resolve so the centered logo uses the final native wordmark geometry.
hook_file=P/'compositions/frames/01-hook.html'
hook_html=hook_file.read_text().replace('<script>const tl=gsap.timeline({paused:true});','<script>document.fonts.ready.then(()=>{const tl=gsap.timeline({paused:true});').replace('window.__timelines["hook"]=tl;</script>','window.__timelines["hook"]=tl;});</script>')
hook_file.write_text(hook_html)
exec((P/'scripts/product-middle.py').read_text())
