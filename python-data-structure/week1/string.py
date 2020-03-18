# my_str = 'apple'
# count = 0
# for i in my_str:
#     count += 1
#     print(i)
# print(count)
#
# print(my_str[1])

# x = 'From marquard@uct.ac.za'
# print(x[17])
# print(x[14:17])
# print(type(len(x)))
# print(x.upper())

# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.


# 6.5使用find（）和字符串切片（请参见第6.10节）编写代码以提取以下行末的数字。 将提取的值转换为浮点数并打印出来。


text = "X-DSPAM-Confidence:    0.8475"
print(float(text[text.find(':') + 1:].strip()))

