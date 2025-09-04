I am trying to create a Verilog model for a sequence generator. It must meet the following specifications:
	- Inputs:
		- Clock
		- Active-low reset
		- Enable
	- Outputs:
		- Data (8 bits)

While enabled, it should generate an output sequence of the following hexadecimal values and then repeat:
	- 0xAF
	- 0xBC
	- 0xE2
	- 0x78
	- 0xFF
	- 0xE2
	- 0x0B
	- 0x8D

How would I write a design that meets these specifications?