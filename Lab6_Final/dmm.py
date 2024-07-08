import pyvisa
class DMM:
    
    # Constructor
    def __init__(self, Resource_Manager, DMM_VISA_ADDRESS):
        self.rm = Resource_Manager
        self.dmm_handle = None
        self.connectstatus = False
        self.visa_address = DMM_VISA_ADDRESS
        self.windowtxt = ':PRIM'
    # Function to connect computer to power supply    
    def connect(self):
        if self.connectstatus == False:
            try:
                self.dmm_handle = self.rm.open_resource(self.visa_address)
                self.dmm_handle.read_termination = '\n'
                self.dmm_handle.write_termination = '\n'
            except Exception:
                print("Unable to Connect to Digital Multimeter at " + 
                      str(self.visa_address))
                #sys.exit()
                return False
            print("Successfully Connected to Digital Multimeter")
            # self.dmm_handle.timeout = 10000
            self.dmm_handle.timeout = 20000
            self.dmm_handle.clear()
            self.connectstatus = True
        else:
            print("Device already connected")
        return self.dmm_handle
    
    # Function to disconnect computer from power supply
    def disconnect(self):
        self.dmm_handle.query("*OPC?")
        if self.connectstatus == True:
            self.dmm_handle.clear()
            self.dmm_handle.close()
            self.dmm_handle = None
            self.connectstatus = False
            print("Device Successfully Disconnected")
            return True
        else:
            print("Device not Connected")
            return False
    
    # Function to reset power supply    
    def reset(self):
        self.dmm_handle.query("*OPC?")
        self.dmm_handle.write("*RST")

        return
    
    # Function to wait until all commands are caught up
    def wait(self):
        self.dmm_handle.query("*OPC?")
        self.dmm_handle.write("*WAI")
        return
    
    # Function to return the device Address
    def __str__(self):
        return "\nDigital Multimeter Address: %s"\
        % (self.dmm_handle)
    
        # Function to return the identification string of the power supply
    def id(self):
        self.dmm_handle.query("*OPC?")
        return self.dmm_handle.write("*IDN?")
    
    def set_measurement_mode(self,mode):
        self.dmm_handle.query("*OPC?")
        if mode == 'single':
            self.dmm_handle.write('INIT:CONT OFF')
        elif mode == 'multiple':
            self.dmm_handle.write('INIT:CONT ON')
        else:
            return print('No measurement mode selected: single or multiple')
        
    def set_measurement_window(self, window):
        self.dmm_handle.query("*OPC?")
        if window == 'PRIM':
            # self.dmm_handle.write('DISP:WIND1 ON') #'CONF:PRIM:VOLT:DC AUTO'
            self.windowtxt = ':PRIM'
        elif window == 'SEC':
            # self.dmm_handle.write('DISP:WIND2 ON')
            self.windowtxt = ':SEC'

    def measure_voltage_dc(self):
        self.dmm_handle.query("*OPC?")
        print('MEAS'+self.windowtxt+':VOLT:DC?')
        # measure DC voltage
        return float(self.dmm_handle.query('MEAS'+self.windowtxt+':VOLT:DC?'))

    def measure_current_dc(self):
        self.dmm_handle.query("*OPC?")
        print('MEAS'+self.windowtxt+':CURR:DC?')
        # measure DC current
        return float(self.dmm_handle.query('MEAS'+self.windowtxt+':CURR:DC?'))

    def diode_continuity(self):
        # perform diode continuity check
        self.dmm_handle.query("*OPC?")
        return float(self.dmm_handle.query('MEAS:DIOD?'))
        #return float(self.dmm_handle.query(':MEAS:CONT?'))

    def measure_resistance(self):
        # measure resistance
        self.dmm_handle.query("*OPC?")
        return float(self.dmm_handle.query('MEAS:RES?'))

    def measure_capacitance(self):
        # measure capacitance
        self.dmm_handle.query("*OPC?")
        return float(self.dmm_handle.query('MEAS:CAP?'))

    def set_measurement_type(self, measurement_type):
        # set the measurement type to DC voltage, AC voltage, DC current, or AC current
        self.dmm_handle.query("*OPC?")
        if measurement_type == 'DCV':
            self.dmm_handle.write(':CONF:VOLT:DC')
        elif measurement_type == 'ACV':
            self.dmm_handle.write(':CONF:VOLT:AC')
        elif measurement_type == 'DCI':
            self.dmm_handle.write(':CONF:CURR:DC')
        elif measurement_type == 'ACI':
            self.dmm_handle.write(':CONF:CURR:AC')
        else:
            return print("Didn't pick a valid measurement type:\nDCV\nACV\nDCI\nACI")
        
    def find_error(self):
        self.dmm_handle.query("*OPC?")
        return print(self.dmm_handle.query('SYSTem:ERRor?'))