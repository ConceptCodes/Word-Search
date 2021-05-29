from board import Board

tmp = Board(word_list=['hello','world','computer','vision'])

#print(tmp)
# print(tmp._word_list[3])
print('horizontal',tmp._horizontal_(tmp._word_list[3]))