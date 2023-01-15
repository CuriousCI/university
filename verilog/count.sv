module count (
	input logic clock, reset,
	output logic [3:0] out
);
	always_ff @(posedge clock, posedge reset ) 
		if (reset) out <= 0;
		else if (clock) begin
			if (out == 12)out <= 0;
			else out <= out + 1;
		end 
		
	
endmodule