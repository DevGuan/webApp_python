# -conding:utf-8
import sys

def _main(argv):
    from argparse import ArgumentParser

    parser = ArgumentParser(usage="usage:%sprog [options] package.module:app")
    parser.add_argument('app',help='This is a test py')
    parser.add_argument('-end','--end',action='append',help='stay')
    parser.add_argument('-s','-heheh',action='store_true',help='Stop')
    cli_args = parser.parse_args(argv)
    print cli_args


if __name__=='__main__':
    _main(sys.argv)
