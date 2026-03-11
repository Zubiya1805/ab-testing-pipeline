import pandas as pd
import numpy as np

def generate_ab_data(n_users=10000, control_rate=0.10, 
                     treatment_rate=0.12, seed=42):
    """
    Generates simulated A/B test data.
    
    Parameters:
    - n_users: total number of users
    - control_rate: conversion rate for control group
    - treatment_rate: conversion rate for treatment group
    - seed: random seed for reproducibility
    
    Returns:
    - DataFrame with columns: user_id, group, converted
    """
    np.random.seed(seed)
    size = n_users // 2
    
    control_users = pd.DataFrame({
        'user_id': np.arange(1, size + 1),
        'group': 'control',
        'converted': np.random.binomial(1, control_rate, size)
    })
    
    treatment_users = pd.DataFrame({
        'user_id': np.arange(size + 1, n_users + 1),
        'group': 'treatment',
        'converted': np.random.binomial(1, treatment_rate, size)
    })
    
    df = pd.concat([control_users, treatment_users], ignore_index=True)
    return df