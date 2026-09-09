# Fifteen-second product story: giant prompt → native setup → rule request → tested result.
exec((P/'scripts/erpnext-demo-records.py').read_text())
midcss='''
#setup-warehouses,#setup-bom,#setup-accounts{opacity:1;visibility:visible}

.mid-status{position:absolute;left:200px;top:76px;font:32px 'Instrument Sans',sans-serif;display:flex;align-items:center;gap:18px}.mid-status img{width:36px;height:36px}.mid-title{position:absolute;left:200px;top:132px;font-size:80px;line-height:1.05;letter-spacing:-.04em}.mid-viewport{position:absolute;left:216px;top:254px;width:1488px;height:630px;overflow:hidden;background:white;border:1px solid #dedbd6;border-radius:12px;box-shadow:0 20px 70px #20232315;font-family:Inter,sans-serif}.mid-page{position:absolute;left:0;top:0;width:850px;height:653px;transform-origin:0 0}.mid-page .erp-page{position:absolute;inset:0;opacity:1;visibility:visible}.mid-progress{position:absolute;left:200px;top:957px;width:1520px;height:10px;background:#e3dfd8;overflow:hidden;border-radius:5px}.mid-fill{width:100%;height:100%;background:#ff7134;transform-origin:0 50%}.mid-progress-label{position:absolute;left:200px;top:908px;font-size:30px}.mid-count{position:absolute;right:200px;top:908px;font-size:30px}.mid-cursor{position:absolute;left:0;top:0;width:134px;height:168px;z-index:30;pointer-events:none;transform-origin:8px 8px;filter:drop-shadow(0 4px 6px #0004)}.big-composer .native-ui{width:800px}.big-composer .native-ui>div{min-height:212px}.big-composer .native-ui>div>div:first-child{font-size:32px;line-height:1.4;padding:24px 26px}.big-composer .native-ui>div>div:first-child>span:last-child{height:33px}.big-composer .native-ui>div>div:last-child{padding:10px 20px 18px}.big-composer .native-ui>div>div:last-child>div>span:last-child{background:#ff7134}.mid-note{position:absolute;left:200px;top:916px;font-size:30px}.mid-chip{padding:8px 16px;border-radius:7px;background:#e6f3eb;color:#236244;font-size:26px}.native-detail{position:absolute;width:850px;height:653px;font-family:Inter,sans-serif;background:#fff;color:#383838;transform-origin:0 0}#rule-preview{left:740px!important;top:132px!important;width:1105px!important;height:835px!important}#rule-preview .native-detail,#result-order .native-detail{color:#383838}.native-detail .erp-field{font-size:13px}.native-detail .erp-value{font-size:16px;padding:10px 12px}.native-detail .erp-field-row{gap:24px;margin-bottom:24px}.native-detail .erp-title{font-size:25px}.native-detail .erp-section{font-size:15px}.native-detail .erp-grid-row{font-size:13px;min-height:38px}#result-order .erp-grid-row{grid-template-columns:34px 1.15fr 1.05fr 45px 110px}#result-order{left:740px;top:180px;width:1105px;height:787px}#root .result-headline{left:100px;top:300px;width:560px;font-size:98px;line-height:1.03}#root .result-headline span{display:block}#root .result-status{left:100px;top:75px}#root #result-note{left:100px;top:810px;width:520px;font-size:32px;line-height:1.3}#rule-after-title{position:absolute;left:100px;top:300px;width:560px;font-size:98px;line-height:1.05;color:#fcfcfb;opacity:0}#rule-after-title span{display:block}#root #rule-building .mid-progress{left:100px;top:935px;width:510px}#root #rule-building .mid-progress-label{left:100px;top:800px;width:510px;font-size:32px}
'''
def cursor(id):
 return f'<svg id="{id}" class="mid-cursor" data-layout-allow-overflow viewBox="0 0 64 80" aria-hidden="true"><path d="M4 4V61L18 47L30 73L42 67L29 42L52 39Z" fill="#202323" stroke="white" stroke-width="2.5" stroke-linejoin="round"/></svg>'
def tap(id,t):return f"tl.to('#{id}',{{scale:.84,duration:.09,ease:'power2.in'}},{t});tl.to('#{id}',{{scale:1,duration:.18,ease:'power2.out'}},{t+.09});\n"
def big_input(id,sentence):
 return '<div id="'+id+'" class="big-composer" style="position:absolute;left:200px;top:405px;width:800px;transform-origin:0 0">'+input_ui(id).replace('I run a manufacturing business. We make furniture. Set up inventory, production and accounting.',sentence)+'</div>'
