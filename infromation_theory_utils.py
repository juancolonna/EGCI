
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import entropy

def n_components_95(a):
    a = a/np.sum(a)
    n = np.sum(np.cumsum(a) >= 0.95)    
    return n

def Entropy(p1):
    p1 = p1/np.sum(p1)
    return entropy(p1)/np.log(len(p1))

def JSD(p):
    n = len(p)
    q = np.ones(n)/n # Uniform reference
    p = np.asarray(p)
    q = np.asarray(q)
    p = p/p.sum() # normalize
    m = (p + q) / 2
    jensen0 = -2*((((n+1)/n)*np.log(n+1)-2*np.log(2*n) + np.log(n))**(-1))
    return jensen0*(entropy(p, m) + entropy(q, m)) / 2

def diff_freq_entropy(Sf):
    """Sf must be the spectrogram"""
    n = Sf.shape[1]-1
    h = np.zeros(n)
    histogramas = np.diff(Sf, axis=1)**2
#     histograma = histograma/np.sum(np.abs(histograma))
    for i in range(n):
        h = np.append(h, Entropy(histogramas[:,i]))
        
    return h

def diff_freq_HxC(Sf):
    """Sf must be the spectrogram"""
    n = Sf.shape[1]-1
    h = np.zeros(n)
    jsd = np.zeros(n)
    c = np.zeros(n)
    histogramas = np.diff(Sf, axis=1)**2
    for i in range(n):
        h = np.append(h, Entropy(histogramas[:,i]))
        jsd = np.append(jsd, JSD(histogramas[:,i]))
        c = np.append(c, h[-1]*jsd[-1])
            
    return h, jsd, c

def spectrogram_to_HfxCf(Sf):
    """Sf must be the spectrogram"""

    h = 0
    jsd = 0
    c = 0
    histograma = np.abs(np.diff(Sf, axis=1))
    sum_histograma = np.sum(histograma, axis=1)
    h = Entropy(sum_histograma)
    jsd = JSD(sum_histograma)
    c = h*jsd
            
    return h, jsd, c

def autocorr_coef(wave, lag=2):
    """Given a temporal series 'wave', autocorr_coef(wave, lag) calculates 'lag+1' autocorrelation coefficients"""
    assert lag>1, "time lag should be bigger than zero"
    assert lag<len(wave)/2, "time lag should be bigger than zero"

    n = len(wave)
    corr = np.ones(lag)
    for i in range(1,lag):
        corr[i] = np.corrcoef(wave[i:], wave[:n-i])[0, 1]
    return corr

