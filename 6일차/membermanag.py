# 맴버의 정보를 가지고 있는 맴버클래스로부터 정보를 가져와서
# dictionary 형태로 변경한다  (mid:psw)
# 회원리스트는  dictionary를 요소로 하는 리스트를 구성
# 로그인여부 확인( 아이디하고 페스워드 확인)
# 맴버삭제
# 맵버추가
# import member
from member import Member

class MemberManage:
    memberList = []
    def __init__(self):
        self.memberList = {}

    def addMember(self, member):
        self.memberList[member.getId()] = member.getPwd()

    def show(self):
        for key in self.memberList:
           print("{}:{}".format(key, self.memberList[key]) )

    def __str__(self):
        for key in self.memberList:
            print("{}:{}".format(key, self.memberList[key]))
        return ""

    def isMember(self, mid, psw):
        return mid in self.memberList.keys() and psw in self.memberList.values()


mgr = MemberManage()

mgr.addMember(Member('guest', '1111'))
mgr.addMember(Member('guest2', '2222'))
mgr.addMember(Member('guest3', '3333'))
str(mgr)

# 아디와 패스워드로 맴버를 찾으면 로그인 성공   그렇지 않으면 로그인 실패 라고 출력
# if mgr.isMember('guest', '1111'):
#     print("로그인성공")
# else:
#     print("로그인실패")
# 삼항연산자
print("로그인성공") if mgr.isMember('guest', '1111') else print("로그인실패")




