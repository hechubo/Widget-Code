#递归搜索这个文件夹下所有的.cpp文件，包括子文件夹里的（所有的都递归查询），返回一个数字

find . -type f -name "*.cpp" | grep -c "\.cpp$"
