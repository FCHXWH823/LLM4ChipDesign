`timescale 1ns/1ps

module tb_abro_state_machine();
    reg clk;
    reg rst_n;
    reg A;
    reg B;
    wire O;
    wire [3:0] State;

    // Instantiate the ABRO state machine
    abro_state_machine uut (
        .clk(clk),
        .rst_n(rst_n),
        .A(A),
        .B(B),
        .O(O),
        .State(State)
    );

    // Clock generation
    always begin
        #5 clk = ~clk;
    end

    integer i;
    reg [3:0] expected_state;
    reg expected_O;

    // Test stimulus and checking
    initial begin
        // Initialize signals
        clk = 0;
        rst_n = 1;
        A = 0;
        B = 0;

        // Test cases
        for (i = 0; i < 16; i = i + 1) begin
            // Determine the input and expected output based on the test case index
            case (i)
                0: begin
                    A = 0; B = 0; // Reset
                    expected_O = 1'b0;
                    expected_state = 4'b0001;
                end
                1: begin
                    A = 0; B = 1; // A=0, B=1
                    expected_O = 1'b0;
                    expected_state = 4'b0001;
                end
                2: begin
                    A = 1; B = 0; // A=1, B=0
                    expected_O = 1'b0;
                    expected_state = 4'b0010;
                end
                3: begin
                    A = 1; B = 1; // A=1, B=1
                    expected_O = 1'b1;
                    expected_state = 4'b0100;
                end
                default: begin
                    // Repeat the same sequence of inputs for the remaining test cases
                    A = (i-1) % 2;
                    B = ((i-1) / 2) % 2;
                    expected_O = (A && B) ? 1'b1 : 1'b0;
                    expected_state = (A && !B) ? 4'b0010 : ((!A && B) ? 4'b0001 : 4'b0100);
                end
            endcase

            // Apply reset
            if (i == 0) begin
                rst_n = 0;
                @(posedge clk);
                rst_n = 1;
            end

            @(posedge clk); // Wait for the state change on the rising edge of the clock

            // Check the output and state
            if (O !== expected_O || State !== expected_state) begin
                $display("Error: Test case %0d failed (A=%b, B=%b)", i, A, B);
                $display("  Expected: O=%b, State=%b", expected_O, expected_state);
                $display("  Got: O=%b, State=%b", O, State);
                $finish;
            end
        end

        $display("All test cases passed.");
        $finish;
    end


	reg vcd_clk;
initial begin
    $dumpfile("my_design.vcd");
    $dumpvars(0, tb_abro_state_machine);
end

always #5 vcd_clk = ~vcd_clk; // Toggle clock every 5 time units

endmodule

