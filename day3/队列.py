
import  collections

d = collections.deque()
d.append('1')
d.appendleft('10')
d.appendleft('1')
print(d)
print(d.count('1'))
d.extendleft(['aa','bb','cc'])
d.extend(['yy','uu','ii'])
print(d)
d.rotate(5)
print(d)