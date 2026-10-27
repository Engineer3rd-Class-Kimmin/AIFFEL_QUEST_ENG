"""Run original notebook definitions only; never execute notebook top-level cells."""
import ast, contextlib, hashlib, io, json, math, platform, random, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
def load(path, cell, names):
    nb = json.loads((ROOT/path).read_text(encoding='utf-8'))
    source = ''.join(nb['cells'][cell]['source'])
    tree = ast.parse(source)
    nodes = [n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name in names]
    if {n.name for n in nodes} != set(names):
        raise RuntimeError('Selected source definitions missing')
    env = {'random':random}
    exec(compile(ast.Module(body=nodes,type_ignores=[]),path,'exec'),env)
    return env
def run(case):
    kind, x = case['kind'],case['input']
    with contextlib.redirect_stdout(io.StringIO()):
        if kind in ('palindrome','classifier'):
            env=load('01_Python/Py01/Quest0520.ipynb',0 if kind=='palindrome' else 1,
                     ['check_palindrome'] if kind=='palindrome' else ['is_palindrome','palindrome_classifier'])
            if kind=='palindrome': return env['check_palindrome'](x)
            groups,count,ratio=env['palindrome_classifier'](x)
            return {'count':count,'ratio':ratio}
        if kind=='minmax':
            env=load('01_Python/Py02/QUEST0522.ipynb',1,['find_min_max'])
            low,high=env['find_min_max'](x)
            return [low(),high()]
        if kind=='account':
            env=load('01_Python/Py04/QuestC0529.ipynb',1,['Account'])
            obj=env['Account']('synthetic-user',1000)
            for method,amount in x: getattr(obj,method)(amount)
            return dict(balance=obj.money,deposits=len(obj.deposit_list),withdrawals=len(obj.withdraw_list))
        if kind=='character':
            env=load('01_Python/Py04/QuestC0529.ipynb',3,['Character'])
            obj=env['Character']('synthetic-character',1,100,10,5)
            obj.take_damage(x)
            return obj.hp
    raise ValueError(kind)
def safe(value):
    if isinstance(value,float) and not math.isfinite(value): return str(value)
    if isinstance(value,list): return [safe(v) for v in value]
    return value
def main():
    cases=json.loads((HERE/'cases.json').read_text(encoding='utf-8'))
    rows=[]
    for case in cases:
        try: actual=safe(run(case))
        except Exception as exc: actual=type(exc).__name__
        rows.append({**case,'actual':actual,'status':'PASS' if actual==case['expected'] else 'FAIL'})
    files=sorted({ '01_Python/Py01/Quest0520.ipynb','01_Python/Py02/QUEST0522.ipynb','01_Python/Py04/QuestC0529.ipynb'})
    report=dict(evaluation='portfolio-v1-development-diagnostic',scope='original Python definitions; not full notebook execution or ML evaluation',
        executed_at=datetime.now(timezone.utc).isoformat(),python=platform.python_version(),
        source_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
        hashes={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in files+['evaluation/portfolio-v1/cases.json','evaluation/portfolio-v1/run.py']},
        total=len(rows),passed=sum(r['status']=='PASS' for r in rows),failed=sum(r['status']=='FAIL' for r in rows),cases=rows)
    (HERE/'results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n',encoding='utf-8',newline='\n')
    lines=['# Python 과제 개발 진단 결과','',f"총 {report['total']}건: PASS {report['passed']}, FAIL {report['failed']}",'',
        '기존 노트북 정의를 AST로 읽어 실행했다. input(), 출력 예제, 학습 및 외부 호출 셀은 실행하지 않았다. 아래 실패는 수정 전 실제 관측이며, 전체 교육 과정의 성능 점수가 아니다.','',
        '| ID | 종류 | 결과 | 기대값 | 실제값 |','|---|---|---|---|---|']
    for r in rows: lines.append(f"| {r['id']} | {r['kind']} | {r['status']} | {json.dumps(r['expected'],ensure_ascii=False)} | {json.dumps(r['actual'],ensure_ascii=False)} |")
    lines+=['','빈 목록 처리와 0 이하 출금 거부는 이번에 추가한 견고성 기준이다. 원래 과제 채점 결과와 구분한다. 실패를 없애기 위해 정답을 변경하거나 원본 과제를 수정하지 않았다.','',
        '재현: 저장소 루트에서 `python evaluation/portfolio-v1/run.py`. Python 표준 라이브러리만 필요하다. FAIL이 있으면 종료 코드 1이며 results.json과 이 문서를 먼저 저장한다.','',
        '평가셋과 실행기는 Codex로 작성했다(ai-assisted). 독립 평가자의 블라인드 검토는 받지 않았다. CV/NLP/LLM 과제의 모델 재학습·추론은 이 점수에 포함하지 않았다.']
    (HERE/'RESULTS.md').write_text('\n'.join(lines)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:report[k] for k in ('total','passed','failed')}))
    return 1 if report['failed'] else 0
if __name__=='__main__': sys.exit(main())
