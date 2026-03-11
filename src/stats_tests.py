import numpy as np
from statsmodels.stats.proportion import proportions_ztest

def run_ztest(control, treatment):
    """
    Runs a two proportion Z-test.
    
    Parameters:
    - control: pandas Series of control group conversions
    - treatment: pandas Series of treatment group conversions
    
    Returns:
    - z_stat, p_value, control_rate, treatment_rate, uplift
    """
    counts = [treatment.sum(), control.sum()]
    nobs = [len(treatment), len(control)]
    
    z_stat, p_value = proportions_ztest(counts, nobs)
    
    control_rate = control.mean()
    treatment_rate = treatment.mean()
    uplift = (treatment_rate - control_rate) / control_rate * 100
    
    return {
        'z_statistic': round(z_stat, 4),
        'p_value': round(p_value, 4),
        'control_rate': round(control_rate, 4),
        'treatment_rate': round(treatment_rate, 4),
        'uplift_pct': round(uplift, 2)
    }