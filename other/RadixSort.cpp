#include <iostream>
using namespace std;

void countSort(int * arr, int n, int max, int min) {
    int range = max - min + 1;
    int * count = new int[range];
    int * output = new int[n];
    
    for(int i = 0; i < n; i++) 
        count[arr[i]-min]++; 
          
    for(int i = 1; i < range; i++) 
           count[i] += count[i-1]; 
    
    for(int i = n-1; i >= 0; i--) 
    {  
         output[ count[arr[i]-min] -1 ] = arr[i];  
              count[arr[i]-min]--;  
    } 
      
    for(int i=0; i < n; i++) 
            arr[i] = output[i]; 
}

void radixSort(int * arr, int n) {

}

void print(int * arr, int n){
    for (int i = 0; i < n; i++) {
        cout<< arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {4,1,3,2,5,4,3};
    countSort(arr, 7, 5,1);
    print(arr, 7);
    return 1;
}