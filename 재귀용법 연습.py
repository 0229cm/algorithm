#!/usr/bin/env python
# coding: utf-8

# ## 재귀 용법 (recursive call, 재귀 호출)
# 
# > 고급 정렬 알고리즘엥서 재귀 용법을 사용하므로, 고급 정렬 알고리즘을 익히기 전에 재귀 용법을 먼저 익히기로 합니다.

# ### 1. 재귀 용법 (recursive call, 재귀 호출)
# * 함수 안에서 동일한 함수를 호출하는 형태
# * 여러 알고리즘 작성시 사용되므로, 익숙해져야 함

# In[1]:


def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return num


# In[2]:


for num in range(10):
    print (factorial(num))


# ### 예제 - 시간 복잡도와 공간 복잡도
# * factorial(n) 은 n - 1 번의 factorial() 함수를 호출해서, 곱셈을 함 
#   - 일종의 n-1번 반복문을 호출한 것과 동일
#   - factorial() 함수를 호출할 때마다, 지역변수 n 이 생성됨
# 
# * 시간 복잡도/공간 복잡도는 O(n-1) 이므로 결국, 둘 다 O(n)
# 

# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="4em">프로그래밍 연습</font></strong><br>
# 다음 함수를 재귀 함수를 활용해서 완성해서 1부터 num까지의 곱이 출력되게 만드세요
# </div>
# <pre>
# def muliple(data):
#     if data <= 1:
#         return data
#     
#     return -------------------------
#     
# multiple(10)
# </pre>
# </div>

# In[4]:


def multiple(num):
    return_value = 1
    for index in range(1, num+ 1):
        return_value = reutrn_vlaue * index
    return return_value


# In[5]:


def multiple(num):
    if num <=1:
        return num
    return num * multiple(num -1)


# In[6]:


multiple(10)


# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="4em">프로그래밍 연습</font></strong><br>
# 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요
# </div>
# <pre>
# 참고: 임의 값으로 리스트 만들기 random.sample(0 ~ 99까지 중에서, 임의로 10개를 만들어서 10개 값을 가지는 리스트 변수 만들기
# import random 
# data = random.sample(range(100), 10)
# </pre>

# In[1]:


import random 
data = random.sample(range(100), 10)
data


# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="4em">프로그래밍 연습</font></strong><br>
# 숫자가 들어 있는 리스트가 주어졌을 때, 리스트의 합을 리턴하는 함수를 만드세요 (재귀함수를 써보세요)
# </div>
# <pre>
# def sum_list(data):
#     if len(data) == 1:
#         return data[0]
#     
#     return --------------------------------
# 
# import random 
# data = random.sample(range(100), 10)
# print (sum_list(data))
# </pre>

# In[3]:


def sum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + sum_list(data[1:])


# In[4]:


sum_list(data)


# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="4em">프로그래밍 연습</font></strong><br>
# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함<br>
# 회문을 판별할 수 있는 함수를 리스트 슬라이싱을 활용해서 만드세요
# <img src="https://www.fun-coding.org/00_Images/palindrome.png" width=200/>
# </div>
# <pre>
# 참고 - 리스트 슬라이싱
# string = 'Dave' 
# string[-1] --> e
# string[0] --> D
# string[1:-1] --> av
# string[:-1] --> Dav
# </pre>

# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="4em">프로그래밍 연습</font></strong><br>
# 회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 의미함<br>
# 회문을 판별할 수 있는 함수를 재귀함수를 활용해서 만들어봅니다.
# </div>

# In[5]:


def palindrome(string):
    if len(strung) <= 1:
        return True
    
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False


# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="4em">프로그래밍 연습</font></strong><br>
# 1, 정수 n에 대해<br>
# 2. n이 홀수이면 3 X n + 1 을 하고,<br>
# 3. n이 짝수이면 n 을 2로 나눕니다.<br>
# 4. 이렇게 계속 진행해서 n 이 결국 1이 될 때까지 2와 3의 과정을 반복합니다.<br>
# <br>
# 예를 들어 n에 3을 넣으면,  
# <pre>
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1
# </pre>
# 이 됩니다.
# 
# 이렇게 정수 n을 입력받아, 위 알고리즘에 의해 1이 되는 과정을 모두 출력하는 함수를 작성하세요.

# In[8]:


def func(n):
    print(n)
    if n == 1:
        return n
    
    if n % 2 == 1:
        return(func((3*n) + 1))
    else:
        return (func(n/2))


# In[9]:


func(3)


# <div class="alert alert-block alert-warning">
# <strong><font color="blue" size="4em">프로그래밍 연습</font></strong><br>
# <pre>
# 문제: 정수 4를 1, 2, 3의 조합으로 나타내는 방법은 다음과 같이 총 7가지가 있음
# 1+1+1+1
# 1+1+2
# 1+2+1
# 2+1+1
# 2+2
# 1+3
# 3+1
# 정수 n이 입력으로 주어졌을 때, n을 1, 2, 3의 합으로 나타낼 수 있는 방법의 수를 구하시오
# </pre>    
# 
# 힌트: 정수 n을 만들 수 있는 경우의 수를 리턴하는 함수를 f(n) 이라고 하면,<br>
# f(n)은 f(n-1) + f(n-2) + f(n-3) 과 동일하다는 패턴 찾기<br>
# 출처: ACM-ICPC > Regionals > Asia > Korea > Asia Regional - Taejon 2001 
# </div>

# ### 문제 분석을 연습장에 작성해 본 예
# <img src="https://www.fun-coding.org/00_Images/algopractice.jpg" />

# In[11]:


def func(data):
    if data == 1:
        return 1
    elif data == 2:
        return 2
    elif data == 3:
        return 4
    
    return func(data -1) + func(data -2) + func(data -3)


# In[12]:


func(5)


# In[ ]:




