# -*- coding: utf-8 -*-
"""
@author: Hamideh
Created on Wed Oct  8 12:02:14 2025

Program Description:
-------------------------
Demonstration of JSON and YAML File Handling
--------------------------------------------------------------
Covers:
✔ json.dump() / json.load()
✔ yaml.safe_dump() / yaml.safe_load()
✔ Reading and writing structured data
✔ Ensuring safe parsing
"""

import json
import yaml

data = {
    "name": "Hamideh",
    "age": 39,
    "skills": ["Python", "Control Systems", "Embedded"],
    "active": True
}

# --- JSON Handling ---
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)
print("✅ JSON file created.")

with open("data.json", "r", encoding="utf-8") as f:
    json_data = json.load(f)
print("\nJSON Read:", json_data)

# --- YAML Handling ---
with open("data.yaml", "w", encoding="utf-8") as f:
    yaml.safe_dump(data, f, sort_keys=False)
print("✅ YAML file created.")

with open("data.yaml", "r", encoding="utf-8") as f:
    yaml_data = yaml.safe_load(f)
print("\nYAML Read:", yaml_data)

"""
Quick Summary:
--------------
✔ JSON → Lightweight data-interchange format (key-value)
✔ YAML → Human-friendly data format, allows comments
✔ Use safe_load/dump → Avoid security risks
"""