def progress(id,text,count):return f'<div id="{id}-label" class="mid-progress-label">{text}</div><div id="{id}-count" class="mid-count">{count}</div><div class="mid-progress"><div id="{id}-fill" class="mid-fill"></div></div>'
def status(text):return '<div class="mid-status"><img src="assets/brand/crator_logo_icon_only_black.svg" alt="Crator"><span>'+text+'</span></div>'
# 6–10s: native composer expanded to 1520px, with 61px prompt text on the video canvas.
sentence='We make furniture. Set up stock, production and accounting.'
body=paper_bg('describe-paper')+'<div id="describe-title" class="display" style="left:160px;top:478px;width:1600px;text-align:center;font-size:112px">Describe your business.</div>'+big_input('business-input',sentence)+cursor('business-cursor')+'<div id="describe-ink" class="fill" data-layout-allow-overflow style="background:#202323"></div><div id="describe-handoff" style="position:absolute;left:160px;top:440px;width:1600px;text-align:center;font-size:104px;line-height:1.1;letter-spacing:-.04em;color:#fcfcfb;visibility:hidden">Migrating your data.</div>'
js="""
const text=document.getElementById('business-input-prompt');const sentence=text.textContent;text.textContent='';const typing={n:0};
tl.to('#describe-title',{y:-280,scale:.82,duration:.4,ease:'power3.inOut'},.15);
tl.fromTo('#business-input',{scale:1.9,y:100,opacity:0},{scale:1.9,y:0,opacity:1,duration:.4,ease:'expo.out'},.3);
tl.to(typing,{n:sentence.length,duration:1.95,ease:'none',onUpdate:()=>text.textContent=sentence.slice(0,Math.floor(typing.n))},.65);
tl.fromTo('#business-cursor',{x:1640,y:1160},{x:1640,y:746,duration:.5,ease:'power3.out'},2.65);
gsap.set('#describe-ink',{x:1920});
tl.to('#describe-ink',{x:0,duration:.3,ease:'power3.inOut'},3.4);
tl.set('#business-input,#describe-title',{autoAlpha:0},3.7);
tl.fromTo('#describe-handoff',{autoAlpha:0,x:80},{autoAlpha:1,x:0,duration:.3,ease:'power3.out'},3.7);
tl.to('#business-input',{scale:1.86,duration:.09,ease:'power2.in'},3.2);
tl.to('#business-input',{scale:1.9,duration:.18,ease:'power2.out'},3.3);
tl.to('#business-cursor',{x:1980,y:890,duration:.4,ease:'power2.in'},3.5);
"""+tap('business-cursor',3.2)
comp(2,'describe',4,body,js,True,extra=midcss)
exec((P/'scripts/build-montage.py').read_text())

# 16–18s: implementation cost and duration, supplied by the user.
costcss='''
.cost-kicker{position:absolute;left:180px;top:145px;font-size:40px;letter-spacing:-.02em}.cost-time{position:absolute;left:180px;top:300px;font-size:144px;letter-spacing:-.045em;line-height:1.05}.cost-price{position:absolute;left:180px;top:590px;display:flex;align-items:baseline;gap:24px;font-size:190px;letter-spacing:-.055em;line-height:1.05}.cost-unit{font-size:68px;letter-spacing:-.035em}.cost-label{position:absolute;left:187px;top:531px;font-size:36px}.cost-strike{position:absolute;left:170px;top:691px;width:980px;height:7px;background:#202323;transform-origin:0 50%}.cost-rail{position:absolute;right:160px;top:170px;width:7px;height:740px;background:#20232320}.cost-tick{position:absolute;right:0;width:65px;height:4px;background:currentColor}
'''
body=paper_bg('cost-paper')+'<div class="cost-kicker">Traditional implementation</div><div id="old-time" class="cost-time">Months.</div><div class="cost-label">Implementation cost</div><div id="old-price" class="cost-price">$10,000+</div><div id="cost-strike" class="cost-strike"></div><div class="cost-rail">'+''.join(f'<div class="cost-tick" style="top:{i*92}px"></div>' for i in range(9))+'</div>'
js='''
tl.fromTo('#old-time',{y:55,opacity:0},{y:0,opacity:1,duration:.35,ease:'expo.out'},0);
tl.fromTo('#old-price',{y:55,opacity:0},{y:0,opacity:1,duration:.35,ease:'expo.out'},.15);
tl.fromTo('#cost-strike',{scaleX:0},{scaleX:1,duration:.28,ease:'power3.inOut'},1.45);
'''
comp(4,'request',2,body,js,extra=costcss)
# 18–21s: exact same typographic anchors invert to Crator's offer.
body='<div class="fill" style="background:#202323"></div><div class="cost-kicker" style="color:#fcfcfb">With Crator</div><div id="new-time" class="cost-time" style="color:#fcfcfb">Weeks.</div><div class="cost-label" style="color:#fcfcfb">Starting from</div><div id="new-price" class="cost-price" style="color:#fcfcfb"><span>$150</span><span class="cost-unit">/mo</span></div><div id="price-line" style="position:absolute;left:180px;top:845px;width:540px;height:6px;background:#fcfcfb;transform-origin:0 50%"></div>'
js='''
tl.fromTo('#new-time',{y:35,opacity:0},{y:0,opacity:1,duration:.35,ease:'expo.out'},0);
tl.fromTo('#new-price',{y:35,opacity:0},{y:0,opacity:1,duration:.35,ease:'expo.out'},.12);
tl.fromTo('#price-line',{scaleX:0},{scaleX:1,duration:.45,ease:'power3.inOut'},.55);
'''
comp(5,'result',3,body,js,extra=costcss)

# v26 applies the approved spatial direction to the business prompt.
exec((P/'scripts/describe-motion.py').read_text())
