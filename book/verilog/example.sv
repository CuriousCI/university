module mux (
	input logic a, b, c,
	output logic y
);
	always_comb
		case ({c, a, b})
			1: y = c; 
			3: y = 1; 
			5: y = 0; 
			7: y = a ^ b; 
			default: y = a & b;
		endcase
endmodule