# *****************
# --- Data Type ---
# *****************

'''
Python has Five standard types
scalar
    Numbers : int, float, complex
    String : str
vector : List, Tuple, Dictionary, Set
'''

hello = 'hello'
print(hello)
print(hello[0])
print(hello[2:5])
print(hello[2:])

# List CRUD Example

ls = ['abcd', 786, 2.23, 'john', 70.2]
tinyls = [123, 'john']

print('\n-----[List CRUD Example]-----')

# Create: ls 에 '100'을 추가 Create

ls += [100]
print(f'[1.Create]{ls}')

# Read: ls 의 목록을 출력

print(f'[2.Read]{ls}')

# Update: ls와 tinyls 의 결합

ls += tinyls
print(f'[3.Update]{ls}')

# Delete: ls 에서 786을 제거

ls.remove(786)
print(f'[4.Remove]{ls}')

# Tuple CRUD Example

print('\n-----[Tuple CRUD Example]-----')

tp = ('abcd', 786, 2.23, 'john', 70.2)
tinytp = (123, 'john')

# Create: tp 에 '100'을 추가 Create

tp += (100, )
print(f'[1.Create]{tp}')

# Read: tp 의 목록을 출력

print(f'[2.Read]{tp}')

# Update: tp와 tinytp 의 결합

tp += tinytp
print(f'[3.Update]{tp}')

# Delete: tp 에서 786을 제거

ls = list(tp)
ls.remove(786)
tp = tuple(ls)
print(f'[4.Delete]{tp}')

# dictionary CRUD Example

print('\n-----[Dictionary CRUD Example]-----')

dt = {'abcd': 786, 'john': 70.2}
tinydt = {'홍': '30세'}

# Create: dt 에 키값으로 'tom', 밸류로 '100'을 추가 Create

dt['tom'] = 100
print(f'[1.Create]{dt}')

# Read: dt 의 목록을 출력

print(f'[2.Read]{dt}')

# Update: dt와 tinydt 의 결합

dt.update(tinydt)
print(f'[3.Update]{dt}')

# Delete: dt 에서 'abcd' 제거

del dt['abcd']
print(f'[4.Delete]{dt}')