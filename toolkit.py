import time

def WriteInFile(filename, args, dict_write_mode='opol'):
    '''
    this method is to write a list/ndarray/dict in a file
    :param filename:
    :param args:
    :param dict_write_mode:
    :return:
    '''
    with open(filename,'w') as f:
        if dict_write_mode is not None and dict_write_mode not in ['opol','optl']:
            raise ValueError
        if type(args).__name__ in ['list', 'ndarray']:
            for each in args:
                f.write(str(each).strip()+'\n')
        elif type(args).__name__ in ['dict']:
            ### mode is one_pair_one_line or one_pair_two_line
            if dict_write_mode == 'opol':
                for key,value in args.items():
                    f.write(str(key).strip()+'\t'+str(value).strip()+'\n')
            elif dict_write_mode == 'optl':
                for key,value in args.items():
                    f.write(str(key).strip()+'\n')
                    f.write(str(value).strip()+'\n')
            else:
                pass
        else:
            pass
    return None









def time_cost(fn):
    '''
    print the time cost of the function
    :param fn:
    :return:
    '''
    def cost(*args,**kwargs):
        beg = time.time()
        fn(*args,**kwargs)
        end = time.time()
        print('-'*50)
        print('total time cost:' + str(end - beg))
        print('-' * 50)
    return cost

def ttime(fn):
    '''
    print the begin time and end time of the function
    :param fn:
    :return:
    '''
    def _ttime(*args,**kwargs):
        print('-' * 50)
        print('begin time:'+ time.ctime())
        print('-'*50)
        fn(*args,**kwargs)
        print('-' * 50)
        print('end time:' + time.ctime())
        print('-' * 50)
    return _ttime











def test():
    @time_cost
    @ttime
    def p(x,y,a=10):
        print('000')
    p(10,20,20)
if __name__ =='__main__':
    test()

