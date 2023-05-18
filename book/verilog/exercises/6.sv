module display (
	input logic [3:0] number,
	output logic [6:0] display
);

	always_comb 
		case (number)
			4'h0:  display = 7'b1111111;
			4'h1:  display = 7'b1111000;
			4'h2:  display = 7'b1101101;
			4'h3:  display = 7'b1111001;
			4'h4:  display = 7'b0110011;
			4'h5:  display = 7'b1011011;
			4'h6:  display = 7'b1011111;
			4'h7:  display = 7'b1110000;
			4'h8:  display = 7'b1111111;
			4'h9:  display = 7'b1110011;
			4'ha:  display = 7'b1110111;
			4'hb:  display = 7'b0011111;
			4'hc:  display = 7'b1001110;
			4'hd:  display = 7'b0111101;
			4'he:  display = 7'b1001111;
			4'hf:  display = 7'b1000111;
			default: display = 7'b000_0000; 
		endcase
	
endmodule