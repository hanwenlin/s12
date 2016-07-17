# xml是实现不同语言或程序之间进行数据交换的协议，跟json差不多，但json使用起来更简单，不过，古时候，在json还没诞生的黑暗年代，大家只能选择用xml呀，至今很多传统公司如金融行业的很多系统的接口还主要是xml。
import xml.etree.ElementTree as ET


tree = ET.parse("test.xml")
root = tree.getroot()
print(root.tag)


#遍历xml文档
# for child in root:
#     print(child.tag,child.attrib)
#     for i in child:
#         print("---->",i.tag,i.text)


#只遍历年份
# for node in root.iter('year'):
#     print(node.tag,node.text)



#修改  #找到年份+1之后添加一个updated属性
# for node in root.iter('year'):
#     new_year = int(node.text) + 1
#     node.text = str(new_year)
#     node.set("updated","yes")
#
# tree.write("xmltest.xml")

#删除node
for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
     root.remove(country)

tree.write('output.xml')