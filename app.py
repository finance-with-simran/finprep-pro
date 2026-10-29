"""
FinPrep Pro — Complete Finance Learning & Career Preparation Platform
Built with Streamlit and modern clean light-mode UI design.
"""

import streamlit as st
import pandas as pd
import os

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
from data.curriculum_data import MODULES
from data.interview_questions import INTERVIEW_QUESTIONS, COMPANY_TITLE_MAP
from data.careers_data import CAREER_ROLES
from utils.pdf_processor import extract_text_from_pdf
from utils.ai_notes import generate_organized_notes
from utils.resume_analyzer import analyze_resume
from utils.interactive_tools import simulate_depreciation_flow, calculate_dcf_sandbox, calculate_ccc

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
