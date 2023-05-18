module tb4 ();
	logic [3:0] a;
	logic y;

	ex3 exercise(a, y);

	initial begin
		$dumpfile("ex4.vcd");
		$dumpvars(0, tb4);

		#00 a = 4'b0000;
		#10 a = 4'b0001;
		#20 a = 4'b0010;
		#30 a = 4'b0011;
		#40 a = 4'b0100;
		#50 a = 4'b0101;
		#60 a = 4'b0110;
		#70 a = 4'b0111;
		#80 a = 4'b1000;
		#90 a = 4'b1001;
		#100 a = 4'b1010;
		#110 a = 4'b1011;
		#120 a = 4'b1100;
		#130 a = 4'b1101;
		#140 a = 4'b1110;
		#150 a = 4'b1111;
	end


	
endmodule