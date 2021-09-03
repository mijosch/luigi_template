#!/usr/bin/env python
# coding: utf-8

# In[7]:


import luigi
import datetime
from luigi import Task, LocalTarget, Parameter


class getlocaltime(Task):
    def requires(self):
        return None
    
    def output(self):
        return luigi.LocalTarget('time.txt')
    
    def run(self):
        with self.output().open('w') as outfile:
            outfile.write(str(datetime.datetime.utcnow()))

class HelloWorld(Task):
    def requires(self):
        return [getlocaltime()]
    
    def output(self):
        return luigi.LocalTarget('helloworld.txt')
    
    def run(self):
        with self.output().open('w') as outfile:
            outfile.write('Hello World!\n')

if __name__ == '__main__':
    luigi.run()




