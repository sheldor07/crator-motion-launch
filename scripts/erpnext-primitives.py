"""ERPNext visual primitives for the launch demonstration.
Field/grid treatment: original src/HeroErp.tsx. Record labels/schema: local ERPNext source.
Account hierarchy: accounts/doctype/account/chart_of_accounts/verified/standard_chart_of_accounts.py.
Illustrative demo records; no live ERP is modified.
"""
erp_primitive_css='''
.erp-shell{position:absolute;left:652px;top:92px;width:1226px;height:944px;border:1px solid #e5e5e5;border-radius:10px;background:#fff;overflow:hidden;font-family:Inter,sans-serif;color:#383838}
.erp-desk{position:relative;width:908px;height:699px;transform:scale(1.35);transform-origin:0 0}
.preview-toolbar{height:46px;border-bottom:1px solid #e5e5e5;display:flex;align-items:center;justify-content:space-between;padding:0 14px;font:13px 'Instrument Sans',sans-serif}
.preview-tabs{display:flex;gap:4px;padding:3px;border:1px solid #e5e5e5;border-radius:8px}.preview-tabs span{padding:5px 10px}.preview-tabs .selected{background:#f3f3f3;border-radius:5px}.preview-open{padding:7px 10px;border-radius:7px;background:#f3f3f3}
.erp-rail{position:absolute;left:0;top:46px;width:58px;height:653px;display:flex}.erp-content{position:absolute;left:58px;top:46px;width:850px;height:653px;overflow:hidden}.erp-page{position:absolute;inset:0;background:#fff;padding:0 24px}
#setup-warehouses,#setup-bom,#setup-accounts{opacity:0;visibility:hidden}.erp-breadcrumb{height:36px;display:flex;align-items:center;gap:10px;font-size:12px;color:#656565;border-bottom:1px solid #ededed}
.erp-titlebar{height:66px;display:flex;align-items:center;justify-content:space-between}.erp-title{font-size:25px;font-weight:600;color:#171717;letter-spacing:-.025em}.erp-button{padding:8px 12px;border-radius:7px;background:#f3f3f3;font-size:12px}.erp-primary{background:#171717;color:white}.erp-toolbar{display:flex;gap:9px;align-items:center;margin-bottom:24px;font-size:12px}
.erp-filter{padding:9px 12px;background:#f3f3f3;border-radius:7px;color:#525252}.erp-filter.wide{width:236px}.erp-list{border-top:1px solid #ededed}.erp-list-row{display:grid;grid-template-columns:30px 1.3fr 1.1fr .9fr 72px;min-height:60px;align-items:center;border-bottom:1px solid #ededed;font-size:13px}.erp-list-row>span{padding:9px 7px;min-width:0}.erp-list-head{min-height:40px;font-size:11px;color:#656565;background:#fafafa}.erp-check{display:inline-block;width:13px;height:13px;border:1px solid #c7c7c7;border-radius:4px}.erp-link{font-weight:500;color:#171717}.erp-enabled{font-size:11px;color:#1b704c}.erp-dot{display:inline-block;width:6px;height:6px;border-radius:50%;background:#1b704c;margin-right:5px}
.erp-field-row{display:flex;gap:24px;margin-bottom:16px}.erp-field{flex:1;font-size:12px;color:#525252}.erp-value{margin-top:7px;background:#f3f3f3;padding:10px 12px;border-radius:8px;font-size:13px;color:#383838}.erp-section{font-size:15px;font-weight:600;color:#171717;margin:12px 0}.erp-grid{border:1px solid #ededed;border-radius:8px;overflow:hidden}.erp-grid-row{display:grid;grid-template-columns:34px 1.15fr 1.05fr 65px 72px;align-items:center;min-height:38px;border-bottom:1px solid #ededed;font-size:12px}#setup-bom .erp-grid:last-child .erp-grid-row{grid-template-columns:34px 1fr 1fr 100px 90px}.erp-grid-row:last-child{border:0}.erp-grid-row>span{padding:9px}.erp-grid-head{font-size:11px;color:#656565;background:#fafafa;min-height:36px}.erp-tabs{display:flex;gap:25px;font-size:12px;border-bottom:1px solid #ededed;margin-bottom:20px}.erp-tabs span{padding:10px 0}.erp-tabs .active{border-bottom:2px solid #171717;color:#171717;font-weight:500}.erp-badge{font-size:11px;color:#1b704c;background:#e7f4ed;padding:4px 8px;border-radius:12px;font-weight:500;vertical-align:middle;margin-left:10px}
.erp-tree{font-size:14px;line-height:1.3;border-top:1px solid #ededed;padding-top:14px}.erp-tree-row{display:flex;align-items:center;gap:10px;height:43px;padding-right:12px}.erp-tree-indent{display:inline-block;flex-shrink:0}.erp-folder{width:16px;height:14px;color:#656565;flex-shrink:0}.erp-tree-type{margin-left:auto;font-size:11px;color:#656565}.erp-tree-row.highlight{background:#f3f3f3;border-radius:6px}.erp-muted{color:#656565;font-size:12px}.erp-footer{margin-top:22px;font-size:12px;color:#656565}
.builder-rule{position:absolute;left:622px;top:92px;width:1px;height:944px;background:#e5e5e5}.builder-heading{position:absolute;left:48px;top:61px;display:flex;gap:12px;align-items:center;font:500 23px 'Instrument Sans',sans-serif}.builder-heading img{width:28px;height:28px}.user-message{position:absolute;left:48px;top:145px;width:526px;padding:23px;border-radius:10px;background:#f2f2f2;color:#171717;font:20px/1.45 'Instrument Sans',sans-serif}.agent-message{position:absolute;left:48px;top:395px;width:526px;font:21px/1.45 'Instrument Sans',sans-serif}.agent-message strong{font-weight:500}.agent-message .detail{font-size:19px;color:#656565;margin-top:15px}.agent-message .tool{font-size:19px;border-left:2px solid #dedede;margin-top:25px;padding-left:18px;color:#525252;line-height:1.9}.builder-bottom{position:absolute;left:48px;top:870px;width:560px;transform:scale(1);transform-origin:0 0}.build-proof-caption{position:absolute;left:652px;top:36px;font:500 29px 'Instrument Sans',sans-serif}
'''
def erp_field(label,value):return f'<div class="erp-field">{label}<div class="erp-value">{value}</div></div>'
def erp_page(id,title,breadcrumb,content,button=''):
 return f'<div id="{id}" class="erp-page" data-layout-allow-overflow><div class="erp-breadcrumb">☰ <span>/</span> {breadcrumb}</div><div class="erp-titlebar"><div class="erp-title">{title}</div><span class="erp-button erp-primary">{button or "+ Add "+title}</span></div>{content}</div>'
