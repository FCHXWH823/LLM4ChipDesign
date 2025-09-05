`timescale 1ns / 1ps

module tb_dice_roller();
    reg clk;
    reg rst_n;
    reg [1:0] die_select;
    reg roll;
    wire [7:0] rolled_number;

    dice_roller dut (
        .clk(clk),
        .rst_n(rst_n),
        .die_select(die_select),
        .roll(roll),
        .rolled_number(rolled_number)
    );

    // Clock generation
    always begin
        #5 clk = ~clk;
    end

    integer i;
    integer j;
    integer error_count;
    reg [31:0] roll_counts [0:20]; // Declare roll_counts as a memory

    // Testbench stimulus
    initial begin

        clk = 0;
        rst_n = 0;
        die_select = 0;
        roll = 0;

        // Reset and initialization
        #10 rst_n = 1;
        #10 roll = 1;

        error_count = 0;

        // Test loop
        for (i = 0; i < 4; i++) begin
            die_select = i;

            // Clear roll_counts
            for (j = 1; j <= 20; j++) begin
                roll_counts[j] = 0;
            end

            // Perform 1000 rolls and count the results
            for (j = 0; j < 1000; j++) begin
                #10;
                roll = 0;
                #10;
                roll = 1;
                #10;
                roll = 0;
                #10;

                // Check the rolled_number is within the expected range
                case (die_select)
                    2'b00: begin
                        if (rolled_number < 1 || rolled_number > 4) begin
                            $display("Error: Invalid roll result for 4-sided die: %d", rolled_number);
                            error_count = error_count + 1;
                        end
                    end
                    2'b01: begin
                        if (rolled_number < 1 || rolled_number > 6) begin
                            $display("Error: Invalid roll result for 6-sided die: %d", rolled_number);
                            error_count = error_count + 1;
                        end
                    end
                    2'b10: begin
                        if (rolled_number < 1 || rolled_number > 8) begin
                            $display("Error: Invalid roll result for 8-sided die: %d", rolled_number);
                            error_count = error_count + 1;
                        end
                    end
                    2'b11: begin
                        if (rolled_number < 1 || rolled_number > 20) begin
                            $display("Error: Invalid roll result for 20-sided die: %d", rolled_number);
                            error_count = error_count + 1;
                        end
                    end
                endcase

                roll_counts[rolled_number] = roll_counts[rolled_number] + 1;
            end

            $display("Results for die_select %b:", die_select);
            for (j = 1; j <= 20; j++) begin
                if (roll_counts[j] > 0) begin
                    $display("  Rolled %d: %d times", j, roll_counts[j]);
                end
            end
        end

        if (error_count == 0) begin
            $display("Testbench completed successfully.");
        end else begin
            $display("Testbench completed with %d errors.", error_count);
        end

        $finish;
    end

reg vcd_clk;
initial begin
    $dumpfile("my_design.vcd");
    $dumpvars(0, tb_dice_roller);
end

always #5 vcd_clk = ~vcd_clk; // Toggle clock every 5 time units
endmodule

