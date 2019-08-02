# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:46:12 2019

@author: Brodie

Recursively fill out the table:

| P (mb) | T (°C)  | Td (°C) | θ (K) | θe (K) | θes (K) | w (g/kg) | RH (%) |
|:------:|:-------:|:-------:|:-----:|:------:|:-------:|:--------:|:------:|
|   -    | 0       | -5      | 309   |   -    | -       | -        | -      |
| 1000   | 28      | 23      | -     |   -    | -       | -        | -      |
|   -    | -       | -       | 305   | 335    | 360     | -        | -      |
|   -    | -       | -       | 325   |   -    | -       | 6        | 80     |
| 750    | -       | 16      | -     |   -    | 370     | -        | -      |
"""
import metpy.calc as mp
from metpy.units import units
table = {'r_1': [True, 0, -5, 309, True, True, True, True],
         'r_2': [1000, 28, 23, True, True, True, True, True],
         'r_3': [True, True, True, 305, 335, 360, True, True],
         'r_4': [True, True, True, 325, True, True, 6, 80],
         'r_5': [750, True, 16, True, True, 370, True, True]}

def getPress(table):
    """
    Pressure can be had from Temp and Theta but I don't

theta_r1 = mpcalc.potential_temperature(p, t)
thetaE_r1 = mpcalc.equivalent_potential_temperature(p, t, td)
thetaEs_r1 = mpcalc.saturation_equivalent_potential_temperature(p, t)

c_to_k = 273.15
p = 900
t = 20
td = 15
th = False
th_e = False
th_es = False
w =False
rh = False
th = mp.potential_temperature(p * units.mbar,  (t + c_to_k) * units.kelvin)
th_e = mp.equivalent_potential_temperature(p * units.mbar, (t + c_to_k) * units.kelvin, (td + 273.15) * units.kelvin)
th_es = mp.saturation_equivalent_potential_temperature(p * units.mbar, (t + c_to_k) * units.kelvin)
rh = mp.relative_humidity_from_dewpoint((t + c_to_k) * units.kelvin, ((td + c_to_k) * units.kelvin))
w = mp.mixing_ratio_from_relative_humidity(rh, (t + c_to_k) * units.kelvin, p * units.mbar)
