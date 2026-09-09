# v26: business objects -> native composer -> send-button camera dive.
describe_chair=chair.replace('id="chair','id="describe-chair').replace('left:330px;top:570px','left:420px;top:305px')
desc_css='''
#business-input .native-ui>div{height:236px;min-height:236px}
#business-input .native-ui>div>div:first-child{height:138px;min-height:138px;flex:none}
#composer-footer{height:96px;padding:14px 26px 22px}
#composer-actions{gap:14px}
#composer-attachment,#composer-usage,#composer-send{width:60px;height:60px;flex:none}
#composer-send,#composer-attachment{border-radius:15px}
#composer-model{height:60px;gap:11px;padding:0 16px}
#composer-model span{font-size:26px;line-height:1}
#composer-model svg{width:26px;height:26px}
#composer-attachment svg,#composer-send svg{width:34px;height:34px}
#composer-usage svg{width:40px;height:40px}

.describe-world{position:absolute;inset:0;transform-origin:0 0}
.business-sheet{position:absolute;left:1020px;top:45px;width:700px;height:320px;background:#fcfcfb;color:#202323;padding:28px 36px;border-radius:8px;font-family:Inter,sans-serif;box-shadow:0 7px 0 #d3cec5,0 14px 0 #e8e3db,0 28px 36px #20232325;transform-origin:50% 50%}
.business-sheet strong{font-size:40px;font-weight:500}.business-sheet div{font-size:30px;border-bottom:1px solid #ddd;padding:12px 0;display:flex;justify-content:space-between}
.business-sheet .sheet-heading{align-items:center;justify-content:flex-start;gap:18px;padding:0 0 18px;margin-bottom:8px}
'''
body=paper_bg('describe-paper')+'<div id="business-orange" class="fill" style="background:#FFDAB6;clip-path:circle(0px at 420px 305px)"></div><div id="describe-title" class="display" style="left:160px;top:478px;width:1600px;text-align:center;font-size:112px">Describe your business.</div><div id="describe-world" class="describe-world" data-layout-allow-overflow>'+describe_chair+'<div id="business-sheet" class="business-sheet" data-layout-allow-overflow><div class="sheet-heading"><svg width="52" height="60" viewBox="0 0 52 60" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Spreadsheet" style="flex:none"><path d="M5 0H34L52 18V55Q52 60 47 60H5Q0 60 0 55V5Q0 0 5 0Z" fill="#217346"/><path d="M34 0V18H52" fill="#49A274"/><path d="M10 27H42V49H10Z M10 34H42 M10 42H42 M21 27V49 M32 27V49" stroke="white" stroke-width="2.4" stroke-linejoin="round"/></svg><strong>Inventory.csv</strong><span style="font-size:26px;margin-left:auto">CSV</span></div><div><span>Dining chairs</span><span>100</span></div><div><span>Timber</span><span>400</span></div></div>'+big_input('business-input','I run a furniture business. Set up stock, production and accounting.')+'</div>'+cursor('business-cursor')+'<div id="describe-ink" class="fill" style="background:#202323;clip-path:circle(0px at 960px 540px)"></div><div id="describe-handoff" style="position:absolute;left:160px;top:440px;width:1600px;text-align:center;font-size:104px;line-height:1.1;letter-spacing:-.04em;color:#fcfcfb;visibility:hidden">Migrating your data.</div>'
js='''
const text=document.getElementById('business-input-prompt');const sentence=text.textContent;text.textContent='';const typing={n:0};
gsap.set('#business-input',{scale:1.9,autoAlpha:0});
gsap.set('#business-sheet',{autoAlpha:0,transformPerspective:1200,rotationY:-12,rotation:3});
gsap.set('#business-cursor',{x:1900,y:1180});
for(const e of document.querySelectorAll('#business-input span')){if(!e.children.length&&e.textContent.trim()==='GPT-6 Astra'){e.parentElement.id='composer-model';e.parentElement.nextElementSibling.id='composer-usage';e.parentElement.parentElement.id='composer-actions';e.parentElement.parentElement.lastElementChild.id='composer-send';e.parentElement.parentElement.parentElement.id='composer-footer';e.parentElement.parentElement.parentElement.firstElementChild.id='composer-attachment';}}
tl.to('#composer-model,#composer-usage',{opacity:0,duration:.18},2.4);
tl.to('#describe-title',{x:-1920,scale:1.3,duration:.42,ease:'power3.in'},.18);
tl.set('#describe-title',{autoAlpha:0},.62);
tl.to('#business-orange',{clipPath:'circle(1900px at 420px 305px)',duration:.62,ease:'power3.inOut'},.3);
tl.fromTo('#describe-chair-stage',{autoAlpha:0,x:-450,y:-200,scale:.5},{autoAlpha:1,x:0,y:0,scale:.78,duration:.6,ease:'power3.out'},.38);
tl.fromTo('#describe-chair-model',{rotationY:-90},{rotationY:-20,duration:.9,ease:'power3.out'},.4);
tl.fromTo('#business-sheet',{autoAlpha:0,x:550,y:-180},{autoAlpha:1,x:0,y:0,rotationY:0,duration:.62,ease:'power3.out'},.5);
tl.fromTo('#business-input',{y:560,autoAlpha:0,rotation:-4},{y:0,autoAlpha:1,rotation:0,duration:.5,ease:'power3.out'},.45);
tl.to(typing,{n:sentence.length,duration:1.4,ease:'none',onUpdate:()=>text.textContent=sentence.slice(0,Math.floor(typing.n))},.72);
// The prompt grows to fill the feed while its business context passes behind it.
tl.to('#describe-world',{x:-80,y:-40,scale:1.08,duration:1.25,ease:'power1.inOut'},1.03);
tl.to('#business-sheet',{rotationY:0,rotation:0,duration:1.16,ease:'power1.inOut'},1.12);
tl.to('#business-cursor',{x:1661,y:773,duration:.35,ease:'power3.out'},2.2);
// A macro dive follows the send control, then the control supplies the dark reveal.
tl.to('#describe-world',{x:960-1612*2.8,y:540-753*2.8,scale:2.8,duration:.52,ease:'power3.inOut'},2.58);
tl.to('#business-cursor',{x:960,y:540,duration:.52,ease:'power3.inOut'},2.58);
tl.to('#describe-ink',{clipPath:'circle(1300px at 960px 540px)',duration:.37,ease:'power3.in'},3.18);
tl.to('#business-cursor',{x:2050,y:1000,duration:.3,ease:'power3.in'},3.23);
tl.set('#describe-world',{autoAlpha:0},3.56);
tl.fromTo('#describe-handoff',{autoAlpha:0,x:80},{autoAlpha:1,x:0,duration:.3,ease:'power3.out'},3.5);
'''+tap('business-cursor',3.14)
comp(2,'describe',4,body,js,True,extra=midcss+story_css+desc_css)
