#!/usr/bin/zsh

my_array=(apple banana "Fruit Basket" orange)
echo "Listenin eleman sayisi: "${#my_array[@]}
echo "Listenin 4. elemani: "${my_array[4]}
my_array[4]='carrot'
echo "Yeni listenin eleman sayisi :"${#my_array[@]}
echo "Fantastik eleman alma sekli: "${my_array[${#my_array[@]}-1]}
echo "Listenin 4. elemani: "${my_array[4]}
