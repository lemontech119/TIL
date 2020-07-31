import sys

rule = list(map(int, sys.stdin.readline().split()))
card_list = list(map(int, sys.stdin.readline().split()))

result = 0
for one in range(0, rule[0]-2):
    for two in range(one+1, rule[0]-1):
        if card_list[one] + card_list[two] > rule[1]:
            continue
        for three in range(two+1, rule[0]):
            if card_list[one] + card_list[two] + card_list[three] > rule[1]:
                continue
            if card_list[one] + card_list[two] + card_list[three] >= result:
                result = card_list[one] + card_list[two] + card_list[three]

print(result)



