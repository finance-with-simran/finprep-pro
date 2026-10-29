"""
AI and heuristic-powered notes generator for finance documents.
Provides structured notes: Summary, Key Principles, Formulas, Practical Context, and Flashcards.
Works 100% out-of-the-box offline, with optional Gemini API upgrade.
"""

import os
import re
from typing import Dict, Any, List

def generate_organized_notes(content: str, api_key: str = "") -> Dict[str, Any]:
    """
    Transforms raw document content into structured, high-retention finance notes.
    Attempts Gemini API if key is available; otherwise uses deterministic finance NLP engine.
    """
    key = api_key.strip() or os.getenv("GEMINI_API_KEY", "").strip()
    
    if key:
        try:
            from google import genai
            client = genai.Client(api_key=key)
            prompt = f"""
You are a senior Wall Street finance professor and expert curriculum architect.
Analyze the following financial document or notes and produce structured, professional study notes.

Document Content:
\"\"\"{content[:15000]}\"\"\"

Generate your output in valid markdown with these exact sections:
### 1. Executive Summary & Core Thesis
(3-4 high-impact sentences explaining the fundamental business or financial significance)

### 2. Core Concepts & Technical Breakdown
(Detailed bullet points deconstructing the mechanisms, accounting flows, or corporate finance logic)

### 3. Financial Formulas & Mathematical Definitions
(List key formulas, defining each component and metric clearly)

### 4. Real-World Corporate Example
(An industry case or practical scenario illustrating how a company like Apple, Amazon, or Deloitte would apply this)

### 5. High-Yield Exam & Interview Revision Checklist
(5-6 punchy, memorable bullet points for quick recall)

### 6. Active Recall Flashcards
(Provide 4-5 flashcard pairs in this format:
- **Q:** [Specific question]
  **A:** [Crisp, high-impact answer]
)
"""
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            if response and response.text:
                return {
                    "source": "Gemini AI Engine",
                    "markdown": response.text,
                    "flashcards": extract_flashcards_from_text(response.text)
                }
        except Exception as e:
            # Fall back to offline rule-based parser on any error
            pass

    # Built-in offline Financial NLP Engine
    return generate_offline_notes(content)

