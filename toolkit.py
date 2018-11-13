import time
import os
import sys
import itertools

def WriteInFile(filename, args, dict_write_mode='opol'):
    "this method is to write a list/ndarray/dict in a file"
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
    "print the time cost of the function"
    def cost(*args,**kwargs):
        beg = time.time()
        fn(*args,**kwargs)
        end = time.time()
        print('-'*50)
        print('total time cost:' + str(end - beg))
        print('-' * 50)
    return cost

def ttime(fn):
    "print the begin time and end time of the function"
    def _ttime(*args,**kwargs):
        print('-' * 50)
        print('begin time:'+ time.ctime())
        print('-'*50)
        fn(*args,**kwargs)
        print('-' * 50)
        print('end time:' + time.ctime())
        print('-' * 50)
    return _ttime

def ensure_dir_exists(directory):
    "Creates directories if they don't exist."
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)


def path_walk(pathname):
    for root, dirs, files in os.walk(pathname, topdown=False):
        for name in files:
            yield os.path.join(root, name)



def iter_chunks(chunk_size, iterator):
    "Yield from an iterator in chunks of chunk_size."
    iterator = iter(iterator)
    while True:
        next_chunk = list(itertools.islice(iterator, chunk_size))
        # If len(iterable) % chunk_size == 0, don't return an empty chunk.
        if next_chunk:
            yield next_chunk
        else:
            break


















@time_cost
@ttime
def p(x,y,a=10):
    print('000')

def test():
    # for file in path_walk('.'):
    #     print(file)


    # it= [1,2,3,4,5,6,7,8,9,10]
    # chunk_size = 2
    # for i in iter_chunks(chunk_size,it):
    #     print(i)

    pass


if __name__ =='__main__':
    test()
