void main(){
    int a;
    const int fls = 0;
    if (2+3 > 2){
         a++;
    }

    if (fls){
         a = 2;
    }


    if (2+3 > 2){
       ++a;
    }else{
       --a;
    }

    if (3-5 > fls){
         a++;
    }else{
         a--;
    }

    if (2+3 > 2){
         ++a;
    }else if (2) {
         --a;
    }else{
         a++;
    }

    if (2+3 < 2){
          a--;
    }else if (2) {
          ++a;
    }else{
          --a;
    }

    if (2+3 < 2){
          a--;
    }else if (fls) {
          ++a;
    }else{
          --a;
    }

}