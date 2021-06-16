top_heights = [6, 9, 5, 7, 4]


#
#  시도물..
# for i in range(1,n):
#     if heights[n-1]<heights[n-i]:
#         print(heights[n-i], '??')
#         n -= 1


def get_receiver_top_orders(heights):
    n = len(heights)
    ans = [0] * n  # [0, 0, 0, 0, 0]

    while heights:  # heights 가 빈상태가 아닐 때 까지
        print(len(heights), 'pop_before')
        height = heights.pop()

        print(height, '???')
        print(len(heights), 'pop_after')
        for idx in range(len(heights) - 1, 0, -1):
            if heights[idx] > height:
                ans[len(heights)] = idx + 1
                break
    return ans


print(get_receiver_top_orders(top_heights))
# [0, 0, 2, 2, 4] 가 반환되어야 한다!
