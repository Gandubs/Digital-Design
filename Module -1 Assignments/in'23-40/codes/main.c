#include <avr/io.h>

int main(void)
{
	DDRD = 0b11111100;
	DDRB = 0b00000001;
	int q[15],op_a[15],op_b[15],op_c[15],op_d[15],count = 0;
	int op_a_count=0,op_b_count=0,op_c_count=0,op_d_count=0;
	int a,b,c,d,e,f,g;
	int portd, portb;
		while(1)
		{
		/*question - !w&x&!y&!z | !w&x&!y&z | w&!x&y&!z | w&!x&y&z | w&x&!y&!z | w&x&!y&z | w&x&y&!z | w&x&y&z */ 
		//option 1 - w&x | !w&x&!y | w&!x&y
		//option 2 - w&x | w&yi | x&!y
		//option 3 - x&!y | w&y
		//option 4 - !x&y | !w&!y 
		for(int w=0;w<=1;++w)
		{
			for(int x=0;x<=1;++x)
			{
				for(int y=0;y<=1;++y)
				{
					for(int z=0;z<=1;++z)
					{
					q[count] = (!w&&x&&!y&&!z) || (!w&&x&&!y&&z) || (w&&!x&&y&&!z) || (w&&!x&&y&&z) || (w&&x&&!y&&!z) || (w&&x&&!y&&z) || (w&&x&&y&&!z) || (w&&x&&y&&z);
					op_a[count] = (w&&x) || (!w&&x&&!y) || (w&&!x&&y);
					op_b[count] = (w&&x) || (w&&y) || (x&&!y);
					op_c[count] = (x&&!y) || (w&&y);
					op_d[count] = (!x&&y) || (!w&&!y);
					count ++;
					}
				}
			}
		}
		for(int m=0; m<16; ++m)
		{
			if(q[m]==op_a[m])
			{
			op_a_count=op_a_count+1;
			}
			if(q[m]==op_b[m])
			{
			op_b_count=op_b_count+1;
			}
			if(q[m]==op_c[m])
			{
			op_c_count=op_c_count+1;
			}
			if(q[m]==op_d[m])
			{
			op_d_count=op_d_count+1;
			}
		}
		if(op_c_count==16)
		{
		a=0;b=0;c=0;d=0;e=1;f=1;g=0;
		}
		if(op_d_count==16)
		{
		a=1;b=1;c=0;d=1;e=1;f=0;g=0;
		}
		 if(op_b_count==16)
		{
		a=0;b=0;c=1;d=0;e=0;f=1;g=0;
		}
		 if(op_a_count==16)
		{
		a=1;b=0;c=0;d=1;e=1;f=1;g=1;
		}
		if(op_a_count==op_c_count)
		{
				a=0;
				b=0;
				c=0;
				d=0;
				e=1;
				f=1;
				g=0;
		}
		portd = (a<<PD2);
		portd |= (b<<PD3);
		portd |= (c<<PD4);
		portd |= (d<<PD5);
		portd |= (e<<PD6);
		portd |= (f<<PD7);
		portb = (g<<PB0);
		PORTD = portd, PORTB = portb;
		}
		/*for error handling 
		printf("%d\n" ,a);
			printf("%d\n" ,b);
			printf("%d\n" ,c);
			printf("%d\n" ,d);
			printf("%d\n" ,e);
			printf("%d\n" ,f);
			printf("%d\n" ,g);*/
		return 0;
}
