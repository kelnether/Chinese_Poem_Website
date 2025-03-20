#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统计模块：提供统计诗词数量、诗人数量及热门诗人功能。
"""

def get_statistics(poems):
    authors = {}
    for poem in poems:
        author = poem.get("author", "未知")
        authors[author] = authors.get(author, 0) + 1
    stats = {
        "total": len(poems),
        "unique_authors": len(authors),
        "top_authors": sorted(authors.items(), key=lambda x: x[1], reverse=True)[:5]
    }
    return stats
