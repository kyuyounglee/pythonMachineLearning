languages = ['java', 'c/c++', 'c#', 'java']
print(languages)

for str in languages:		# languages 리스트의 모든 아이템 검색
    if str == 'java':			# 만약 아이템이 ‘java’라면 
        languages.remove('java')	# 리스트에서 삭제 

print(languages)
