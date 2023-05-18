module muxes (
	input logic a, b, c, d,
	output logic f
);
	assign f = (a&c +!a&d)&d^(b&!c+!b&a);
endmodule