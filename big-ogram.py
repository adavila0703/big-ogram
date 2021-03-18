import time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg')

class BigO:
    runtimes = set()
    file = open('runtime.txt', 'w')
    input_test = ['test']
    
    def __init__(self) -> None:
        pass

    def calc_bigo(self, *args, **kwargs) -> None:
        """
        Big o notation calculation

        :func object: your function
        :loop int: how many time you would like the function to loop
        :returns: this is a description of what is returned
        :raises keyError: raises an exception
        """

        for i in range(0, kwargs['loop'] + 1):
            start_time = time.time()
            try:
                kwargs['func'](BigO.input_test * i)
            except TypeError:
                kwargs['func']()
            BigO.runtimes.add(time.time() - start_time)
            BigO.file.writelines(str(time.time() - start_time) + '\n')

        BigO.file.close()
        df = pd.DataFrame(BigO.runtimes)
        
        df.plot()
        # plt.gca().invert_xaxis()
        fig = plt.savefig('runtime_img.png')
        plt.close(fig)
        return BigO.runtimes