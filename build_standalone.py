import os

base_dir = r"C:\Users\Syeda Simran\.gemini\antigravity\scratch\finprep_pro"

with open(os.path.join(base_dir, "data", "curriculum_data.py"), encoding="utf-8") as f:
    curr = f.read()
with open(os.path.join(base_dir, "data", "interview_questions.py"), encoding="utf-8") as f:
    iq = f.read()
with open(os.path.join(base_dir, "data", "careers_data.py"), encoding="utf-8") as f:
    car = f.read()
with open(os.path.join(base_dir, "utils", "pdf_processor.py"), encoding="utf-8") as f:
    pdf = f.read()
with open(os.path.join(base_dir, "utils", "ai_notes.py"), encoding="utf-8") as f:
    notes = f.read()
with open(os.path.join(base_dir, "utils", "resume_analyzer.py"), encoding="utf-8") as f:
    res = f.read()
with open(os.path.join(base_dir, "utils", "interactive_tools.py"), encoding="utf-8") as f:
    tools = f.read()
with open(os.path.join(base_dir, "app.py"), encoding="utf-8") as f:
    app = f.read()

import_lines = [
    "from data.curriculum_data import MODULES",
    "from data.interview_questions import INTERVIEW_QUESTIONS, COMPANY_TITLE_MAP",
    "from data.careers_data import CAREER_ROLES",
    "from utils.pdf_processor import extract_text_from_pdf",
    "from utils.ai_notes import generate_organized_notes",
    "from utils.resume_analyzer import analyze_resume",
    "from utils.interactive_tools import simulate_depreciation_flow, calculate_dcf_sandbox, calculate_ccc"
]

for line in import_lines:
    app = app.replace(line, f"# {line} (embedded directly above)")

combined = f"""\"\"\"
FinPrep Pro — Standalone All-In-One Edition
Self-contained single-file deployment for Streamlit Community Cloud.
\"\"\"

import streamlit as st
import pandas as pd
import os
import sys
import io
import re
from typing import Dict, Any, List, Tuple, Optional
import pypdf

# ==========================================
# 1. CURRICULUM DATA
# ==========================================
{curr}

# ==========================================
# 2. INTERVIEW QUESTIONS & COMPANY TITLES
# ==========================================
{iq}

# ==========================================
# 3. CAREER ROLES DATA
# ==========================================
{car}

# ==========================================
# 4. UTILITIES & PROCESSING ENGINES
# ==========================================
{pdf}

{notes}

{res}

{tools}

# ==========================================
# 5. USER INTERFACE & APPLICATION LOGIC
# ==========================================
{app}
"""

out_path = os.path.join(base_dir, "app_standalone.py")
with open(out_path, "w", encoding="utf-8") as f:
    f.write(combined)

print("Created standalone file at:", out_path)
