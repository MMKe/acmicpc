def read_int():
    """
    표준 입출력으로 숫자 하나를 받아서 리턴한다. 
    """
    import sys

    return int(sys.stdin.readline().rstrip())


def make_card_counter():
    """
    표준 입출력으로 카드 리스트를 읽어들여서 
    카드들의 출현 횟수를 저장한 dict을 반환한다.
    """

    import sys
    from collections import defaultdict

    result_dict = defaultdict(int)

    line = sys.stdin.readline().rstrip()

    for num in line.split():
        num = int(num)

        result_dict[num] += 1

    return result_dict


def read_list_of_int():
    """
    표준 입출력으로 숫자들을 읽어들여 리스트로 반환한다. 
    입력 형식은 아래와 같이 띄어쓰기로 구분된다.
    ex) n1 n2 n3 n4 ... 
    """
    import sys

    line = sys.stdin.readline().rstrip()

    return [int(num) for num in line.split(" ")]


# 입력값 처리
N = read_int()
cards = make_card_counter()
M = read_int()
targets = read_list_of_int()


answers = []
for target in targets:
    answers.append(cards[target])

answers = map(str, answers)

print(" ".join(answers))

