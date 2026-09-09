# v23: dimensional import, chair assembly, manufacturing reveal, workflow dive.
# v22: centered introduction -> import -> selected chair -> production -> approval.
# The window and cursor carry the story. No counter, checklist, duplicate status or footer.
story_css='''
.story-mask{position:absolute;inset:0;clip-path:inset(164px 160px 86px 160px round 14px)}
.story-mask{transform-origin:50% 50%;filter:drop-shadow(0 24px 24px #0002)}
.story-camera{position:absolute;left:0;top:0;width:850px;height:653px;background:white;transform-origin:0 0;font-family:Inter,sans-serif;color:#383838;overflow:hidden;border-radius:10px}
.story-page{position:absolute;inset:0;background:white;overflow:hidden}.story-page .erp-page{opacity:1;visibility:visible}
#story-bom,#story-workflow{visibility:hidden}.story-camera .erp-footer{display:none}
.story-intro{position:absolute;left:160px;top:440px;width:1600px;text-align:center;font-size:104px;line-height:1.1;letter-spacing:-.04em}
.story-action{position:absolute;left:80px;top:64px;font-size:60px;letter-spacing:-.035em;line-height:1.1}
#story-custom,#story-rules{visibility:hidden}
#setup-workflow .erp-grid-row{grid-template-columns:34px 1fr 1.15fr 1fr 1fr}
.story-done{position:absolute;left:1280px;top:90px;font-size:32px;display:flex;align-items:center;gap:12px;visibility:hidden}.story-done svg{width:34px;height:34px}
'''
# A manufactured object built from cuboids, with actual depth and solid shaded faces.
def chair_box(id,x,y,z,w,h,d):
 faces=[('front',w,h,f'translateZ({d/2}px)','#b79b7a'),('back',w,h,f'rotateY(180deg) translateZ({d/2}px)','#80694f'),('right',d,h,f'rotateY(90deg) translateZ({w/2}px)','#91775b'),('left',d,h,f'rotateY(-90deg) translateZ({w/2}px)','#c7ad8b'),('top',w,d,f'rotateX(90deg) translateZ({h/2}px)','#d4bc9b'),('bottom',w,d,f'rotateX(-90deg) translateZ({h/2}px)','#77634c')]
 return f'<div id="{id}" class="chair-part" style="transform:translate3d({x}px,{y}px,{z}px)">'+''.join(f'<div class="chair-face" style="width:{fw}px;height:{fh}px;margin-left:{-fw/2}px;margin-top:{-fh/2}px;background:{color};transform:{tr}"></div>' for _,fw,fh,tr,color in faces)+'</div>'
