/*
Binary adder with carry using formula
*/

int getSum(int a, int b){
    unsigned int res = 0;
    
    unsigned int a_bit = 0;
    unsigned int b_bit = 0;
    
    unsigned int sum_bit = 0;
    unsigned int carry_bit = 0;
    
    int i;
    
    for(i = 0;i < 32; i++)
    {
        a_bit = (a >> i) & 0x1;
        b_bit = (b >> i) & 0x1;
        
        sum_bit = a_bit ^ b_bit ^ carry_bit;
        
        carry_bit = (a_bit & b_bit) | (carry_bit & (a_bit ^ b_bit));
        
        res = res | (sum_bit << i);
        
    }
    
    return (int)res;

}
