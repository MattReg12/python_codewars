def delete_nth(order, max_e):
    count = {}
    new_arr = []
    for item in order:
        item_count = count.get(item) or 0
        count[item] = item_count + 1
        if count[item] <= max_e:
            new_arr.append(item)

    return new_arr
