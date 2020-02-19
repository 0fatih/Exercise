# Often you will want to do some file tests on the file system you are running. In this case, shell will provide you with several useful commands to achieve it.

# Does the file is exist?
filename="sample.md"
if [ -e "$filename" ];then
    echo "$filename exist as a file"
fi

# Does the directory is exist?
dir_name="test_directory"
if [ -d "$dir_name" ];then
    echo "$dir_name exists as a directory"
fi

# Does the file has read permission for the user running the script/test
filename="d.txt"
if [ ! -f "$filename" ];then
    touch "$filename"
fi
if [ -r "$filename" ];then
    echo "You are allowed to read $filename"
else
    echo "You are not allowed to read $filename"
fi
