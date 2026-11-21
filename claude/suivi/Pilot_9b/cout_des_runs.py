import json,sys,re,collections
D='/root/.claude/projects/-home-user-DG-777/a53d38a4-2da0-5e06-9ee2-c76fc7c01b1f/subagents/'
runs={"17k":"af3bb120836cfdccc","17l":"a5184484010bd1d11","18k":"ade228a502679fce8","18l":"ad330af217f2e231c"}
for nom,i in runs.items():
    msgs=[json.loads(l) for l in open(D+f'agent-{i}.jsonl')]
    usage=[];tools=collections.Counter();res=collections.Counter();resn=collections.Counter();imgs=0;img_files=collections.Counter()
    idmap={}
    for m in msgs:
        msg=m.get('message',{})
        if m.get('type')=='assistant':
            u=msg.get('usage',{})
            if u: usage.append(u)
            for c in msg.get('content',[]) if isinstance(msg.get('content'),list) else []:
                if c.get('type')=='tool_use':
                    inp=c.get('input',{}); k=c['name']
                    if k=='Bash':
                        cmd=inp.get('command','')
                        mm=re.search(r'scripts/(\w+)\.py\s*(\w+)?',cmd)
                        k='Bash:'+(mm.group(1)+(' '+mm.group(2) if mm.group(1)=='parcours' and mm.group(2) else '') if mm else 'autre')
                    if k=='Read':
                        p=inp.get('file_path','')
                        k='Read:'+('image' if p.lower().endswith(('.png','.jpg','.jpeg','.webp')) else ('html' if p.endswith('.html') else ('skill' if 'skills/' in p else 'autre')))
                    tools[k]+=1; idmap[c['id']]=k
        if m.get('type')=='user':
            for c in msg.get('content',[]) if isinstance(msg.get('content'),list) else []:
                if c.get('type')=='tool_result':
                    k=idmap.get(c.get('tool_use_id'),'?')
                    cont=c.get('content')
                    if isinstance(cont,list):
                        n=0
                        for x in cont:
                            if x.get('type')=='text': n+=len(x.get('text',''))
                            if x.get('type')=='image': imgs+=1; n+=0; img_files[k]+=1
                    else: n=len(str(cont))
                    res[k]+=n; resn[k]+=1
    # tokens : la somme du contexte relu à chaque tour
    inp=sum(u.get('input_tokens',0) for u in usage); cr=sum(u.get('cache_read_input_tokens',0) for u in usage); cw=sum(u.get('cache_creation_input_tokens',0) for u in usage); out=sum(u.get('output_tokens',0) for u in usage)
    last=usage[-1] if usage else {}
    ctxmax=max((u.get('input_tokens',0)+u.get('cache_read_input_tokens',0)+u.get('cache_creation_input_tokens',0)) for u in usage)
    print(f"=== {nom} : tours {len(usage)} · sortie {out} · cache lu {cr} · cache écrit {cw} · entrée {inp} · contexte max {ctxmax} · images reçues {imgs}")
    print("   appels :",dict(tools.most_common(12)))
    print("   texte retourné (car.) :",dict(res.most_common(8)))
    print("   images par outil :",dict(img_files))
