int minFlips(int a, int b, int c){
    int res = 0;
    int i;
    
    for(i=0;i<32;i++)
    {
        unsigned char bit_a = a & 0x1;
        unsigned char bit_b = b & 0x1;
        unsigned char bit_c = c & 0x1;
        
        if (bit_c == 0)
        {
            if (bit_a == 1) res ++;
            if (bit_b == 1) res ++;
        }
        
        if (bit_c == 1)
        {
            if(bit_a == 0 && bit_b == 0) res++;
        }
        
        a >>= 1;
        b >>= 1;
        c >>= 1;
        
    }

    return res;
}
