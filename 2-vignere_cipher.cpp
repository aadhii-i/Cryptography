#include <iostream>
#include <string>
using namespace std;

int main() {
    string plaintext, keyword, autokey, ciphertext = "";

    cout << "Enter Plaintext (UPPERCASE): ";
    cin >> plaintext;

    cout << "Enter Keyword (UPPERCASE): ";
    cin >> keyword;

    autokey = keyword;

    for (int i = 0; autokey.length() < plaintext.length(); i++) {
        autokey += plaintext[i];
    }

    for (int i = 0; i < plaintext.length(); i++) {
        char c = ((plaintext[i] - 'A') + (autokey[i] - 'A')) % 26 + 'A';
        ciphertext += c;
    }

    cout << "Autokey Used : " << autokey << endl;
    cout << "Ciphertext   : " << ciphertext << endl;

    return 0;
}