# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# 7.1编写一个提示输入文件名的程序，然后打开该文件并读取该文件，并以大写形式打印该文件的内容。 使用words.txt文件生成以下输出。
# 您可以从http://www.py4e.com/code3/words.txt下载示例数据


file_name = input('Enter file name:')
print(open(file_name).read().upper().rstrip())
