from pathlib import Path
import json,os
from fastapi import FastAPI,HTTPException
from .predict import predict
app=FastAPI(title='AgentPulse',version='0.1.0',description='Synthetic-data research demo; not production-validated')
MODEL=json.loads(Path(os.getenv('AGENTPULSE_MODEL','models/logistic.json')).read_text())
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/predict')
def score(record:dict):
    try: return predict(record,MODEL)
    except (ValueError,TypeError) as e: raise HTTPException(status_code=422,detail=str(e)) from e

from fastapi.responses import HTMLResponse
from .schema import FEATURES
@app.get('/',response_class=HTMLResponse)
def index():
    defaults=[1200,1800,200,4,1,80,.3,.2,.5,.5,.5,.7,.4,25,8,5]
    fields=''.join(f'<label>{k}<input name="{k}" type="number" step="any" value="{v}" required></label>' for k,v in zip(FEATURES,defaults))
    return '''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>AgentPulse risk demo</title><style>body{max-width:850px;margin:40px auto;padding:20px;font:17px system-ui;background:#0a1523;color:#eaf6ff}form{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}label{display:grid;gap:5px}input,button{font:inherit;padding:9px}button{background:#63e4cf;border:0;cursor:pointer}pre{white-space:pre-wrap}</style><h1>AgentPulse / Failure risk</h1><p>Synthetic model. Not production validated.</p><form id="f">'''+fields+'''<button>Score telemetry</button></form><pre id="o" role="status"></pre><script>document.querySelector('#f').onsubmit=async e=>{e.preventDefault();let d=Object.fromEntries([...new FormData(e.target)].map(([k,v])=>[k,Number(v)]));try{let r=await fetch('/predict',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)});document.querySelector('#o').textContent=JSON.stringify(await r.json(),null,2)}catch(e){document.querySelector('#o').textContent=String(e)}};</script>'''
