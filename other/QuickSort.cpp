#include <iostream>
using namespace std;

int partition(int * arr, int i, int j) {
    int x = arr[j];
    int a = i - 1;
    for (int b = i; b <= j - 1; b++){
        if (arr[b] <= x) {
            a ++;
            swap(arr[a], arr[b]);
        }
    }
    swap(arr[a+1], arr[j]);
    return a + 1;
}

void quickSort(int * arr, int i, int j){
    if (i < j) {
        int p = partition(arr, i, j);
        quickSort(arr, i, p - 1);
        quickSort(arr, p, j);
    }
}

void print(int * arr, int n){
    for (int i = 0; i < n; i++) {
        cout<< arr[i] << " ";
    }
}

int main() {
    int arr[] = {10, 8, 7, 4,19, 30};
    quickSort(arr, 0, 5);
    print(arr, 6);
    cout << endl;
    return 1;
}