#coding:utf-8
from Classe_Automate import *
from L_star import *

from os import listdir
from os.path import isfile, join
import sys

import datetime

# Tests (Victor)
#automate1 = Automate.importFromFile("DataAutomate/141_Cambodian.fsa.att")

def run(fct):
  false = []
  mypath = "DataAutomate"

  count = 0
  for f in listdir(mypath):
      if isfile(join(mypath, f)):
          count += 1
	  sys.stdout.write(f+"	")
          a = Automate.importFromFile(join(mypath, f))
          #print a
          
          oracle = Oracle(a)
          alphabet = a.getAlphabet()
          l_star = L_star(alphabet, oracle)
                
          if fct == "run":
            res = l_star.run()
          elif fct == "run_without_equivalence":
            res = l_star.run_without_equivalence()        
          
          if not res:
            false.append(f)

  print "##", len(false), '/', count, false

print "#Run with equivalence"
run("run")

for i in range(5):
  print "#Run_without_equivalence", i
  run("run_without_equivalence")
