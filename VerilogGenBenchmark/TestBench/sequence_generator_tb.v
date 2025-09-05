`timescale 1ns/1ps

module tb_sequence_generator();
    reg clk;
    reg reset_n;
    reg enable;
    wire [7:0] data;

    // Instantiate the sequence_generator
    sequence_generator seq_gen (
        .clk(clk),
        .reset_n(reset_n),
        .enable(enable),
        .data(data)
    );

    // Clock generation
    always begin
        #5 clk = ~clk;
    end

    // Test sequence
    localparam TEST_SEQ_LEN = 8;
    reg [7:0] test_sequence [0:TEST_SEQ_LEN-1];

    // Initialize test sequence array
    initial begin
        test_sequence[0] = 8'hAF;
        test_sequence[1] = 8'hBC;
        test_sequence[2] = 8'hE2;
        test_sequence[3] = 8'h78;
        test_sequence[4] = 8'hFF;
        test_sequence[5] = 8'hE2;
        test_sequence[6] = 8'h0B;
        test_sequence[7] = 8'h8D;
    end

    integer i;

    // Testbench
    initial begin
        // Initialize signals
        clk = 0;
        reset_n = 0;
        enable = 0;

        // Apply reset
        #10 reset_n = 1;
        #10 reset_n = 0;
        #10 reset_n = 1;

        // Test case: sequence generation
        enable = 1;
        for (i = 0; i < TEST_SEQ_LEN; i = i + 1) begin
            @(posedge clk);
            if (data !== test_sequence[i]) begin
                $display("Error: Mismatch at position %0d. Expected: %h, Got: %h", i, test_sequence[i], data);
                $finish;
            end
        end
        $display("Test case passed: sequence generation");

        // Test case: sequence repetition
        for (i = 0; i < TEST_SEQ_LEN; i = i + 1) begin
            @(posedge clk);
            if (data !== test_sequence[i]) begin
                $display("Error: Mismatch in sequence repetition at position %0d. Expected: %h, Got: %h", i, test_sequence[i], data);
                $finish;
            end
        end
        $display("Test case passed: sequence repetition");

        // Test case: disable the sequence generator
        enable = 0;
        @(posedge clk);
        if (data !== test_sequence[TEST_SEQ_LEN-1]) begin
            $display("Error: Sequence generator not disabled. Expected: %h, Got: %h", test_sequence[TEST_SEQ_LEN-1], data);
            $finish;
        end
        $display("Test case passed: disable sequence generator");

        $display("All test cases passed");
        $finish;
    end

endmodule

