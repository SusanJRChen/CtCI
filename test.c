#include <stdio.h>

int MSB(int  n) {
    while (n > 9) {
        n /= 10;
    }
    return n;
}

int length(int n) {
    int c= 0;
    while (n > 0) {
        n/= 10;
        c ++;
    }
    return c;
}

void print(int n) {
    printf("%d\n",n);
}

int power(int x, int y) {
    if (y == 0) 
        return 1; 
    else if (y%2 == 0) 
        return power(x, y/2)*power(x, y/2); 
    else
        return x*power(x, y/2)*power(x, y/2); 
}

int seed(int n) {
    int result = 0;
    int counters[9] = {0};
    int len = length(n);
    int order[20] = {0};
    int counter = 0;

    while (n > 0) {
        int msb = MSB(n);
        len = length(n);
        int m = power(10, length(n) - 1) * MSB(n);
        n -= m;
        if (counters[msb-1] == 0) {
            order[counter] = msb;
            counter++;
        }
            
        counters[msb-1]++;
    }
    for (int i = 0; i < counter; i++) {
        int j = order[i] - 1;
        if (counters[j] != 0) {
            result *= 10;
            result += counters[j];
            result *= 10;
            result += j + 1;
        }
    }
    return result;
}

int main() {
    int  n = 1;
    // seed(1221);
    for (int i = 0; i < 5; i++) {
        n = seed(n);
        print(n);
    }
    return 0;
}