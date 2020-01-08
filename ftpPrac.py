import ftplib
import sys
import os
import argparse
import getpass

def upload(ftp):
    ftp.cwd("/incoming")  
    filename = input('업로드할 파일 : ')
    ftp.storbinary("STOR " + filename, open(filename, "rb"))

def download(ftp):
    ftp.cwd("/pub")
    filename = input('다운로드할 파일 : ')

    ftp.retrbinary("RETR " + filename, open(filename, 'wb').write)
def showfiles(ftp):
    filelist = os.listdir()
    print('파일 목록 = ', filelist)

# address는 ftp.cs.brown.edu 
# username은 anonymous 라는 매개변수를 받는 가정을 합니다. 
# 암호는 따로 입력하지 않고 접속하실 수 있습니다.
def main():
    parser = argparse.ArgumentParser(description='Access to FTP Server')
    parser.add_argument('--address', action="store", dest="address", required=True)
    parser.add_argument('--username', action="store", dest="username", required=True)
    given_args = parser.parse_args()
    address = given_args.address
    username = given_args.username
    password = getpass.getpass(prompt="암호를 입력하시오 :")
    ftp = ftplib.FTP(address)
    ftp.login(username, password)

    print ("환영합니다. 서버에 연결되었습니다.")
    print ("==============작업 목록==============")
    print ("1. Display files in the directory \n2. Change directory \n3. Upload file(s) \n4. Download file \n5. Exit")
    
    while True:
        job = input('원하는 작업번호를 선택하시오 : ')
        # 1번 파일 목록 보여주기
        if job == '1':
            print(ftp.dir())
            continue
        
        # 2번 디렉토리 이동
        elif job == '2':
            print("* 뒤로가기 : '..'")
            cd = input('작업 입력하세요 : ')
            ftp.cwd(cd)

        # 3번 파일 업로드
        # 파일 형식까지 입력해줘야 합니다.
        elif job == '3':
            upload(ftp)
            print("경로에 업로드 되었습니다.")
            continue
        
        # 4번 파일 다운로드
        elif job == '4':
            download(ftp)
            print("다운로드가 완료되었습니다.")
            continue

        # 5번 종료하기
        elif job == '5':
            print('서버와의 연결이 종료되었습니다.')
            break

        else:
            continue
    
if __name__ == '__main__':
    main()