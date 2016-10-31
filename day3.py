#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/3

import sys

def visit_routing(filename):
  #load file as a single string
  elfspeak = open(filename, 'rU').read()
  #santa starts off at the origin, coordinates = tuple
  loc_x = 0
  loc_y = 0
  #santa delivers to the origin, deliveries = dict
  visited = {(0,0): 1}
  #santa begins receiving instructions from elf
  for inst in elfspeak:
    #depending on the instruction, move santa's coordinates
    if inst == 'v':
      loc_y = loc_y - 1
    elif inst == '^':
      loc_y = loc_y + 1
    elif inst == '<':
      loc_x = loc_x - 1
    elif inst == '>':
      loc_x = loc_x + 1
    else:
      print "Error: Input must be v, ^, <, or > only!"
    #add santa's new location to his visited houses list,
    #or add 1 to a visited house's present count
    if (loc_x,loc_y) in visited:
      visited[(loc_x,loc_y)] = visited[(loc_x,loc_y)] + 1
    else:
      visited[(loc_x,loc_y)] = 1
  #elfspeak.close()
  return len(visited)

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  unique_visits = visit_routing(sys.argv[1])
  print "Santa gave " + str(unique_visits) + " houses at least one present."

if __name__ == '__main__':
  main()