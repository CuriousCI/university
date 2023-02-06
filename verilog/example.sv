module mux (
	input logic a, b, c,
	output logic y
);
	always_comb
		case ({c, a, b})
			3'd1: y = c; 
			3'd3: y = 1; 
			3'd5: y = 0; 
			3'd7: y = a ^ b; 
			default: y = a & b;
		endcase
endmodule