#include <iostream>
#include <bitset>
#include <string>

int number;
std::string numberBin;

int main () {
    std::cout << "Enter 32 Bit Integer: ";
    std::cin >> number;

    numberBin = std::bitset<32>(number).to_string();
    std::cout << "Number In Binary (32 Bit)" << numberBin << "\n";
}
