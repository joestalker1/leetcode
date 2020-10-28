def buy_and_sell_with_fee(arr, fee):
    current_max_profit = 0
    hold = -arr[0]
    for price in arr[1:]:
        # max is either we keep the current stick or sell it buying at before days
        current_max_profit = max(current_max_profit, hold + price - fee)
        # max if we buy this at this day
        hold = max(hold, current_max_profit - price)
    return current_max_profit


print(buy_and_sell_with_fee([1, 3, 2, 8, 4, 10], 2))

