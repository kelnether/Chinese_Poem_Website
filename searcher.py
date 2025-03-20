#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
搜索模块：根据关键词在诗词中匹配标题、作者或内容，
返回包含 (索引, 诗词内容) 的列表。
"""

def search_poems(poems, keyword):
    results = []
    for idx, poem in enumerate(poems):
        title = poem.get("title", "")
        author = poem.get("author", "")
        paragraphs = poem.get("paragraphs", [])
        if keyword in title or keyword in author or any(keyword in line for line in paragraphs):
            results.append((idx, poem))
    return results
