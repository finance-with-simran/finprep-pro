"""
FinPrep Pro — Standalone All-In-One Edition
Self-contained single-file deployment for Streamlit Community Cloud.
"""

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
"""
Curriculum and foundational finance learning modules for FinPrep Pro.
Designed for learners starting from scratch up to advanced corporate finance concepts.
"""

MODULES = [
    {
        "id": "statements",
        "title": "Module 1: The 3 Financial Statements & Their Linkages",
        "level": "Beginner to Intermediate",
        "est_time": "35 mins",
        "description": "Master how the Income Statement, Balance Sheet, and Cash Flow Statement interconnect. The foundation of 90% of finance technical interviews.",
        "lessons": [
            {
                "subtitle": "1.1 The Income Statement (P&L)",
                "summary": "Measures profitability over a specific period (Quarter or Year). Shows revenue earned minus expenses incurred.",
                "key_takeaways": [
                    "Revenue (Top line) represents earned income from goods or services.",
                    "COGS includes direct costs to manufacture or deliver the product.",
                    "Gross Profit = Revenue - COGS.",
                    "Operating Expenses (SG&A, R&D) are indirect operating overheads.",
                    "EBITDA = Earnings Before Interest, Taxes, Depreciation & Amortization (core operational cash proxy).",
                    "Net Income (Bottom line) = EBITDA - D&A - Interest - Taxes."
                ],
                "formula": "Net Income = Revenue - COGS - Operating Expenses - Interest Expense - Income Taxes",
                "pro_tip": "Interviewers love testing whether an item is on the Income Statement. Remember: Capex is NEVER on the Income Statement immediately; it is capitalized on the Balance Sheet and depreciated over time."
            },
            {
                "subtitle": "1.2 The Balance Sheet",
                "summary": "A snapshot at a single point in time showing what the company owns (Assets) and what it owes (Liabilities + Shareholders' Equity).",
                "key_takeaways": [
                    "Fundamental Equation: Assets = Liabilities + Shareholders' Equity.",
                    "Current Assets (<12 months): Cash, Accounts Receivable, Inventory, Prepaid Expenses.",
                    "Non-Current Assets (>12 months): Property, Plant & Equipment (PP&E), Intangibles, Goodwill.",
                    "Current Liabilities (<12 months): Accounts Payable, Accrued Expenses, Short-term Debt.",
                    "Shareholders' Equity: Common Stock, Additional Paid-In Capital (APIC), Retained Earnings."
                ],
                "formula": "Assets = Liabilities + Shareholders' Equity  |  Retained Earnings = Beginning RE + Net Income - Dividends",
                "pro_tip": "If your balance sheet does not balance, the most common culprit is miscalculating Cash from the Cash Flow Statement or forgetting to link Net Income to Retained Earnings."
            },
            {
                "subtitle": "1.3 The Cash Flow Statement (CFS)",
                "summary": "Tracks the actual cash generated and consumed. Crucial because Net Income uses accrual accounting and does not equal physical cash.",
                "key_takeaways": [
                    "Cash Flow from Operations (CFO): Starts with Net Income, adds back non-cash expenses (D&A), and adjusts for changes in Working Capital (AR, AP, Inventory).",
                    "Cash Flow from Investing (CFI): Capital Expenditures (Capex), acquisitions, asset sales.",
                    "Cash Flow from Financing (CFF): Debt issuance/repayment, equity issuance, share repurchases, dividends paid."
                ],
                "formula": "Ending Cash = Beginning Cash + CFO + CFI + CFF",
                "pro_tip": "Working capital rule of thumb: An INCREASE in an asset is an OUTFLOW of cash (uses cash). An INCREASE in a liability is an INFLOW of cash (sources cash)."
            },
            {
                "subtitle": "1.4 The Universal Statement Linkage (The $10 Depreciation Flow)",
                "summary": "The single most common interview question in finance across Deloitte, Goldman Sachs, JP Morgan, and Big 4.",
                "key_takeaways": [
                    "Income Statement: Operating expenses increase by $10 (Depreciation). Operating Income (EBIT) decreases by $10. Assuming a 20% tax rate, Net Income decreases by $8.",
                    "Cash Flow Statement: Net income is down $8. We add back the non-cash $10 depreciation. CFO increases by +$2 (-$8 + $10). Net change in cash is +$2.",
                    "Balance Sheet: Assets side: Cash increases by +$2, PP&E decreases by -$10 (due to accumulated depreciation). Net Assets decrease by -$8. Liabilities & Equity side: Retained earnings decrease by -$8 (from Net Income). Both sides balance at -$8!"
                ],
                "formula": "Asset Side Δ: ΔCash (+2) + ΔPP&E (-10) = -8  <==>  Equity Side Δ: ΔRetained Earnings = -8",
                "pro_tip": "Why does cash increase when depreciation goes up? Because depreciation is a tax shield. You save 20% on taxes ($2), leaving you with more physical cash."
            }
        ]
    },
    {
        "id": "ratios",
        "title": "Module 2: Financial Ratio Analysis & Working Capital",
        "level": "Intermediate",
        "est_time": "30 mins",
        "description": "Understand liquidity, profitability, leverage, and the operational Cash Conversion Cycle used by analysts to evaluate corporate health.",
        "lessons": [
            {
                "subtitle": "2.1 Liquidity & Solvency Ratios",
                "summary": "Evaluate if a firm can pay its obligations in the short-term and sustain long-term leverage.",
                "key_takeaways": [
                    "Current Ratio = Current Assets / Current Liabilities. (Target: > 1.2x to 1.5x)",
                    "Quick Ratio (Acid-Test) = (Cash + Marketable Securities + Accounts Receivable) / Current Liabilities. (Excludes less-liquid Inventory)",
                    "Debt-to-Equity (D/E) = Total Debt / Total Equity.",
                    "Interest Coverage Ratio = EBIT / Interest Expense. Indicates safety buffer for servicing debt."
                ],
                "formula": "Current Ratio = Current Assets / Current Liabilities  |  Interest Coverage = EBIT / Interest Expense",
                "pro_tip": "A current ratio well above 3.0x isn't necessarily great—it can mean the company holds excessive idle cash or has poor inventory turnover."
            },
            {
                "subtitle": "2.2 Working Capital & The Cash Conversion Cycle (CCC)",
                "summary": "Measures how many days it takes for a company to convert raw materials and inventory purchases into cash inflows.",
                "key_takeaways": [
                    "Days Sales Outstanding (DSO) = (Accounts Receivable / Total Credit Sales) * 365. How fast customers pay.",
                    "Days Sales of Inventory (DSI / DIO) = (Inventory / COGS) * 365. How long inventory sits in warehouses.",
                    "Days Payable Outstanding (DPO) = (Accounts Payable / COGS) * 365. How long the company takes to pay suppliers.",
                    "Cash Conversion Cycle (CCC) = DIO + DSO - DPO."
                ],
                "formula": "CCC = DIO + DSO - DPO",
                "pro_tip": "Companies like Amazon and Dell have NEGATIVE Cash Conversion Cycles. They collect cash from customers immediately while taking 60-90 days to pay suppliers, effectively financing growth with supplier capital."
            },
            {
                "subtitle": "2.3 The DuPont Framework (ROE Deconstruction)",
                "summary": "Deconstructs Return on Equity (ROE) into 3 distinct operational and financial levers.",
                "key_takeaways": [
                    "Lever 1: Operating Efficiency (Net Profit Margin = Net Income / Revenue)",
                    "Lever 2: Asset Use Efficiency (Asset Turnover = Revenue / Total Assets)",
                    "Lever 3: Financial Leverage (Equity Multiplier = Total Assets / Total Equity)"
                ],
                "formula": "ROE = Net Profit Margin × Asset Turnover × Financial Leverage",
                "pro_tip": "If a company's ROE is increasing, use DuPont to check why. If it's solely due to financial leverage (more debt), the underlying business is not improving—it is simply taking on more risk."
            }
        ]
    },
    {
        "id": "valuation",
        "title": "Module 3: Valuation Methodologies & DCF Modeling",
        "level": "Intermediate to Advanced",
        "est_time": "45 mins",
        "description": "Master intrinsic valuation (Discounted Cash Flow) and relative valuation (Comparable Companies & Precedent Transactions).",
        "lessons": [
            {
                "subtitle": "3.1 Enterprise Value vs. Equity Value",
                "summary": "The fundamental distinction between firm value (all capital providers) and shareholder value.",
                "key_takeaways": [
                    "Equity Value (Market Cap) = Share Price × Total Diluted Shares Outstanding.",
                    "Enterprise Value (EV) = Equity Value + Total Debt + Preferred Stock + Minority Interest - Cash & Cash Equivalents.",
                    "Why subtract Cash? Cash reduces the effective acquisition cost because an acquirer absorbs the cash balance.",
                    "Matching Principle: EV multiples use metrics available to ALL capital providers (EV/Revenue, EV/EBITDA, EV/EBIT). Equity Value multiples use metrics AFTER interest expense (P/E, Price to Book)."
                ],
                "formula": "EV = Equity Value + Total Debt - Cash & Cash Equivalents",
                "pro_tip": "Never say 'EV / Net Income' in an interview! Net income belongs only to equity holders because debt holders have already been paid interest."
            },
            {
                "subtitle": "3.2 Unlevered Free Cash Flow (FCFF)",
                "summary": "The cash generated by core operations available to both equity and debt providers.",
                "key_takeaways": [
                    "Step 1: Start with EBIT (Operating Income).",
                    "Step 2: Calculate NOPAT = EBIT × (1 - Tax Rate).",
                    "Step 3: Add back non-cash Depreciation & Amortization.",
                    "Step 4: Subtract Capital Expenditures (Capex).",
                    "Step 5: Subtract Net Change in Working Capital (ΔNWC)."
                ],
                "formula": "UFCF = EBIT × (1 - Tax Rate) + D&A - Capex - ΔNWC",
                "pro_tip": "Why do we subtract Capex and ΔNWC? Because even if they don't immediately reduce Net Income on the P&L, they represent real cash leaving the company to fund operations and capacity."
            },
            {
                "subtitle": "3.3 Weighted Average Cost of Capital (WACC)",
                "summary": "The discount rate used in an unlevered DCF, representing the blended required rate of return for debt and equity holders.",
                "key_takeaways": [
                    "Cost of Equity (CAPM) = Risk-Free Rate (Rf) + Beta (β) × Equity Risk Premium (ERP).",
                    "Cost of Debt = Effective interest rate × (1 - Tax Rate) (due to tax deductibility of interest).",
                    "Capital weights: E/V = Equity Value / (Equity Value + Debt); D/V = Debt / (Equity Value + Debt)."
                ],
                "formula": "WACC = (E/V × Ke) + (D/V × Kd × (1 - t))",
                "pro_tip": "Beta measures systematic (non-diversifiable) risk relative to the broader market. A Beta of 1.2 means the stock fluctuates 20% more than the benchmark index."
            },
            {
                "subtitle": "3.4 Terminal Value & Bridge to Per Share Value",
                "summary": "Calculating the value of the firm beyond the explicit 5-year forecast horizon.",
                "key_takeaways": [
                    "Method A: Gordon Growth Model (Perpetuity): TV = [Final Year FCF × (1 + g)] / (WACC - g), where g is long-term GDP growth (typically 2-3%).",
                    "Method B: Exit Multiple: TV = Final Year EBITDA × Target EV/EBITDA multiple.",
                    "Discount both explicit FCFs and Terminal Value back to Year 0 using WACC.",
                    "Sum of PVs = Enterprise Value.",
                    "Subtract Net Debt (Debt - Cash) to find Implied Equity Value, then divide by diluted shares."
                ],
                "formula": "Implied Share Price = (Enterprise Value - Total Debt + Cash) / Diluted Shares",
                "pro_tip": "In an interview, mention that Terminal Value typically represents 60% to 80% of total Enterprise Value in a DCF, highlighting why sensitivity analysis on WACC and terminal growth rate is vital."
            }
        ]
    },
    {
        "id": "fpa",
        "title": "Module 4: FP&A Essentials & Variance Analysis",
        "level": "Intermediate",
        "est_time": "25 mins",
        "description": "Essential methodologies for Financial Planning & Analysis, budgeting, and performance steering in corporate finance.",
        "lessons": [
            {
                "subtitle": "4.1 The FP&A Operating Cadence",
                "summary": "How corporate finance teams steer companies forward rather than just reporting backward.",
                "key_takeaways": [
                    "Annual Operating Plan (AOP / Budget): Set once a year (Q4) establishing top-down corporate targets.",
                    "Rolling Forecasts: Updated quarterly or monthly (e.g. 3+9, 6+6, 9+3) incorporating latest actuals.",
                    "Long-Range Plan (LRP): 3-to-5-year strategic models guiding capital allocation and headcount expansion."
                ],
                "formula": "Forecast = Actuals (YTD) + Projected Run-rate (Rest of Year)",
                "pro_tip": "Highlight the difference between Accounting and FP&A: Accounting looks backwards through the rearview mirror (historical GAAP compliance); FP&A looks through the windshield (future financial trajectory)."
            },
            {
                "subtitle": "4.2 Variance Analysis (Price vs. Volume Deconstruction)",
                "summary": "Explaining why Actual financial results differed from Budget.",
                "key_takeaways": [
                    "Total Variance = Actual Revenue - Budgeted Revenue.",
                    "Price Variance = (Actual Selling Price - Budgeted Selling Price) × Actual Volume.",
                    "Volume Variance = (Actual Volume - Budgeted Volume) × Budgeted Selling Price.",
                    "Cost Variance = Direct Material Variance + Labor Rate Variance + Overhead Variance."
                ],
                "formula": "Price Variance = (P_act - P_bud) × Q_act  |  Volume Variance = (Q_act - Q_bud) × P_bud",
                "pro_tip": "In an FP&A interview, if revenue missed target by $1M, never just say 'sales were down'. Deconstruct it immediately: Was it market demand drop (Volume) or competitive discounting (Price)?"
            }
        ]
    }
]


