#!/usr/bin/env python3
"""
批量更新 Awesome-Exploration README 中论文的 arXiv 链接。

用法：
  1. pip install requests             # 安装一次
  2. python batch_fetch_links.py      # 运行（默认用免费公共 API，有限速）
                                     # 或带上 API key: python batch_fetch_links.py --api_key 你的key

可选参数：
  --api_key YOUR_KEY    Semantic Scholar API key（申请免费：https://www.semanticscholar.org/product/api）
                        有 key 后限速从 ~1 req/s 提升到 ~10 req/s
  --batch 10            每次请求间隔（秒），默认 3 秒（无 key 建议 3-5，有 key 可 0.5-1）
  --output README.md    输出路径，默认覆盖当前 README.md
"""

import requests
import re
import json
import time
import os
import sys
import argparse

README_PATH = r'C:\Users\Matebook14\.openclaw\workspace\awesome-exploration\README.md'
CACHE_PATH = os.path.join(os.path.dirname(README_PATH), '_link_cache.json')

# ============ 解析参数 ============
parser = argparse.ArgumentParser(description='Batch fetch arXiv links for Awesome-Exploration')
parser.add_argument('--api_key', type=str, default='', help='Semantic Scholar API key')
parser.add_argument('--batch', type=float, default=3.0, help='Delay between requests (seconds)')
parser.add_argument('--output', type=str, default=README_PATH, help='Output README path')
args = parser.parse_args()

# ============ 读取 README ============
with open(README_PATH, 'r', encoding='utf-8') as f:
    readme = f.read()

# 提取所有论文标题
titles = list(set(re.findall(r'\*\*"(.+?)"\*\*', readme)))
total = len(titles)
print(f"在 README 中找到 {total} 篇论文")

# ============ 加载缓存 ============
if os.path.exists(CACHE_PATH):
    with open(CACHE_PATH, 'r', encoding='utf-8') as f:
        cache = json.load(f)
    print(f"已缓存 {len(cache)} 篇，剩余 {total - len(cache)} 篇待搜索")
else:
    cache = {}

# ============ 搜索链接 ============
headers = {'User-Agent': 'Mozilla/5.0'}
if args.api_key:
    headers['x-api-key'] = args.api_key

need_search = [t for t in titles if t not in cache]
print(f"本次需要搜索: {len(need_search)} 篇\n")

found_count = 0
for i, title in enumerate(need_search):
    try:
        # 截取前 80 字符作为搜索关键词
        query = title[:80].replace('"', ' ').strip()
        url = f"https://api.semanticscholar.org/graph/v1/paper/search"
        params = {
            'query': query,
            'limit': 5,
            'fields': 'title,externalIds,url,year'
        }
        
        resp = requests.get(url, params=params, headers=headers, timeout=15)
        
        if resp.status_code == 200:
            data = resp.json()
            papers = data.get('data', [])
            found_link = ''
            found_year = ''
            
            for p in papers:
                pt = p.get('title', '')
                ids = p.get('externalIds', {}) or {}
                year = p.get('year', '')
                
                # 优先 arXiv
                if ids.get('ArXiv'):
                    found_link = f"https://arxiv.org/abs/{ids['ArXiv']}"
                    found_year = year if year else ''
                    break
                # 其次 DOI
                elif ids.get('DOI'):
                    found_link = f"https://doi.org/{ids['DOI']}"
                    found_year = year if year else ''
                    break
            
            cache[title] = {'link': found_link, 'year': found_year}
            
            if found_link:
                found_count += 1
                status = f"FOUND  ({year})" if year else "FOUND  "
            else:
                status = "NOT FOUND"
            
            print(f"[{i+1:3}/{len(need_search)}] [{status}] {title[:60]}")
            
        elif resp.status_code == 429:
            print(f"[{i+1:3}/{len(need_search)}] [RATE LIMITED] 暂停 60s...")
            time.sleep(60)
            # 跳过这篇，之后重试
            cache[title] = {'link': '', 'year': ''}
        elif resp.status_code == 403:
            print(f"[{i+1:3}/{len(need_search)}] [FORBIDDEN] API key 无效或额度用完")
            # 跳过
            cache[title] = {'link': '', 'year': ''}
        else:
            print(f"[{i+1:3}/{len(need_search)}] [HTTP {resp.status_code}] {title[:40]}")
            cache[title] = {'link': '', 'year': ''}
    
    except Exception as e:
        print(f"[{i+1:3}/{len(need_search)}] [ERROR] {title[:40]}: {str(e)[:60]}")
        cache[title] = {'link': '', 'year': ''}
    
    # 保存缓存（每 10 篇保存一次）
    if (i + 1) % 10 == 0:
        with open(CACHE_PATH, 'w', encoding='utf-8') as f:
            json.dump(cache, f, ensure_ascii=False, indent=2)
        print(f"  -> 已保存缓存 ({len(cache)} 篇)")
    
    time.sleep(args.batch)

# 最终保存缓存
with open(CACHE_PATH, 'w', encoding='utf-8') as f:
    json.dump(cache, f, ensure_ascii=False, indent=2)

# ============ 用缓存结果更新 README ============
print(f"\n搜索完成！共找到 {found_count} 个新链接")
print(f"正在更新 README...")

# 对每个找到链接的论文，替换 README 中的 [[Paper](TBD)]
for title, info in cache.items():
    link = info.get('link', '')
    if not link:
        continue
    
    # 用正则替换 [[Paper](TBD)] 为 [[Paper](actual_link)]
    # 只替换这篇论文后面的第一个 [[Paper](TBD)]
    escaped_title = re.escape(title)
    pattern = rf'(\*\*"{escaped_title}"\*\*.*?\n\s*)\[\[Paper\]\(TBD\)\]'
    
    def replacer(match):
        return match.group(1) + f'[[Paper]({link})]'
    
    new_readme = re.sub(pattern, replacer, readme, count=1)
    if new_readme != readme:
        readme = new_readme

# 保存
with open(args.output, 'w', encoding='utf-8') as f:
    f.write(readme)

# ============ 统计 ============
linked = len(re.findall(r'\[\[Paper\]\(https?://', readme))
tbd = len(re.findall(r'\[\[Paper\]\(TBD\)\]', readme))
print(f"\n{'='*60}")
print(f"  更新完成！")
print(f"  README 路径: {args.output}")
print(f"  缓存文件:   {CACHE_PATH}")
print(f"  有真实链接:   {linked} 篇")
print(f"  仍为 [TBD]:   {tbd} 篇")
print(f"  缓存总数:    {len(cache)} 篇")
print(f"{'='*60}")
print(f"\n提示: 下次运行脚本会从缓存继续，不会重复搜索已找到的论文。")
