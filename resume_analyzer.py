"""
Resume evaluation engine providing target-role scoring, keyword gap analysis,
bullet point rewrites (Google X-Y-Z formula), and customized 4-week study roadmap.
"""

import re
from typing import Dict, Any, List

ROLE_SKILL_REQUIREMENTS = {
    "Financial Analyst": {
        "core_keywords": ["financial analysis", "variance analysis", "budgeting", "forecasting", "excel", "financial statements", "kpi", "reporting", "p&l", "reconciliation"],
        "tools": ["excel", "power bi", "tableau", "sql", "sap", "netsuite", "quickbooks"],
        "modeling": ["three-statement", "cash flow", "break-even", "sensitivity"]
    },
    "FP&A Analyst": {
        "core_keywords": ["fp&a", "annual operating plan", "aop", "rolling forecast", "variance analysis", "driver-based", "ebitda", "opex", "capex", "headcount modeling", "strategic planning"],
        "tools": ["anaplan", "hyperion", "adaptive insights", "excel", "power bi", "sql"],
        "modeling": ["scenario analysis", "three-statement", "waterfall", "price volume"]
    },
    "Valuation Analyst (Big 4 Deals)": {
        "core_keywords": ["valuation", "dcf", "discounted cash flow", "wacc", "comparable companies", "precedent transactions", "purchase price allocation", "ppa", "asc 805", "intangible assets", "cost of capital"],
        "tools": ["capital iq", "factset", "bloomberg", "pitchbook", "excel"],
        "modeling": ["dcf", "football field", "monte carlo", "black-scholes", "lbo"]
    },
    "Investment Banking Analyst": {
        "core_keywords": ["investment banking", "m&a", "mergers and acquisitions", "accretion", "dilution", "lbo", "leveraged buyout", "pitchbook", "cim", "due diligence", "fairness opinion", "capital markets"],
        "tools": ["factset", "capital iq", "bloomberg", "excel", "powerpoint"],
        "modeling": ["three-statement", "lbo", "m&a accretion dilution", "dcf"]
    },
    "Equity Research Associate": {
        "core_keywords": ["equity research", "stock pitch", "coverage", "earnings call", "consensus", "catalyst", "variant perception", "price target", "10-k", "10-q", "initiation of coverage"],
        "tools": ["bloomberg", "factset", "excel", "python", "r"],
        "modeling": ["quarterly earnings model", "dcf", "segment forecasting"]
    }
}

def analyze_resume(resume_text: str, target_role: str) -> Dict[str, Any]:
    """
    Performs comprehensive audit of resume text against the target finance position.
    """
    text_lower = resume_text.lower()
    role_specs = ROLE_SKILL_REQUIREMENTS.get(target_role, ROLE_SKILL_REQUIREMENTS["Financial Analyst"])
    
    # 1. Check Core Keywords
    found_keywords = [kw for kw in role_specs["core_keywords"] if kw in text_lower]
    missing_keywords = [kw for kw in role_specs["core_keywords"] if kw not in text_lower]
    keyword_score = int((len(found_keywords) / max(len(role_specs["core_keywords"]), 1)) * 100)
    
    # 2. Check Tools
    found_tools = [tool for tool in role_specs["tools"] if tool in text_lower]
    missing_tools = [tool for tool in role_specs["tools"] if tool not in text_lower]
    
    # 3. Check Financial Modeling Skills
    found_modeling = [m for m in role_specs["modeling"] if m in text_lower]
    missing_modeling = [m for m in role_specs["modeling"] if m not in text_lower]
    
    # 4. Check Quantitative Impact Metrics ($, %, x, bps)
    metric_matches = re.findall(r'(\$\d+[\d,.]*[kKmMbB]?|\b\d+%\b|\b\d+\.?\d*x\b|\b\d+\s*bps\b)', resume_text)
    quant_score = min(100, len(metric_matches) * 15)
    
    # 5. Strong Finance Action Verbs
    action_verbs = ["spearheaded", "engineered", "built", "modeled", "streamlined", "forecasted", "structured", "evaluated", "optimized", "audited", "automated"]
    found_verbs = [v for v in action_verbs if v in text_lower]
    
    # Overall Composite Score
    composite_score = int(
        (keyword_score * 0.40) +
        (min(100, len(found_tools) * 25) * 0.20) +
        (min(100, len(found_modeling) * 30) * 0.20) +
        (quant_score * 0.20)
    )
    composite_score = max(25, min(95, composite_score))
    
    # Dynamic Bullet Point Suggestions
    bullet_rewrites = [
        {
            "original": "Responsible for analyzing monthly financial reports and assisting with budget reviews.",
            "critique": "Passive phrasing ('Responsible for'), lacks quantified scale, doesn't mention the financial tooling used.",
            "improved": f"Engineered monthly dynamic variance models across $12M+ operational budget in Excel, identifying $140K in annualized SG&A savings."
        },
        {
            "original": "Helped the team with valuation models and comparable company analysis.",
            "critique": "Weak verb ('Helped'), no mention of methodology rigor, discount rates, or deal outcomes.",
            "improved": f"Constructed multi-stage DCF and Trading Comps models for 4 cross-border transactions, calibrating WACC and presenting sensitivity tables to senior partners."
        }
    ]
    
    # Personalized 4-Week Prep Roadmap
    roadmap = [
        {
            "week": "Week 1: Foundational Modeling & Statement Linking",
            "action": f"Master 3-statement linking in Excel and address keyword gaps: {', '.join(missing_keywords[:3]) if missing_keywords else 'Core financial mechanisms'}. Practice the $10 depreciation flow until verbal delivery is effortless."
        },
        {
            "week": "Week 2: Role-Specific Tooling & Metrics",
            "action": f"Incorporate industry tools ({', '.join(missing_tools[:2]) if missing_tools else 'Power BI / Capital IQ'}) into portfolio projects. Quantify every bullet on your resume with dollar values or margin percentages."
        },
        {
            "week": "Week 3: Valuation & Case Modeling Drills",
            "action": f"Build a clean Unlevered DCF model from scratch. Master {', '.join(missing_modeling[:2]) if missing_modeling else 'LBO and sensitivity tables'}. Memorize the exact WACC formula and CAPM components."
        },
        {
            "week": "Week 4: Mock Verbal Delivery & Fit Mastery",
            "action": "Record yourself answering high-stakes interview questions using the FinPrep Pro Verbal Delivery Coach. Practice eliminating filler words ('um', 'like') and deliver structured 60-second answers."
        }
    ]
    
    return {
        "role": target_role,
        "composite_score": composite_score,
        "found_keywords": found_keywords,
        "missing_keywords": missing_keywords,
        "found_tools": found_tools,
        "missing_tools": missing_tools,
        "found_modeling": found_modeling,
        "missing_modeling": missing_modeling,
        "quant_matches_count": len(metric_matches),
        "found_verbs": found_verbs,
        "bullet_rewrites": bullet_rewrites,
        "roadmap": roadmap
    }
