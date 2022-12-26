module ex1 (
	input logic a, b, c,
	output logic y, z
);
	assign y = a & b & c | a & b & ~c | a & ~b & c;
	assign z = a & b | ~a & ~b;
endmodule