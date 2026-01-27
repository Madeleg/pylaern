# 2026年,01月,23日,20时
import test_exception_moudle
def use_exception1():
    try:
        num = int(input('整数'))
        print(num)
    except:
        print('11')

def use_exception2():
    """
    不同的异常类型
    :return:
    """
    try:
        num = int(input('整数'))
        result = 2 / num
        print(result)
    # except ValueError:
    #     print('要整数')
    except ZeroDivisionError:
        print('0错误')
        return
    except Exception as e: #万能异常
        print(e)
    else:
        print('正常')#没异常
    finally:
        print('执行结束，结果不保证')#不受return影响

def use_exception5():
    """
    Python 如何捕获异常发生的文件（模块）和具体行数
    """
    try:
        test_exception_moudle.test()
    except Exception as e:
        print(e)
        print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
        print(e.__traceback__.tb_lineno)  # 发生异常所在的行数

if __name__ == '__main__':
    use_exception5()