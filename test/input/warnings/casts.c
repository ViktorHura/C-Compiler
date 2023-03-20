void main(){
    float a = (float) 1.0;      // ok
    int b = 1;                  // ok
    char c = 'c';               // ok

    float d = 1.0;
    float e = 1;                // ok
    float f = 'c';              // ok

    int g = 1.0;
    int h = (float) 1.0;
    int i = (int) 1.0;          // ok
    int j = (char) 1.0;         // ok
    int k = (char) 1;           // ok
    int l = 'c';                // ok

    char m = 1.0;
    char n = 1;
    char o = (char) 1.0;        // ok
    char p = (char) 1;          // ok
}