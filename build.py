# -*- coding: utf-8 -*-
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cx_Freeze builder
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os

if __name__ == "__main__":
    os.system("TITLE cx_Freeze builder")

    version = input("1. 컴퓨터 기본 파이썬 버전(python)\n2. 파이썬 3.8.10(python3.8)\n빌드에 사용할 파이썬 버전을 선택하세요. : ")
    py = "python3.8" if version == "2" else "python"

    print("cx_Freeze 설치")
    os.system(f"{py} -m pip install cx_Freeze " + ("PySide2" if version == "2" else "PySide6"))

    opt = input("\n1. 빌드만\n2. MSI 만들기(실제 배포시에는 다른 패키징 방식을 사용하세요!)\n작업을 선택하세요. : ")
    os.system(f"{py} ./setup.py " + ("bdist_msi" if opt == "2" else "build"))
    input("\n작업이 종료되었습니다. 오류 로그가 있는지 확인하세요. 아무키나 눌러서 종료합니다. ")
