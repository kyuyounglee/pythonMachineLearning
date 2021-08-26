languages = ['java', 'c/c++', 'c#', 'java']
print(languages)

while ('java' in languages):    # languages 리스트에 ‘java’문자열이 있다면 반복
    languages.remove('java')  # 리스트에서 삭제 

print(languages)
