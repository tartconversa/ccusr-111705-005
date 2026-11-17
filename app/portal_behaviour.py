"""本地业务页面交互。"""

def detail_fragment(item):
    return '<div id="campaign">报名窗口待开放</div><button id="countdown">更新时段</button><button id="notice">关闭提示</button><div id="overlay">活动提示</div><script>document.querySelector(\'#notice\').onclick=()=>document.querySelector(\'#overlay\').remove();document.querySelector(\'#countdown\').onclick=()=>{document.querySelector(\'#campaign\').textContent=\'更新中\';setTimeout(()=>document.querySelector(\'#campaign\').textContent=\'报名候补\',50)};</script>'
