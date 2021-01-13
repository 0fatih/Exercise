// Zinciri bırakma şeysi

#include <iostream>

int main()
{
    float deger;
    std::cout << "Ilk gun degerini gir:";
    std::cin >> deger;
    int sayac = int(deger);
    int toplam = 0;

    for (int gun = 1; gun <= 365; gun++)
    {
        if (deger >= sayac)
        {
            std::cout << gun << ". gunde minimum limit: " << int(deger) << std::endl;
            sayac++;
        }
        toplam += int(deger);
        deger += deger / 100;
    }

    std::cout << "\n\n TOPLAM:" << toplam << "\n\n";
    system("pause");
}

