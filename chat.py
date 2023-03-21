import os
import openai
openai.api_key = "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"

messages = []


# while True를 작성함으로서 무한반복으로 채팅할 수 있도록 한다.
while True:
    #Question part: role에 user라고 적어서 '이런 거 물어 볼 거야~'라고 알려준다.
    user_content = input("user : ") 
    messages.append({"role":"user", "content": f"{user_content}"})
    completion = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages = messages)

    #Answer part: role에 assistant라고 적어서 '이러헥 답해줄 거야~'라고 알려준다.
    assistant_content = completion.choices[0].message["content"].strip()
    messages.append({"role":"assistant", "content": f"{assistant_content}"})

    print(f"gpt: {assistant_content}")
    
    #gpt란 이름을 붙이기 싫다면 아래처럼 작성해도 된다.
    # print(assistant_content)



# role: system은 chatgpt한테 응답의 대상자가 누구인지 알려주는 것이다.
# role: system, content: 너는 유치원생한테 정보를 알려줄 거야,
# 라고 작성하면 chatgpt가 질문에 답할 때 유치원생한테 답변하듯이 쉬운 언어로 친근히 말해준다.
# 반대로 'conetn: 너는 박사과정한테 답변한다.'고 알려주면, 어려운 단어 섞어가면서 설명한다.
# chatgpt의 응답 대상자가 누구인지 알려줌으로서 chatgpt의 대답 방식도 달라지는 것이다.


# 이상한 문장
# print(completion.choices[0].message) 라고 작성하면 이상한 문자만 나온다.
# print(completion.choices[0].message['content']) 
# 라고 작성하면 문장은 잘 나오는 데 앞에 공백이 있는 채 나오기도 한다.

# strip()
# print(completion.choices[0].message['content'].strip()) 
# 위에처럼 strip 함수를 사용해서 공백을 제거할 수 있다.
# >>> ex_str = "        hello         "
# >>> ex_str.strip()
# # 'hello'

# 변형
# print(completion.choices[0].message['content']) 
# 위에처럼 작성할 수도 있고 아래처럼 작성할 수도 있다. 결과는 똑같다.
# print(completion["choices"][0]["message"]["content"])


#f는 f string이다. 문자열 안에 변수 쓸 때 사용된다.
# person1 = "철수"
# person2 = "영희"
# print("{}는 {}를 좋아한데요!".format(person1, person2))
#위에 걸 아래처럼 f string을 사용하면 가독성 높게 바꿀 수 있다.
# person1 = "철수"
# person2 = "영희"
# print(f"{person1}는 {person2}를 좋아한데요!")