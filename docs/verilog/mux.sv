module mux2 (
	input logic [3:0] d0, d1,
	input logic s,
	output logic [3:0] y
);
	assign y = s ? d1 : d0;
endmodule

module mux4 (
	input logic [3:0] d0, d1, d10, d11,
	input logic [2:0] s,
	output logic [3:0] y
);
	assign y = s[1] ? (s[0] ? d11 : d10) : (s[0] ? d1 : d0);
endmodule

// module mux  (
// 	input logic select,
// 	output logic [1:0] out
// );

// always_comb 
// 	case (select)
// 		1'b0: out = 2'b10;
// 		1'b1: out = 2'b11;
// 		// default: out = 1'b1;
// 	endcase
	
	
// endmodule