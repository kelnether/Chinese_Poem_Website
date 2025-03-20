#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识图谱模块：提供关键词抽取和更新 Neo4j 知识图谱的功能。
"""

from py2neo import Graph, Node, Relationship

def extract_keywords(text, topK=3):
    # 方法1：使用 jieba.analyse.extract_tags（如需使用，请取消下行注释并安装 jieba）
    # import jieba.analyse
    # return jieba.analyse.extract_tags(text, topK=topK)
    # 方法2：简单示例，按空格分词返回长度大于1的词
    words = text.split()
    keywords = [w for w in words if len(w) > 1][:topK]
    return keywords

def update_knowledge_graph(poetry_data, neo4j_url="bolt://localhost:7687",
                           neo4j_auth=("neo4j", "your_password")):
    """
    将诗词知识数据写入 Neo4j 图数据库，建立 Author、Poem、Keyword 节点及关系。
    """
    graph = Graph(neo4j_url, auth=neo4j_auth)
    #graph.delete_all()  # 清空数据库，可根据需求移除此行

    for category, poems in poetry_data.items():
        for poem in poems:
            title = poem.get("title", "无标题")
            author_name = poem.get("author", "未知")
            paragraphs = poem.get("paragraphs", [])
            content = "\n".join(paragraphs)
            keywords = extract_keywords(content, topK=3)

            author_node = Node("Author", name=author_name)
            graph.merge(author_node, "Author", "name")

            poem_node = Node("Poem", title=title, content=content, category=category)
            graph.merge(poem_node, "Poem", "title")

            rel = Relationship(author_node, "CREATED", poem_node)
            graph.merge(rel)

            for kw in keywords:
                keyword_node = Node("Keyword", word=kw)
                graph.merge(keyword_node, "Keyword", "word")
                rel2 = Relationship(poem_node, "EXPRESSES", keyword_node)
                graph.merge(rel2)
