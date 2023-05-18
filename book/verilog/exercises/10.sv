module mux4 (
	input logic [1:0] s,
	input logic d0, d1, d2, d3,
	output logic y
);
	always_comb 
	case (s)
		'd0: y = d0;
		'd1: y = d1;
		'd2: y = d2;
		'd3: y = d3;
		default: y = 'b0; 
	endcase
		
	
endmodule

module ex9 (
	input logic a, b, c,
	output logic y
);

	logic e, f;
	
	mux4 alpha({b, c}, 1'b1, 1'b1, 1'b0, 1'b0, e);
	mux4 beta({b, c}, 1'b1, 1'b0, 1'b0, 1'b1, f);

	assign y = a ? f : e;
endmodule