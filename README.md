# PythonAlgo
Python 감 떨어질라 감 떨어질라...
---
## 기본 원칙
1. 구현 문제는 C++로 푼다. (메모리 직관력이 C++ 이 우세)
2. 그 외의 {문자열 매칭, Subset, String 처리} 부분 류의 문제들은 파이썬으로 푼다.
3. 그리디, 위상 정렬, Set Union, DP 등은 C++ 과 Python 같이 푼다.
4. 해당 문제집은 2번 조건을 중심으로 설명한다.
---

## 파이썬 Debugging 방법
1. C++ 와 Python 디버깅 방식은 통일한다.
```python
DEBUG = True #제출 시 DEBUG 는 False 로 변경한다.
lists = [1,2,3]
if DEBUG:
    print(f"'설명 주저리'={lists}")

```  
2. 만일 DEBUG 변수를 다르게 두고싶으면 DEBUG2 형태로 둔다.
```python
DEBUG = True #제출 시 DEBUG 는 False 로 변경한다.
DEBUG2 = True

lists = [1,2,3]
if DEBUG:
    print(f"'설명 주저리'={lists}")

if DEBUG2:
    print(f"다르게 주고싶은데?{lists}")
```

---
## 연습
1. [Subset 알고리즘](1_subset.py)
