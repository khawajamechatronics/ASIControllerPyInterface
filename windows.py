#!/usr/bin/env python
import minimalmodbus
import time
import os

#_____________________________________#
#____SETUP THE SERIAL COMUNICATION____#
#_____________________________________#


instrument = minimalmodbus.Instrument('COM8', 1) # port name, slave address (in decimal)
instrument.serial.baudrate = 115200
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1
# instrument.debug = True
instrument.mode = minimalmodbus.MODE_RTU


#read_register(self, registeraddress, numberOfDecimals=0, functioncode=3, signed=False):

        # Args:
            # * registeraddress (int): The slave register address (use decimal numbers, not hex).
            # * numberOfDecimals (int): The number of decimals for content conversion, numberOfDecimals=1``
			# which will divide the received data by 10 before returning the value.for a full value use 0.
            # * functioncode (int): Modbus function code. Can be 3 or 4.
            # * signed (bool): Use the parameter ``signed=True`` if reading from a register that can hold
			# negative values. Then upper range data will be automatically converted into
			# negative return values (two's complement).

#_________________________________#
#____READ INFORMATION FROM ACI____#
#_________________________________#

reading=True

while (reading):

	try:

		maximumMeasurableCurrent	 = instrument.read_register(functioncode = 3, registeraddress = 384 , numberOfDecimals= 0 , signed= False)
		maximumMeasurableCurrentScale = 1
		print('{:<30} {:<10} {}'.format("Maximum Measurable Current  :", maximumMeasurableCurrent/maximumMeasurableCurrentScale,"    A"))

		batteryVoltage	= instrument.read_register(functioncode = 3, registeraddress = 265 , numberOfDecimals= 0 , signed= False)
		batteryVoltageScale = 32
		print('{:<30} {} {}'.format("Battery Voltage  :", batteryVoltage/batteryVoltageScale,"    Volts"))

		batteryCurrent	= instrument.read_register(functioncode = 3, registeraddress = 266 , numberOfDecimals= 0 , signed= False)
		batteryCurrentScale = 32
		print("Battery Current  :" , batteryCurrent/batteryCurrentScale, "    Amps")

		vehicleSpeed = instrument.read_register(functioncode = 3, registeraddress = 260 , numberOfDecimals= 0 , signed= False)
		vehicleSpeedScale = 256
		print("Vehicle Speed  :" , vehicleSpeed/vehicleSpeedScale,"    km/hr")



		#__________________________#
		#_____DIGITAL OUTPUTS______#
		#__________________________#


		digitalOutputs = instrument.read_register(functioncode = 3, registeraddress = 295 , numberOfDecimals= 0 , signed= False)
		digitalOutputsbin= bin(digitalOutputs)
		Headlightbin = digitalOutputsbin[0]
		Headlight = int(Headlightbin,2)
		digitalOutputsbin= digitalOutputsbin[::-1]

		if (Headlight == 0):
			print("Headlight  : not active ")
		elif (Headlight == 1):
			print("Headlight  :  active ")


		#______________________#
		#_____EBIKE FLAGS______#
		#______________________#

		ebikeFlags	 = instrument.read_register(functioncode = 3, registeraddress = 327 , numberOfDecimals= 0 , signed= False)
		ebikeFlagsbin = bin(ebikeFlags)
		ebikeFlagsbin=ebikeFlagsbin[::-1]
		brakebin =  ebikeFlagsbin[0]
		brake = int (brakebin,2)
		if (brake == 0):
			print("Brake  : not active ")
		elif (brake == 1):
			print("Brake  :  active ")

		cutoutbin = ebikeFlagsbin[1]
		cutout = int(cutoutbin,2)
		if (cutout == 0):
			print("cutout  : not active ")
		elif (cutout == 1):
			print("cutout  :  active ")

		runReqbin= ebikeFlagsbin[2]
		runReq = int(runReqbin,2)
		if (runReq == 0):
			print("runReq  : not active ")
		elif (runReq == 1):
			print("runReq  :  active ")

		pedalbin= ebikeFlagsbin[3]
		pedal= int(pedalbin,2)
		if (pedal == 0):
			print("Pedal  : not active ")
		elif (pedal == 1):
			print("Pedal  :  active ")

		regenbin= ebikeFlagsbin[4]
		regen= int(regenbin,2)
		if (regen == 0):
			print("Regen  : not active ")
		elif (regen == 1):
			print("Regen  :  active ")


		batteryPower = instrument.read_register(functioncode = 3, registeraddress = 268 , numberOfDecimals= 0 , signed= False)
		batteryPowerScale = 1
		print("Battery Power  :" , batteryPower/batteryPowerScale,"    Watts")



		BatteryStateOfCharge	= instrument.read_register(functioncode = 3, registeraddress = 267 , numberOfDecimals= 0 , signed= False)
		BatteryStateOfChargeScale = 1
		print("Battery State Of Charge  :" , BatteryStateOfCharge/BatteryStateOfChargeScale,"    %")
		time.sleep(1)
		os.system('cls' if os.name == 'nt' else 'clear')

	except:
		print("Oops!  there is a problem with the comunication.  Try again...")
		reading=False