# ==========================================
# 2. INTERVIEW QUESTIONS & COMPANY TITLES
# ==========================================
"""
Database of authentic finance interview questions with company mappings,
role-specific filters, written model answers, and natural verbal delivery coaching scripts.
"""

COMPANY_TITLE_MAP = {
    "Deloitte": {
        "Financial Analyst": "Financial Advisory Analyst / Corporate Finance Analyst",
        "Valuation": "Valuation & Business Modeling Analyst (Financial Advisory)",
        "FP&A": "Commercial Advisory / FP&A Solutions Analyst",
        "Corporate Finance": "M&A Advisory & Restructuring Analyst"
    },
    "EY": {
        "Financial Analyst": "Strategy and Transactions (SaT) Analyst",
        "Valuation": "Valuation, Modeling and Economics (VME) Analyst",
        "FP&A": "Business Consulting - Finance Performance Analyst",
        "Corporate Finance": "Corporate Finance & Lead Advisory Analyst"
    },
    "PwC": {
        "Financial Analyst": "Deals - Transaction Services Analyst",
        "Valuation": "Deals - Valuation & Financial Modeling Analyst",
        "FP&A": "Finance Transformation & Strategy Consultant",
        "Corporate Finance": "Corporate Finance Advisory Analyst"
    },
    "KPMG": {
        "Financial Analyst": "Deal Advisory Analyst",
        "Valuation": "Deal Advisory - Valuations & Economic Consulting Analyst",
        "FP&A": "Financial Management Advisory Analyst",
        "Corporate Finance": "Deal Advisory - M&A Advisory Analyst"
    },
    "Goldman Sachs": {
        "Financial Analyst": "Controllers / Financial Planning & Analysis Analyst",
        "Investment Banking": "Investment Banking Analyst (Global Banking & Markets)",
        "Equity Research": "Global Investment Research (GIR) Associate",
        "Valuation": "Classic Investment Banking - Structured Finance / Valuation"
    },
    "J.P. Morgan": {
        "Financial Analyst": "Corporate Financial Planning & Analysis (C&P) Analyst",
        "Investment Banking": "Investment Banking Analyst (J.P. Morgan CIB)",
        "Equity Research": "Equity Research Analyst (Global Research)",
        "Valuation": "Corporate Valuation & Advisory Group Analyst"
    },
    "Amazon": {
        "Financial Analyst": "Financial Analyst (AFE / Operations Finance)",
        "FP&A": "Senior Financial Analyst - Central FP&A / AWS Finance",
        "Corporate Finance": "Corporate Development / Treasury Financial Analyst"
    },
    "Apple": {
        "Financial Analyst": "Operations Finance Analyst (WW Operations)",
        "FP&A": "Product FP&A / Services Financial Planning Analyst",
        "Corporate Finance": "Treasury & Structured Finance Analyst"
    },
    "Google": {
        "Financial Analyst": "Finance & Business Operations (BizOps) Analyst",
        "FP&A": "FP&A Financial Analyst (Cloud / Ads / Hardware)",
        "Corporate Finance": "Corporate Development (Alphabet Capital) Analyst"
    },
    "McKinsey": {
        "Financial Analyst": "Corporate Finance & Strategy Fellow / Analyst",
        "Valuation": "Valuation Specialist (Strategy & Corporate Finance Practice)",
        "Corporate Finance": "Corporate Finance Knowledge Specialist"
    }
}

