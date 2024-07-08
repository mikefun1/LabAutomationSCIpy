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
print(ps.ps_handle.query("*OPC?"))
ps.set_voltage(5,"2")
print(ps.ps_handle.query("*OPC?"))
ps.set_voltage(0,"2")
print(ps.ps_handle.query("*OPC?"))


ps.disconnect()
