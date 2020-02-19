
#Index

echo "---# INDEX #---"
echo
string="this is a string"
substr="hat"
echo ${#string}                 #String'in uzunlugunu verir
expr index "$string" "$substr"  #1 iss the position of the firs 't' in $string
echo

echo "---# Substring Extraction #---"
echo
#Substring Extraction
pos=1
len=3
echo ${string:$pos:$len}        #his
echo

echo "---# Simple Data Extraction #---"
echo
#Simple data extraction example
#Code to extract the First name from the data record
DATARECORD="last=Clifford,first=Johnny Boy,state=CA"
COMMA1=`expr index "$DATARECORD" ','`   #14 position of first comma
CHOP1FIELD=${DATARECORD:$COMMA1}        #
COMMA2=`expr index "$CHOP1FIELD" ','`
LENGTH=`expr $COMMA2 - 6 - 1`
FIRSTNAME=${CHOP1FIELD:6:$LENGTH}
echo "$FIRSTNAME"
echo

echo "---# Substring Replacement #---"
echo
#Substring Replacement
str="to be or not to be, be, be, be"
echo "Our string is $str."
echo
echo 'With one "/"     '${str[@]/be/eat}
echo 'With two "/"     '${str[@]//be/eat}
echo "Let's delete not "${str[@]// not/}
echo "Multichange      "${str[@]//to be/eat now}
echo "Start from last  "${str[@]/%be/eat}
echo "WTF?             "${str[@]/%be/be on $(date +%Y-%m-%d)}
