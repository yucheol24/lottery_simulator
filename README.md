# 로또 시뮬레이터

이 프로젝트는 Python을 사용하여 만든 로또 시뮬레이터입니다. 사용자가 로또 번호를 생성하고 당첨 결과를 시뮬레이션할 수 있습니다.

## 기능

- 로또 번호 무작위 생성
- 당첨 번호 추첨
- 당첨 확인 및 등수별 상금 계산
- 여러 번의 시도를 통한 시뮬레이션
- 결과를 HTML 형식으로 시각화

## 기술 스택

- Backend: Python
- Frontend: HTML, CSS
- 프레임워크: Bootstrap

## 프로젝트 구조

- `lottery.py`: 로또 관련 핵심 기능을 담은 모듈
- `lottery_driver.py`: 시뮬레이션을 실행하고 결과를 HTML로 생성하는 메인 스크립트
- `lottery.html`: 생성된 결과를 보여주는 HTML 파일

## 사용 방법

1. Python 환경에서 `lottery_driver.py` 파일을 실행합니다:
2. 실행이 완료되면 `lottery.html` 파일이 생성됩니다.
3. 웹 브라우저에서 `lottery.html` 파일을 열어 결과를 확인합니다.

## 주요 기능 설명

### lottery.py

- `generate_numbers(n)`: n개의 무작위 로또 번호 생성
- `draw_winning_numbers()`: 당첨 번호 7개(보너스 번호 포함) 추첨
- `count_matching_numbers(numbers, winning_numbers)`: 일치하는 번호 개수 계산
- `check(numbers, winning_numbers)`: 당첨 금액 확인

### lottery_driver.py

- HTML 템플릿 정의
- 당첨 번호 및 시도 결과를 시각화하는 함수들 포함
- 시뮬레이션 실행 및 결과 HTML 생성

## 커스터마이징

- `NUM_TRIES` 변수를 수정하여 시뮬레이션 횟수 조정 가능
- CSS 스타일을 수정하여 결과 페이지의 디자인 변경 가능
