
# 导入装饰器，用于超时退出
import func_timeout

@func_timeout.func_set_timeout(2)
def askChoice():
    return input('yes or no:')


if __name__ == '__main__':
    # get_input(e)
    try:
        s = askChoice()
    except:
        s = 'f'
    print(s)
