def solution(prices):
    n = len(prices)
    ans = [0] * n
    st = []  # index stack

    for t, p in enumerate(prices):
        while st and prices[st[-1]] > p:
            i = st.pop()
            ans[i] = t - i
        st.append(t)

    while st:
        i = st.pop()
        ans[i] = (n - 1) - i

    return ans
