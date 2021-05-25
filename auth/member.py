# 회원가입(아이디, 비번, 이름, 이메일), 로그인, 마이페이지, 정보수정, 회원탈퇴

class Member(object):
    ID = '(blank)'
    pw = '(blank)'
    name = '(blank)'
    email = '(blank)'

    def set_id(self, id, pw, name, email):
        self.ID = id
        self.pw = pw
        self.name = name
        self.email = email
        return self

    def get_id(self):
        return self.ID

    def join(self):
        id = input('[회원가입 기능]\n사용할 ID를 입력하십시오 -> ')
        pw = input('사용할 비밀번호를 입력하십시오 -> ')
        name = input('이름을 입력하십시오 -> ')
        email = input('이메일을 입력하십시오 -> ')
        self.ID = id
        self.pw = pw
        self.name = name
        self.email = email

    def login(self):
        id = input('[로그인 기능]\nID를 입력하십시오 -> ')
        pw = input('비밀번호를 입력하십시오 -> ')
        if self.ID == id and self.pw == pw:
            print('[로그인 성공]')
            return self
        else:
            print('[로그인 실패]')
            return Member()

    def my_page(self):
        print(f'[마이페이지 기능]\nID : {self.ID}\nNAME : {self.name}\nEMAIL : {self.email}')

    def update(self):
        pw = input('[정보변경 기능]\n바꿀 비밀번호를 입력하십시오 -> ')
        name = input('바꿀 이름을 입력하십시오 -> ')
        email = input('바꿀 이메일을 입력하십시오 -> ')
        self.pw = pw
        self.name = name
        self.email = email
        return Member().set_id(self.ID, pw, name, email)

    def remove(self):
        pw = input('[계정탈퇴 기능]\n탈퇴하시려면 현재 계정의 비밀번호를 입력하십시오 -> ')
        if self.pw == pw:
            print('[계정 삭제됨]')
            return self.set_id('(blank)', '(blank)', '(blank)', '(blank)')  # 이 자리에 삭제가 들어가야 함)
        else:
            print('[정보가 일치하지 않음]')

    @staticmethod
    def main():
        member = Member() # 회원 DB 역할
        login_member = Member() # 로그인한 계정 역할
        while 1:
            menu = input('[메뉴]\n[1.회원가입] [2.로그인] [3.마이페이지] [4.정보수정] [5.회원탈퇴] [0.종료]')
            if menu == '0':
                break
            elif menu == '1':
                member.join()
            elif menu == '2':
                login_member = member.login()
            elif menu == '3':
                login_member.my_page()
            elif menu == '4':
                login_member = member.update()
            elif menu == '5':
                login_member = member.remove()
            elif menu == '6':
                print(f'[DB]{member.ID} {member.pw} / [Logon]{login_member.ID} {login_member.pw}')
            else:
                print('[Error]')


Member.main()
