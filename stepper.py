import serial
import struct

ser = serial.Serial('/dev/tty.usbmodem1411', 9600)

def send_command(x, y):
	print ser.read(ser.in_waiting)
	a = bytearray()
	a.append(0)
	a.extend(struct.pack("h", x))
	a.extend(struct.pack("h", y))
	ser.write(a)
	print ser.read(ser.in_waiting)
