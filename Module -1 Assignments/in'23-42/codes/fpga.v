module helloworldfpga(
output a,
output b,
output c,
output d,
output e,
output f,
output g);

//decalring variables
reg[3:0] reg_a = 4'b1101;
 reg [3:0] reg_a_shifted  ;
    reg new_msb_a ;	
    
reg[3:0] reg_b = 4'b1010;
 reg [3:0] reg_b_shifted ;
  reg new_msb_b ;

integer i;
integer j=0;
reg[26:0] delay;
wire clk;


   qlal4s3b_cell_macro u_qlal4s3b_cell_macro (
        .Sys_Clk0 (clk),
    );
   
//always #1 clk = ~clk;


always@(posedge clk) begin
    for (i = 0; i < 4; i = i + 1) begin
        new_msb_a = (reg_a[0])^(~reg_a[2]);
        new_msb_b = (reg_a[0]);
        reg_a_shifted = {new_msb_a, reg_a[3:1]};
        reg_a = reg_a_shifted;
        reg_b_shifted = {new_msb_b, reg_b[3:1]};
        reg_b = reg_b_shifted;
    end
 
    	if((reg_a == 4'b0101) & (reg_b == 4'b1101)) begin
        a=0;b=0;c=0;d=0;e=1;f=1;g=0;
        end
      else if((reg_a == 4'b1101) & (reg_b == 4'b1101)) begin
        a=1;b=0;c=0;d=1;e=1;f=1;g=1;
        end
       else if((reg_a == 4'b1110) & (reg_b == 4'b1001)) begin
	{a,b,c,d,e,f,g}= {0,0,0,0,1,1,0};
	a=0;b=0;c=0;d=0;e=1;f=1;g=0;
        end
        else if((reg_a == 4'b1010) & (reg_b == 4'b1111)) begin
	{a,b,c,d,e,f,g}= {0,1,0,1,1,0,0};
	a=0;b=1;c=0;d=1;e=1;f=0;g=0;
        end
        else begin
        a=0;b=0;c=0;d=1;e=1;f=1;g=1;
 	end	
   reg_a = 4'b1101;
   reg_b = 4'b1010;
 end
    /*if((reg_a == 4'b0101) & (reg_b == 4'b1101)) begin
    a=0;b=0;c=0;d=0;e=1;f=1;g=0;
    end
    else begin
    a=0;b=0;c=0;d=1;e=1;f=1;g=1;
    end*/
/*always@(posedge clk) 
	begin
		delay = delay+1; //incrementing the counter.

		//counts from 0 to 20000000 in 1 second
		if(delay > 20000000) //check delay count
			begin
				if((reg_a == 4'b1101) & (reg_b == 4'b1101)) begin
				 {a,b,c,d,e,f,g}= {1,0,0,1,1,1,1};
				end
				else if((reg_a == 4'b1110) & (reg_b == 4'b1001)) begin
 				{a,b,c,d,e,f,g}= {0,0,1,0,0,1,0};
				end
				else if((reg_a == 4'b0101) & (reg_b == 4'b1101)) begin
				{a,b,c,d,e,f,g}= {0,0,0,0,1,1,0};
				end
				else if((reg_a == 4'b1010) & (reg_b == 4'b1111)) begin
				{a,b,c,d,e,f,g}= {0,1,0,1,1,0,0};
				end
				else begin
 				{a,b,c,d,e,f,g}= {0,0,0,0,0,0,0};
				end
              			end //end delay count
		end 
*/
//end counter loop

/*always @(*) begin
if((reg_a == 4'b0101) & (reg_b == 4'b1101)) begin
a=0;b=0;c=0;d=0;e=1;f=1;g=0;
end
/*else if((reg_a == 4'b1101) & (reg_b == 4'b1101)) begin
 a=1;b=0;c=0;d=1;e=1;f=1;g=1;
end
else if((reg_a == 4'b1110) & (reg_b == 4'b1001)) begin
 a=0;b=0;c=1;d=0;e=0;f=1;g=0;
end
else if((reg_a == 4'b1010) & (reg_b == 4'b1111)) begin
{a,b,c,d,e,f,g}= {0,1,0,1,1,0,0};
 a=0;b=1;c=0;d=1;e=1;f=0;g=0;
end
else begin
 {a,b,c,d,e,f,g}= {0,0,1,1,1,1,1};
  a=0;b=0;c=1;d=1;e=1;f=1;g=1;
end
end*/




/*always@(posedge clk) 
begin
	delay = delay+1; //incrementing the counter.

		//counts from 0 to 20000000 in 1 second
	if(delay > 20000000) //check delay count
			begin
for (j = 0; j < 4; j = j + 1) begin
if((reg_a[j]==1'b0)) begin
{a,b,c,d,e,f,g}= {1,0,0,1,1,1,1};
end
else begin
{a,b,c,d,e,f,g}= {1,0,0,0,0,0,1};
end
end
end
end
*/

 endmodule
