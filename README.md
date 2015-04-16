# Python2UnicodeFixer

파이썬2에서의 유니코드가 선언만 잘하면 괜찮은데, 파이썬이 낯선 분들에게는 그게 어렵더라구요.
그래서 그 선언을 체크해주는 서브라임 텍스트 3 플러그인을 만들었습니다.

 * .py 소스코드에 utf8 인코딩 선언이 없으면, 파일 저장 시에 자동추가
 * .py 소스코드에 unicode_literals 선언이 없으면, 파일 저장 시에 자동추가

## Package Control 을 통한 설치
Package Control: Install Package 에서 **Python2UnicodeFixer** 를 검색해서 설치

## 수동 설치
 1. 에디터의 Preferences -> Brower Packages ... 를 선택하시면, Packages 디렉토리가 뜹니다.
 2. Packages 에 Python2UnicodeFixer 디렉토리를 만들고 안에 Python2UnicodeFixer.py 파일을 넣어줍니다.

이제, .py 확장자의 파일을 저장할 때마다 이 플러그인이 동작합니다.

## TODO
 * 자동실행여부 옵션
 * 단축키
