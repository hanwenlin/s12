
# f = open("test.log","w")
#
# f.write("this is the first line\n")
# f.write("this is the second line\n")
# f.write("this is the 3 line\n")
# f.write("this is the 4 line\n")

# f = open("test.log","r")
#
# for line in f:
#     if  "3" in line:
#         print "this is the third line"
#     else:
#         print line,

f = open("test.log","w+")
f.write("new line\n")
# f.write("6\n")
# f.write("7\n")
print("data:",f.read())
f.close()