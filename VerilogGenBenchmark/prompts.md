## Design Prompts:

#### Shift Register:
```
I am trying to create a Verilog model for a shift register. It must meet the following specifications:
	- Inputs:
		- Clock
		- Active-low reset
		- Data (1 bit)
		- Shift enable
	- Outputs:
		- Data (8 bits)

How would I write a design that meets these specifications?
```
#### Sequence Generator
```
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
```

#### Sequence Detector
```
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
```

#### ABRO
```
I am trying to create a Verilog model for an ABRO state machine. It must meet the following specifications:
    - Inputs:
        - Clock
        - Active-low reset
        - A
        - B
    - Outputs:
        - O
        - State

Other than the main output from ABRO machine, it should output the current state of the machine for use in verification.

The states for this state machine should be one-hot encoded.

How would I write a design that meets these specifications?
```

#### Binary to BCD Converter
```
I am trying to create a Verilog model for a binary to binary-coded-decimal converter. It must meet the following specifications:
	- Inputs:
		- Binary input (5-bits)
	- Outputs:
		- BCD (8-bits: 4-bits for the 10's place and 4-bits for the 1's place)

How would I write a design that meets these specifications?
```

#### LFSR
```
I am trying to create a Verilog model for an LFSR. It must meet the following specifications:
	- Inputs:
		- Clock
        - Active-low reset
	- Outputs:
		- Data (8-bits)

The initial state should be 10001010, and the taps should be at locations 1, 4, 6, and 7.

How would I write a design that meets these specifications?
```

#### Traffic Light State Machine
```
I am trying to create a Verilog model for a traffic light state machine. It must meet the following specifications:
    - Inputs:
        - Clock
        - Active-low reset
        - Enable
    - Outputs:
        - Red
        - Yellow
        - Green

The state machine should reset to a red light, change from red to green after 32 clock cycles, change from green to yellow after 20 clock cycles, and then change from yellow to red after 7 clock cycles.

How would I write a design that meets these specifications?
```

#### Dice Roller
```
I am trying to create a Verilog model for a simulated dice roller. It must meet the following specifications:
    - Inputs:
        - Clock
        - Active-low reset
        - Die select (2-bits)
        - Roll
    - Outputs:
        - Rolled number (up to 8-bits)

The design should simulate rolling either a 4-sided, 6-sided, 8-sided, or 20-sided die, based on the input die select. It should roll when the roll input goes high and output the random number based on the number of sides of the selected die.

How would I write a design that meets these specifications?
```

## Testbench Prompt
```
Can you create a Verilog testbench for this design? It should be self-checking and made to work with iverilog for simulation and validation. If test cases should fail, the testbench should provide enough information that the error can be found and resolved.
```
