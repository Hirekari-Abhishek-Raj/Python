def string_repeat(string_to_repeat, repeat):
    X=""
    repeat=int(repeat)
    for i in range(repeat):
        X=X+input_string+" "
    Y=X
    return Y
if __name__ == "__main__":
    input_string = input()
    input_number = input()
    print(string_repeat(input_string, input_number))
