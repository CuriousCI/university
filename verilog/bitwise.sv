module bitwise (
	input logic [3:0] a, b,
	output logic [3:0] y1, y2, y3, y4, y5, y6
);
	// Let's do some bitwise operations
	assign y1 = a | b;
	assign y2 = a & b;
	assign y3 = a ^ b;

	/* What if we 
	* negate them?
	*/
	assign y4 = ~(a | b);
	assign y5 = ~(a & b);
	assign y6 = ~(a ^ b);
	
endmodule