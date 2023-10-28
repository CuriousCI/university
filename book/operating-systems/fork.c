#include <stdio.h>
#include <unistd.h>

int main() {
    int pid = fork();

    if (pid) {
        printf("%d ", pid);
        sleep(1);
        printf("Main\n");
    } else {
        printf("Secondary\n");
        printf("%d\n", getpid());
    }
    
    return 0;
}
