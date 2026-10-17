"""Offline example using the public implementation; see README for evidence scope."""
import sys,json,pathlib,os
repo=pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0,str(repo));sys.path.insert(0,str(repo/'src'));os.chdir(repo)
import numpy as np,pandas as pd,contextlib,io
from scipy import stats
df=pd.DataFrame({'quality':[7,8,7,8,5,4,5,4],'alcohol':[12.,12.5,13.,12.2,10.,10.5,11.,10.2]})
scope={'np':np,'pd':pd,'stats':stats,'df':df}
nb=json.loads((repo/'analysis.ipynb').read_text())
with contextlib.redirect_stdout(io.StringIO()):
 for index in [13,14,15,16]:exec(compile(''.join(nb['cells'][index]['source']),f'analysis.ipynb cell{index}','exec'),scope)
print(json.dumps({"fixture":"eight generated wine records, not historical inference","difference":float(scope['diff']),"ci95":[float(scope['ci_low']),float(scope['ci_high'])],"cohens_d":float(scope['cohens_d']),"p_one_sided":float(scope['p_one_tailed'])}))
