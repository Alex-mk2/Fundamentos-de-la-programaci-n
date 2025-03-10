#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(){
    int N = 2, A = 3;
    int pid, status;

    // ... (resto del código)

    // Esperar a que todos los hijos terminen
    while ((pid = wait(&status)) > 0) {
        // Procesar el estado de salida del hijo
    }

    // Imprimir el número total de procesos (incluyendo el padre)
    printf("Total de procesos: %d\n", getpid());

    return 0;
}