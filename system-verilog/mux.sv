module mux  (
	input logic select,
	output logic [1:0] out
);

always_comb 
	case (select)
		1'b0: out = 2'b10;
		1'b1: out = 2'b11;
		// default: out = 1'b1;
	endcase
	
	
endmodule