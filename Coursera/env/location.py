def decorator(funk):
    def wrapped(num_list):
        result = funk(num_list)
        print('HOLA!')
        return result
    print('HOLA!33')
    return wrapped

@decorator
def summit(num_list):
    print('HOLA!22')
    print(sum(num_list))


summit([1, 2, 3, 4, 5, 6, 7, 8])