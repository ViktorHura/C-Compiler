int * a = 2;

int * b = a * 2; // err
int * c = +a;    // should be error
int * d = -a;    // err
int * e = a / 2; // err

int * f = 3;

int * m = 0 - f; // err
int * n = f - 0; 

int * g = f - a;
int * h = f + a; // err
int * i = f * a; // err
int * j = f / a; // err

int * k = a + 1; 
int * l = a - 3; 

int * o = 4.0; // err
float p = a;   // err

int* q = &1; // err

int main() {
    *(2+3) = 4; // err
}