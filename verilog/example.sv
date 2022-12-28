// module mux(input  logic a, 
//                 input logic  b,
//                 input logic  c,
                
//                 output tri   y);
//   assign y = (!b&!a&!c | !b&a&!c | b&!a&!c | b&b&!c) ? a&b : !b&!a&c ? c : !b&a&c ? 1 : b&!a&c ? 0 :b^c;
// endmodule

module mux (
	input logic a, b, c,
	output logic y
);

	logic [3:0] select = {c, a, b};
	logic f = a & b;

	always_comb
		case (select)
			3'd0: y = f;
			3'd1: y = c; 
			3'd2: y = f;
			3'd3: y = 1; 
			3'd4: y = f; 
			3'd5: y = 0; 
			3'd6: y = f; 
			3'd7: y = a ^ b; 
			default: y = 0;
		endcase
		
	
endmodule