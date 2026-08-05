#include <iostream>
#include <string>
using namespace std;

int main() {
    string plaintext, key, ciphertext = "";

    cout << "Enter Plaintext (UPPERCASE): ";
    cin >> plaintext;

    cout << "Enter Random Key (same length as plaintext): ";
    cin >> key;

    if (plaintext.length() != key.length()) {
        cout << "Error: Key length must be equal to plaintext length!" << endl;
        return 0;
    }

    for (int i = 0; i < plaintext.length(); i++) {
        char c = ((plaintext[i] - 'A') + (key[i] - 'A')) % 26 + 'A';
        ciphertext += c;
    }

    cout << "Ciphertext: " << ciphertext << endl;

    return 0;
}