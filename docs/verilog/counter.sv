module counter(
	output logic [WIDTH-1 : 0] out,
        input logic clk, reset);

parameter WIDTH = 8;

always @(posedge clk, posedge reset)

	if (reset)
		out <= 0;
	else
		out <= out + 1;

endmodule // counter
