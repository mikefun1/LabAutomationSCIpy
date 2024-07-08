# lab 1 ECET380-002 Automation
import pyvisa as visa

rm=visa.ResourceManager()
rm.list_resources()


# 7 

wfg.write("FUNC:SQU")
wfg.write("FUNC:FREQ:20000")
wfg.write("SOUR:FUNC:SQU:DCYC 25")
wfg.write("SOUR:VOLT:LOW 0")
wfg.write("SOUR:VOLT:HIGH 2")