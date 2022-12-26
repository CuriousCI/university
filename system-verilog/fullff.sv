module fullff (
	input logic clock, reset, enable,
	input logic [3:0] d,
	output logic [3:0] q
);

	always_ff @(posedge clock, posedge reset) 
		if (reset) q <= 4'b0;
		else if (enable) q <= d;
	
endmodule