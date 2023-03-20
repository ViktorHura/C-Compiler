void main(){
int na;
int nb = 0;

const int ca;  // err
const int cb = 0;

int * nna;
int * nnb = 0;

const int * cna;
const int * cnb = 0;

int * const nca;  // err
int * const ncb = 0;

const int * const cca;  // err
const int * const ccb = 0;
}