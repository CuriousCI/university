module numbers (
	output logic [7:0] epsilon
);
	logic [7:0] teta;

	assign teta = 8'd10;
	// assign teta = 8'b0000_0101;
	// assign teta = 'd10;
	// assign teta = 'h10;
	// assign teta = 'o73;
	assign epsilon = teta;
	
endmodule