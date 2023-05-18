module minority (
	input logic a, b, c,
	output logic y
);
	logic [3:0] tmp;
 	assign tmp = {a, b, c};
	always_comb 
	casez (tmp)
		3'b?00: y=1;
		3'b0?0: y=1;
		3'b00?: y=1;
		default: y=0;
	endcase
	
endmodule