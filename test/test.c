#include <stdio.h>

void print(int * a) {
    printf("%d\n", *a);
}

int main() {
    int a[3] = {1,0,0};
    int *p = a; // p points to a[0]
    int *q = p + 2; // q points to a[2]
    print(p);
    print(q);
    p += 2;
    print(p);
    ++(*q); // does the same as "++a[2]", increment a[2] by 1
    print(q);
    return 0;
}