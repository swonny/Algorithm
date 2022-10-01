#include <stdio.h>

int sum(int n) {
    if(n == 1) {
        return n;
    }
    int tmp = sum(n - 1);
    int res = tmp + n;
    return res;
}

int main() {
    int i = 2;
    while(i < 10000) i = sum(i);
    int res = i;
    printf("%d", res);
}