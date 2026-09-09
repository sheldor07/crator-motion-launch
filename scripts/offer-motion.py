# v39: one continuous trial headline, balanced line and grouped closing hierarchy.
offer_css='''
.offer-world{position:absolute;inset:0;transform-origin:0 0}
.offer-sentence{position:absolute;left:80px;top:373px;width:1760px;text-align:center;font-size:112px;line-height:1.14;letter-spacing:-.04em;color:#202323}
.crator-sentence{position:absolute;left:100px;top:448px;width:1720px;text-align:center;font-size:128px;line-height:1.14;letter-spacing:-.045em;color:#202323}
.plan-sheet{position:absolute;width:1720px;height:650px;background:#fcfcfb;border:1px solid #e5e3df;border-radius:12px;padding:48px 54px;box-shadow:0 10px 0 #d9d8d2,0 23px 28px #2023231b;font-family:Inter,sans-serif;transform-origin:50% 50%}
.plan-heading{font-size:48px;margin-bottom:34px;letter-spacing:-.03em}
.plan-row{height:108px;display:grid;grid-template-columns:360px 1fr;align-items:center;gap:28px;transform-origin:50% 50%}
.plan-label{font-size:34px;white-space:nowrap}.plan-track{height:34px;background:repeating-linear-gradient(90deg,#ecebe8 0 68px,#fcfcfb 68px 72px)}.plan-bar{height:34px;background:#202323;border-radius:6px;transform-origin:0 50%}.plan-row:last-child .plan-bar{background:#df9771}
.implementation-quote{position:absolute;left:2395px;top:1160px;width:960px;height:800px;transform-origin:50% 50%;color:#202323;filter:drop-shadow(0 14px 18px #20232320);font-family:Inter,sans-serif}
.estimate-paper{position:absolute;inset:0;width:960px;height:800px}
.estimate-title{position:absolute;left:56px;top:43px;font-size:48px;font-weight:500;letter-spacing:-.035em}
.estimate-subtitle{position:absolute;left:56px;top:111px;font-size:28px;color:#626561}
.estimate-rule{position:absolute;left:56px;top:176px;width:848px;height:2px;background:#deded8}
.estimate-scope{position:absolute;left:56px;top:202px;font-size:24px;color:#626561}
.estimate-lines{position:absolute;left:56px;top:246px;width:848px}
.estimate-line{height:62px;display:flex;align-items:center;border-bottom:1px solid #e9e9e4;font-size:32px;gap:24px}
.estimate-line-number{font-size:22px;color:#73756f;width:32px}.estimate-included{margin-left:auto;font-size:24px;color:#626561}
.estimate-total-rule{position:absolute;left:56px;top:527px;width:848px;border-top:2px dashed #b9bab3}
.estimate-total-label{position:absolute;left:56px;top:557px;font-size:30px}
.quote-price{position:absolute;left:56px;top:608px;font-size:150px;line-height:1;letter-spacing:-.055em;white-space:nowrap}
.new-plan{left:100px;top:215px;transform-origin:50% 50%}
.price-world{position:absolute;inset:0;transform-origin:450px 600px}
.price-logo{position:absolute;left:360px;top:508px;width:180px;height:180px}
.price-copy{position:absolute;left:610px;top:359px;width:1130px;transform-origin:0 50%}
.price-start{font-size:56px;letter-spacing:-.025em;margin-bottom:20px}.price-value{font-size:280px;line-height:1;letter-spacing:-.06em;white-space:nowrap}.price-unit{font-size:92px;letter-spacing:-.04em;margin-left:12px}
'''
def plan_rows(prefix):
 return ''.join(f'<div id="{prefix}-row-{i}" class="plan-row"><div class="plan-label">{label}</div><div class="plan-track"><div id="{prefix}-bar-{i}" class="plan-bar" style="margin-left:{offset}%;width:{width}%"></div></div></div>' for i,(label,offset,width) in enumerate([('Discovery',0,38),('Data migration',18,55),('Configuration',42,48),('Go-live',87,13)]))
