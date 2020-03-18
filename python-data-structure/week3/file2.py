# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# 7.2编写一个提示输入文件名的程序，然后打开该文件并读取该文件，查找格式如下的行：
# X-DSPAM-置信度：0.8475
# 对这些行进行计数，并从每行中提取浮点值，并计算这些值的平均值，并产生如下所示的输出。 不要在解决方案中使用sum（）函数或名为sum的变量。
# 在下面进行测试时，可以从http://www.py4e.com/code3/mbox-short.txt下载示例数据。输入mbox-short.txt作为文件名。

file_name = input('Enter file name:')
res = open(file_name)
count = 0
number = 0
for line in res:
    if line.startswith('X-DSPAM-Confidence:'):
        line = float(line[line.find(':') + 1:].strip())
        number += line
        count += 1

print('Average spam confidence:', number / count)
