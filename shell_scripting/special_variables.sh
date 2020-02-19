# $0 = The filename of the current script
# $n = The Nth argument passed to script was invoked or function was called
# $# = The number of argument passed to script of function
# $@ - All arguments passed to script of function
# $* - All arguments passed to script or function
# $? - The exit status of the last command executed
# $$ - The process ID of the current shell. For shell script, this is the process ID under which they are executing
# $1 - The process number of the last background command

echo "Script name: $0"
function func {
    for var in $*
    do let i=i+1
        echo "the \$${i} argument is: ${var}"
    done
    echo "Total count of arguments: $#"
}
func we are arguments

echo
# $@ and $* have different behavior when they were enclosed in double quotes
echo

function func2 {
    echo "--- \"\$*\""
    for arg in "$*"
    do
        echo $arg
    done

    echo "--- \"\$@\""
    for arg in "$@"
    do
        echo $arg
    done
}
func2 we are arguments
