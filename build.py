# -*- coding: utf-8 -*-
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cx_Freeze builder
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import sys

if __name__ == "__main__":
    os.system("TITLE cx_Freeze builder")

    py_version = sys.version.split(" ")[0].split(".")
    if int(py_version[0]) < 3 or int(py_version[1]) < 8 or (int(py_version[1]) == 8 and int(py_version[2]) < 10):
        raise Exception("Python 3.8.10 or higher is required.")

    version = input("1. 컴퓨터 기본 파이썬 버전(python)\n2. 파이썬 3.8.10(python3.8, Windows 7용)\n빌드에 사용할 파이썬 버전을 선택하세요. : ")
    py = "python"
    if version == "1":
        py += ("3" if input("\n1. python\n2. python3\n환경변수에 등록된 python3의 호출 키워드를 선택하세요. : ") == "2" else "")
    elif version == "2":
        py += "3.8"
        print("\n\nWindows 7 호환성을 위해 Pyside버전을 2버전으로 변경합니다. 스크립트가 정상 종료되지 못한 경우 수동으로 qt_core.py 파일을 원래대로 되돌려주세요.\n\n")
        os.rename("src/main/qt_core.py", "qt_core.py.bak")
        with open("qt_core.py.bak", "rt", encoding='utf-8') as ori, \
                open("src/main/qt_core.py", "wt", encoding='utf-8') as new:
            for line in ori.readlines():
                if "_SUPPORT_WINDOWS_7_" in line:
                    print(line)
                    line.replace("False", "True")
                    print(">> " + line, end="\n\n\n")
                new.write(line)
    print("선택된 파이썬 버전 : ", end='')
    if 1 == os.system(f"{py} --version"):
        raise Exception(f"파이썬 버전({py})을 찾을 수 없습니다.")

    print("cx_Freeze 설치")
    os.system(f"{py} -m pip install cx_Freeze " + ("PySide2" if version == "2" else "PySide6"))

    opt = input("\n1. 빌드만\n2. MSI 만들기(실제 배포시에는 다른 패키징 방식을 사용하세요!)\n작업을 선택하세요. : ")
    os.system(f"{py} ./setup.py " + ("bdist_msi" if opt == "2" else "build"))

    if version == "2":
        os.remove("src/main/qt_core.py")
        os.rename("qt_core.py.bak", "src/main/qt_core.py")
        print("\nqt_core.py 파일을 원래대로 되돌렸습니다.")

    input("\n작업이 종료되었습니다. 오류 로그가 있는지 확인하세요. 아무키나 눌러서 종료합니다. ")
