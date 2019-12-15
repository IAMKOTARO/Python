# -*- Coding: utf-8 -*-

def is_subsequence(word, S):
    for s in word:
        if s in S:
            slice_point = S.index(s)
            S = S[slice_point:]
            # print(S)
        else:
            return False
    return True


def get_longest_subsequence(S, D):
    longest_subsequence = ""
    for d in D:
        # print(len(d) > len(longest_subsequence))
        if is_subsequence(d, S) and len(d) > len(longest_subsequence):
            longest_subsequence = d
            # print(len(longest_subsequence))
    return longest_subsequence

def main():
    S = "abppplee"
    D = ["able", "ale", "apple", "bale", "kangaroo"]

    #is_subsequence()のデバッグ用
    # for index in range(5):
    #     print(D[index], is_subsequence(D[index], S))

    print("The longest subsequence of " + S +  " is " + get_longest_subsequence(S, D))

if __name__ == "__main__":
    main()