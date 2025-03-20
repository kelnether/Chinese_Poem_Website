#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
主 Flask 应用：调用各模块实现诗词查询、详情、AI生成及知识图谱功能，
同时设置统一的顶栏导航，便于不同功能页面之间跳转。
"""

import os
from flask import Flask, render_template, request, jsonify, abort
from data_loader import load_all_data
from statistics import get_statistics
from searcher import search_poems
from ai_generator import generate_poem
from kg import update_knowledge_graph
from py2neo import Graph

app = Flask(__name__)

# 加载诗词数据
poetry_data = load_all_data()

@app.route("/", methods=["GET"])
def index():
    categories = list(poetry_data.keys())
    default_category = categories[0] if categories else ""
    poem_type = request.args.get("poem_type", default_category)
    search_query = request.args.get("search", "").strip()

    poems = poetry_data.get(poem_type, [])
    stats = get_statistics(poems) if poems else {"total": 0, "unique_authors": 0, "top_authors": []}
    results = search_poems(poems, search_query) if search_query else []

    return render_template("index.html",
                           categories=categories,
                           poem_type=poem_type,
                           stats=stats,
                           search_query=search_query,
                           results=results)

@app.route("/poem", methods=["GET"])
def poem_detail():
    category = request.args.get("category")
    idx = request.args.get("idx")
    if category not in poetry_data or idx is None:
        abort(404)
    try:
        idx = int(idx)
    except ValueError:
        abort(404)
    poems = poetry_data.get(category)
    if idx < 0 or idx >= len(poems):
        abort(404)
    poem = poems[idx]
    return render_template("detail.html", poem=poem, category=category, idx=idx)

@app.route("/chat", methods=["GET"])
def chat():
    return render_template("chat.html")

@app.route("/ai", methods=["POST"])
def ai():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "无效的请求"}), 400
    user_input = data["message"]
    reply = generate_poem(user_input)
    return jsonify({"reply": reply})

@app.route("/update_kg", methods=["GET"])
def update_kg():
    try:
        update_knowledge_graph(poetry_data)
        return "知识图谱更新成功！"
    except Exception as e:
        return f"知识图谱更新失败：{str(e)}", 500

@app.route("/query_kg", methods=["GET"])
def query_kg():
    query_type = request.args.get("type")
    name = request.args.get("name")
    if query_type == "author" and name:
        graph = Graph("bolt://localhost:7687", auth=("neo4j", "your_password"))
        cypher = """
            MATCH (a:Author {name:$name})-[:CREATED]->(p:Poem)
            RETURN p.title AS title, p.category AS category
        """
        results = graph.run(cypher, name=name).data()
        return render_template("query.html", results=results, query_type=query_type, name=name)
    else:
        return "不支持的查询类型或缺少参数", 400

if __name__ == "__main__":
    app.run(debug=True)
