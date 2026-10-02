#!/usr/bin/env python3
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
manifest=json.loads((ROOT/'manifest.json').read_text())
for row in manifest['articles']:
    stem=ROOT/'articles'/row['article_id']
    article=json.loads(stem.with_suffix('.json').read_text())
    text=stem.with_suffix('.txt').read_bytes()
    assert text.decode()==article['body_text'], row['article_id']
    if article['body_sha256']:
        assert hashlib.sha256(text).hexdigest()==article['body_sha256'], row['article_id']
images=ROOT/'image_manifest.json'
checked=missing=0
for row in json.loads(images.read_text())['images']:
    image=ROOT/row['local_path']
    if image.is_file():
        assert hashlib.sha256(image.read_bytes()).hexdigest()==row['sha256'], row['url']
        checked+=1
    else: missing+=1
print(f"Verified {len(manifest['articles'])} article records, {checked} images; {missing} images not extracted locally.")
