module ex12 (
	input logic [7:0] in,
	output logic [7:0] out
);

	always_comb
		begin
			// out[0] = in[0] & ~(|in[7:1]);
			// out[1] = in[1] & ~(|in[7:2]);
			// out[2] = in[2] & ~(|in[7:3]);
			// out[3] = in[3] & ~(|in[7:4]);
			// out[4] = in[4] & ~(|in[7:5]);
			// out[5] = in[5] & ~(|in[7:6]);
			// out[6] = in[6] & ~(|in[7]);
			// out[7] = in[7];

			out[0] = in[0] & &(~in[7:1]);
			out[1] = in[1] & &(~in[7:2]);
			out[2] = in[2] & &(~in[7:3]);
			out[3] = in[3] & &(~in[7:4]);
			out[4] = in[4] & &(~in[7:5]);
			out[5] = in[5] & &(~in[7:6]);
			out[6] = in[6] & &(~in[7]);
			out[7] = in[7];
		end
	
endmodule