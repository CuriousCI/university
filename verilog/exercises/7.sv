module tb7 ();
	logic [3:0] number;
	logic [6:0] display;


	display exercise(number, display);

	initial begin
		$dumpfile("7.vcd");
		$dumpvars(0, tb7);

		#0 number = 4'h0;
		#1 number = 4'h1;
		#2 number = 4'h2;
		#3 number = 4'h3;
		#4 number = 4'h4;
		#5 number = 4'h5;
		#6 number = 4'h6;
		#7 number = 4'h7;
		#8 number = 4'h8;
		#9 number = 4'h9;
		#10 number = 4'ha;
		#11 number = 4'hb;
		#12 number = 4'hc;
		#13 number = 4'hd;
		#14 number = 4'he;
		#15 number = 4'hf;
	end
	
endmodule