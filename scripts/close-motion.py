# v40: destination is a tightly attached continuation of the CTA.
close_css='''
.close-logo{position:absolute;left:750px;top:328px;width:420px;height:130px;object-fit:contain;transform-origin:50% 50%}
.close-cta{position:absolute;left:180px;top:528px;width:1560px;text-align:center;font-size:128px;line-height:1.125;letter-spacing:-.04em;font-weight:400;color:#fcfcfb}
.close-url{position:absolute;left:180px;top:672px;width:1560px;text-align:center;font-size:56px;line-height:1.25;letter-spacing:-.02em;color:#cbd1ce}
'''
body='<div class="fill" style="background:#202323"></div><img id="close-logo" class="close-logo" src="assets/brand/crator_logo_full_white.svg" alt="Crator"><div id="close-cta" class="close-cta">Start your free trial</div><div id="close-url" class="close-url">at cratorlabs.ai</div>'
js='''
// Both logo and headline are already present in the incoming frame. Only the destination is new.
tl.fromTo('#close-url',{autoAlpha:0},{autoAlpha:1,duration:.36,ease:'sine.inOut'},.12);
'''
comp(7,'close',3,body,js,extra=close_css)