INTERVIEW_QUESTIONS = [
    {
        "id": "q1",
        "company": "Deloitte",
        "company_title": "Valuation & Business Modeling Analyst (Financial Advisory)",
        "role": "Valuation",
        "topic": "The $10 Depreciation Flow",
        "difficulty": "Junior / Entry-Level",
        "type": "Technical Core",
        "question": "Walk me through how a $10 increase in depreciation flows through the three financial statements assuming a 20% tax rate.",
        "written_answer": (
            "1. Income Statement: Operating expenses increase by $10 due to higher depreciation, reducing Operating Income (EBIT) by $10. "
            "Assuming a 20% tax rate, tax expense decreases by $2 ($10 * 20%), so Net Income decreases by $8.\n\n"
            "2. Cash Flow Statement: Net income at the top of Cash Flow from Operations (CFO) is down by $8. "
            "We add back the $10 non-cash depreciation expense. Therefore, CFO increases by +$2 (-$8 + $10). "
            "Assuming no changes in CFI or CFF, net cash increases by +$2.\n\n"
            "3. Balance Sheet: On the Assets side, Cash is up +$2, but PP&E is down -$10 due to accumulated depreciation, so Total Assets decrease by -$8. "
            "On the Liabilities & Equity side, Retained Earnings decrease by -$8 from Net Income. Both sides balance at -$8."
        ),
        "spoken_script": (
            "\"Sure. I'll walk through the statements in order: Income Statement, Cash Flow Statement, and Balance Sheet.\n\n"
            "[Pause 1 second]\n\n"
            "First, on the Income Statement: Depreciation increases by $10. That reduces Operating Income by $10. "
            "With a 20% tax rate, our tax expense drops by $2, so Net Income goes down by $8.\n\n"
            "Second, moving to the Cash Flow Statement: Net Income starts down $8 at the top of Operating Activities. "
            "Because depreciation is a non-cash expense, we add back the entire $10. "
            "That means cash flow from operations is actually up by $2. So ending cash increases by $2.\n\n"
            "Finally, on the Balance Sheet: On the asset side, Cash is up $2, but PP&E decreases by $10 from accumulated depreciation. "
            "So net assets are down $8. On the equity side, Retained Earnings are down $8 from Net Income. "
            "Both sides balance down by $8. The net effect is that depreciation created a $2 tax shield in cash.\""
        ),
        "vocal_cues": [
            "State your structure upfront: 'I'll walk through Income Statement, Cash Flow Statement, then Balance Sheet.' This signals structured thinking.",
            "Emphasize the phrase 'non-cash expense' when moving to the Cash Flow Statement.",
            "Conclude with the insight ('tax shield of $2') rather than stopping abruptly at 'both sides balance'."
        ],
        "rookie_trap": "Candidate forgets that depreciation is tax-deductible and says cash decreases by $10, or forgets that Net Income drops by $8 and adds back $10 without adjusting for taxes.",
        "follow_up": "What happens if this was Year 2 and there was no new depreciation? How does the asset get written off?"
    },
    {
        "id": "q2",
        "company": "Deloitte",
        "company_title": "Financial Advisory Analyst / Corporate Finance Analyst",
        "role": "Financial Analyst",
        "topic": "Working Capital Impact",
        "difficulty": "Junior / Entry-Level",
        "type": "Technical Core",
        "question": "If Accounts Receivable increases by $50, how does this affect our cash balance and working capital?",
        "written_answer": (
            "An increase in Accounts Receivable of $50 means the company recognized $50 in revenue on credit but has not yet collected the cash. "
            "Operating Working Capital increases by $50 (Operating Current Assets increased). "
            "On the Cash Flow Statement under Operating Activities, an increase in AR is a cash outflow (-$50), so Net Cash decreases by $50 relative to reported earnings."
        ),
        "spoken_script": (
            "\"An increase in Accounts Receivable of $50 means we've delivered goods or services and booked revenue, but we haven't collected the cash yet.\n\n"
            "[Slight emphasis]\n\n"
            "From a working capital perspective, Operating Working Capital increases by $50 because current assets went up. "
            "However, on the Cash Flow Statement, working capital increases represent an outflow—we're essentially extending interest-free credit to our customers. "
            "So, cash decreases by $50 compared to our accrual earnings. In short: revenue is up, but cash in bank is down by $50 until collections occur.\""
        ),
        "vocal_cues": [
            "Use clear, confident terminology: 'extending credit to customers' demonstrates real business intuition.",
            "Keep the cadence brisk. This is a 30-second answer, not a 3-minute lecture."
        ],
        "rookie_trap": "Thinking an increase in an asset is a cash inflow. Always remember: buying/increasing an asset consumes cash.",
        "follow_up": "How would you look at Days Sales Outstanding (DSO) to determine if this increase is healthy growth or customer delinquency?"
    },
    {
        "id": "q3",
        "company": "PwC",
        "company_title": "Deals - Valuation & Financial Modeling Analyst",
        "role": "Valuation",
        "topic": "DCF vs Comparable Companies",
        "difficulty": "Associate / Experienced",
        "type": "Methodology",
        "question": "When would a DCF produce a higher valuation than Comparable Companies analysis, and when would it produce a lower valuation?",
        "written_answer": (
            "A DCF typically produces a higher valuation than Comps when the market is in a cyclical downturn or underpricing the sector, or when management's internal projections are aggressive regarding revenue growth or margin expansion. "
            "Conversely, a DCF produces a lower valuation when the public markets are in a speculative bubble / peak valuation multiples, or when high discount rates (WACC) or conservative terminal growth rates are applied."
        ),
        "spoken_script": (
            "\"In practice, a DCF produces a higher valuation when public market sentiment is depressed, or when the forecast reflects aggressive operational improvements that the market hasn't priced in yet.\n\n"
            "[Pivot cleanly]\n\n"
            "For example, in a cyclical trough, trading multiples like EV/EBITDA compress, making Comparable Companies look low. But a DCF looks past the cycle at 5-year normalized cash flows, producing a higher value.\n\n"
            "On the flip side, during a market peak or tech bubble where multiples are trading at all-time highs, market comps will almost certainly beat a DCF, because a disciplined DCF with a realistic WACC and terminal growth rate anchors to intrinsic fundamentals.\""
        ),
        "vocal_cues": [
            "Contrast 'cyclical trough' vs 'speculative peak' with confident vocal contrast.",
            "Mention 'intrinsic valuation' vs 'relative market sentiment' to show seniority."
        ],
        "rookie_trap": "Saying 'DCF is always more accurate because it's scientific.' In reality, DCF is hyper-sensitive to assumptions (garbage in, garbage out).",
        "follow_up": "How do you pick between Gordon Growth and Exit Multiple when calculating Terminal Value in a Deals team?"
    },
    {
        "id": "q4",
        "company": "EY",
        "company_title": "Valuation, Modeling and Economics (VME) Analyst",
        "role": "Valuation",
        "topic": "WACC & Capital Structure",
        "difficulty": "Associate / Experienced",
        "type": "Technical Core",
        "question": "Why is debt cheaper than equity, and why can't a company just finance itself with 100% debt to minimize WACC?",
        "written_answer": (
            "Debt is cheaper than equity for two reasons: (1) Seniority in the capital structure: Debt holders are paid first and have collateral claims in bankruptcy, representing lower risk. (2) Tax Shield: Interest expense is tax-deductible, whereas dividends and equity returns are paid from after-tax earnings.\n\n"
            "A company cannot finance with 100% debt because as leverage increases, the risk of financial distress and default escalates rapidly. Lenders demand significantly higher interest rates (Cost of Debt rises), and equity holders face higher volatility (Beta rises, Cost of Equity rises), eventually driving WACC up (Trade-off Theory)."
        ),
        "spoken_script": (
            "\"Debt is fundamentally cheaper than equity for two core reasons.\n\n"
            "First is seniority: debt holders sit at the very top of the capital structure. In a liquidation, they get paid before equity holders see a single dollar, so their required risk premium is lower.\n\n"
            "Second is the tax shield: interest expense is tax-deductible, reducing the effective cost of debt to Kd times (1 - tax rate).\n\n"
            "[Pause for contrast]\n\n"
            "However, you cannot simply take on 100% debt. As debt levels rise, credit rating agencies downgrade the debt, default probability increases, and lenders demand punitive interest rates. Simultaneously, equity risk skyrockets, pushing Beta higher. "
            "According to the Trade-off Theory, there is an optimal capital structure curve where WACC is minimized—push past it, and the cost of financial distress outweighs the tax benefits.\""
        ),
        "vocal_cues": [
            "Use the word 'Seniority' clearly and firmly.",
            "Refer to the 'U-shaped WACC curve' or 'Trade-off Theory' to demonstrate textbook depth coupled with practical deal acumen."
        ],
        "rookie_trap": "Only mentioning the tax shield and forgetting seniority/risk differences in the capital structure.",
        "follow_up": "If a company has an optimal capital structure of 40% debt, how do you calculate its unlevered beta from peer comps?"
    },
    {
        "id": "q5",
        "company": "Amazon",
        "company_title": "Senior Financial Analyst - Central FP&A / AWS Finance",
        "role": "FP&A Analyst",
        "topic": "Variance Analysis in Practice",
        "difficulty": "Associate / Experienced",
        "type": "Corporate Case",
        "question": "Our cloud division missed Q3 revenue by 8% versus budget, but gross margin dollars were flat. How do you explain this to the CFO?",
        "written_answer": (
            "I would break this down using Price-Volume-Mix variance analysis. Since revenue missed target by 8% but gross margin dollars remained flat, the gross margin percentage actually expanded. "
            "This suggests two likely drivers: (1) Mix shift towards higher-margin services (e.g., enterprise software / compute services rather than low-margin storage), or (2) Lower sales volume offset by lower cost of delivery / infrastructure efficiency improvements."
        ),
        "spoken_script": (
            "\"If revenue missed budget by 8% but gross margin dollars stayed flat, my immediate headline to the CFO would be: 'We saw top-line volume softness, but our gross margin percentage expanded significantly.'\n\n"
            "[Structured breakdown]\n\n"
            "I'd unpack this into three drivers:\n"
            "First, Product Mix: Did customers shift consumption toward higher-tier, higher-margin services like AI compute rather than commodity storage?\n"
            "Second, Infrastructure Cost Efficiency: Did AWS server utilization rates improve or data center power contracts decrease, lowering COGS?\n"
            "And third, Pricing Discipline: Did we discount less aggressively than assumed in the budget?\n\n"
            "I'd pull the Price-Volume-Mix waterfall chart to show the exact dollar contribution of each lever before the executive meeting.\""
        ),
        "vocal_cues": [
            "Open directly with an executive headline. Senior FP&A managers want the 'so what?' first, not a calculation recap.",
            "Use terms like 'Product Mix', 'Price-Volume-Mix waterfall', and 'Capacity utilization'."
        ],
        "rookie_trap": "Stumbling into a theoretical formula instead of thinking like an executive business partner.",
        "follow_up": "How would you forecast Q4 if you suspect customer cloud optimization is a permanent trend?"
    },
    {
        "id": "q6",
        "company": "Goldman Sachs",
        "company_title": "Investment Banking Analyst (Global Banking & Markets)",
        "role": "Investment Banking",
        "topic": "Walk Me Through a DCF",
        "difficulty": "Junior / Entry-Level",
        "type": "Technical Core",
        "question": "Walk me through a Discounted Cash Flow model from start to finish.",
        "written_answer": (
            "1. Project Unlevered Free Cash Flows (EBIT*(1-t) + D&A - Capex - ΔNWC) for 5 to 10 years.\n"
            "2. Calculate WACC (cost of debt & equity weighted by capital structure).\n"
            "3. Discount explicit cash flows to present value using WACC.\n"
            "4. Calculate Terminal Value using either Gordon Growth (FCF*(1+g)/(WACC-g)) or Exit Multiple method.\n"
            "5. Discount Terminal Value to present value and add to PV of explicit cash flows to get Enterprise Value.\n"
            "6. Subtract Net Debt (Total Debt - Cash) to find Implied Equity Value, then divide by diluted share count for implied share price."
        ),
        "spoken_script": (
            "\"A DCF values a company based on the present value of its future cash flows plus its terminal value.\n\n"
            "[Structure with fingers: 4 steps]\n\n"
            "First, we project Unlevered Free Cash Flows over a 5 to 10-year period. We start with EBIT, tax-affect it to get NOPAT, add back non-cash D&A, and subtract Capex and changes in Net Working Capital.\n\n"
            "Second, we calculate the discount rate using WACC, blending the Cost of Equity via CAPM and the after-tax Cost of Debt.\n\n"
            "Third, we estimate Terminal Value at the end of the forecast period, using either the Gordon Growth Method or an Exit Multiple like EV/EBITDA, and discount both the explicit cash flows and Terminal Value back to today at WACC.\n\n"
            "Finally, summing these gives us Enterprise Value. To reach Implied Equity Value, we subtract Net Debt—adding cash and subtracting debt and debt-equivalents—and divide by diluted shares outstanding for our target per-share price.\""
        ),
        "vocal_cues": [
            "Keep your pace steady. Most candidates speak too fast here and sound panicked. Aim for 60 to 75 seconds total.",
            "Explicitly clarify that you are using Unlevered Free Cash Flows (cash available to all capital providers), which justifies using WACC as the discount rate."
        ],
        "rookie_trap": "Saying 'we start with Net Income' for an Unlevered DCF without explaining that Net Income is levered, or forgetting to discount Terminal Value back to Year 0.",
        "follow_up": "Why do we use Unlevered FCF instead of Levered FCF for most investment banking valuations?"
    },
    {
        "id": "q7",
        "company": "J.P. Morgan",
        "company_title": "Equity Research Analyst (Global Research)",
        "role": "Equity Research",
        "topic": "Stock Pitch Framework",
        "difficulty": "Associate / Experienced",
        "type": "Pitch / Analysis",
        "question": "How do you pitch a stock in 90 seconds to an equity research portfolio manager?",
        "written_answer": (
            "A structured stock pitch consists of: (1) Recommendation, company name, ticker, current price, and 12-month price target with implied upside; (2) Business overview (revenue model); (3) Variant perception / 2-3 key catalytic investment pillars (what the market is getting wrong); (4) Valuation methodology; (5) Key downside risks and mitigants."
        ),
        "spoken_script": (
            "\"I have a BUY recommendation on Company ABC, trading at $120, with a 12-month price target of $160, representing 33% upside.\n\n"
            "[Concise business summary]\n\n"
            "ABC is the market leader in enterprise cloud compliance with 65% recurring ARR.\n\n"
            "My variant perception centers on two catalysts that consensus is underappreciating:\n"
            "First, international expansion in APAC is compounding at 45% CAGR, whereas consensus models flat 20%.\n"
            "Second, their gross margin is inflection-bound due to internal GPU cost optimizations, creating 400 bps of EBITDA margin expansion by Q4.\n\n"
            "On valuation: Trading at 14x forward EV/EBITDA versus peer median of 19x, our blended DCF and comps model supports our $160 target.\n\n"
            "The primary downside risk is regulatory delay in the EU, but this is mitigated by their existing compliance contracts. I recommend initiating a full position.\""
        ),
        "vocal_cues": [
            "State ticker, recommendation, current price, and price target in the first 10 seconds.",
            "Use the phrase 'My variant perception is...' Portfolio managers care about what YOU see that the consensus misses."
        ],
        "rookie_trap": "Spending 80 seconds describing what the company sells and only 10 seconds on why the stock is mispriced.",
        "follow_up": "What is the consensus view on this stock, and what specific metric in next quarter's earnings will prove your thesis right?"
    },
    {
        "id": "q8",
        "company": "McKinsey",
        "company_title": "Corporate Finance & Strategy Fellow / Analyst",
        "role": "Corporate Finance",
        "topic": "M&A Strategic Framework",
        "difficulty": "Associate / Experienced",
        "type": "Case Interview",
        "question": "Company A is considering acquiring Company B for $500M in cash. How would you evaluate whether this deal creates shareholder value?",
        "written_answer": (
            "Shareholder value is created if Return on Invested Capital (ROIC) exceeds WACC, or if Net Present Value (NPV) of standalone target cash flows plus net after-tax synergies exceeds the purchase price paid (including premium). "
            "Framework: (1) Strategic fit & Market attractiveness, (2) Valuation & Synergy quantification (Cost synergies vs Revenue synergies), (3) Financial feasibility (Accretion/Dilution, Debt capacity), (4) Integration & Execution risks."
        ),
        "spoken_script": (
            "\"To determine if this $500M acquisition creates value, I evaluate whether the present value of Company B's standalone cash flows plus after-tax synergies exceeds the $500M purchase price.\n\n"
            "[Structure into 3 pillars]\n\n"
            "I'd assess this across three distinct lenses:\n"
            "First, Strategic & Market rationale: Does Company B expand Company A's TAM, cross-sell into existing enterprise accounts, or fill a critical technological IP gap?\n\n"
            "Second, Synergy Economics: We categorize synergies into hard cost synergies (SG&A consolidation, procurement power) and soft revenue synergies. Cost synergies have higher certainty and discount rate reliability. We also deduct one-off integration costs.\n\n"
            "Third, Deal Mechanics: We assess whether the deal is EPS accretive in year 1 and year 2, check pro-forma Debt/EBITDA leverage to ensure investment-grade rating maintenance, and evaluate cultural retention of Company B's key talent.\""
        ),
        "vocal_cues": [
            "Distinguish between 'hard cost synergies' and 'soft revenue synergies'—interviewers love this prudence.",
            "Speak at an executive consulting pace: clear signposting (First, Second, Third)."
        ],
        "rookie_trap": "Saying 'if it's EPS accretive, it creates value.' Accretion is an accounting metric; a deal can be EPS accretive but destroy economic value if paid with cheap debt while ROIC < WACC.",
        "follow_up": "Why might an EPS accretive deal actually destroy true economic value for shareholders?"
    }
]


