shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus) #O(N)
    for order in orders: #O(M)
        if order not in menus_set:
            return False
    return True

#O(N+M)
# def is_available_to_order(menus, orders): O((N + M ) * log N)
#     # 이 부분을 채워보세요!
#     menus.sort() O(N log N)
#     orders.sort()
#     min_index = 0
#     max_index = len(menus) -1
#     index = (min_index + max_index) // 2
#     count = 0
#     for order in orders: O (M log N)
    #     while(min_index <= max_index):
    #         if order == menus[index]:
    #             print(order)
    #             min_index = 0
    #             max_index = len(menus) - 1
    #             count += 1
    #             break
    #         elif menus[index] < order:
    #             min_index = index + 1
    #         else:
    #             max_index = index - 1
    #         index = (min_index + max_index) // 2
    # if count == len(orders):
    #     return True
    # return False

result = is_available_to_order(shop_menus, shop_orders)
print(result)