#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from rtlsdr import *
import numpy as np

from candphy.logs import log

#def for get signal on the space signals on Mhz
def get_signal_radio(freq_center,freq_rate=3.1,
                     again=8,bytes=1024,bits_base=256):
    '''
    freq_center: the frequency central (Mhz) type: float
    freq_rate: the space of frequency's (Mhz) [1.4Mhz-3.1Mhz] type:float
    '''
    mhz = 1e6
    freq_rate*=mhz
    freq_center*=mhz
    init_freq = round(freq_center-(freq_rate/2),3)
    end_freq = round(freq_center+(freq_rate/2),3)
    log(f"init frequency: {init_freq}Mhz\nend frequency: {end_freq}Mhz")
    #initalizng the sdr
    log("initializing the sdr drive...")
    sdr = RtlSdr()
    
    log("configuring the sample rate...")
    sdr.sample_rate=(freq_rate)
    
    log("configuring the frequency center of samples...")
    sdr.center_freq=(freq_center)
    
    log("configuring the again...")
    sdr.again = again
    
    log("getting the samples using the bits and bytes as base as numpy array...")
    samples = np.array(sdr.read_samples(bits_base*bytes))
    log(f"size of samples signal: {samples.size} bits")
    
    res = {'freq_center':freq_center,
           'freq_rate':freq_rate,
           'bytes':bytes,
           'order':mhz,
           'size_signal':samples.size,
           'samples':samples,
           'type':'signal_radio'}
    
    return res
    



def get_signal_radio_more(freq_center:float
                          ,freq_rate:float=9.0,
                          bytes:int=1024,
                          again:int=8,
                          bits_base=256):
       fc = freq_center
       fr = freq_rate
       f0 = fc - (fr/2)
       if fr > 3:
              n = fr//3
              rest = fr%3
              f_ = np.array([])
              for _ in range(round(n)):
                     fcent = f0 + 1.5
                     s = get_signal_radio(freq_center=fcent,freq_rate=3,
                                          bits_base=bits_base,
                                          again=again,
                                          bytes=bytes)
                     f_ = np.concatenate((f_,s['samples']))
                     f0 = fcent + 3
              if rest > 0:
                     fcent_rest = f0 + (rest/2)
                     frest = get_signal_radio(freq_center=fcent_rest,freq_rate=rest,
                                          bits_base=bits_base,
                                          again=again,
                                          bytes=bytes)
                     f_ = np.concatenate((f_,frest['samples']))
       mhz = 1e6
       fr*=mhz
       fc*=mhz
       res = {'freq_center':fc,
           'freq_rate':fr,
           'bytes':bytes,
           'order':mhz,
           'size_signal':len(f_),
           'samples':f_,
           'type':'signal_radio'}
       return res
    