def erp_grid(headers,rows,id):
 h='<div class="erp-grid"><div class="erp-grid-row erp-grid-head">'+''.join('<span>'+v+'</span>' for v in headers)+'</div>'
 for i,row in enumerate(rows):h+=f'<div id="{id}-{i}" class="erp-grid-row">'+''.join('<span>'+v+'</span>' for v in row)+'</div>'
 return h+'</div>'
def erp_tree(rows,id):
 h='<div class="erp-tree">'
 for i,(depth,label,kind,open_) in enumerate(rows):
  glyph='⌄' if open_ else '›' if kind=='Group' else ''
  path='M2 5V3h7l3 3h10v12H2z' if kind=='Group' else 'M5 2h9l5 5v11H5z M14 2v5h5'
  h+=f'<div id="{id}-{i}" class="erp-tree-row"><span class="erp-tree-indent" style="width:{depth*25}px"></span><span style="width:12px;color:#656565">{glyph}</span><svg class="erp-folder" viewBox="0 0 24 20" fill="none" stroke="currentColor" stroke-width="1.5"><path d="{path}"/></svg><span>{label}</span></div>'
 return h+'</div>'

erp_primitive_css+=' .builder-bottom .relative{font-size:14px}.agent-message{top:340px}.user-message{padding:20px}.build-proof-caption{font-size:26px}.erp-shell{box-shadow:0 18px 50px #20232312}'
