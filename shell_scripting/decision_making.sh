a=5
b=5

if [ "$a" == "$b" ]; then
    echo "Variables are equal."
fi

if [ "$a" = "$b" ]; then
    echo "Variables are equal."
fi

if [ "$a" -eq "$b" ]; then
    echo "Variables are equal."
fi

if [ "$a" -ne "$b" ]; then
    echo "Variables are equal."
fi

if [ "$a" -lt "$b" ]; then
    echo "Variable a is lower then b."
fi

if [ "$a" -gt "$b" ]; then
    echo "Variable b is bigger then a."
fi

if [ "$a" -le "$b" ]; then
    echo "Variable a is lower then or equal to b."
fi

if [ "$a" -ge "$b" ]; then
    echo "Variable b is bigger then or equal to a."
fi

case "$a" in
    "1")
        echo "A=1"
        ;;
    "2")
        echo "A=2"
        ;;
    "5")
        echo "A=5"
        ;;
esac

echo
echo

mycase=1
case $mycase in
    1) echo "You selected option 1";;
    2) echo "You selected option 2";;
    3) echo "You selected option 3";;
esac

