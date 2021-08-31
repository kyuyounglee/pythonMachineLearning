# __변수이름   -> private 속성   외부에서 접근을 불허  클래스 내부에서만 사용가능
# --> 캡슐화
# 클래스의 변수는 98% 이상은  privat 속성으로 외부의 직접 접근을 막는다

class Member:
    def __init__(self, mid, mpw):
        self.__mid = mid
        self.__mpw = mpw

    def setmid(self, mid):
        self.__mid = mid

    def getmid(self):
        return self.__mid

    def setmpw(self, mpw):
        self.__mpw = mpw

    def getmpw(self):
        return self.__mpw


class MemberManage:
    def __init__(self):
        self.members = {}    # 빈 dictionary 자료구조를 생성
        # list_a = [1,2,3,4,5]   빈 리스트
        # tupple_a = (,1,2,3,4,5)  빈 튜플

    def addMember(self, m):
        self.members[m.getmid()] = m.getmpw()

    def loginMember(self, m):
        ismember = m.getmid() in self.members
        if not ismember:
            print("아이디가 존재 하지 않습니다.")
            return

        if self.members[m.getmid()] != m.getmpw():
            print("패스워드가 틀렸습니다.")
            return

    def removeMember(self, m):
        del self.members[m.getmid()]

    def printMembers(self):
        for i in self.members:
            print(i,self.members[i])

# MemberManage 객체를 생성
mm = MemberManage()

# 사용자에 해당하는 맴버객체를 생성
mm.addMember(Member('id1', '111'))
mm.addMember(Member('id2', '222'))

mm.printMembers()

