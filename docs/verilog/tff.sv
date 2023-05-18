// module tff (
// 	input logic clock, reset, t,
// 	output logic out
// );

// always_ff @( posedge clock ) begin 
// 	if (reset) out <= 1'b0;
// 	else if (t) out <= ~out;
	
// end
	
// endmodule

module tff (
	input logic t, elm, reset, clock, 
	output logic out
);
	always_ff @(posedge clock) begin
		if (reset) out <= 1'b0;
		else if (t) out <= ~out;
	end
	
endmodule