# ==========================================
# 3. CAREER ROLES DATA
# ==========================================
"""
Finance Career Explorer data defining roles, company-specific titles, skill matrices,
and interview assessment formats.
"""

CAREER_ROLES = [
    {
        "id": "financial_analyst",
        "title": "Financial Analyst (Corporate & Commercial)",
        "category": "Corporate Finance",
        "overview": "Evaluates business unit performance, creates financial reports, performs variance analysis, and supports operational decision-making.",
        "company_titles": {
            "Deloitte": "Financial Advisory Analyst / Corporate Advisory",
            "EY": "Strategy and Transactions Analyst",
            "PwC": "Deals - Transaction Services Analyst",
            "Tech Companies": "Finance Business Partner / Operations Finance Analyst",
            "Fortune 500": "Commercial Financial Analyst"
        },
        "technical_skills": [
            "Advanced Excel (Index/Match, XLOOKUP, Pivot Tables, SUMIFS)",
            "Three-Statement Financial Accounting (GAAP / IFRS)",
            "Variance Analysis (Budget vs Actuals)",
            "Financial Dashboarding (Power BI / Tableau)",
            "Basic SQL / Data extraction"
        ],
        "soft_skills": [
            "Cross-functional stakeholder translation",
            "Executive deck presentation",
            "Business partnering mindset"
        ],
        "day_in_life": "Participating in month-end close reviews, analyzing gross margin variances across product lines, updating forecast models, and presenting spend analyses to department heads.",
        "interview_format": "Behavioral STAR questions, Excel proficiency test (30-60 min), and accounting statement flow questions.",
        "comp_band": "$70,000 - $95,000 Base + 10-15% Bonus"
    },
    {
        "id": "fpa_analyst",
        "title": "FP&A Analyst (Financial Planning & Analysis)",
        "category": "Corporate Finance & Strategy",
        "overview": "Forward-looking corporate financial architects responsible for the Annual Operating Plan (AOP), rolling quarterly forecasts, and long-range strategic plans.",
        "company_titles": {
            "Amazon / Big Tech": "Financial Analyst - Central FP&A / AWS Finance",
            "Deloitte": "Commercial Advisory / FP&A Solutions Analyst",
            "EY": "Business Consulting - Finance Performance Analyst",
            "PwC": "Finance Transformation Consultant",
            "Fortune 500": "Senior FP&A Analyst / Strategic Finance Analyst"
        },
        "technical_skills": [
            "Dynamic driver-based financial modeling",
            "Annual Budgeting & Rolling 12-Month Forecasting",
            "Price-Volume-Mix Variance Deconstruction",
            "Anaplan / Hyperion / Adaptive Planning (EPM tools)",
            "SQL / Power BI for automated reporting"
        ],
        "soft_skills": [
            "C-suite executive presence",
            "Strategic storytelling with numbers",
            "Persuasion & commercial negotiation"
        ],
        "day_in_life": "Revising quarterly forecast scenarios, stress-testing headcount additions against budget limits, meeting with VP of Sales to review pipeline conversion rates, and preparing board decks.",
        "interview_format": "Case study on building a 3-year revenue and expense forecast, price-volume variance drill, and behavioral alignment.",
        "comp_band": "$80,000 - $115,000 Base + 15-20% Bonus"
    },
    {
        "id": "valuation_analyst",
        "title": "Valuation & Deal Modeling Analyst",
        "category": "Advisory & Big 4 Deals",
        "overview": "Values business entities, intangible assets, stock options, and debt instruments for M&A transactions, financial reporting (ASC 805 / 820), and tax compliance.",
        "company_titles": {
            "Deloitte": "Valuation & Business Modeling Analyst (Financial Advisory)",
            "EY": "Valuation, Modeling and Economics (VME) Analyst (Strategy and Transactions)",
            "PwC": "Deals - Valuation & Financial Modeling Analyst",
            "KPMG": "Deal Advisory - Valuations & Economic Consulting Analyst",
            "Boutique Advisory": "Valuation Analyst / Financial Opinions Associate"
        },
        "technical_skills": [
            "Discounted Cash Flow (DCF) modeling & WACC calculations",
            "Comparable Company Analysis (Trading Comps) & Precedent Transactions",
            "Purchase Price Allocation (PPA - ASC 805)",
            "Option Pricing Models (Black-Scholes, Monte Carlo simulations)",
            "Capital IQ, PitchBook, FactSet"
        ],
        "soft_skills": [
            "Meticulous attention to detail and methodology documentation",
            "Defensibility under audit scrutiny (PCAOB standards)",
            "Client management in deal settings"
        ],
        "day_in_life": "Spreading comparable trading multiples, conducting cost of capital calculations using Bloomberg beta data, constructing a multi-stage DCF for a target acquisition, and writing valuation reports for audit defense.",
        "interview_format": "Intense technical accounting drills ($10 depreciation flow), 2-hour DCF modeling test in Excel, and methodology defense questions.",
        "comp_band": "$85,000 - $110,000 Base + 15-25% Bonus"
    },
    {
        "id": "ib_analyst",
        "title": "Investment Banking Analyst (M&A / Capital Markets)",
        "category": "Investment Banking",
        "overview": "Advises corporate clients and private equity sponsors on buying, selling companies (M&A), and raising debt or equity capital (IPOs, bond issuances).",
        "company_titles": {
            "Goldman Sachs": "Investment Banking Analyst (Global Banking & Markets)",
            "J.P. Morgan": "Investment Banking Analyst (CIB)",
            "Morgan Stanley": "Investment Banking Analyst (Investment Banking Division)",
            "Evercore / Lazard / Moelis": "M&A Restructuring Analyst (Elite Boutique)"
        },
        "technical_skills": [
            "Three-statement integrated financial modeling without a mouse",
            "M&A Accretion/Dilution modeling",
            "Leveraged Buyout (LBO) modeling & Debt schedules",
            "Pitchbook design and PowerPoint perfection",
            "CIM (Confidential Information Memorandum) drafting"
        ],
        "soft_skills": [
            "Extreme stamina and grit (70-90 hour work weeks)",
            "Flawless formatting and zero tolerance for calculation errors",
            "Rapid synthesis of company filings (10-K, 10-Q, S-1)"
        ],
        "day_in_life": "Updating buyer logs for an ongoing sell-side mandate, adjusting pro-forma EBITDA for transaction adjustments, building a football field valuation chart in PowerPoint, and preparing management presentations.",
        "interview_format": "Rapid-fire technicals (Accounting flow, Enterprise vs Equity Value, LBO mechanics, paper LBO), 90-second stock pitch, and 'fit' interviews.",
        "comp_band": "$110,000 - $130,000 Base + 70-100% Bonus ($180k-$220k total)"
    },
    {
        "id": "equity_research",
        "title": "Equity Research Associate",
        "category": "Public Markets & Investing",
        "overview": "Analyzes publicly traded equities within a specific industry coverage (e.g. Software, Healthcare, Industrials) to issue Buy/Hold/Sell recommendations and price targets.",
        "company_titles": {
            "Goldman Sachs": "Global Investment Research (GIR) Associate",
            "J.P. Morgan": "Equity Research Analyst (Global Research)",
            "Morgan Stanley": "Research Associate (Institutional Equities)",
            "Sell-Side Brokers": "Sector Research Associate"
        },
        "technical_skills": [
            "Proprietary quarterly earnings models",
            "Variant perception and catalyst tracking",
            "KPI regression and channel checking (survey analysis)",
            "DCF and target multiple derivation",
            "Rapid report writing under strict morning deadlines"
        ],
        "soft_skills": [
            "Clear, concise written opinion formulation",
            "Verbal pitching to institutional asset managers",
            "Critical skepticism toward corporate management hype"
        ],
        "day_in_life": "Listening to 7:00 AM earnings calls, updating the quarterly financial model within 45 minutes of release, writing a 'First Take' note to institutional clients, and speaking with hedge fund clients about stock implications.",
        "interview_format": "90-second stock pitch (Buy or Short), financial statement analysis exam, and timed writing/thesis defense.",
        "comp_band": "$100,000 - $125,000 Base + 40-75% Bonus"
    },
    {
        "id": "corp_dev",
        "title": "Corporate Development Analyst (In-House M&A)",
        "category": "Corporate Strategy & Deals",
        "overview": "The buy-side M&A and venture arm of an operating company. Sits inside the corporation identifying, evaluating, and executing acquisitions and strategic partnerships.",
        "company_titles": {
            "Google / Alphabet": "Corporate Development Analyst (Alphabet Capital)",
            "Amazon": "Corporate Development Financial Analyst",
            "Microsoft": "Strategic Acquisitions & M&A Associate",
            "Salesforce": "Corporate Development & Salesforce Ventures Analyst"
        },
        "technical_skills": [
            "Buy-side valuation and business case modeling",
            "Synergy modeling (cost, revenue, headcount)",
            "Due diligence coordination across product, legal, tax",
            "Post-merger integration (PMI) planning"
        ],
        "soft_skills": [
            "Internal executive diplomacy",
            "Target founder relationship building",
            "Long-term strategic vision"
        ],
        "day_in_life": "Reviewing pitch decks from target startup founders, modeling acquisition returns (IRR, NPV, ROIC) for internal investment committees, and coordinating legal and commercial due diligence teams.",
        "interview_format": "M&A case study (Should Company X buy Company Y?), DCF/LBO modeling test, and strategic fit discussions.",
        "comp_band": "$100,000 - $130,000 Base + 20-35% Bonus + Equity/RSUs"
    }
]


