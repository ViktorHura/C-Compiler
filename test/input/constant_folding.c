void main(){
    // unary operations and conversions
    int a = ! 2.0;
    float b = -2;
    float c = +'c';

    // binary operations
    int d = 4 + (int)2.0;
    int e = 2 - 1.0;
    int f = 2 * 'c';
    int g = 4.0 / 2;

    int h = 2 < 4;
    int i = 4 > 2;
    int j = 1 == 0;

    int k = 7 % 5;

    int l = 2 >= 1;
    int m = 2 <= 2;
    int n = 2 != 2;

    int o = 1 && 0;
    int p = 1 || 0;

    // mix
    int q = (((2 + 1) - (int)(2.34 * 'c') % 4 + (2>1) + (1<2) + (1&&0) + (2 >= 2)) / 0.5);

    // prevent unused variables
    a++;
    b++;
    c++;
    d++;
    e++;
    f++;
    g++;
    h++;
    i++;
    j++;
    k++;
    l++;
    m++;
    n++;
    o++;
    p++;
    q++;
}