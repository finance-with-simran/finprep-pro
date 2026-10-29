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
