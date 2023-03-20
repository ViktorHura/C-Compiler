int n = 0;
const int c = 0;

int * nn = 0;
const int * cn = 0;
int * const nc = 0;
const int * const cc = 0;

int main() {
    n = 1; 
    c = 1; // err
    nn = 1;
    cn = 1; 
    nc = 1; // err
    cc = 1; // err

    *nn = 1; 
    *cn = 1; // err
    *nc = 1; 
    *cc = 1; // err
}