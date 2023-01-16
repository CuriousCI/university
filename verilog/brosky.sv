module counter (
	input logic clk, reset,
	output logic [3:0] y 
);
	always_ff @(posedge clk, posedge reset ) begin
		if (reset) y <= 4'd0;
		else if (y < 4'd12) y <= y + 1;
		else y = 'b0;
		// if (reset) y = 4'b0000;
		// else if (y == 4'b1100) y = 4'b0000;
		// else y = y + 1;
	end
endmodule