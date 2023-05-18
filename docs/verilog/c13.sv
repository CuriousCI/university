module cont13 (input logic clock, reset, output logic [3:0] y);
	always_ff @(posedge clock)
		if (reset) y = 0;
		else if (y==0)  y= 1;
		else if (y==1)  y= 2;
		else if (y==2)  y= 3;
		else if (y==3)  y= 4;
		else if (y==4)  y= 5;
		else if (y==5)  y= 6;
		else if (y==6)  y= 7;
		else if (y==7)  y= 8;
		else if (y==8)  y= 9;
		else if (y==9)  y= 10;
		else if (y==10)  y= 11;
		else if (y==11)  y = 12;
		else y = 0;
endmodule