module tristate (
	input logic[3:0] value,
	input logic enable,
	output tri [3:0] out
);
	assign out = enable ? value : 4'bz;
endmodule