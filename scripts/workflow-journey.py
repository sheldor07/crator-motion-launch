"""One work order travels through an unbounded approval workflow.
World coordinates, camera poses, and route sampling are deterministic.
"""
order_fields='<div class="erp-tabs"><span class="active">Details</span><span>Connections</span></div>'
order_fields+='<div class="erp-field-row">'+erp_field('Production Item','DINING-CHAIR')+erp_field('Qty to Manufacture','100')+'</div>'
order_fields+='<div class="erp-field-row">'+erp_field('BOM No','BOM-DINING-CHAIR-001')+erp_field('Company','Furniture Co.')+'</div>'
order_fields+='<div class="erp-section">Required Items</div>'+erp_grid(['No.','Item Code','Source Warehouse','Required Qty','UOM'],[['1','TIMBER','Raw Materials','400','Nos'],['2','WOOD-SCREW','Raw Materials','1,600','Nos'],['3','WOOD-FINISH','Raw Materials','25','L']],'journey-material')
order_fields+='<div class="erp-section" style="margin-top:24px">Operations</div>'+erp_grid(['No.','Operation','Workstation','Time','Status'],[['1','Cutting','Cutting station','20 min','Open'],['2','Assembly','Assembly line','35 min','Open']],'journey-operation')
order_page=erp_page('journey-order','MFG-WO-0001 <span class="erp-badge" id="journey-state">Draft</span>','Manufacturing / Work Order',order_fields,'Submit')
approved_page=order_page.replace('journey-order','journey-approved-order').replace('journey-state','journey-approved-state').replace('>Draft<','>Approved<').replace('>Submit<','>Start<').replace('journey-material','approved-material').replace('journey-operation','approved-operation')
overview_items=item_page.replace('id="','id="overview-')
overview_bom=bom_page.replace('id="','id="overview-')
flow_css='''
.journey{position:absolute;inset:0;visibility:hidden;overflow:hidden;perspective:1800px}
.journey-world{position:absolute;left:0;top:0;width:4400px;height:1600px;transform-origin:0 0;transform-style:preserve-3d}
.journey-doc{position:absolute;width:850px;height:653px;background:white;border-radius:12px;font-family:Inter,sans-serif;color:#383838;transform-origin:50% 50%;box-shadow:0 8px 0 #c8c8c5,0 16px 0 #e1e1db,0 30px 38px #24232622;overflow:hidden}
.journey-doc .erp-page{opacity:1;visibility:visible}.journey-doc .erp-badge{color:#785000;background:#fff0c5}
.journey-final .erp-badge{background:#e7f4ed;color:#1b704c}
.journey-type{position:absolute;left:170px;top:260px;width:1580px;font-size:164px;line-height:.99;letter-spacing:-.045em;font-weight:500;color:#202323}
.journey-route{position:absolute;left:0;top:-800px;width:4400px;height:2200px;overflow:visible}
.route-label{position:absolute;font:500 32px Inter,sans-serif;white-space:nowrap;color:#202323}
.journey-manager{position:absolute;left:1810px;top:-405px;width:660px;color:#202323;font-family:Inter,sans-serif}
.manager-avatar{position:absolute;left:0;top:0;width:136px;height:136px;background:#202323;color:#FFDAB6;border-radius:50%;font-size:44px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 0 #a4a0b3}
.manager-role{position:absolute;left:162px;top:10px;font-size:34px;line-height:1.2;letter-spacing:-.025em}
.manager-state{position:absolute;left:162px;top:100px;font-size:22px;color:#55505d}
.approval-menu{position:absolute;left:156px;top:178px;width:330px;background:#fff;border:1px solid #ddd;border-radius:12px;padding:9px;box-shadow:0 10px 0 #c6c2d1,0 25px 30px #20232318}
.approval-action{padding:20px 25px;font-size:28px;border-radius:7px;background:#202323;color:#fff;display:flex;justify-content:space-between}
.approval-secondary{padding:20px 25px;font-size:23px;color:#525252}
.travel-token{position:absolute;left:0;top:0;width:250px;height:156px;background:#FFDAB6;border-radius:12px;padding:21px;color:#202323;font-family:Inter,sans-serif;box-shadow:0 8px 0 #c6a585,0 20px 25px #20232320;transform-origin:50% 50%}
.travel-token b{display:block;font-size:25px;font-weight:600;margin-top:12px}.travel-token span{font-size:17px}.travel-token i{display:block;width:115px;height:5px;background:#20232333;margin-top:14px}
.journey-stripe{position:absolute;width:2000px;height:64px;background:#202323;transform:rotate(-26deg);transform-origin:0 50%}
.journey-stamp{position:absolute;left:200px;top:428px;width:1520px;display:flex;gap:52px;justify-content:center;align-items:center;font-size:172px;line-height:1;letter-spacing:-.04em;color:#fcfcfb;visibility:hidden}
.journey-stamp svg{width:224px;height:224px;flex-shrink:0;overflow:visible}
.journey-prop{position:absolute;color:#202323;font-size:24px;font-family:Inter,sans-serif;white-space:nowrap}
.journey-overview{visibility:hidden;transform-origin:50% 50%}.journey-overview .erp-footer{display:none}
'''
flow_visual='''<div id="journey-orange" class="fill" style="background:#FFC5C6;visibility:hidden"></div>
<div id="journey-lilac" class="fill" style="background:#fcfcfb;visibility:hidden"></div>
<div id="journey-ink" class="fill" style="background:#202323;visibility:hidden"></div>
<div id="journey-title" class="journey-type" style="visibility:hidden">Building<br>workflows.</div>
<div id="journey" class="journey" data-layout-allow-overflow>
<div id="journey-world" class="journey-world" data-layout-allow-overflow>
<svg class="journey-route" viewBox="0 0 4400 2200" fill="none" aria-hidden="true">
<path d="M 690 1120 C 1040 1120 1030 600 1460 600 L 1970 600" stroke="#202323" stroke-width="8"/>
<path d="M 1480 600 C 1600 600 1510 200 1830 200 L 2290 200" stroke="#20232330" stroke-width="6" stroke-dasharray="12 15"/>
<path id="journey-live-route" d="M 690 1120 C 1040 1120 1030 600 1460 600 L 1970 600" stroke="#FFDAB6" stroke-width="12"/>
<path id="journey-exit-route" d="M 2320 600 C 2730 600 2510 1140 3090 1140" stroke="#202323" stroke-width="8"/>
<circle cx="1480" cy="600" r="20" fill="#202323"/><circle cx="2290" cy="200" r="13" fill="#20232330"/>
</svg>
<div id="journey-source" class="journey-doc" style="left:0;top:0" data-layout-allow-overflow>'''+order_page+'''</div>
<div class="route-label" style="left:920px;top:320px">Submit ↗</div>
<div class="route-label" style="left:1310px;top:-110px">Production approval</div>
<div class="journey-prop" style="left:1710px;top:-700px;color:#6b6575">Request changes ↵</div>
<div id="journey-manager" class="journey-manager" data-layout-allow-overflow>
<div class="manager-avatar">MM</div><div class="manager-role">Manufacturing<br>Manager</div><div class="manager-state">Work Order · Pending approval</div>
<div class="approval-menu"><div id="journey-approve" class="approval-action">Approve <span>↗</span></div><div class="approval-secondary">Request changes</div></div></div>
<div id="journey-token" class="travel-token"><span>Work Order</span><b>MFG-WO-0001</b><i></i></div>
<div id="journey-inventory" class="journey-doc journey-overview" style="left:2130px;top:400px" data-layout-allow-overflow>'''+overview_items+'''</div>
<div id="journey-production" class="journey-doc journey-overview" style="left:3880px;top:-400px" data-layout-allow-overflow>'''+overview_bom+'''</div>
<div id="journey-final" class="journey-doc journey-final" style="left:2950px;top:90px" data-layout-allow-overflow>'''+approved_page+'''</div>

</div></div>
<div id="journey-stamp" class="journey-stamp"><svg viewBox="0 0 224 224" fill="none"><circle cx="112" cy="112" r="98" stroke="#B7FFBA" stroke-width="15"/><path id="approval-check" d="m59 111 36 38 70-78" stroke="#B7FFBA" stroke-width="17" stroke-linecap="round" stroke-linejoin="round"/></svg><span>Approved.</span></div>
'''
flow_js='''
// World poses are calculated from a film camera's focal point, not from DOM layout.
function journeyPose(cx,cy,s){return {x:960-cx*s,y:540-cy*s,scale:s};}
gsap.set('#journey-world',journeyPose(425,326,1.65));
gsap.set('#journey-source',{transformPerspective:1800,rotationY:-18,rotationX:8,rotation:-5});
gsap.set('#journey-final',{transformPerspective:1800,rotationY:14,rotationX:-7,rotation:5});
gsap.set('#journey-token,#journey-final',{autoAlpha:0});
gsap.set('#journey-inventory',{transformPerspective:1800,rotationY:20,rotationX:5,rotation:-12,scale:.82});
gsap.set('#journey-production',{transformPerspective:1800,rotationY:-20,rotationX:-5,rotation:12,scale:.82});
const route=document.getElementById('journey-live-route'),routeLength=route.getTotalLength();
gsap.set(route,{strokeDasharray:routeLength,strokeDashoffset:routeLength});
const run={p:0};
function positionOrder(){let p=route.getPointAtLength(run.p*routeLength);gsap.set('#journey-token',{x:p.x-125,y:p.y-800-78});}
// The chair and BOM leave at speed. The orange field takes over the full canvas.
tl.to('#chair-stage',{x:-1050,y:180,rotation:-22,duration:.42,ease:'power3.in'},3.62);
tl.to('#story-mask',{y:1180,rotation:-8,duration:.42,ease:'power3.in'},3.62);
tl.to('#story-custom',{x:-1600,duration:.38,ease:'power3.in'},3.62);
tl.to('#build-cursor',{x:2080,y:1040,duration:.3,ease:'power2.in'},3.62);
tl.fromTo('#journey-orange',{autoAlpha:1,x:1920},{autoAlpha:1,x:0,duration:.38,ease:'power3.inOut',immediateRender:false},3.7);
tl.fromTo('#journey-title',{autoAlpha:1,x:260,rotation:5},{autoAlpha:1,x:0,rotation:0,duration:.36,ease:'power3.out',immediateRender:false},3.83);
tl.to('#journey-title',{x:-2200,scale:1.5,duration:.48,ease:'power3.in'},4.36);
tl.set('#journey',{autoAlpha:1},4.48);
tl.set('#journey-title',{autoAlpha:0},4.85);
tl.fromTo('#journey-source',{x:1400},{x:0,duration:.55,ease:'power3.out'},4.48);
tl.to('#journey-source',{rotationY:-7,rotationX:3,rotation:-2,duration:.55,ease:'power3.out'},4.48);
// Pull back to discover the route attached to this document, then travel along it.
tl.to('#journey-world',{...journeyPose(740,220,.96),duration:.6,ease:'power3.inOut'},5.03);
tl.to('#journey-source',{rotationY:-18,rotationX:7,rotation:-8,duration:.6,ease:'power3.inOut'},5.03);
tl.fromTo('#journey-lilac',{autoAlpha:1,x:1920},{autoAlpha:1,x:0,duration:.7,ease:'power3.inOut',immediateRender:false},5.12);
tl.set('#journey-token',{autoAlpha:1},5.42);
tl.to(run,{p:1,duration:1.18,ease:'power2.inOut',onUpdate:positionOrder},5.42);
tl.to(route,{strokeDashoffset:0,duration:1.18,ease:'power2.inOut'},5.42);
tl.fromTo('#journey-token',{rotation:-10,scale:.65},{rotation:8,scale:1,duration:.6,ease:'power2.out'},5.42);
tl.to('#journey-world',{...journeyPose(1440,-160,1.12),duration:.7,ease:'power2.inOut'},5.5);
tl.to('#journey-world',{...journeyPose(2090,-180,1.7),duration:.58,ease:'power3.inOut'},6.2);
tl.to('#journey-token',{scale:.6,autoAlpha:0,duration:.15},6.38);
tl.set('#journey-source',{autoAlpha:0},6.4);
tl.set('#story-custom,#story-mask,#chair-stage',{autoAlpha:0},4.1);
// The camera arrives inside the native action menu; the click advances the work order.
tl.set('#build-cursor',{x:1640,y:1180},6.56);
tl.to('#build-cursor',{x:1040,y:565,duration:.34,ease:'power3.out'},6.56);
tl.to('#journey-approve',{backgroundColor:'#B7FFBA',color:'#202323',duration:.1},6.9);
tl.to('#journey-world',{...journeyPose(2130,-187,3.3),duration:.385,ease:'power3.in'},6.94);
tl.set('#journey-ink',{autoAlpha:1},7.325);
tl.set('#journey',{autoAlpha:0},7.325);
tl.to('#build-cursor',{x:2100,y:880,duration:.22,ease:'power2.in'},7.22);
tl.fromTo('#journey-stamp',{autoAlpha:1,scale:1.7,rotation:-8},{autoAlpha:1,scale:1,rotation:0,duration:.34,ease:'power3.out',immediateRender:false},7.325);
tl.fromTo('#approval-check',{strokeDasharray:155,strokeDashoffset:155},{strokeDashoffset:0,duration:.25,ease:'power2.out'},7.39);
// Approved becomes the actual ERP state. A diagonal pull reveals the fulfilled document.
tl.to('#journey-stamp',{x:-1920,rotation:-5,duration:.38,ease:'power3.in'},7.9);
tl.to('#journey-ink',{x:-1920,duration:.4,ease:'power3.inOut'},7.96);
tl.set('#journey-world',journeyPose(3375,365,1.32),8.02);
tl.set('#journey,#journey-final',{autoAlpha:1},8.02);
tl.fromTo('#journey-final',{y:940,rotationY:20,rotation:10},{y:0,rotationY:0,rotationX:0,rotation:0,duration:.48,ease:'power3.out'},8.02);
tl.to('#journey-world',{...journeyPose(3375,430,1.05),duration:.75,ease:'power2.out'},8.2);
tl.fromTo('#journey-inventory',{x:-450,y:240,autoAlpha:0},{x:0,y:0,autoAlpha:1,duration:.65,ease:'power3.out'},8.2);
tl.fromTo('#journey-production',{x:450,y:-240,autoAlpha:0},{x:0,y:0,autoAlpha:1,duration:.65,ease:'power3.out'},8.2);
'''+tap('build-cursor',6.9)
