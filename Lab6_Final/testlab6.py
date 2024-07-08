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





print(dmm.dmm_handle.query("*OPC?"))
#dmm.dmm_handle.write('MEAS:CURR:DC?')

curr = dmm.measure_current_dc()
# print(dmm.dmm_handle.query("*OPC?"))
volty = dmm.measure_voltage_dc()
# print(dmm.dmm_handle.query("*OPC?"))


diodey = dmm.diode_continuity()
# print(dmm.dmm_handle.query("*OPC?"))
resisty = dmm.measure_resistance()
# print(dmm.dmm_handle.query("*OPC?"))
cappy = dmm.measure_capacitance()
# print(dmm.dmm_handle.query("*OPC?"))
print("Curr:",curr," Volty:",volty," Diodey:",diodey," Resisty:",resisty," Cappy:",cappy)






#dmm.dmm_handle.query('MEAS:CURR:DC?')

# Set initial DMM settings
#dmm.set_measurement_mode('multiple')

#dmm.set_measuremnt_window('primary')
#dmm.set_measurement_type('DCV')

#dmm.set_measuremnt_window('secondary')
#dmm.set_measurement_type('DCI')



dmm.disconnect()



ps.disconnect()