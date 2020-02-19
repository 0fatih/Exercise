#!/usr/bin/zsh


FILELIST=`ls`
greeting='Hello       world!'
echo "Hello, World!"
echo $greeting" now with spaces: $greeting"
FileWithTimeStamp=/tmp/my-dir/file_$(/bin/date +%Y-%m-%D).txt
echo $FileWithTimeStamp
