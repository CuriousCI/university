module fulladder (
	input logic a, b, cin,
	output logic y, cout
);

	logic p, g;

	assign g = a & b; 
	assign p = a ^ b;

	assign cout = g | p & cin;

	assign y = p ^ cin;
	
endmodule