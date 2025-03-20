#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数据加载模块：自动扫描 dataset 目录下所有子文件夹，
将每个子文件夹中的所有 JSON 文件数据合并为一个列表，
返回一个字典，键为子文件夹名称（类别），值为对应诗词列表。
"""

import os
import json

def load_all_data(data_dir="dataset"):
    all_data = {}
    if not os.path.exists(data_dir):
        print("数据目录不存在！")
        return all_data

    for entry in os.listdir(data_dir):
        entry_path = os.path.join(data_dir, entry)
        if os.path.isdir(entry_path):
            poems = []
            for filename in os.listdir(entry_path):
                if filename.endswith(".json"):
                    file_path = os.path.join(entry_path, filename)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            if isinstance(data, list):
                                poems.extend(data)
                            else:
                                poems.append(data)
                    except Exception as e:
                        print(f"加载 {file_path} 时出错: {e}")
            if poems:
                all_data[entry] = poems
    return all_data
