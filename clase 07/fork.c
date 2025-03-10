int main(){
    int a = 0;
    int i;
    for(i = 1; i <= 2; i++){
        a++;
        printf("Primer a %d\n", a);
        a--;
        fork();
    }
        printf("Segundo a %d\n", a);
        
}