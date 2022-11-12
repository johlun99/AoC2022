import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-d', '--day', help = 'Day to solve')

args = parser.parse_args()

print('day' + args.day + '/solution.py')
exec(open('day' + args.day + '/solution.py').read())