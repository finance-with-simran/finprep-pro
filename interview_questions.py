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
