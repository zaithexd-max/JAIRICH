#include <iostream>
namespace first{
  int x = 1;
}
namespace second{
  int x = 2;
}
int main(){
  using std::cout;
  using std::string;
  string name = "bro";
  std::cout << name << std::endl;
}