def generate_offline_notes(content: str) -> Dict[str, Any]:
    """
    High-quality deterministic financial extractor when running offline or without an API key.
    """
    paragraphs = [p.strip() for p in content.split("\n\n") if len(p.strip()) > 30]
    sentences = re.split(r'(?<=[.!?])\s+', content)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]
    
    # Financial keywords mapping
    finance_keywords = {
        "Valuation": ["dcf", "wacc", "discount rate", "terminal value", "enterprise value", "equity value", "multiples", "ebitda"],
        "Financial Statements": ["income statement", "balance sheet", "cash flow", "depreciation", "working capital", "net income", "cfo"],
        "Profitability & Metrics": ["gross margin", "operating margin", "roe", "roic", "ebit", "revenue", "cogs"],
        "Corporate Strategy": ["synergies", "merger", "acquisition", "capital structure", "leverage", "debt", "equity"]
    }
    
    # Identify key topic matches
    matched_topics = []
    lower_content = content.lower()
    for topic, terms in finance_keywords.items():
        if any(term in lower_content for term in terms):
            matched_topics.append(topic)
            
    topic_header = ", ".join(matched_topics) if matched_topics else "Corporate Finance & Financial Analysis"

    # Select representative sentences for summary
    summary_sentences = sentences[:3] if len(sentences) >= 3 else sentences
    exec_summary = " ".join(summary_sentences)
    if not exec_summary:
        exec_summary = "The uploaded material provides foundational finance analysis, operational metrics, and corporate financial principles."

    # Identify potential formulaic or quantitative lines
    formula_lines = []
    concept_lines = []
    for s in sentences:
        if any(sym in s for sym in ["=", "+", "-", "/", "×", "%", "ratio", "calculated as"]):
            if len(formula_lines) < 4:
                formula_lines.append(s)
        elif len(s) > 40 and len(concept_lines) < 6:
            concept_lines.append(s)

    if not formula_lines:
        formula_lines = [
            "Operating Margin = Operating Income (EBIT) / Total Revenue",
            "Free Cash Flow = CFO - Capital Expenditures (Capex)",
            "Enterprise Value = Equity Value + Total Debt - Cash & Cash Equivalents"
        ]

    if not concept_lines:
        concept_lines = sentences[:5] if sentences else ["Analysis of underlying revenue drivers and capital allocation."]

    # Build Markdown structure
    md = []
    md.append(f"### 1. Executive Summary & Core Thesis ({topic_header})")
    md.append(f"{exec_summary}\n")
    
    md.append("### 2. Core Concepts & Technical Breakdown")
    for i, line in enumerate(concept_lines[:5], 1):
        md.append(f"- **Key Point {i}:** {line}")
    md.append("")
    
    md.append("### 3. Financial Formulas & Mathematical Definitions")
    for formula in formula_lines[:4]:
        md.append(f"- ` {formula} `")
    md.append("")
    
    md.append("### 4. Real-World Corporate Application")
    md.append(
        "In corporate practice (e.g. at firms like Deloitte, Amazon, or Goldman Sachs), these principles guide "
        "capital deployment, M&A due diligence, and financial reporting. Analysts utilize these exact drivers "
        "to evaluate operating leverage and forecast sustainable free cash flow under various sensitivity scenarios.\n"
    )
    
    md.append("### 5. High-Yield Exam & Interview Revision Checklist")
    md.append("- Verify whether cash or non-cash adjustments are reflected on the Cash Flow Statement.")
    md.append("- Always tie Income Statement net results directly into Retained Earnings on the Balance Sheet.")
    md.append("- Scrutinize working capital movements: asset increases represent cash drains; liability increases provide short-term funding.")
    md.append("- Ensure the discount rate (WACC) matches the cash flow definition (Unlevered FCF vs Levered FCF).\n")
    
    # Generate interactive flashcards
    flashcards = [
        {
            "question": f"What is the primary objective of {matched_topics[0] if matched_topics else 'Financial Modeling'}?",
            "answer": "To translate operational and market assumptions into integrated cash flow projections for valuation and strategic capital allocation."
        },
        {
            "question": "How does an increase in operating working capital affect cash flow?",
            "answer": "An increase in working capital (e.g. higher Accounts Receivable or Inventory) consumes cash, resulting in a cash outflow on the CFS."
        },
        {
            "question": "What is the critical difference between Enterprise Value and Equity Value?",
            "answer": "Enterprise Value represents the total value of core operating assets available to ALL capital providers, whereas Equity Value is attributable solely to common shareholders."
        },
        {
            "question": "Why do analysts add back Depreciation and Amortization to Net Income in CFO?",
            "answer": "Depreciation is an accounting allocation of past capex (non-cash expense). Adding it back restores the true cash generated by current operations."
        }
    ]
    
    return {
        "source": "Smart Financial NLP Synthesizer (Offline Ready)",
        "markdown": "\n".join(md),
        "flashcards": flashcards
    }

def extract_flashcards_from_text(text: str) -> List[Dict[str, str]]:
    """Extracts Q&A flashcards from generated markdown text."""
    cards = []
    qa_pattern = re.findall(r'-\s*\*\*Q:\*\*\s*(.*?)\n\s*-\s*\*\*A:\*\*\s*(.*?)(?=\n-|\Z)', text, re.DOTALL)
    if not qa_pattern:
        qa_pattern = re.findall(r'\*\*Q:\*\*\s*(.*?)\n\s*\*\*A:\*\*\s*(.*?)(?=\n\*\*Q|\Z)', text, re.DOTALL)
        
    for q, a in qa_pattern:
        cards.append({"question": q.strip(), "answer": a.strip()})
        
    if not cards:
        cards = [
            {"question": "How do you define Free Cash Flow?", "answer": "Operating cash flow minus capital expenditures, representing discretionary cash for investors."},
            {"question": "Why is WACC the appropriate discount rate for an Unlevered DCF?", "answer": "Because unlevered cash flows belong to all capital providers (both debt and equity holders)."}
        ]
    return cards
