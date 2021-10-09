#include <stdio.h>
int main(void) {
    long int a, b, c;
    scanf("%ld %ld %ld", &a, &b, &c);
    c = c - b;
    if (c <= 0) {
        printf("%d\n", -1);
    } else { 
        printf("%ld\n", a / c + 1);
    }
    return 0;
}