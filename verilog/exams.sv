module exercise (
	input logic a, clk,
	output logic [1:0] y
);

	logic n1, n2;

	always_ff @(posedge clk)
		begin
			n1 <= a;
			n2 <= ~n1;
		end
	
	assign y = {n2, n1};
	
endmodule