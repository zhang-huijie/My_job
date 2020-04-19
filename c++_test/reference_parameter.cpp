#include<iostream>
using namespace std;
//值传递
 void change1(int n){
    cout<<"............."<<&n<<endl;         //显示的是拷贝的地址而不是源地址 
    n++;
}

//引用传递
void change2(int & n){
    cout<<"...................."<<&n<<endl; 
    n++;
}
 //指针传递
void change3(int *n){
     cout<<"................ "<<n<<endl; 
    *n=*n+1;
 } 
int main(){
    int n=10;
    //cout<<"real_address"<<&n<<endl;
    change1(n);
    cout<<"after change1() n=    "<<n<<endl;
    change2(n);
    cout<<"after change2() n=   "<<n<<endl;
    change3(&n);
    cout<<"after change3() n=    "<<n<<endl;
    return true;
}