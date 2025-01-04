#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    int n;
    string a, b, word;
    vector<string> words;

    cin >> n;
    cin >> a;
    cin.ignore();
    getline(cin, b);


    for (int i = 0; i < b.size(); i++) {
        if (b[i] == ' ') {
            if (!word.empty()) {
                words.push_back(word);
                word.clear();
            }
        } else {
            word += b[i];
        }
    }
    
    if (!word.empty()) {
        words.push_back(word);
    }

    for (const string& w : words) {
        if (w != a) {
            cout << "NO";
            return 0;
        }
    }

    cout << "YES";
    return 0;
}

