module latch (
	input logic clock,
	input logic [7:0] d,
	output logic [7:0] q
);

	always_latch 
	begin 
		if (clock) q <= d;
	end
	
endmodule