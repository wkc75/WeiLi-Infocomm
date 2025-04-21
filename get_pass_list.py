def get_pass_list(class_test):
    pass_list = []

    # looping through the list of results
    for result in class_test:
        # checking if the result is greater than or equal to 50
        if result >= 50:
            # if the result is greater than or equal to 50
            # append it to the list
            pass_list.append(result)

    return pass_list