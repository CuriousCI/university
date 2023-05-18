module flipflop (
	input logic clock,
	input logic reset,
	input logic [3:0] d,
	output logic [3:0] q
);

	// Async reset
	always_ff @( posedge clock, posedge reset )  
		if (reset)
			q <= 4'b00;
		else
			q <= d;
	
endmodule