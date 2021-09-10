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

def stock_gain():
    '''
    the most loss
    # 7
    # 3 4 1 2 1 5 1
    :return:
    '''
    n = int(input())
    prices = map(int, input().split())
    print(prices)
    gain = 0
    low = next(prices)
    for p in prices:
        low = min(low, p)
        gain = max(gain, p - low)
    print("gain",gain)


stock_gain()



