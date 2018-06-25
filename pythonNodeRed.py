#!/usr/bin/env python
import minimalmodbus
import serial
#_____________________________________#
#____SETUP THE SERIAL COMUNICATION____#
#_____________________________________#

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1) # port name, slave address (in decimal)
instrument.serial.baudrate = 115200
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1
##instrument.debug = True
instrument.mode = minimalmodbus.MODE_RTU
maximumMeasurableCurrent = instrument.read_register(functioncode = 3, registeraddress = 384 , numberOfDecimals= 0 , signed= False)

batteryVoltage	= instrument.read_register(functioncode = 3, registeraddress = 265 , numberOfDecimals= 0 , signed= False)
batteryVoltageScale = 32
batteryVoltage = batteryVoltage / batteryVoltageScale

batteryCurrent	= instrument.read_register(functioncode = 3, registeraddress = 266 , numberOfDecimals= 0 , signed= False)
batteryCurrentScale = 32
#batteryCurrent = batteryCurrent / batteryCurrentScale

vehicleSpeed = instrument.read_register(functioncode = 3, registeraddress = 260 , numberOfDecimals= 0 , signed= False)
vehicleSpeedScale = 256
vehicleSpeed = vehicleSpeed / vehicleSpeedScale


digitalOutputs = instrument.read_register(functioncode = 3, registeraddress = 295 , numberOfDecimals= 0 , signed= False)
digitalOutputsbin= bin(digitalOutputs)
Headlightbin = digitalOutputsbin[0]
Headlight = int(Headlightbin,2)
digitalOutputsbin= digitalOutputsbin[::-1]

if (Headlight == 0):
    Headlight = 0
elif (Headlight == 1):
    Headlighgt = 1

		#______________________#
		#_____EBIKE FLAGS______#
		#______________________#

ebikeFlags	 = instrument.read_register(functioncode = 3, registeraddress = 327 , numberOfDecimals= 0 , signed= False)
ebikeFlagsbin = bin(ebikeFlags)
ebikeFlagsbin=ebikeFlagsbin[::-1]
brakebin =  ebikeFlagsbin[0]
brake = int (brakebin,2)
if (brake == 0):
	Brake = 0
elif (brake == 1):
	Brake = 1

cutoutbin = ebikeFlagsbin[1]
cutout = int(cutoutbin,2)
if (cutout == 0):
    cutout = bool(0)
elif (cutout == 1):
    cutout = bool(1) 

ratedMotorSpeed = instrument.read_register(functioncode = 3, registeraddress = 72 , numberOfDecimals= 0 , signed= False)

engineBrakingTorque = instrument.read_register(functioncode = 3, registeraddress = 177 , numberOfDecimals= 0 , signed= False)
engineBrakingTorqueScale = 40.96
engineBrakingTorque= engineBrakingTorque / engineBrakingTorqueScale

motorSpeed = instrument.read_register(functioncode = 3, registeraddress = 264 , numberOfDecimals= 0 , signed= False)

LINOdometer = instrument.read_register(functioncode = 3, registeraddress = 404 , numberOfDecimals= 0 , signed= False)

controllerStatus = instrument.read_register(functioncode = 3, registeraddress = 257 , numberOfDecimals= 0 , signed= False)

batteryStateOfCharge = instrument.read_register(functioncode = 3, registeraddress = 267 , numberOfDecimals= 0 , signed= False)


rawBatteryVoltage =  instrument.read_register(functioncode = 3, registeraddress = 291 , numberOfDecimals= 0 , signed= False)
rawBatteryVoltageScale = 4096
rawBatteryVoltage = rawBatteryVoltage / rawBatteryVoltageScale

return (maximumMeasurableCurrent, batteryVoltage, batteryCurrent, vehicleSpeed, Headlight,Brake,cutout, ratedMotorSpeed, motorSpeed, LINOdometer, controllerStatus , batteryStateOfCharge, rawBatteryVoltage )