# ==========================================
# 4. UTILITIES & PROCESSING ENGINES
# ==========================================
"""
Utility for processing and extracting text from uploaded PDFs or raw paste input.
"""

import io
from typing import Tuple, Optional
import pypdf

def extract_text_from_pdf(file_bytes: bytes) -> Tuple[str, int, Optional[str]]:
    """
    Extracts text cleanly from PDF bytes.
    Returns: (extracted_text, page_count, error_message)
    """
    try:
        pdf_file = io.BytesIO(file_bytes)
        reader = pypdf.PdfReader(pdf_file)
        
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception:
                return "", 0, "The PDF file is encrypted and password-protected."
                
        num_pages = len(reader.pages)
        extracted_pages = []
        
        for idx, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            if page_text.strip():
                extracted_pages.append(f"--- [Page {idx + 1}] ---\n{page_text.strip()}")
                
        full_text = "\n\n".join(extracted_pages)
        if not full_text.strip():
            return "", num_pages, "No readable text found in PDF. It might contain only scanned images or rasterized pages."
            
        return clean_text(full_text), num_pages, None
    except Exception as e:
        return "", 0, f"Error reading PDF: {str(e)}"

def clean_text(text: str) -> str:
    """Sanitizes text by stripping excessive whitespace and formatting artifacts."""
    lines = [line.strip() for line in text.split("\n")]
    # Remove empty line runs
    cleaned = []
    prev_empty = False
    for line in lines:
        if not line:
            if not prev_empty:
                cleaned.append("")
                prev_empty = True
        else:
            cleaned.append(line)
            prev_empty = False
    return "\n".join(cleaned).strip()


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


"""
Interactive financial calculation engines for hands-on learning:
1. Three-Statement $10 Depreciation Flow Simulator
2. Interactive DCF Sandbox with valuation output
3. Cash Conversion Cycle (CCC) Simulator
"""

from typing import Dict, Any

def simulate_depreciation_flow(depr_amount: float = 10.0, tax_rate: float = 0.20) -> Dict[str, Any]:
    """
    Computes exact financial statement adjustments for any depreciation amount and tax rate.
    """
    tax_savings = depr_amount * tax_rate
    net_income_impact = - (depr_amount * (1 - tax_rate))
    cfo_impact = net_income_impact + depr_amount  # = + tax_savings
    cash_impact = cfo_impact
    ppe_impact = -depr_amount
    assets_impact = cash_impact + ppe_impact  # = -depr_amount*(1-tax_rate)
    retained_earnings_impact = net_income_impact
    equity_impact = retained_earnings_impact
    
    return {
        "depreciation": depr_amount,
        "tax_rate": tax_rate,
        "tax_shield": tax_savings,
        "is_ebit_delta": -depr_amount,
        "is_tax_delta": -tax_savings,
        "is_net_income_delta": net_income_impact,
        "cfs_net_income_delta": net_income_impact,
        "cfs_addback": depr_amount,
        "cfs_cfo_delta": cfo_impact,
        "cfs_net_cash_delta": cash_impact,
        "bs_cash_delta": cash_impact,
        "bs_ppe_delta": ppe_impact,
        "bs_total_assets_delta": assets_impact,
        "bs_retained_earnings_delta": retained_earnings_impact,
        "bs_total_liab_equity_delta": equity_impact,
        "is_balanced": abs(assets_impact - equity_impact) < 0.001
    }

def calculate_dcf_sandbox(
    base_revenue: float = 100.0,
    growth_rate: float = 0.08,
    ebit_margin: float = 0.20,
    tax_rate: float = 0.21,
    capex_pct_rev: float = 0.05,
    nwc_pct_rev: float = 0.02,
    wacc: float = 0.09,
    terminal_growth: float = 0.025,
    cash: float = 20.0,
    debt: float = 40.0,
    shares: float = 10.0
) -> Dict[str, Any]:
    """
    5-Year Unlevered DCF model with terminal value and per share calculation.
    """
    years = [1, 2, 3, 4, 5]
    projections = []
    pv_cash_flows = []
    
    current_rev = base_revenue
    for yr in years:
        rev = current_rev * (1 + growth_rate)
        current_rev = rev
        ebit = rev * ebit_margin
        nopat = ebit * (1 - tax_rate)
        depr = rev * 0.04
        capex = rev * capex_pct_rev
        change_nwc = rev * nwc_pct_rev
        ufcf = nopat + depr - capex - change_nwc
        discount_factor = 1 / ((1 + wacc) ** yr)
        pv = ufcf * discount_factor
        
        projections.append({
            "Year": f"Yr {yr}",
            "Revenue ($M)": round(rev, 2),
            "EBIT ($M)": round(ebit, 2),
            "NOPAT ($M)": round(nopat, 2),
            "UFCF ($M)": round(ufcf, 2),
            "PV of FCF ($M)": round(pv, 2)
        })
        pv_cash_flows.append(pv)
        
    sum_pv_fcfs = sum(pv_cash_flows)
    
    # Terminal Value calculation (Gordon Growth)
    yr5_fcf = projections[-1]["UFCF ($M)"]
    if wacc <= terminal_growth:
        terminal_value = 0.0
        pv_tv = 0.0
    else:
        terminal_value = (yr5_fcf * (1 + terminal_growth)) / (wacc - terminal_growth)
        pv_tv = terminal_value / ((1 + wacc) ** 5)
        
    enterprise_value = sum_pv_fcfs + pv_tv
    equity_value = enterprise_value + cash - debt
    implied_share_price = max(0.0, equity_value / shares) if shares > 0 else 0.0
    tv_pct_of_ev = (pv_tv / enterprise_value * 100) if enterprise_value > 0 else 0.0
    
    return {
        "projections": projections,
        "sum_pv_fcfs": round(sum_pv_fcfs, 2),
        "terminal_value": round(terminal_value, 2),
        "pv_tv": round(pv_tv, 2),
        "enterprise_value": round(enterprise_value, 2),
        "equity_value": round(equity_value, 2),
        "implied_share_price": round(implied_share_price, 2),
        "tv_pct": round(tv_pct_of_ev, 1)
    }

def calculate_ccc(dio: float = 45.0, dso: float = 35.0, dpo: float = 50.0) -> Dict[str, Any]:
    """Computes Cash Conversion Cycle and business interpretation."""
    ccc = dio + dso - dpo
    return {
        "ccc": round(ccc, 1),
        "dio": dio,
        "dso": dso,
        "dpo": dpo,
        "is_negative": ccc < 0
    }


# ==========================================
# 5. USER INTERFACE & APPLICATION LOGIC
# ==========================================
"""
FinPrep Pro — Complete Finance Learning & Career Preparation Platform
Built with Streamlit and modern clean light-mode UI design.
"""

import streamlit as st
import pandas as pd
import os
import sys

