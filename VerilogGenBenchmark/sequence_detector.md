I am trying to create a Verilog model for a sequence detector. It must meet the following specifications:
	- Inputs:
		- Clock
		- Active-low reset
		- Data (3 bits)
	- Outputs:
		- Sequence found

While enabled, it should detect the following sequence of binary input values:
	- 0b001
	- 0b101
	- 0b110
	- 0b000
	- 0b110
	- 0b110
	- 0b011
	- 0b101

How would I write a design that meets these specifications?