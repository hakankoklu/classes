# Uses python3
from pprint import pprint


def edit_distance(s, t):
    edit_matrix = [list(range(len(t) + 1))]
    for i in range(len(s)):
        edit_matrix.append([])
        edit_matrix[i + 1].append(i + 1)
    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            # pprint(edit_matrix)
            i_score = edit_matrix[i][j - 1] + 1
            d_score = edit_matrix[i - 1][j] + 1
            m_score = edit_matrix[i - 1][j -  1]
            mm_score = edit_matrix[i - 1][j - 1] + 1
            if s[i - 1] == t[j - 1]:
                edit_matrix[i].append(min(i_score, d_score, m_score))
            else:
                edit_matrix[i].append(min(i_score, d_score, mm_score))
    return edit_matrix[-1][-1]


print(edit_distance(input(), input()))
