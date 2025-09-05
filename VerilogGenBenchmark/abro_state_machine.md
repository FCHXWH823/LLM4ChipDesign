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
