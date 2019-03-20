#include <stdio.h>

int MSB(int  n) {
    // returns most significant digit (first digit of a number)

    // while n has more than 1 digit
    while (n > 9) {
        // divide it by 10 so it shifts to the right by one
        // number abcd becomes abc.d, but since its int, it becomes abc
        n /= 10;
    }
    return n;
}

void print(int n) {
    printf("%d\n",n);
}

int power(int x, int y) {
    // returns x^y, i literally copy and paste it from the internet, but it should be straight forward
    if (y == 0) 
        return 1; 
    else if (y%2 == 0) 
        return power(x, y/2)*power(x, y/2); 
    else
        return x*power(x, y/2)*power(x, y/2); 
}

int count_num_digits(int n) {
    // q4a
    // returns length of n
    int c= 0;

    // while n > 0, keep dividing it by 10 and count the number of times you do it
    while (n > 0) {
        n/= 10;
        c ++;
    }
    return c;
}

int count_digit_in_number(int n, int digit) {
    // q4b
    // return number of times a digit shows up in a number n
    int result = 0;
    int counter = 0;

    // this loop will loop through every digit of the number n
    while (n > 0) {
        // take the most sigificant digit (left most digit)
        int msb = MSB(n);
        // find the length of the number
        int len = count_num_digits(n);
        // for n = abcd, our msb = a, length = 4
        // we want the new n = bcd, so we have to subtract a000 such that n = n - a000
        // m = a000 = msb * 10 ^ (length - 1) 
        int m = power(10, count_num_digits(n) - 1) * MSB(n);
        n -= m;

        //if our msb is our digit, we count it
        if (msb == digit) {
            counter++;
        }
    }

    return counter;
}


int seed(int n) {
    // q4
    int result = 0;
    int order[9] = {0};
    int counter = 0;

    // this loop will loop through every digit of the number n
    while (n >0) {
        int msb = MSB(n);
        int count = count_digit_in_number(n, msb);
        
        // if we haven't already counted the number, we dont want to count the same number twice
        if (order[msb-1] == 0) {
            // then we will add the number to our result
            // result = ab initially
            // multiply it by 10, so that it becomes result = ab0
            // then we add our first count, c, such that result = abc
            // multiply by 10, so that it becomes result = abc0
            // add it by the digit we are looking at, d, becomes result = abcd
            result *= 10;
            result += count;
            result *= 10;
            result += msb;

            // we set the array such that it shows we already counted this digit, d, so we dont count it again in future iterations of the loop
            order[msb-1] ++;
        }

        // we take out the left most digit to loop through the number n
        int m = power(10, count_num_digits(n) - 1) * MSB(n);
        n -= m;
    }

    return result;
}

void seedforn(int aseed, int n) {
    // q4c-seq

    // print out aseed
    print(aseed);

    // calculate new seed
    int newseed = seed(aseed);

    // recusively repeat this print until we do it n times
    n -= 1;
    if (n > 0) {
        seedforn(newseed, n);
    }
}

int main() {
    //test
    seedforn(1, 6);
    return 0;
}