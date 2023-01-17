// module magic (
// 	input logic a, b, c,
// 	output logic y
// );
// 	logic o = a & b;

// 	always_comb 
// 		case ({b, a, c})
// 			0: y = o;
// 			1: y = c; 
// 			2: y = o;
// 			3: y = 1; 
// 			4: y = o;
// 			5: y = 0; 
// 			6: y = o;
// 			7: y = a ^ b ;
// 			default: y = 0; 
// 		endcase
	
// endmodule

module x(input logic a,b,c, output logic y);
	logic ab = a^b;
	
	always_comb 
		case ({b,a,c})
			0: y= ab;
			1: y= ab;
			2: y= c;
			3: y= 1;
			4: y= b|a;
			5: y= 0;
			6: y= ab;
			7: y= ab;
			default : y = 0;
		endcase
endmodule