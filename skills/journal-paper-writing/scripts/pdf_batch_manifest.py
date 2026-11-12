"""Create a read-only PDF inventory; requires PyMuPDF for page counts."""
from pathlib import Path
import argparse, csv, hashlib, json, sys

def inventory(inputs, recursive=False):
    import fitz
    paths=[]
    for source in inputs:
        p=Path(source).resolve()
        if not p.exists(): raise FileNotFoundError(str(p))
        if p.is_file():
            if p.suffix.lower()!='.pdf': raise ValueError('Not a PDF: '+str(p))
            paths.append(p)
        else:
            paths.extend(sorted((x for x in (p.rglob('*') if recursive else p.iterdir()) if x.is_file() and x.suffix.lower()=='.pdf'),key=lambda x:str(x).casefold()))
    paths=list(dict.fromkeys(paths))
    records=[]; hashes={}
    for i,p in enumerate(paths,1):
        pid=f'P{i:03d}'
        with p.open('rb') as f: sha=hashlib.file_digest(f,'sha256').hexdigest()
        r=dict(paper_id=pid,filename=p.name,original_path=str(p),sha256=sha,size_bytes=p.stat().st_size,duplicate_of=hashes.get(sha),page_count=None,status='DISCOVERED',extraction_status='NOT_STARTED',blockers=[])
        hashes.setdefault(sha,pid)
        try:
            with fitz.open(p) as d:
                if d.needs_pass: raise ValueError('Encrypted PDF requires password')
                r['page_count']=len(d)
        except Exception as e: r['blockers'].append(str(e))
        records.append(r)
    return {'recursive_import':recursive,'inputs':[str(Path(x).resolve()) for x in inputs],'papers':records}

def main():
    a=argparse.ArgumentParser(description=__doc__)
    a.add_argument('inputs',nargs='+'); a.add_argument('--output',required=True); a.add_argument('--recursive',action='store_true')
    args=a.parse_args(); result=inventory(args.inputs,args.recursive)
    out=Path(args.output); out.parent.mkdir(parents=True,exist_ok=True)
    if out.exists() or out.with_suffix('.csv').exists(): raise FileExistsError('Output already exists; choose a new batch path: '+str(out))
    out.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    with out.with_suffix('.csv').open('x',encoding='utf-8-sig',newline='') as f:
        fields=['paper_id','filename','original_path','sha256','size_bytes','duplicate_of','page_count','status','extraction_status','blockers']
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(result['papers'])
    print(json.dumps({'files':len(result['papers']),'exact_duplicates':sum(bool(x['duplicate_of']) for x in result['papers']),'blocked':sum(bool(x['blockers']) for x in result['papers']),'output':str(out)},ensure_ascii=False))
if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
