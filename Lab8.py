import pyvisa as visa
import numpy as np
import time
import matplotlib.pyplot as plt
from TME import device_addresses
from power_supply_library_bare import power_supply
from dmm import DMM 

rm = visa.ResourceManager()
devices = device_addresses()
scope = rm.open_resource(devices.scope_address)
wfg = rm.open_resource(devices.wfg_address)


scope.write(':SING')
scope.query('*OPC?')
scope.write(':DISP:CLE')
scope.query('*OPC?')
scope.write(':CHAN1:DISP 0')
scope.query('*OPC?')
scope.write(':CHAN1:DISP 1')
scope.query('*OPC?')
scope.write(':CHAN2:SCAL 1V')
scope.query('*OPC?')
scope.write(':TIM:RANG 100e-5')
scope.query('*OPC?')
scope.write(':SING')
scope.query('*OPC?')
wfg.write('OUTP OFF')
wfg.query('*OPC?')
wfg.write('APPL:SIN 20000, 3, 1')
wfg.query('*OPC?')
wfg.write('OUTP ON')


scope.write(':RUN')
scope.query('*OPC?')
scope.write(':AUT')
