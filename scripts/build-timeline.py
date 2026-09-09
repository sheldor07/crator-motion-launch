# Timings are explicit so Studio scrubbing and rendered scene boundaries agree.
shots=[('hook',4),('describe',4),('modules',9),('request',3.5),('result',4),('close',3)]
head='''<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=1920, height=1080"><title>Crator — motion launch</title><script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><style>*{box-sizing:border-box}html,body{margin:0;width:1920px;height:1080px;overflow:hidden;background:#faf7f5}#root{position:relative;width:1920px;height:1080px;overflow:hidden}.clip{position:absolute;inset:0;width:1920px;height:1080px}</style></head><body>'''
body='<div id="root" data-composition-id="main" data-start="0" data-duration="27.5" data-width="1920" data-height="1080">'
body+='<audio id="reference-music" src="assets/audio/get-down-launch-offset1-27p5s.wav" data-start="0" data-duration="27.5" data-track-index="2" data-volume="1" data-label="Get Down — Rex Banner"></audio>'
js='const tl=gsap.timeline({paused:true});';start=0
for i,(id,duration) in enumerate(shots,1):
 body+=f'<div class="clip" id="{id}" data-composition-id="{id}" data-composition-src="compositions/frames/{(7 if id=='close' else i):02}-{id}.html" data-start="{start}" data-duration="{duration}" data-width="1920" data-height="1080" data-track-index="1"></div>'
 if start:js+=f'gsap.set("#{id}",{{autoAlpha:0}});'
 js+=f'tl.set("#{id}",{{autoAlpha:1}},{start});tl.set("#{id}",{{autoAlpha:0}},{start+duration});'
 start+=duration
(P/'index.html').write_text(head+body+'</div><script>'+js+'window.__timelines["main"]=tl;</script></body></html>')
