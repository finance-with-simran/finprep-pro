# 📊 FinPrep Pro — Enterprise Finance Learning & Interview Preparation Platform

A comprehensive, production-ready web platform built with **Python** and **Streamlit** to master corporate finance from scratch, generate structured notes from lecture PDFs, prepare for company-accurate interview roles (Deloitte, PwC, EY, Goldman Sachs, Amazon), and master natural verbal delivery.

---

## ✨ Features Included

### 1. 📚 Learn Finance from Scratch (Interactive Curriculum)
- **Module 1**: The Three Financial Statements & Their Linkages (The $10 Depreciation Flow step-by-step).
- **Module 2**: Financial Ratio Analysis & Working Capital (Cash Conversion Cycle, DSO, DPO, DIO, DuPont ROE analysis).
- **Module 3**: Corporate Valuation & DCF Modeling (Enterprise Value vs. Equity Value, Unlevered Free Cash Flow, WACC breakdown, Terminal Value).
- **Module 4**: FP&A Essentials & Variance Analysis (AOP Budgeting, Price vs. Volume variance deconstruction).
- **🧪 Interactive Live Sandboxes**:
  - **The $10 Depreciation Real-Time Simulator**: Watch the 3 statements balance with any depreciation amount and tax rate.
  - **Dynamic 5-Year DCF Sandbox**: Tweak revenue growth, margins, WACC, and terminal growth to see Enterprise Value and Share Price calculated live.
  - **Cash Conversion Cycle (CCC) Tool**: Simulate working capital efficiency and negative working capital models (like Amazon).

### 2. 📝 Smart Notes Generator
- **Dual-Input**: Upload any finance PDF (10-K, equity research report, lecture slides) or paste raw text.
- Generates **Executive Summaries, Formula Breakdowns, Corporate Analogies, Revision Checklists, and Interactive Flip Flashcards**.
- **Dual-Engine**: Works 100% offline out-of-the-box using the built-in Financial NLP engine, with optional Gemini 2.5 Flash neural upgrade.

### 3. 💼 Searchable Interview Question Bank & Role Matching
- **Live Search**: Type company names like `"Deloitte"`, `"Goldman"`, `"PwC"`, `"Amazon"`, or concepts like `"Depreciation"`.
- **Role Filters**: Financial Analyst, FP&A Analyst, Valuation & Deal Advisory, Investment Banking, Equity Research, Corporate Finance.
- **Company-Accurate Titles Matrix**: Automatically maps company naming conventions:
  - *Deloitte*: `Valuation & Business Modeling Analyst (Financial Advisory)`
  - *EY*: `Strategy and Transactions (SaT) - VME Analyst`
  - *PwC*: `Deals - Valuation & Financial Modeling Analyst`
  - *Amazon*: `Financial Analyst - AFE / AWS FP&A`

### 4. 🎙️ Interview Verbal Delivery Coach
- Not just written answers, but **teaches you how to actually speak out loud**:
  - **Natural Spoken Script**: Conversational phrasing using the PREP/STAR frameworks.
  - **Vocal & Cadence Cues**: Pacing instructions (`[Pause for contrast]`, `[Emphasize: tax shield]`).
  - **The Rookie Trap**: Common blunders that disqualify 90% of candidates.
  - **Interviewer Follow-Up Probes**: The sharp questions asked right after your answer.

### 5. 📄 Resume-Based Personalization & Action Plan
- Upload your PDF resume or paste text.
- Select your target finance path (e.g., FP&A Analyst, Deloitte Valuation, Goldman IB).
- Instant **ATS Keyword Gap Audit**, **Quantitative Impact Scan** ($, %, x multiples), **Google X-Y-Z Bullet Point Rewrites**, and a **Personalized 4-Week Prep Plan**.

### 6. 🧭 Finance Career Explorer
- Complete profiles for 6+ major finance paths with salary benchmarks, technical skill requirements, day-in-the-life overviews, interview testing styles, and 1-click question practice.

### 7. 🎨 Clean, Professional Light-Theme UI
- Polished corporate light theme (`#FFFFFF`, `#F8FAFC`, `#0F2744`, `#2563EB`) configured via `.streamlit/config.toml` and custom CSS cards.

---

## 🚀 Quickstart: Running Locally

1. **Clone or navigate to the project directory:**
   ```bash
   cd finprep_pro
   ```

2. **(Optional) Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
   Open your browser at `http://localhost:8501`.

---

## 🌐 Publishing to GitHub & Free Deployment on Streamlit Cloud

### Step 1: Initialize Git and Push to GitHub

1. Open your terminal in the `finprep_pro` directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: FinPrep Pro finance learning platform"
   ```

2. Create a new repository on [GitHub](https://github.com/new) named `finprep-pro` (choose Public).

3. Link and push your code:
   ```bash
   git branch -M main
   git remote add origin https://github.com/YOUR_GITHUB_USERNAME/finprep-pro.git
   git push -u origin main
   ```

### Step 2: Deploy to Streamlit Community Cloud (100% Free)

1. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.
2. Click **"New app"**.
3. Select your repository: `YOUR_GITHUB_USERNAME/finprep-pro`.
4. Branch: `main`.
5. Main file path: `app.py`.
6. Click **"Deploy!"**.
7. In under 2 minutes, your website is live with a free shareable URL (e.g. `https://finprep-pro.streamlit.app`)!

---

## 📁 Project Architecture

```
finprep_pro/
├── .streamlit/
│   └── config.toml             # Light theme & UI styling configuration
├── data/
│   ├── curriculum_data.py      # Core lessons, formulas, and concepts
│   ├── interview_questions.py  # Questions, company titles, spoken scripts & traps
│   └── careers_data.py         # Career tracks, skills matrices, salary bands
├── utils/
│   ├── pdf_processor.py        # PDF text extraction & sanitization
│   ├── ai_notes.py             # Dual-engine structured notes & flashcard builder
│   ├── resume_analyzer.py      # ATS scoring, keyword gaps & bullet rewriter
│   └── interactive_tools.py    # $10 Depreciation, DCF, and CCC calculators
├── app.py                      # Main Streamlit web application
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # Documentation & setup instructions
```
