#include <iostream>

int LCM(int a, int b) 
{ 
	int greater = std::max(a, b); 
	int smallest = std::min(a, b); 
	for (int i = greater; ; i += greater) { 
		if (i % smallest == 0) 
			return i; 
	} 
} 

int main() 
{ 
	int a,b,c;
    std::cin >> a >> b >> c;
	int res = LCM(a,b);
    res = LCM(res,c);
    std::cout << res;
	return 0; 
}