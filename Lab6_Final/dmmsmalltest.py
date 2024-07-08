import pyvisa as visa
import numpy as np
import time
import matplotlib.pyplot as plt
from dmm import DMM
from TME import device_addresses
from power_supply_library_bare import power_supply
devices = device_addresses()

rm = visa.ResourceManager()

ps_address_ = devices.ps_address
ps = power_supply(rm,ps_address_)
ps.connect()
ps.reset()
ps.wait()

ps.enable_output("2")
ps.set_voltage(5,"2")

# ps.ps_handle.write('OUTP 1,(@2)')
# ps.ps_handle.write('VOLT 5, (@ 2)')

# ps.disconnect()
# time.sleep(1)
# DMM 
dmm_address_ = devices.dmm_address
dmm = DMM(rm,dmm_address_)
dmm.connect()
dmm.reset()
dmm.wait()

# dmm.set_measurement_mode('multiple')
dmm.set_measurement_window('PRIM')
dmm.measure_voltage_dc()
dmm.set_measurement_window('SEC')
dmm.measure_current_dc()


ps.enable_output("2")
ps.set_voltage(7,"2")
dmm.set_measurement_window('PRIM')
dmm.measure_voltage_dc()
dmm.set_measurement_window('SEC')
dmm.measure_current_dc()




dmm.disconnect()
ps.disconnect()