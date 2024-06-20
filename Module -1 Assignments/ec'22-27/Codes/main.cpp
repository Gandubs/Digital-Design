#include <arduino.h>

 int E=0,F=0,G=0,D=0,C=0,B=0,A=0;
 int w,x,y;

/*int qno(int X_1 , int X_2, int X_3)
{
 Y= (X_1) ||((X_2)&&(X_3));
 return Y;
}*/

 void display(int D, int C, int B, int A)
 {
  digitalWrite(2, A); 
  digitalWrite(4, B); 
  digitalWrite(5, C); 
  digitalWrite(6, D); 
  digitalWrite(7, E); 
  digitalWrite(8, F); 
  digitalWrite(9, G); 
        
 }
 
 
 void setup() {
    pinMode(2, OUTPUT);  
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);  
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
   
}

void loop()
 {
	int q[8],op_a[8],op_b[8],op_c[8],op_d[8],count = 0;
	int op_a_count=0,op_b_count=0,op_c_count=0,op_d_count=0;
		/*question - (X_1) ||((X_2)&&(X_3)) */ 
		//option 1 - (X_1) || (X_3) || (X_1&&X_2)
		//option 2 - (X_1||X_2)&&(X_1||X_3)
		//option 3 - (X_1)||(X_1&&X_2)||(X_2&&X_3)
		//option 4 - (X_1)||(X_1&&X_3)||(X_1&&X_2)
		for(int w=0;w<=1;w++)
		{
			for(int x=0;x<=1; x++)
			{
				for(int y=0;y<=1;y++)
				{
					q[count] = (w) ||(x&&y);
					op_a[count] = (w) || (y) || (w&&x);
					op_b[count] = (w||x)&&(w||y);
					op_c[count] = (w)||(w&&x)||(x&&y);
					op_d[count] = (w)||(w&&y)||(w&&x);
					count ++;
				}
			}
		}
		for(int m=0; m<8; ++m)
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
		if(op_c_count==8)
		{
		 display(0,0,0,0,1,1,0);  
                 delay(1000);
		}
		if(op_d_count==8)
		{
	        display(1,1,0,1,1,0,0);  
                 delay(1000);
		}
		 if(op_b_count==8)
		{
	         display(0,0,1,0,0,1,0);    
                 delay(1000);
		}
		 if(op_a_count==8)
		{
	         display(1,0,0,1,1,1,1);    
                 delay(1000);
		}
		if(op_b_count==op_c_count)
		{
		 display(0,0,0,0,1,1,0);  
		delay(1000);
	         display(0,0,1,0,0,1,0);    
                 delay(1000);
		}
}
