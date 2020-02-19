names=(fatih furkan necmi alo)
for n in ${names[@]} ; do
    echo "My name is $n"
done

for f in $(ls prog.sh /etc/localtime);do
    echo "File is: $f"
done

a=0
while [ $a -lt 10 ]; do
    echo "A'nin degeri: $a"
    a=$(($a+1))
done

a=1
#The until construct tests for a condition, and if false, executes commands. It keeps looping as long as the condition is false (opposite of while construct)
until [ $a -gt 6 ]; do
    echo "A'nin degeri: $a"
    a=$(($a+1))
done

count=0
while [ $count -ge 0 ];do
    echo "Count'in degeri: $count"
    count=$((count+1))
    if [ $count -ge 5 ];then
        break
    fi
done

#Tek sayilari yazdirma
count=0
while [ $count -lt 10 ];do
    count=$((count+1))
    # Count'in cift olup olmadigina bak
    if [ $((count%2)) = 0 ];then
        continue
    fi
    echo Tek sayi: $count
done
