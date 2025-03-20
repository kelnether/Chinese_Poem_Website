#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 诗词生成模块：调用 OpenAI API 生成诗词。
"""

import os
from openai import OpenAI

def generate_poem(prompt):
    """
    根据用户输入的提示生成诗词。
    使用 OpenAI 的 GPT 模型完成诗词生成。
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    # 示例中直接写入 api_key（建议配置为环境变量）

    if not api_key:
        return "未设置 OPENAI_API_KEY，请在环境变量中配置。"

    try:
        client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": f"请根据{prompt}写一首古诗词，"},
                {"role": "user", "content": f"请根据{prompt}写一首古诗词"}
            ],
            temperature=1.5,
            stream=False
        )
        poem = response.choices[0].message.content
        return poem
    except Exception as e:
        return f"生成诗词时出错：{str(e)}"
