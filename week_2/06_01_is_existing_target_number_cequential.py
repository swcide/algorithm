finding_target = 101
finding_numbers = [i for i in range(100)]


def is_existing_target_number_sequential(target, array):
    find_count = 0
    for number in array:
        find_count += 1
        if target == number:
            print(find_count) # 14!
            return True

    return False


result = is_existing_target_number_sequential(finding_target, finding_numbers)
print(result)  # True