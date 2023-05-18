module ex2 (
	input logic [3:0] a,
	output logic [1:0] y
);

	always_comb  
		if (a[0]) y = 2'b11;
		else if (a[1]) y = 2'b10;
		else if (a[2]) y = 2'b01;
		else if (a[3]) y = 2'b00;
		else y = a[1:0];
		
	
endmodule