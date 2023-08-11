from enum import Enum

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])

for m in Menu:
    print(m.name)