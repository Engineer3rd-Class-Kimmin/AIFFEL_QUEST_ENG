# Python 과제 개발 진단 결과

총 35건: PASS 31, FAIL 4

기존 노트북 정의를 AST로 읽어 실행했다. input(), 출력 예제, 학습 및 외부 호출 셀은 실행하지 않았다. 아래 실패는 수정 전 실제 관측이며, 전체 교육 과정의 성능 점수가 아니다.

| ID | 종류 | 결과 | 기대값 | 실제값 |
|---|---|---|---|---|
| PY-01 | palindrome | PASS | true | true |
| PY-02 | palindrome | PASS | false | false |
| PY-03 | palindrome | PASS | true | true |
| PY-04 | palindrome | PASS | true | true |
| PY-05 | palindrome | PASS | true | true |
| PY-06 | palindrome | PASS | false | false |
| PY-07 | palindrome | PASS | true | true |
| PY-08 | palindrome | PASS | true | true |
| PY-09 | palindrome | PASS | false | false |
| PY-10 | classifier | PASS | {"count": 2, "ratio": 0.6666666666666666} | {"count": 2, "ratio": 0.6666666666666666} |
| PY-11 | classifier | PASS | {"count": 0, "ratio": 0} | {"count": 0, "ratio": 0.0} |
| PY-12 | classifier | PASS | {"count": 2, "ratio": 1} | {"count": 2, "ratio": 1.0} |
| PY-13 | classifier | FAIL | {"count": 0, "ratio": 0} | "ZeroDivisionError" |
| PY-14 | minmax | PASS | [1, 9] | [1, 9] |
| PY-15 | minmax | PASS | [-9, -1] | [-9, -1] |
| PY-16 | minmax | PASS | [4, 4] | [4, 4] |
| PY-17 | minmax | PASS | [2, 2] | [2, 2] |
| PY-18 | minmax | PASS | [-2.5, 1.5] | [-2.5, 1.5] |
| PY-19 | minmax | FAIL | "ValueError" | ["inf", "-inf"] |
| PY-20 | account | PASS | {"balance": 1100, "deposits": 1, "withdrawals": 0} | {"balance": 1100, "deposits": 1, "withdrawals": 0} |
| PY-21 | account | PASS | {"balance": 1000, "deposits": 0, "withdrawals": 0} | {"balance": 1000, "deposits": 0, "withdrawals": 0} |
| PY-22 | account | PASS | {"balance": 1000, "deposits": 0, "withdrawals": 0} | {"balance": 1000, "deposits": 0, "withdrawals": 0} |
| PY-23 | account | PASS | {"balance": 900, "deposits": 0, "withdrawals": 1} | {"balance": 900, "deposits": 0, "withdrawals": 1} |
| PY-24 | account | PASS | {"balance": 1000, "deposits": 0, "withdrawals": 0} | {"balance": 1000, "deposits": 0, "withdrawals": 0} |
| PY-25 | account | PASS | {"balance": 0, "deposits": 0, "withdrawals": 1} | {"balance": 0, "deposits": 0, "withdrawals": 1} |
| PY-26 | account | FAIL | {"balance": 1000, "deposits": 0, "withdrawals": 0} | {"balance": 1100, "deposits": 0, "withdrawals": 1} |
| PY-27 | account | FAIL | {"balance": 1000, "deposits": 0, "withdrawals": 0} | {"balance": 1000, "deposits": 0, "withdrawals": 1} |
| PY-28 | account | PASS | {"balance": 1515, "deposits": 5, "withdrawals": 0} | {"balance": 1515.0, "deposits": 5, "withdrawals": 0} |
| PY-29 | character | PASS | 100 | 100 |
| PY-30 | character | PASS | 100 | 100 |
| PY-31 | character | PASS | 99 | 99 |
| PY-32 | character | PASS | 55 | 55 |
| PY-33 | character | PASS | 0 | 0 |
| PY-34 | character | PASS | 0 | 0 |
| PY-35 | character | PASS | 100 | 100 |

빈 목록 처리와 0 이하 출금 거부는 이번에 추가한 견고성 기준이다. 원래 과제 채점 결과와 구분한다. 실패를 없애기 위해 정답을 변경하거나 원본 과제를 수정하지 않았다.

재현: 저장소 루트에서 `python evaluation/portfolio-v1/run.py`. Python 표준 라이브러리만 필요하다. FAIL이 있으면 종료 코드 1이며 results.json과 이 문서를 먼저 저장한다.

평가셋과 실행기는 Codex로 작성했다(ai-assisted). 독립 평가자의 블라인드 검토는 받지 않았다. CV/NLP/LLM 과제의 모델 재학습·추론은 이 점수에 포함하지 않았다.
