import pyvisa as visa
from TME import device_addresses
import time
from matplotlib import pyplot as plt


devices_add = device_addresses()
ps_address = devices_add.ps_address

if not (ps_address):
    print("Could not find E36300 series power supply.")
    exit()

rm = visa.ResourceManager()
ps = rm.open_resource(ps_address)

# Reset power supply to default settings
ps.write('*RST')

# Set channel 2 to 0V and 20mA
ps.write('INST CH2')  # Select channel 2
ps.write('VOLT 0')   # Set voltage to 0V
ps.write('CURR 0.02')   # Set current to 20mA

# Turn on power supply
ps.write('OUTP ON')


voltages = []
currents = []

# Set voltage in increments of 0.5V and record values
for voltage in range(0, 21, 1):
    voltage *= 0.5
    ps.write('INST CH2')  # Select channel 2
    ps.write(f'VOLT {voltage}')   # Set voltage to 0V
    ps.write(f'CURR 0.02')   # Set current to 20mA

    # Wait for voltage and current to settle
    time.sleep(1)

    # Record values
    voltage_meas = float(ps.query("MEASure:VOLTage? CH2"))
    current = float(ps.query("MEASure:CURRent? CH2"))
    
    # Append values to arrays
    voltages.append(voltage_meas)
    currents.append(current)
    
    print("Voltage: %.4f V" % voltage_meas)
    print("Current: %.4f mA" % current)
    print("\n")

plt.figure()
plt.plot(voltages, currents)
plt.title("I-V Curve of Red LED")
plt.ylabel("Current")
plt.xlabel("Voltage")
plt.show()

