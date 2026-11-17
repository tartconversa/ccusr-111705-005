"""本地业务页面交互。"""

def detail_fragment(item):
    return "<div id=\"campaign\">报名窗口待开放</div><button id=\"countdown\">更新时段</button><button id=\"notice\">关闭提示</button><div id=\"overlay\">活动提示</div><select id=\"scene\"><option>午后场</option><option>夜场</option></select><button id=\"end\">模拟名额变化</button><script>let scene=document.querySelector('#scene');let campaign=document.querySelector('#campaign');let ended=false;scene.onchange=()=>campaign.textContent=scene.value+'：报名窗口待开放';document.querySelector('#notice').onclick=()=>document.querySelector('#overlay').remove();document.querySelector('#countdown').onclick=()=>{campaign.textContent='更新中';let key=scene.value;setTimeout(()=>campaign.textContent=key+'：'+(ended?'候补':'可报名'),50)};document.querySelector('#end').onclick=()=>{ended=true;campaign.textContent=scene.value+'：候补'};</script>"

def source_extension(item):
    return f"""<output id="scene-id" data-scene="afternoon" data-venue="{item['id']}">午后场 / 场次 afternoon</output><output id="signup-preview"></output><script>(()=>{{
let sceneId=document.querySelector('#scene-id'),signup=document.querySelector('#signup-preview'),scene=document.querySelector('#scene'),campaign=document.querySelector('#campaign');
let revision=1;scene.addEventListener('change',()=>{{revision++;sceneId.dataset.scene=scene.value==='午后场'?'afternoon':'evening';sceneId.textContent=scene.value+' / 场次 '+sceneId.dataset.scene;signup.textContent='';}});
document.querySelector('#countdown').addEventListener('click',()=>{{revision++;signup.textContent='';}});
document.querySelector('#preview').addEventListener('click',()=>{{let key=sceneId.dataset.scene,version=revision,current=campaign.textContent;signup.textContent='报名预览读取中';setTimeout(()=>{{signup.textContent='场次 '+key+' / v'+version+'：'+(current.includes('候补')?'候补':current.includes('可报名')?'可报名':'尚待核对');}},65)}});
document.querySelector('#end').addEventListener('click',()=>{{revision++;signup.textContent='';}});
}})();</script>"""
