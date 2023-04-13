import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 728846853 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p = st.mannwhitneyu(x,y,alternative = 'greater').pvalue
    if p < 0.09:
        return True
    else:
        return False
