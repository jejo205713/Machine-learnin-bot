#C O D E B L O C K S

import json
from difflib import get_close_matches


def load_knowledge_base(file_path:str) ->dict:
    with open(file_path,'r')as file:
        data:dict=json.load(file)
    return data


def save_knowledge_base(file_path: str,data:dict):
    with open(file_path,'w')as file:
        json.dump(data,file,indent=2)


def find_best_match(user_question:str,questions:list[str])->str | None:
    matches: list = get_close_matches(user_question,questions,n=1,cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question: str,knowledge_base:dict)->str | None:
    for q in knowledge_base["questions"]:
        if q["question"]==question:
            return q["answer"]


def chat_bot():
    knowledge_base: dict=load_knowledge_base('knowledge_base.json')

    while  True:
        user_input: str = input('you: ')

        if user_input.lower() == 'quit':
            break

        best_match: str | none = find_best_match(user_input, [q['question'] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('bot: i don\'t know the answer, can you teach me?')
            new_answer: str = input('type the answer or "skip" to the skip:')

            if new_answer.lower() != 'skip':
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base("knowledge_base.json", knowledge_base)
                print("bot: thank you! i learned a new response!")


if __name__ == '__main__':
    chat_bot()