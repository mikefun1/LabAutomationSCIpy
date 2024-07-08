import pyvisa
class power_supply:
    # Constructor
    def __init__(self, Resource_Manager, PS_VISA_ADDRESS):
        self.rm = Resource_Manager
        self.ps_handle = None
        self.connectstatus = False
        self.visa_address = PS_VISA_ADDRESS
    
    # Function to connect computer to power supply    
    def connect(self):
        if self.connectstatus == False:
            try:
                self.ps_handle = self.rm.open_resource(self.visa_address)
                self.ps_handle.read_termination = '\n'
                self.ps_handle.write_termination = '\n'
            except Exception:
                print("Unable to Connect to Power Supply at " + 
                      str(self.visa_address))
                #sys.exit()
                return False
            print("Successfully Connected to Power Supply")
            #self.ps_handle.timeout = 10000
            self.ps_handle.timeout = 10000
            self.ps_handle.clear()
            self.connectstatus = True
        else:
            print("Device already connected")
        return self.ps_handle
    
    # Function to disconnect computer from power supply
    def disconnect(self):
        if self.connectstatus == True:
            self.ps_handle.clear()
            self.ps_handle.close()
            self.ps_handle = None
            self.connectstatus = False
            print("Device Successfully Disconnected")
            return True
        else:
            print("Device not Connected")
            return False
    
    # Function to reset power supply    
    def reset(self):
        self.ps_handle.write("*RST")

        return
    
    # Function to wait until all commands are caught up
    def wait(self):
        self.ps_handle.write("*WAI")
        return
    
    # Function to return the device Address
    def __str__(self):
        return "\nPower suppply Address: %s"\
        % (self.ps_address)
    
        # Function to return the identification string of the power supply
    def id(self):
        self.ps_handle.query("OUTP?")
        self.ps_handle.write("*IDN?")
        return self.ps_handle.read()
    
    # Function to select the channel to activate
    def select_channel(self, channel):
        self.ps_handle.query("OUTP?")
        self.ps_handle.write("INST:NSEL " + str(channel))
        return
    
    # Function to return the currently selected channel
    def selected_channel(self):
        self.ps_handle.query("OUTP?")
        self.ps_handle.write("INST:NSEL?")
        return int(self.ps_handle.read())
    
    # Function to enable channel output
    def enable_output(self,channel):
        #self.ps_handle.write("OUTP ON")
        self.ps_handle.query("*OPC?")
        self.ps_handle.write("OUTP ON"+ ",(@" + str(channel) + ")")
        print("OUTP ON"+ ",(@" + str(channel) + ")")
        return 
    
    # Function to disable channel output
    def disable_output(self,channel):
        self.ps_handle.query("OUTP?")
        self.ps_handle.write("OUTP 0"+ ",(@ " + str(channel) + ")")
        return
    
    # Function to return channel state
    def output_state(self):
        self.ps_handle.query("OUTP?")
        return bool(int(self.ps_handle.read()))
    
    # Function to set the voltage setting of one or more channels
    def set_voltage(self, voltage, channel):
        self.ps_handle.query("OUTP?")
        if len(channel) == 1:
            self.ps_handle.write("VOLT " + str(voltage) + ",(@ " + str(channel) + ")")
            print("VOLT " + str(voltage) + ",(@ " + str(channel) + ")")
            #self.ps_handle.write("VOLT 2,(@2)")
            
        elif len(channel) > 1:    
            for i in channel:
                self.ps_handle.write("VOLT " + str(voltage[i]) + ",(@ " + str(channel[i]) + ")")
                print("VOLT " + str(voltage[i]) + ",(@ " + str(channel[i]) + ")")
                
        else:
            return print("You must set at least one channel and voltage!")
        return
    
    # Function to set the current setting of one or more channels
    def set_current(self, current, channel):
        self.ps_handle.query("OUTP?")
        if len(channel) == 1:
            self.ps_handle.write("CURR " + str(current) + ",(@ " + str(channel) + ")")
            
        elif len(channel) > 1:    
            for i in channel:
                self.ps_handle.write("CURR " + str(current[i]) + ",(@ " + str(channel[i]) + ")")
                print("CURR " + str(current[i]) + ",(@ " + str(channel[i]) + ")")
            
        else:
            return print("You must set at least one channel and current!")
        return
    
    # Function to return the voltage setting of one or more channels
    def get_voltage(self, channels=1):
        if len(channels) == 1:
            voltage = self.ps_handle.query(f"VOLT? CH{channels}")
            self.ps_handle.query("OUTP?")
            return float(voltage)
        elif len(channels) > 1:
            voltages = []
            for channel in channels:
                voltage = self.ps_handle.query(f"VOLT? CH{channel}")
                voltages.append(float(voltage))
            self.ps_handle.query("OUTP?")
            return voltages
    
    # Function to return the current setting of one or more channels
    def get_current(self, channels=1):
        if len(channels) == 1:
            current = self.ps_handle.query(f"CURR? CH{channels}")
            self.ps_handle.query("OUTP?")
            return float(current)
        elif len(channels) > 1:
            currents = []
            for channel in channels:
                current = self.ps_handle.query(f"CURR? CH{channel}")
                currents.append(float(current))
            self.ps_handle.query("OUTP?")
            return currents    

