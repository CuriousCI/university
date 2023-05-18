module dec2 (
	input logic [1:0] in,
	output logic [3:0] out
);
	always_comb  
		case (in)
			2'b00: out = 4'b0001;
			2'b01: out = 4'b0010;
			2'b10: out = 4'b0100;
			2'b11: out = 4'b1000;
			default: out = 4'b0000;
		endcase
endmodule


module ex14 (
	input logic [5:0] in,
	output logic [63:0] out
);

	dec2 a(in[1:0], out[3:0]);
	dec2 b(in[3:2], out[7:4]);
	dec2 c(in[5:4], out[11:8]);
	
endmodule