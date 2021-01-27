def stock_loss():
    '''
    the most loss
    # 7
    # 3 4 1 2 1 5 1
    :return:
    '''
    n = int(input())
    prices = map(int, input().split())
    loss = 0
    high = next(prices)
    for p in prices:
        high = max(high, p)
        loss = min(loss, p - high)
    print("loss",loss)



