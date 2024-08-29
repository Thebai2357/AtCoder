#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
    vector<int> vec;
    int N,K;
    cin>>N>>K;
    for(int i=0;i<N;i++){
        for(int k=0;k<K;k++){
            vec.push_back(i+1);
        }
    }

    for(int i=0;i<N*K;i++){
        cout<<vec.at(i)<<" ";
    }


}
