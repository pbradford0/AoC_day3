#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/3

import sys

def visit_routing(filename):
  #load file as a single string
  elfspeak = open(filename, 'rU').read()
  #santa starts off at the origin
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

def robo_routing(filename):
  #load file as a single string
  elfspeak = open(filename, 'rU').read()
  #meat santa starts off at the origin
  santa_x = 0
  santa_y = 0
  #robo santa does too
  robo_x = 0
  robo_y = 0
  #santa + robo delivers to the origin, deliveries = dict
  visited = {(0,0): 2}
  #santa begins receiving instructions from elf
  inst_count = 0
  for inst in elfspeak:
    #santa goes first, then robo
    if inst_count % 2 == 0:
      if inst == 'v':
        santa_y = santa_y - 1
      elif inst == '^':
        santa_y = santa_y + 1
      elif inst == '<':
        santa_x = santa_x - 1
      elif inst == '>':
        santa_x = santa_x + 1
      else:
        print "Error: Input must be v, ^, <, or > only!"
    elif inst_count % 2 == 1:
      if inst == 'v':
        robo_y = robo_y - 1
      elif inst == '^':
        robo_y = robo_y + 1
      elif inst == '<':
        robo_x = robo_x - 1
      elif inst == '>':
        robo_x = robo_x + 1
      else:
        print "Error: Input must be v, ^, <, or > only!"
    #add santa's new location to his visited houses list,
    #or add 1 to a visited house's present count
    #santa delivers first, then robo
    if inst_count % 2 == 0:
      if (santa_x,santa_y) in visited:
        visited[(santa_x,santa_y)] = visited[(santa_x,santa_y)] + 1
      else:
        visited[(santa_x,santa_y)] = 1
    elif inst_count % 2 == 1:
      if (robo_x,robo_y) in visited:
        visited[(robo_x,robo_y)] = visited[(robo_x,robo_y)] + 1
      else:
        visited[(robo_x,robo_y)] = 1
    #finally, increment inst_count at the end of the inst processing
    inst_count = inst_count + 1
  #elfspeak.close()
  return len(visited)

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  #unique_visits = visit_routing(sys.argv[1])
  #print "Santa gave " + str(unique_visits) + " houses at least one present."

  unique_visits = robo_routing(sys.argv[1])
  print "Team Santa and Robo-Santa gave " + str(unique_visits) + " houses at least one present."
  

if __name__ == '__main__':
  main()