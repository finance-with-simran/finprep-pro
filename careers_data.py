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