chair_parts=''.join(chair_box(f'chair-leg-{i}',x,118,z,24,236,24) for i,(x,z) in enumerate([(-97,-87),(97,-87),(-97,87),(97,87)]))
chair_parts+=chair_box('chair-seat',0,-8,0,244,26,220)
chair_parts+=chair_box('chair-back-left',-97,-126,-87,24,250,24)+chair_box('chair-back-right',97,-126,-87,24,250,24)
chair_parts+=chair_box('chair-back-slat',0,-187,-87,210,94,22)
chair='<div id="chair-stage" data-layout-allow-overflow style="position:absolute;left:330px;top:570px;width:1px;height:1px;perspective:1400px;visibility:hidden"><div id="chair-shadow" style="position:absolute;left:-215px;top:246px;width:440px;height:70px;border-radius:50%;background:#20232318"></div><div id="chair-model" style="transform-style:preserve-3d;transform:rotateX(-18deg) rotateY(-28deg)">'+chair_parts+'</div></div>'
story_css+=' .chair-part{position:absolute;left:0;top:0;transform-style:preserve-3d}.chair-face{position:absolute;left:0;top:0;backface-visibility:hidden;outline:1px solid #9a816222}'
workflow_fields='<div class="erp-field-row">'+erp_field('Workflow Name','Production approval')+erp_field('Document Type','Work Order')+'</div>'
workflow_fields+='<div class="erp-section">States</div>'+erp_grid(['No.','State','Doc Status','Update Field','Update Value'],[['1','Draft','0','',''],['2','Approved','1','','']],'workflow-state')
workflow_fields+='<div class="erp-section" style="margin-top:26px">Transition Rules</div>'+erp_grid(['No.','State','Action','Next State','Allowed'],[['1','Draft','Approve','Approved','Manufacturing Manager']],'workflow-transition')
workflow_page=erp_page('setup-workflow','Production approval','Settings / Workflow',workflow_fields,'Save')
exec((P/'scripts/workflow-journey.py').read_text())
body='<div id="story-stage" class="fill" style="background:#202323;color:#fcfcfb">'+paper_bg('story-paper')+chair+'<div id="story-intro" class="story-intro">Migrating your data.</div><div id="story-custom" class="story-action" data-layout-allow-overlap>Customizing your modules.</div><div id="story-rules" class="story-action" data-layout-allow-overlap>Building your workflows.</div><div id="story-mask" class="story-mask" data-layout-allow-overflow><div id="story-camera" class="story-camera" data-layout-allow-overflow><div id="story-items" class="story-page">'+item_page.replace('+ Add Item','Import')+'</div><div id="story-bom" class="story-page">'+bom_page+'</div><div id="story-workflow" class="story-page">'+workflow_page+'</div></div></div><div id="story-done" class="story-done"><svg viewBox="0 0 40 40" fill="none"><path d="m7 20 9 9 17-19" stroke="currentColor" stroke-width="3"/></svg>Changes ready</div>'+flow_visual+cursor('build-cursor')+'</div>'
js='''
gsap.set('#story-paper',{autoAlpha:0});
gsap.set('#story-mask',{transformPerspective:1800,rotationY:-18,rotationX:10,scale:.82});
gsap.set('#story-camera',{x:2120,y:164,scale:1.88});
gsap.set('#story-bom,#story-workflow',{autoAlpha:0});
gsap.set('#build-cursor',{x:1640,y:1160});
gsap.set('#stock-item-0,#stock-item-1,#stock-item-2,#stock-item-3',{opacity:0});
// The introductory sentence gives way to the actual import in one leftward move.
tl.to('#story-intro',{x:-1920,duration:.48,ease:'power3.inOut'},.38);
tl.set('#story-intro',{autoAlpha:0},.87);
tl.to('#story-mask',{rotationY:0,rotationX:0,scale:1,duration:.65,ease:'power3.out'},.38);
tl.to('#story-camera',{x:160,duration:.48,ease:'power3.inOut'},.38);
tl.to('#build-cursor',{x:1615,y:281,duration:.48,ease:'power3.out'},.58);
// Click Import. The four related records arrive as a single batch, then the chair is selected.
tl.to('#setup-items .erp-primary',{backgroundColor:'#555555',duration:.09},1.06);
tl.to('#setup-items .erp-primary',{backgroundColor:'#171717',duration:.18},1.16);
tl.to('#stock-item-0,#stock-item-1,#stock-item-2,#stock-item-3',{opacity:1,duration:.15,stagger:.045},1.06);
tl.to('#build-cursor',{x:409,y:592,duration:.42,ease:'power3.inOut'},1.3);
tl.to('#stock-item-0',{backgroundColor:'#ffe1cb',duration:.12},1.74);
// Selection pushes into the manufacturing record; the view travels down to materials and operations.
tl.to('#story-camera',{x:-550,y:-580,scale:3.15,duration:.24,ease:'power3.in'},1.74);
tl.to('#story-mask',{clipPath:'inset(0px 0px 0px 0px round 0px)',duration:.24,ease:'power3.in'},1.74);
tl.set('#story-paper',{autoAlpha:1},1.98);
tl.set('#story-custom',{color:'#202323'},1.98);
tl.to('#story-camera',{x:720,y:160,scale:1.28,duration:.55,ease:'power3.out'},1.98);
tl.fromTo('#chair-stage',{autoAlpha:1,x:150,scale:2},{autoAlpha:1,x:0,scale:1.13,duration:.72,ease:'power3.out',immediateRender:false},1.98);
tl.fromTo('#chair-model',{rotationY:-65},{rotationY:-28,duration:1.05,ease:'power2.out'},2.1);
tl.fromTo('#chair-seat',{y:-100},{y:-8,duration:.3,ease:'power3.out'},2.22);
tl.fromTo('#chair-back-left,#chair-back-right,#chair-back-slat',{opacity:0},{opacity:1,duration:.22,stagger:.055},2.43);
tl.to('#story-mask',{clipPath:'inset(160px 112px 84px 720px round 14px)',duration:.55,ease:'power3.out'},1.98);
tl.set('#story-items',{autoAlpha:0},1.98);
tl.set('#story-bom',{autoAlpha:1},1.98);
tl.fromTo('#story-custom',{autoAlpha:0,x:60},{autoAlpha:1,x:0,duration:.32,ease:'power3.out'},2.04);
tl.to('#story-custom',{x:-1600,duration:.3,ease:'power3.in'},2.65);
tl.set('#story-custom',{autoAlpha:0},2.96);
tl.to('#build-cursor',{x:1080,y:555,duration:.55,ease:'power3.out'},1.98);
tl.fromTo('#bom-material-0,#bom-material-1,#bom-material-2',{backgroundColor:'#ffb78a'},{backgroundColor:'#fff',duration:.35,stagger:.06},2.3);
tl.to('#build-cursor',{x:1090,y:855,duration:.45,ease:'power3.inOut'},2.6);
tl.fromTo('#bom-operation-0,#bom-operation-1',{clipPath:'inset(0 100% 0 0)'},{clipPath:'inset(0 0% 0 0)',duration:.28,stagger:.15,ease:'power2.out'},2.8);
// Hold the connected production setup briefly; a horizontal document handoff advances to its workflow.
tl.to('#build-cursor',{x:1530,y:790,duration:.4,ease:'power3.inOut'},3.16);
'''+tap('build-cursor',1.06)+tap('build-cursor',1.74)+flow_js
comp(3,'modules',9,body,js,True,extra=erp_primitive_css+midcss+story_css+flow_css)