new_sentence='<div id="new-sentence" class="crator-sentence">Crator takes weeks</div>'
body='<div class="fill" style="background:#fcfcfb"></div><div id="old-world" class="offer-world" data-layout-allow-overflow><div id="old-sentence" class="offer-sentence">Traditional implementation<br>takes months</div><div id="old-plan" class="plan-sheet" data-layout-allow-overflow style="left:100px;top:1150px"><div class="plan-heading">Implementation plan</div>'+plan_rows('old')+'</div><div id="implementation-quote" class="implementation-quote" data-layout-allow-overflow><svg class="estimate-paper" viewBox="0 0 960 800" aria-hidden="true"><polygon points="0,0 890,0 960,70 960,800 936,782 912,800 888,782 864,800 840,782 816,800 792,782 768,800 744,782 720,800 696,782 672,800 648,782 624,800 600,782 576,800 552,782 528,800 504,782 480,800 456,782 432,800 408,782 384,800 360,782 336,800 312,782 288,800 264,782 240,800 216,782 192,800 168,782 144,800 120,782 96,800 72,782 48,800 24,782 0,800 0,0" fill="#fcfcfb"/><path d="M890 0 V70 H960" fill="#e8e5df"/></svg><div class="estimate-title">Implementation estimate</div><div class="estimate-subtitle">ERP setup · Professional services</div><div class="estimate-rule"></div><div class="estimate-scope">Scope of work</div><div class="estimate-lines"><div class="estimate-line"><span class="estimate-line-number">01</span><span>Discovery &amp; planning</span><span class="estimate-included">Included</span></div><div class="estimate-line"><span class="estimate-line-number">02</span><span>Data migration</span><span class="estimate-included">Included</span></div><div class="estimate-line"><span class="estimate-line-number">03</span><span>Module customization</span><span class="estimate-included">Included</span></div><div class="estimate-line"><span class="estimate-line-number">04</span><span>Workflow setup</span><span class="estimate-included">Included</span></div></div><div class="estimate-total-rule"></div><div class="estimate-total-label">Estimated total</div><div class="quote-price">$10,000+</div></div></div><div id="offer-paper" class="fill" style="background:#F6F0E8;opacity:0"></div>'+new_sentence.replace('id="new-sentence"','id="old-handoff" style="visibility:hidden"')
js='''
gsap.set('#old-plan',{transformPerspective:1800,rotationY:-12,rotation: -3});
gsap.set('#implementation-quote',{transformPerspective:1800,rotationY:-16,rotation:0});
tl.fromTo('#old-sentence',{y:85,scale:1.08},{y:0,scale:1,duration:.32,ease:'power3.out'},0);
// Leave the sentence by moving down into the actual plan, rather than parking it beside a diagram.
tl.to('#old-world',{x:960-960*.88,y:540-1450*.88,scale:.88,duration:.8,ease:'power2.inOut'},.75);
tl.to('#old-plan',{rotationY:0,rotation:0,duration:.45,ease:'sine.out'},1.1);
tl.fromTo('#old-plan .plan-bar',{scaleX:0},{scaleX:1,duration:.34,stagger:.065,ease:'power2.out'},1.03);
tl.set('#old-sentence',{autoAlpha:0},1.57);
// Follow the long implementation track to the quote at the far end of the same canvas.
tl.to('#old-world',{x:960-2875*1.1,y:540-1560*1.1,scale:1.1,duration:.66,ease:'sine.inOut'},1.6);
tl.to('#implementation-quote',{rotationY:0,rotation:0,duration:.48,ease:'sine.out'},1.78);
tl.set('#old-plan',{autoAlpha:0},2.3);
tl.fromTo('.estimate-line',{x:26,autoAlpha:0},{x:0,autoAlpha:1,duration:.32,stagger:.075,ease:'sine.out'},1.94);
tl.fromTo('.quote-price',{y:22,autoAlpha:0},{y:0,autoAlpha:1,duration:.36,ease:'sine.out'},2.35);
// Dissolve into the replacement sentence without a hard field cut.
tl.to('#old-world',{autoAlpha:0,duration:.22,ease:'sine.inOut'},3.06);
tl.to('#offer-paper',{opacity:1,duration:.36,ease:'sine.inOut'},3.14);
tl.fromTo('#old-handoff',{autoAlpha:0,y:24},{autoAlpha:1,y:0,duration:.22,ease:'sine.out'},3.28);
'''
comp(4,'request',3.5,body,js,extra=offer_css)
offer_css += """
#new-plan{box-shadow:0 10px 0 #ddd4c9,0 23px 28px #20232314}
#price-copy{left:2720px;top:528px;width:1560px;text-align:center;font-size:128px;line-height:1.125;letter-spacing:-.04em;font-weight:400}
.offer-close-headline{position:absolute;left:180px;top:528px;width:1560px;text-align:center;font-size:128px;line-height:1.125;letter-spacing:-.04em;font-weight:400;color:#fcfcfb}
#runway{position:absolute;left:0;top:0;width:4300px;height:1080px;overflow:visible}
"""
body='<div class="fill" style="background:#F6F0E8"></div>'+new_sentence+'<div id="fast-world" class="offer-world" data-layout-allow-overflow><div id="new-plan" class="plan-sheet new-plan" data-layout-allow-overflow style="visibility:hidden"><div class="plan-heading">Implementation plan</div>'+plan_rows('new')+'</div><svg id="runway" viewBox="0 0 4300 1080" aria-hidden="true"><path id="runway-line" d="M830 733 H2200 C2320 733 2320 720 2440 720 H4060" fill="none" stroke="#D77B4E" stroke-width="12" stroke-linecap="round"/><circle id="runway-dot" cx="830" cy="733" r="20" fill="#D77B4E"/></svg><div id="price-copy" class="price-copy" style="visibility:hidden">Start your free trial</div></div><div id="offer-close-ink" class="fill" style="background:#202323;clip-path:polygon(400px 720px,1520px 720px,1520px 720px,400px 720px)"><img id="offer-close-logo" src="assets/brand/crator_logo_full_white.svg" alt="Crator" style="position:absolute;left:750px;top:328px;width:420px;height:130px;object-fit:contain"><div id="offer-close-headline" data-layout-allow-overlap class="offer-close-headline">Start your free trial</div></div>'
js='''
const runway=document.querySelector('#runway-line');
const runwayLength=runway.getTotalLength();
const travel={p:0};
function positionDot(){const p=runway.getPointAtLength(travel.p*runwayLength);gsap.set('#runway-dot',{x:p.x-830,y:p.y-733});}
gsap.set('#runway-line',{strokeDasharray:runwayLength,strokeDashoffset:runwayLength});
gsap.set('#runway-dot,#runway-line',{autoAlpha:0});
// The sentence reads, then a short vertical mask reveals the timeline in place.
tl.to('#new-sentence',{autoAlpha:0,duration:.24,ease:'sine.inOut'},.66);
tl.fromTo('#new-plan',{y:65,autoAlpha:0},{y:0,autoAlpha:1,duration:.44,ease:'sine.out'},.92);
// The actual bars contract; the sheet stays intact, with no fold or logo morph.
tl.to('#new-plan .plan-bar',{x:(i)=>-[0,219.96,513.24,1063.14][i]+i*80,scaleX:.3,duration:.4,stagger:.035,ease:'sine.inOut'},1.24);
tl.set('#runway-dot,#runway-line',{autoAlpha:1},1.72);
tl.to('#runway-line',{strokeDashoffset:0,duration:1,ease:'sine.inOut'},1.72);
tl.to(travel,{p:1,duration:1,ease:'sine.inOut',onUpdate:positionDot},1.72);
// One continuous camera curve has zero velocity at both ends, with no mid-flight gear change.
tl.to('#fast-world',{x:-2540,y:0,scale:1,duration:1.02,ease:'sine.inOut'},1.72);
tl.set('#new-plan',{autoAlpha:0},2.74);
tl.fromTo('#price-copy',{y:40,autoAlpha:0},{y:0,autoAlpha:1,duration:.36,ease:'sine.out'},2.38);
// Retract the incoming tail so the resting line shares the headline center and width.
tl.to('#runway-dot',{scale:0,duration:.2,ease:'sine.inOut'},2.72);
tl.to('#runway-line',{strokeDashoffset:-(runwayLength-1120),duration:.46,ease:'sine.inOut'},2.76);
// The aligned line opens into ink. The overlap allowance is only for the exact white duplicate inside the opaque reveal mask; the two copies share every glyph position.
tl.to('#runway-line',{stroke:'#202323',duration:.22,ease:'sine.inOut'},3.3);
tl.to('#offer-close-ink',{clipPath:'polygon(0px 0px,1920px 0px,1920px 1080px,0px 1080px)',duration:.66,ease:'sine.inOut'},3.34);
tl.fromTo('#offer-close-logo',{y:20,autoAlpha:0},{y:0,autoAlpha:1,duration:.36,ease:'sine.out'},3.64);
'''
comp(5,'result',4,body,js,extra=offer_css)
