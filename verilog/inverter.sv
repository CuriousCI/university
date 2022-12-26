module inverter (
	input logic [7:0] a,
	output logic [7:0] s
);

	assign s = ~a;
	
endmodule