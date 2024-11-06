def find_max_value(students):
    max_score = -1
    top_student = ""
    for student in students:
        score = students[student]
        if score > max_score:
            max_score = score
            top_student = student
    return top_student

def reverse_dict(d):
    reversed_dict = {}
    for key in d:
        value = d[key]
        if value in reversed_dict:
            reversed_dict[value] = reversed_dict[value] + key
        else:
            reversed_dict[value] = key
    return reversed_dict

def word_freq_counter(words):
    if not words:
        return {}
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict

def find_biggest_expense(expenses):
    max_average = -1
    biggest_expense = ""
    for expense in expenses:
        costs = expenses[expense]
        total = 0
        count = 0
        for cost in costs:
            total = total + cost
            count = count + 1
        average = total / count
        if average > max_average:
            max_average = average
            biggest_expense = expense
    return biggest_expense

def sum_of_expenses(expenses):
    if not expenses:
        return {}
    total_expenses = {}
    for expense in expenses:
        costs = expenses[expense]
        total = 0
        for cost in costs:
            total += cost
        total_expenses[expense] = total
    return total_expenses

def sum_of_expenses_by_type(expenses):
    if not expenses:
        return {}
    type_totals = {}
    for expense in expenses:
        items = expenses[expense]
        for item in items:
            expense_type, cost = item[0], item[1]
            if expense_type in type_totals:
                type_totals[expense_type] += cost
            else:
                type_totals[expense_type] = cost
    return type_totals
