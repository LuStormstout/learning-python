# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# ＃8.4打开文件romeo.txt并逐行读取。 对于每一行，使用split（）方法将该行拆分为单词列表。 该程序应建立单词列表。 对于每一行中的每个单词，请检查该单词是否已在列表中，如果没有，则将其附加到列表中。 程序完成后，按字母顺序对结果单词进行排序和打印。
# ＃您可以从http://www.py4e.com/code3/romeo.txt下载示例数据

my_list = open('romeo.txt').read().split()
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)

new_list.sort()
print(new_list)

