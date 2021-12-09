import os

class App():
    def __init__(self):
        pass

    @staticmethod
    def run_command(cmd,args):
        result_code=os.system(cmd+" "+args)
        return (result_code)
    @staticmethod
    def run_command_output(cmd,args):
        result=os.popen(cmd+" "+args).read()
        return (result)
