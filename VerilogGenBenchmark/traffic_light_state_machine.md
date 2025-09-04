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