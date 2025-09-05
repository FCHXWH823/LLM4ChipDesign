`timescale 1ns / 1ps

module tb_lfsr();
    reg clk;
    reg reset_n;
    wire [7:0] data;

    // Instantiate the LFSR design
    lfsr lfsr_inst (
        .clk(clk),
        .reset_n(reset_n),
        .data(data)
    );

    // Clock generation
    always begin
        #5 clk = ~clk;
    end

    // Variables for stimulus and checking
    integer i;
    reg [7:0] data_expected;

    // Function to generate the reference LFSR output
    function [7:0] reference_lfsr_output;
        input [7:0] current_state;
        begin
            reference_lfsr_output = {current_state[6:0], current_state[0] ^ current_state[3] ^ current_state[5] ^ current_state[6]};
        end
    endfunction

    // Stimulus and checking
    initial begin
        // Initialize the clock and reset signals
        clk = 0;
        reset_n = 0;

        // Apply reset and wait for a clock cycle
        #5 reset_n = 1;

        // Initial state check
        if (data !== 8'b10001010) begin
            $display("Error: At time %t, data = %b, expected = 10001010", $time, data);
            $finish;
        end

        // Set the initial expected state
        data_expected = 8'b10001010;

        // Run simulation for 256 cycles and check the output
        for (i = 0; i < 256; i = i + 1) begin
            // Update the expected state
            data_expected = reference_lfsr_output(data_expected);

            // Apply the clock
            #10;

            // Check the output
            if (data !== data_expected) begin
                $display("Error: At time %t, data = %b, expected = %b", $time, data, data_expected);
                $finish;
            end
        end

        // Simulation successful
        $display("Simulation successful. All test cases passed.");
        $finish;
    end

endmodule

