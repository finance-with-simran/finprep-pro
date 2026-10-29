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
