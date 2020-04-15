#include<iostream> 
#include <string>
using namespace std;

class Solution {
public:
    bool isLongPressedName(string name, string typed) {
        
        string::iterator namebe = name.begin();
        string::iterator typedbe = typed.begin();
        //两者相等
        if(name.length()==typed.length()){
            while(typedbe < typed.end())
            {
                if(*namebe==*typedbe){
                   namebe++;
                   typedbe++;
                }
                else if (*namebe!=*typedbe)
                {
                    return false;
                }
            }
        }
        //两者不相等1
        else if(typed.length()<name.length())
        {
            return false;
        }
        //两者不相等2
        else if(typed.length()>name.length())
        {   if(*(--name.end())!=*(--typed.end())){
            return false;
            }
            else{
                while(typedbe!=typed.end()){
                    if((*typedbe==*namebe))
                    {
                        typedbe++;

                    }
                    else{
                        namebe++;
                        if(namebe<name.end()){
                            if(*typedbe!=*namebe){
                            return false;  
                            }
                            else{
                            typedbe++; 
                            }
                        }
                        else{
                            return false;
                        }
                    }
                }
            }
      
        }
    }      
};