# Ensure current directory is on python path for Streamlit Cloud
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Set page configuration - Light theme enforcement
st.set_page_config(
    page_title="FinPrep Pro | Learn Finance & Ace Interviews",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Light Theme CSS Styling
CUSTOM_CSS = """
<style>
    /* Global Page Styling */
    .stApp {
        background-color: #F8FAFC;
        color: #0F172A;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Header & Hero */
    .hero-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #EFF6FF 100%);
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 24px 28px;
        margin-bottom: 24px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
    }
    .hero-title {
        font-size: 28px;
        font-weight: 800;
        color: #0F2744;
        margin: 0;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .hero-subtitle {
        font-size: 15px;
        color: #475569;
        margin-top: 6px;
        line-height: 1.5;
    }
    
    /* Custom Cards */
    .fin-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 18px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.04);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .fin-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.08);
        border-color: #CBD5E1;
    }
    
    /* Badges & Pills */
    .badge-role {
        background-color: #EFF6FF;
        color: #1D4ED8;
        border: 1px solid #BFDBFE;
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-company {
        background-color: #F1F5F9;
        color: #334155;
        border: 1px solid #E2E8F0;
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-official-title {
        background-color: #FEF3C7;
        color: #92400E;
        border: 1px solid #FDE68A;
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    .badge-diff {
        background-color: #ECFDF5;
        color: #047857;
        border: 1px solid #A7F3D0;
        padding: 3px 10px;
        border-radius: 9999px;
        font-size: 12px;
        font-weight: 600;
        display: inline-block;
    }
    
    /* Spoken Coaching Box */
    .spoken-box {
        background-color: #F8FAFC;
        border-left: 4px solid #2563EB;
        border-radius: 4px;
        padding: 16px 18px;
        margin: 12px 0;
        font-size: 14.5px;
        line-height: 1.6;
        color: #1E293B;
    }
    .trap-box {
        background-color: #FFF1F2;
        border-left: 4px solid #E11D48;
        border-radius: 4px;
        padding: 14px 18px;
        margin: 10px 0;
        color: #9F1239;
        font-size: 14px;
    }
    .cue-box {
        background-color: #F0FDF4;
        border-left: 4px solid #16A34A;
        border-radius: 4px;
        padding: 14px 18px;
        margin: 10px 0;
        color: #166534;
        font-size: 14px;
    }
    
    /* Metric pill */
    .metric-container {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 12px 16px;
        text-align: center;
    }
    .metric-val {
        font-size: 22px;
        font-weight: 700;
        color: #1D4ED8;
    }
    .metric-lbl {
        font-size: 12px;
        color: #64748B;
        text-transform: uppercase;
        font-weight: 600;
    }
    
    /* Flashcard Style */
    .flashcard {
        background: #FFFFFF;
        border: 2px dashed #CBD5E1;
        border-radius: 10px;
        padding: 18px;
        margin: 10px 0;
    }
    
    /* Code/Formula Banner */
    .formula-tag {
        background-color: #F1F5F9;
        color: #0F172A;
        padding: 6px 12px;
        border-radius: 6px;
        font-family: monospace;
        font-weight: 600;
        border: 1px solid #E2E8F0;
        display: inline-block;
        margin: 4px 0;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# Import backend modules
# from data.curriculum_data import MODULES (embedded directly above)
# from data.interview_questions import INTERVIEW_QUESTIONS, COMPANY_TITLE_MAP (embedded directly above)
# from data.careers_data import CAREER_ROLES (embedded directly above)
# from utils.pdf_processor import extract_text_from_pdf (embedded directly above)
# from utils.ai_notes import generate_organized_notes (embedded directly above)
# from utils.resume_analyzer import analyze_resume (embedded directly above)
# from utils.interactive_tools import simulate_depreciation_flow, calculate_dcf_sandbox, calculate_ccc (embedded directly above)

# Initialize Session State
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "📚 Learn Finance"
if "filter_role" not in st.session_state:
    st.session_state.filter_role = "All Roles"
if "filter_company" not in st.session_state:
    st.session_state.filter_company = ""

# Sidebar Configuration
with st.sidebar:
    st.markdown("### 📊 FinPrep Pro")
    st.markdown("**Complete Finance Learning & Career Suite**")
    st.caption("From scratch to Bulge Bracket & Big 4 ready.")
    
    st.divider()
    
    # Navigation Radio
    nav_selection = st.radio(
        "Navigation",
        [
            "📚 Learn Finance from Scratch",
            "📝 Smart Notes Generator",
            "💼 Interview Question Bank",
            "🎙️ Verbal Delivery Coach",
            "📄 Resume Personalization",
            "🧭 Finance Career Explorer"
        ],
        index=0
    )
    
    st.divider()
    
    # Optional Gemini API Key for deep generative notes
    st.markdown("#### ⚙️ Settings")
    user_api_key = st.text_input(
        "Gemini API Key (Optional)",
        type="password",
        placeholder="Paste API key for live AI...",
        help="FinPrep Pro works 100% offline out-of-the-box. Add a Gemini key to activate advanced neural summarization."
    )
    if user_api_key:
        st.success("API Key loaded successfully!")
    else:
        st.info("Operating on built-in Financial NLP engine (No API key needed).")
        
    st.divider()
    st.markdown("💡 **Pro-Tip**: Use the **Verbal Delivery Coach** before your phone screens to practice natural speech cadence.")


# Main App Banner
st.markdown("""
<div class="hero-container">
    <div class="hero-title">
        <span>📈 FinPrep Pro</span>
        <span class="badge-role" style="font-size: 13px;">Enterprise Finance Learning</span>
    </div>
    <div class="hero-subtitle">
        Master corporate finance from scratch, generate structured notes from lecture PDFs, prepare for company-accurate interview roles (Deloitte, PwC, Goldman, Amazon), and master natural verbal delivery.
    </div>
</div>
""", unsafe_allow_html=True)


# ==========================================
# TAB 1: LEARN FINANCE FROM SCRATCH
# ==========================================
if nav_selection == "📚 Learn Finance from Scratch":
    st.markdown("## 📚 Learn Finance from Scratch")
    st.markdown("A structured, interactive curriculum designed for students and career switchers. Learn the core principles, formulas, and test them with live financial sandboxes.")
    
    # Module selector
    module_titles = [f"{m['title']} ({m['est_time']})" for m in MODULES]
    selected_idx = st.selectbox("Select Learning Module", range(len(MODULES)), format_func=lambda x: module_titles[x])
    current_module = MODULES[selected_idx]
    
    # Module Header
    st.markdown(f"### {current_module['title']}")
    st.markdown(f"*{current_module['description']}*")
    
    c1, c2 = st.columns([3, 1])
    with c1:
        st.markdown(f"**Difficulty Level:** `{current_module['level']}` | **Estimated Time:** `{current_module['est_time']}`")
    with c2:
        st.progress(1.0, text="Module Content Ready")
        
    st.write("")
    
    # Lessons in Module
    for lesson in current_module["lessons"]:
        with st.expander(f"📖 {lesson['subtitle']}", expanded=True):
            st.markdown(f"**Core Concept:** {lesson['summary']}")
            st.markdown("#### Key Takeaways & Mechanics:")
            for pt in lesson["key_takeaways"]:
                st.markdown(f"- {pt}")
            
            st.markdown(f"<div class='formula-tag'>📐 Formula: {lesson['formula']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='cue-box'>💡 <b>Interviewer Secret & Pro-Tip:</b> {lesson['pro_tip']}</div>", unsafe_allow_html=True)

    st.divider()
    
    # Interactive Sandbox Section
    st.markdown("### 🧪 Hands-On Interactive Sandboxes")
    sandbox_choice = st.radio(
        "Choose an Interactive Calculator:",
        ["1. The $10 Depreciation Flow Simulator", "2. Dynamic 5-Year DCF Sandbox", "3. Cash Conversion Cycle (CCC) Tool"],
        horizontal=True
    )
    
    if sandbox_choice == "1. The $10 Depreciation Flow Simulator":
        st.markdown("#### Real-Time 3-Statement Impact Simulator")
        st.caption("Change the depreciation increase or tax rate to see exactly how all 3 statements balance in real time.")
        
        sc1, sc2 = st.columns(2)
        with sc1:
            depr_input = st.number_input("Depreciation Increase ($)", min_value=1.0, max_value=500.0, value=10.0, step=5.0)
        with sc2:
            tax_input = st.slider("Corporate Tax Rate (%)", min_value=0, max_value=40, value=20, step=1) / 100.0
            
        res = simulate_depreciation_flow(depr_amount=depr_input, tax_rate=tax_input)
        
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Operating Income (EBIT)", f"-${res['depreciation']:.0f}")
        m2.metric("Net Income Delta", f"-${abs(res['is_net_income_delta']):.1f}")
        m3.metric("Tax Shield Savings", f"+${res['tax_shield']:.1f}")
        m4.metric("Net Cash in Bank Delta", f"+${res['cfs_net_cash_delta']:.1f}", delta="Net Inflow")
        
        col_is, col_cfs, col_bs = st.columns(3)
        with col_is:
            st.markdown("""
            <div class='fin-card'>
                <h4>1. Income Statement</h4>
                <p>• Operating Expenses: <b>+$%.1f</b></p>
                <p>• Operating Income (EBIT): <b>-$%.1f</b></p>
                <p>• Tax Expense (Shield): <b>-$%.1f</b></p>
                <hr>
                <p><b>Net Income: -$%.1f</b></p>
            </div>
            """ % (res['depreciation'], res['depreciation'], res['tax_shield'], abs(res['is_net_income_delta'])), unsafe_allow_html=True)
            
        with col_cfs:
            st.markdown("""
            <div class='fin-card'>
                <h4>2. Cash Flow Statement</h4>
                <p>• Starting Net Income: <b>-$%.1f</b></p>
                <p>• Add-back Depreciation: <b>+$%.1f</b></p>
                <p>• Cash Flow from Operations: <b>+$%.1f</b></p>
                <hr>
                <p><b>Net Change in Cash: +$%.1f</b></p>
            </div>
            """ % (abs(res['cfs_net_income_delta']), res['cfs_addback'], res['cfs_cfo_delta'], res['cfs_net_cash_delta']), unsafe_allow_html=True)
            
        with col_bs:
            st.markdown("""
            <div class='fin-card'>
                <h4>3. Balance Sheet</h4>
                <p>• Cash (from CFS): <b>+$%.1f</b></p>
                <p>• Net PP&E: <b>-$%.1f</b></p>
                <p>• <b>Total Assets: -$%.1f</b></p>
                <hr>
                <p>• Retained Earnings: <b>-$%.1f</b></p>
                <p>• <b>Liabilities & Equity: -$%.1f</b></p>
                <p style='color:#059669; font-weight:700;'>✓ Perfectly Balanced!</p>
            </div>
            """ % (res['bs_cash_delta'], abs(res['bs_ppe_delta']), abs(res['bs_total_assets_delta']), abs(res['bs_retained_earnings_delta']), abs(res['bs_total_liab_equity_delta'])), unsafe_allow_html=True)

    elif sandbox_choice == "2. Dynamic 5-Year DCF Sandbox":
        st.markdown("#### 5-Year Unlevered Discounted Cash Flow Sandbox")
        st.caption("Adjust fundamental company growth, margins, and WACC to compute Enterprise Value and Implied Share Price.")
        
        dc1, dc2, dc3 = st.columns(3)
        with dc1:
            base_rev = st.number_input("Base Revenue ($M)", value=100.0, step=10.0)
            rev_growth = st.slider("Revenue Growth (%)", 1, 30, 8) / 100.0
            ebit_margin = st.slider("EBIT Operating Margin (%)", 5, 45, 20) / 100.0
        with dc2:
            wacc_input = st.slider("WACC Discount Rate (%)", 5, 18, 9) / 100.0
            term_g = st.slider("Terminal Growth Rate (%)", 1.0, 4.0, 2.5, step=0.1) / 100.0
            capex_rate = st.slider("Capex as % of Revenue", 2, 12, 5) / 100.0
        with dc3:
            cash_val = st.number_input("Cash on Balance Sheet ($M)", value=25.0, step=5.0)
            debt_val = st.number_input("Total Debt ($M)", value=40.0, step=5.0)
            shares_out = st.number_input("Diluted Shares Outstanding (M)", value=10.0, step=1.0)
            
        dcf_res = calculate_dcf_sandbox(
            base_revenue=base_rev,
            growth_rate=rev_growth,
            ebit_margin=ebit_margin,
            tax_rate=0.21,
            capex_pct_rev=capex_rate,
            wacc=wacc_input,
            terminal_growth=term_g,
            cash=cash_val,
            debt=debt_val,
            shares=shares_out
        )
        
        # Valuation Summary Metrics
        vm1, vm2, vm3, vm4 = st.columns(4)
        vm1.metric("Enterprise Value", f"${dcf_res['enterprise_value']:.1f}M")
        vm2.metric("Equity Value", f"${dcf_res['equity_value']:.1f}M")
        vm3.metric("Implied Share Price", f"${dcf_res['implied_share_price']:.2f}")
        vm4.metric("Terminal Value % of EV", f"{dcf_res['tv_pct']}%")
        
        st.markdown("##### 5-Year Projected Cash Flow Breakdown:")
        st.dataframe(pd.DataFrame(dcf_res["projections"]), use_container_width=True)

    elif sandbox_choice == "3. Cash Conversion Cycle (CCC) Tool":
        st.markdown("#### Cash Conversion Cycle & Working Capital Simulator")
        st.caption("Understand how Days Inventory (DIO), Days Sales Outstanding (DSO), and Days Payable (DPO) dictate corporate cash flow.")
        
        cc1, cc2, cc3 = st.columns(3)
        with cc1:
            dio_val = st.slider("Days Inventory Outstanding (DIO)", 5, 150, 45)
        with cc2:
            dso_val = st.slider("Days Sales Outstanding (DSO)", 5, 120, 35)
        with cc3:
            dpo_val = st.slider("Days Payable Outstanding (DPO)", 10, 150, 50)
            
        ccc_res = calculate_ccc(dio=dio_val, dso=dso_val, dpo=dpo_val)
        
        st.metric("Cash Conversion Cycle (CCC)", f"{ccc_res['ccc']} Days")
        if ccc_res["is_negative"]:
            st.success("🔥 **Negative Working Capital Cycle!** The company collects cash from customers before paying its suppliers (like Amazon). This creates zero-cost supplier financing!")
        else:
            st.info(f"The company takes **{ccc_res['ccc']} days** to convert cash spent on inventory back into cash from sales. Lowering DSO or increasing DPO will free up liquid cash.")


# ==========================================
# TAB 2: SMART NOTES GENERATOR
# ==========================================
elif nav_selection == "📝 Smart Notes Generator":
    st.markdown("## 📝 Smart Notes Generator")
    st.markdown("Upload a PDF (lecture slides, 10-K report, equity research note, or case study) or paste raw text. FinPrep Pro transforms it into structured study notes, formulas, corporate examples, and interactive recall flashcards.")
    
    input_method = st.radio("Choose Input Method:", ["📄 Upload PDF Document", "📋 Paste Raw Content"], horizontal=True)
    
    raw_document_text = ""
    
    if input_method == "📄 Upload PDF Document":
        uploaded_pdf = st.file_uploader("Upload Finance PDF", type=["pdf"])
        if uploaded_pdf is not None:
            with st.spinner("Extracting text from PDF..."):
                extracted_text, pages, err = extract_text_from_pdf(uploaded_pdf.read())
                if err:
                    st.error(err)
                else:
                    st.success(f"Successfully parsed {pages} page(s) ({len(extracted_text):,} characters).")
                    raw_document_text = extracted_text
                    with st.expander("Preview Extracted Document Text", expanded=False):
                        st.text(raw_document_text[:2000] + ("..." if len(raw_document_text) > 2000 else ""))
    else:
        sample_finance_text = (
            "Enterprise Value (EV) represents the total economic value of a company available to all capital providers: "
            "debt holders, common shareholders, and preferred shareholders. It is calculated by taking Equity Value (Market Cap), "
            "adding Total Debt, Preferred Stock, and Minority Interest, and subtracting Cash and Cash Equivalents. "
            "Cash is deducted because in an acquisition, the buyer immediately absorbs the cash balance, reducing the net cash paid. "
            "Unlevered Free Cash Flow (FCFF) is calculated as EBIT*(1 - Tax Rate) + Depreciation - Capital Expenditures - Change in Working Capital. "
            "When performing a DCF valuation, unlevered cash flows must be discounted using the Weighted Average Cost of Capital (WACC), "
            "whereas Levered Free Cash Flow belongs solely to equity holders and is discounted using the Cost of Equity (CAPM)."
        )
        raw_document_text = st.text_area(
            "Paste Financial Text, Lecture Transcripts, or Filing Notes:",
            value=sample_finance_text,
            height=180
        )
        
    generate_btn = st.button("⚡ Generate Organized Finance Notes", type="primary", use_container_width=True)
    
    if generate_btn:
        if not raw_document_text.strip():
            st.warning("Please upload a PDF or enter some text first.")
        else:
            with st.spinner("Synthesizing concepts, extracting formulas, and structuring notes..."):
                notes_output = generate_organized_notes(raw_document_text, api_key=user_api_key)
                
                st.success(f"Notes generated via: **{notes_output['source']}**")
                
                # Render Markdown Notes
                st.markdown(notes_output["markdown"])
                
                st.divider()
                st.markdown("### 🃏 Active Recall Flashcards")
                st.caption("Click to test your memory on the material just generated:")
                
                for idx, card in enumerate(notes_output["flashcards"], 1):
                    with st.expander(f"Card {idx}: {card['question']}", expanded=False):
                        st.markdown(f"**Answer:** {card['answer']}")


# ==========================================
# TAB 3: SEARCHABLE INTERVIEW QUESTION BANK
# ==========================================
elif nav_selection == "💼 Interview Question Bank":
    st.markdown("## 💼 Searchable Interview Question Bank & Role Match")
    st.markdown("Practice authentic interview questions from premier investment banks, Big 4 firms, and tech giants. Filter by specific job roles or search by company name, with authentic company-specific job titles mapped automatically.")
    
    # Filter Row
    f_col1, f_col2, f_col3 = st.columns([2, 1.5, 1.5])
    with f_col1:
        search_query = st.text_input("🔍 Search Company, Topic, or Keyword:", placeholder="e.g. Deloitte, Goldman, WACC, Depreciation, Amazon...", value=st.session_state.filter_company)
    with f_col2:
        roles_list = ["All Roles", "Valuation", "Financial Analyst", "FP&A Analyst", "Investment Banking", "Equity Research", "Corporate Finance"]
        selected_role = st.selectbox("🎯 Filter by Role:", roles_list, index=roles_list.index(st.session_state.filter_role) if st.session_state.filter_role in roles_list else 0)
    with f_col3:
        diff_list = ["All Levels", "Junior / Entry-Level", "Associate / Experienced"]
        selected_diff = st.selectbox("📶 Difficulty:", diff_list)
        
    # Filter logic
    filtered = []
    q_lower = search_query.lower().strip()
    
    for q in INTERVIEW_QUESTIONS:
        # Match company, question, topic, or official title
        company_match = not q_lower or (
            q_lower in q["company"].lower() or 
            q_lower in q["question"].lower() or 
            q_lower in q["topic"].lower() or 
            q_lower in q["company_title"].lower()
        )
        
        role_match = (selected_role == "All Roles") or (selected_role.lower() in q["role"].lower())
        diff_match = (selected_diff == "All Levels") or (q["difficulty"] == selected_diff)
        
        if company_match and role_match and diff_match:
            filtered.append(q)
            
    st.markdown(f"**Showing {len(filtered)} matching interview questions:**")
    
    # Company Title Matrix Callout
    if search_query and any(c.lower() in search_query.lower() for c in COMPANY_TITLE_MAP.keys()):
        for comp, titles in COMPANY_TITLE_MAP.items():
            if comp.lower() in search_query.lower():
                with st.expander(f"🏢 Company Title Guide for {comp}", expanded=False):
                    st.markdown(f"*{comp} utilizes specific division titles for finance roles:*")
                    for r, t in titles.items():
                        st.markdown(f"- **{r}:** `{t}`")

    # Render questions
    if not filtered:
        st.info("No questions matched your current search filters. Try clearing the search query or selecting 'All Roles'.")
    else:
        for item in filtered:
            st.markdown(f"""
            <div class="fin-card">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:8px; flex-wrap:wrap; gap:6px;">
                    <div>
                        <span class="badge-company">🏢 {item['company']}</span>
                        <span class="badge-role">💼 {item['role']}</span>
                        <span class="badge-diff">{item['difficulty']}</span>
                    </div>
                    <span class="badge-official-title">Official Title: {item['company_title']}</span>
                </div>
                <h3 style="margin-top: 10px; font-size: 18px; color: #0F2744;">{item['question']}</h3>
                <p style="color: #64748B; font-size: 13px;">Topic: <b>{item['topic']}</b> | Category: <b>{item['type']}</b></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Sub-tabs for Written vs Spoken vs Trap
            tab_ans, tab_spoken, tab_trap = st.tabs(["📝 Model Written Answer", "🎙️ Spoken Delivery Script", "⚠️ Rookie Trap & Follow-Up"])
            
            with tab_ans:
                st.markdown(item["written_answer"])
                
            with tab_spoken:
                st.markdown("<div class='cue-box'><b>🎙️ How to Say It Out Loud (Natural Verbal Delivery):</b></div>", unsafe_allow_html=True)
                st.markdown(f"<div class='spoken-box'>{item['spoken_script']}</div>", unsafe_allow_html=True)
                st.markdown("##### Vocal & Delivery Cues:")
                for cue in item["vocal_cues"]:
                    st.markdown(f"- 🗣️ {cue}")
                    
            with tab_trap:
                st.markdown(f"""
                <div class='trap-box'>
                    <b>🚫 The Common Rookie Trap:</b><br>{item['rookie_trap']}
                </div>
                """, unsafe_allow_html=True)
                st.markdown(f"**⚔️ Immediate Interviewer Follow-Up Question:** `{item['follow_up']}`")
                
            st.write("")


# ==========================================
# TAB 4: VERBAL DELIVERY COACH
# ==========================================
elif nav_selection == "🎙️ Verbal Delivery Coach":
    st.markdown("## 🎙️ Interview Verbal Delivery Coach")
    st.markdown(
        "Finance interviews aren't just a written exam. Top firms evaluate **how you articulate answers under pressure**. "
        "Learn how to sound polished, natural, and confident without reciting robotic memorized paragraphs."
    )
    
    st.markdown("""
    <div class="hero-container" style="background:#F0FDF4; border-color:#BBF7D0;">
        <h4 style="margin:0; color:#166534;">🌟 The 3 Golden Rules of Spoken Finance Interviews</h4>
        <p style="margin:8px 0 0 0; color:#14532D; font-size:14px;">
            1. <b>Signpost Upfront:</b> Always state your roadmap first (<i>"I'll walk through the 3 statements in order: Income Statement, Cash Flow, then Balance Sheet"</i>).<br>
            2. <b>Vary Your Vocal Cadence:</b> Slow down on non-intuitive items (<i>"Depreciation creates a $2 tax shield in cash"</i>).<br>
            3. <b>End on Business Impact:</b> Don't just say <i>"it balances"</i>—explain what the metric actually means for the business.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Rehearsal Studio
    st.markdown("### 🎙️ Verbal Rehearsal Studio")
    coach_questions = [
        "Walk me through a DCF in 60 seconds",
        "How does a $10 increase in depreciation flow through the statements?",
        "Why is debt cheaper than equity?",
        "Cloud revenue missed budget by 8% but margin dollars were flat. Explain it to the CFO."
    ]
    selected_drill = st.selectbox("Select a High-Stakes Verbal Drill:", coach_questions)
    
    matching_q = next((q for q in INTERVIEW_QUESTIONS if selected_drill.lower().split()[0] in q["question"].lower() or selected_drill.lower().split()[1] in q["question"].lower()), INTERVIEW_QUESTIONS[0])
    
    c_left, c_right = st.columns([1.2, 1])
    
    with c_left:
        st.markdown(f"#### 🎯 Question: *\"{matching_q['question']}\"*")
        st.markdown(f"**Target Company / Role:** `{matching_q['company']}` — `{matching_q['company_title']}`")
        
        st.markdown("##### 🎙️ Natural Spoken Script:")
        st.markdown(f"<div class='spoken-box'>{matching_q['spoken_script']}</div>", unsafe_allow_html=True)
        
    with c_right:
        st.markdown("#### ⏱️ Verbal Cadence Guide")
        st.markdown("""
        - **Target Duration:** 45 to 75 seconds
        - **Ideal Cadence:** 130-150 words per minute
        - **Tone:** Conversational authority, not textbook reading
        """)
        
        st.markdown("##### 💡 Key Delivery Cues:")
        for cue in matching_q["vocal_cues"]:
            st.markdown(f"- {cue}")
            
        st.markdown("##### ⚠️ What Immediately Disqualifies Candidates:")
        st.markdown(f"<div class='trap-box'>{matching_q['rookie_trap']}</div>", unsafe_allow_html=True)


# ==========================================
# TAB 5: RESUME-BASED PERSONALIZATION
# ==========================================
elif nav_selection == "📄 Resume Personalization":
    st.markdown("## 📄 Resume-Based Personalization & Action Plan")
    st.markdown("Upload your resume to receive role-targeted ATS keyword scoring, quantitative impact audits, Google X-Y-Z bullet rewrites, and a customized 4-week interview preparation plan.")
    
    r_col1, r_col2 = st.columns([1, 1])
    with r_col1:
        target_role_choice = st.selectbox(
            "Select Your Target Finance Role:",
            ["Financial Analyst", "FP&A Analyst", "Valuation Analyst (Big 4 Deals)", "Investment Banking Analyst", "Equity Research Associate"]
        )
    with r_col2:
        resume_upload_type = st.radio("Resume Input Format:", ["📄 Upload PDF", "📋 Paste Text"], horizontal=True)
        
    resume_text_content = ""
    
    if resume_upload_type == "📄 Upload PDF":
        res_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"], key="res_uploader")
        if res_file:
            txt, _, err = extract_text_from_pdf(res_file.read())
            if not err:
                resume_text_content = txt
                st.success("Resume loaded successfully.")
    else:
        sample_resume = (
            "FINANCE & BUSINESS ANALYST CANDIDATE\n"
            "EDUCATION: Bachelor of Science in Finance\n"
            "EXPERIENCE:\n"
            "Financial Analyst Intern - ABC Capital\n"
            "- Responsible for analyzing monthly financial reports and assisting with budget reviews.\n"
            "- Built Excel models for revenue tracking and used Pivot Tables.\n"
            "- Helped the team with valuation models and comparable company analysis.\n"
            "- Coordinated with accounting team during quarterly close.\n"
            "SKILLS: Excel, Financial Modeling, Power BI, PowerPoint, Accounting, Budgeting"
        )
        resume_text_content = st.text_area("Paste Resume Text:", value=sample_resume, height=200)
        
    analyze_btn = st.button("🔍 Analyze Resume & Generate Personalized Roadmap", type="primary", use_container_width=True)
    
    if analyze_btn:
        if not resume_text_content.strip():
            st.warning("Please provide resume text or upload a PDF first.")
        else:
            with st.spinner("Analyzing resume against finance benchmarks..."):
                analysis = analyze_resume(resume_text_content, target_role_choice)
                
                st.markdown("### 📊 Resume Audit Results")
                
                # Metrics Row
                m1, m2, m3, m4 = st.columns(4)
                m1.metric("Role Match Score", f"{analysis['composite_score']}%", delta="Target: >80%")
                m2.metric("Target Keywords Found", f"{len(analysis['found_keywords'])}", delta="ATS Friendly")
                m3.metric("Quant Metrics Found", f"{analysis['quant_matches_count']}", delta="Need $, %, x")
                m4.metric("Finance Tools Detected", f"{len(analysis['found_tools'])}")
                
                # Keyword Breakdown
                k_col1, k_col2 = st.columns(2)
                with k_col1:
                    st.markdown("##### ✅ High-Value Keywords Present:")
                    if analysis["found_keywords"]:
                        st.write(", ".join([f"`{kw}`" for kw in analysis["found_keywords"]]))
                    else:
                        st.info("None detected yet.")
                with k_col2:
                    st.markdown("##### ⚠️ Missing ATS Keywords for this Role:")
                    if analysis["missing_keywords"]:
                        st.write(", ".join([f"`{kw}`" for kw in analysis["missing_keywords"]]))
                    else:
                        st.success("Great keyword coverage!")
                        
                st.divider()
                
                # Bullet Point Rewriter
                st.markdown("### ✍️ Bullet Point Transformations (Google X-Y-Z Formula)")
                st.caption("Transform passive duties into quantified, high-impact deal and modeling achievements:")
                
                for b in analysis["bullet_rewrites"]:
                    with st.container():
                        st.markdown(f"**Original Bullet (Weak):** *\"{b['original']}\"*")
                        st.markdown(f"<div class='trap-box'><b>Critique:</b> {b['critique']}</div>", unsafe_allow_html=True)
                        st.markdown(f"<div class='cue-box'><b>🚀 High-Impact Rewrite:</b><br>{b['improved']}</div>", unsafe_allow_html=True)
                        st.write("")
                        
                st.divider()
                
                # 4-Week Roadmap
                st.markdown(f"### 🗓️ Customized 4-Week Prep Plan for {target_role_choice}")
                for step in analysis["roadmap"]:
                    with st.expander(step["week"], expanded=True):
                        st.markdown(step["action"])


# ==========================================
# TAB 6: FINANCE CAREER EXPLORER
# ==========================================
elif nav_selection == "🧭 Finance Career Explorer":
    st.markdown("## 🧭 Finance Career Explorer & Company Title Matrix")
    st.markdown("Explore every major finance career path. Compare day-to-day responsibilities, required technical skills, compensation ranges, and discover how top employers label the exact same role differently.")
    
    # Career selection
    role_names = [r["title"] for r in CAREER_ROLES]
    selected_role_name = st.selectbox("Select Career Track:", role_names)
    career = next(r for r in CAREER_ROLES if r["title"] == selected_role_name)
    
    st.markdown(f"""
    <div class="fin-card">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <span class="badge-role">{career['category']}</span>
            <span class="badge-diff">Compensation: {career['comp_band']}</span>
        </div>
        <h2 style="margin: 8px 0; color:#0F2744;">{career['title']}</h2>
        <p style="font-size: 15px; color:#334155;">{career['overview']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown("#### 🏢 Company-Accurate Titles Matrix")
        st.caption("How premier employers name this specific position:")
        for firm, t in career["company_titles"].items():
            st.markdown(f"- **{firm}:** `{t}`")
            
        st.markdown("#### 📅 A Day in the Life")
        st.info(career["day_in_life"])
        
    with col_t2:
        st.markdown("#### 🛠️ Core Technical Skills Required")
        for skill in career["technical_skills"]:
            st.markdown(f"- 💻 {skill}")
            
        st.markdown("#### 🤝 Essential Soft Skills")
        for s in career["soft_skills"]:
            st.markdown(f"- 🗣️ {s}")
            
        st.markdown("#### 📝 Typical Interview & Testing Format")
        st.warning(career["interview_format"])
        
    st.divider()
    
    # Quick Action: Practice questions for this career
    st.markdown("#### 🚀 Ready to Practice Questions for this Career?")
    if st.button(f"Practice Interview Questions for {career['title']}", type="primary"):
        # Map to role key
        mapped_key = "Valuation" if "Valuation" in career["title"] else ("FP&A Analyst" if "FP&A" in career["title"] else ("Investment Banking" if "Investment Banking" in career["title"] else "Financial Analyst"))
        st.session_state.filter_role = mapped_key
        st.info(f"Filtered for {mapped_key}! Switch to the **💼 Interview Question Bank** tab in the sidebar to view them.")


# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 13px; padding-bottom: 20px;">
    <b>FinPrep Pro</b> — The Complete Finance Learning & Career Suite | Built with Streamlit & Light-Theme Professional Styling
</div>
""", unsafe_allow_html=True)

