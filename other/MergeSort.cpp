#include <iostream>
using namespace std;

void print(int * arr, int n){
    for (int i = 0; i < n; i++) {
        cout<< arr[i] << " ";
    }
    cout << endl;
}

void merge(int * arr, int l, int m, int r) {
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];

    for (int i = 0; i < n1; i++){
        L[i] = arr[l + i];
    }
    for (int i = 0; i < n2; i++) {
        R[i] = arr[m + 1 + i];
    }

    int i = 0, j = 0, k = l;

    while (i < n1 && j < n2) {
        if (L[i] <= R[j]){
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(int * arr, int a, int b){
    int mid = a + (b-a)/2;
    if (a < b) {
        mergeSort(arr, a, mid);
        mergeSort(arr, mid+1, b);
        merge(arr, a, mid, b);
    }
}

int main() {
    int arr[] = {10, 8, 7, 4,19, 30};
    mergeSort(arr, 0, 5);
    print(arr, 6);
    return 1;
}