`timescale 1ns / 1ps

module tb_binary_to_bcd_converter;

reg [4:0] binary_input;
wire [7:0] bcd_output;

binary_to_bcd_converter uut (
    .binary_input(binary_input),
    .bcd_output(bcd_output)
);

integer i;
reg [4:0] test_binary;
reg [7:0] expected_bcd;

initial begin
    $display("Testing Binary-to-BCD Converter...");

    for (i = 0; i < 32; i++) begin
        test_binary = i;
        binary_input = test_binary;

        // Calculate expected BCD output
        expected_bcd[3:0] = test_binary % 10;
        expected_bcd[7:4] = test_binary / 10;

        #10; // Wait for the results

        if (bcd_output !== expected_bcd) begin
            $display("Error: Test case %0d failed. Expected BCD: 8'b%0b, Got: 8'b%0b",
                     test_binary, expected_bcd, bcd_output);
            $finish;
        end
    end

    $display("All test cases passed!");
    $finish;
end

reg vcd_clk;
initial begin
    $dumpfile("my_design.vcd");
    $dumpvars(0, tb_binary_to_bcd_converter);
end

always #5 vcd_clk = ~vcd_clk; // Toggle clock every 5 time units

endmodule

