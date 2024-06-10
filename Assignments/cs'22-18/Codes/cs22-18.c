#include<Arduino.h>
 int D=0,C=0,B=0,A,S,C_1;

//option 1
int W_1=1,X_1=1,Y_1=0,Z_1=1;
int W_2=0,X_2=1,Y_2=1,Z_2=1;
 //option2*
//int W_1=0,X_1=0,Y_1=1,Z_1=1;
//int W_2=0,X_2=1,Y_2=0,Z_2=1;
 //option3 
//int W_1=1,X_1=1,Y_1=0,Z_1=0;
 //int W_2=0,X_2=0,Y_2=1,Z_2=0;
 //option4 
//int W_1=1,X_1=0,Y_1=0,Z_1=1;
//int W_2=1,X_2=1,Y_2=1,Z_2=1;
 
 void display(int D, int C, int B, int A)
 {
  digitalWrite(2, A); //LSB
  digitalWrite(3, B); 
  digitalWrite(4, C); 
  digitalWrite(5, D); //MSB 
 }
 
 void setup() {
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
}

 void loop()
 {
 //LSB of final sum.
 S=((W_1&&!W_2) || (!W_1&&W_2));
 C_1=(W_1&&W_2);
 A=S;
 display(D,C,B,A);  
 delay(1000);
 
 S=((((X_1&&!X_2) || (!X_1&&X_2)) && !C_1) || (!((X_1&&!X_2) || (!X_1&&X_2)) && C_1));
C_1 = ( (X_1&&X_2) || (X_1&&C_1) || (X_2&&C_1));
 A=S;
 display(D,C,B,A);  
 delay(1000);
 
 S=((((Y_1&&!Y_2) || (!Y_1&&Y_2)) && !C_1) || (!((Y_1&&!Y_2) || (!Y_1&&Y_2)) && C_1));
C_1 = ( (Y_1&&Y_2) || (Y_1&&C_1) || (Y_2&&C_1));
 A=S;
 display(D,C,B,A);  
 delay(1000);
 
 //displays the possible overflow bit
 A=C_1;
  display(D,C,B,A);  
delay(1000);

if(A!=Z_1 && A!=Z_2)
{
//displays 2+1 or 2+0 (IF OVERFLOW). just for showing purpose
display(0,0,1,A);
delay(1500);
}
else
{
//displays 4+1 or 4+0 (IF NO OVERFLOW). just for showing purpose
display(0,1,0,A);
delay(1500);
}
 }
