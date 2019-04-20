#include <iostream>
using namespace std;

void printArray(int arr[], int n) { 
    for (int i=0; i<n; ++i) 
        cout << arr[i] << " "; 
    cout << "\n"; 
} 

void heapify (int * arr, int n, int i) {
    int largest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;
    if (l < n && arr[l] > arr[largest]) 
        largest = l;
    if (r < n && arr[r] > arr[largest]) 
        largest = r;
    if (largest != i) 
    { 
        swap(arr[i], arr[largest]); 
        heapify(arr, n, largest); 
    } 
}

void buildHeap(int arr[], int n) {
    for (int i = (n-1)/2; i >= 0; i--) {
        heapify(arr, n, i);
    }
}

void heapSort(int arr[], int n) { 
    buildHeap(arr, n);
    for (int i=n-1; i>=0; i--) 
    { 
        swap(arr[0], arr[i]); 
        heapify(arr, i, 0); 
    } 
}

int extractMax(int arr[], int n) {
    int val = arr[0];
    arr[0] = arr[n];
    n= n - 1;
    heapify(arr, n, 0);
    return val;
}

void insert(int arr[], int n, int k) {
    n ++;
    int i = n;
    arr[n] = k;
    while(i >= 1 && arr[int((i-1)/2)]<k) {
        arr[i] = arr[(i-1)/2];
        i = i/2;
    }
    arr[i] = k;
}

int main() 
{ 
    int arr[] = {12, 11, 13, 5, 6, 7, 4}; 
    int n = sizeof(arr)/sizeof(arr[0]); 
    buildHeap(arr, n);
    
    int max = extractMax(arr, n);
    n = n -1;

    cout << "max: " << max << endl << "heap is \n";
    printArray(arr, n);

    insert(arr, n, 29);
    n++;
    
    cout << "inserted array is \n"; 
    printArray(arr, n);
    
    max = extractMax(arr, n);
    n = n -1;

    cout << "max: " << max << endl << "heap is \n";
    printArray(arr, n);
    
    heapSort(arr, n); 
  
    cout << "Sorted array is \n"; 
    printArray(arr, n);

    return 1;
} 