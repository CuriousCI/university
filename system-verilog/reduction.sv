module reduction (
	input logic [7:0] a,
	output logic y1, y2, y3, y4
);

	assign y1 = &a;
	assign y2 = |a;
	assign y3 = ^a;
	assign y4 = &(~a);
	
endmodule