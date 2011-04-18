#!/usr/bin/env python
#
# Instruction generator.
# @author Nat Welch
#
# This would be so much easier if I actually knew python or perl.

from datetime import datetime, date, time

# First we generate the Math instructions.
mathi = [ 'add', 'div', 'mult', 'sub', 'and', 'or' ]

for instr in mathi:
   classname = instr.capitalize() + "Instruction"
   filename = "src/" + classname + ".java"

   txt = """
public class %(classname)s extends MathInstruction {
   public %(classname)s() {
      super();
      this.instr = "%(instr)s";
   }
}
""" % {'date': datetime.now().isoformat(' '), 'classname': classname, 'instr': instr}

   f = open(filename, 'w')
   f.write(txt)
   f.close()

# The base comparators (write to cc).
compi = [ 'comp', 'compi' ]

for instr in compi:
   classname = instr.capitalize() + "Instruction"
   filename = "src/" + classname + ".java"

   txt = """
public class %(classname)s extends MathInstruction {
   public %(classname)s() {
      super();
      this.instr = "%(instr)s";
      this.reg3 = "cc";
   }
}
""" % {'date': datetime.now().isoformat(' '), 'classname': classname, 'instr': instr}

   f = open(filename, 'w')
   f.write(txt)
   f.close()

# The classes using cc

compi = [ 'cbreq', 'cbrge', 'cbrgt', 'cbrle', 'cbrlt', 'cbrne' ]
for instr in compi:
   classname = instr.capitalize() + "Instruction"
   filename = "src/" + classname + ".java"

   txt = """
public class %(classname)s extends CompareInstruction {
   public %(classname)s() {
      super();
      this.instr = "%(instr)s";
   }
}
""" % {'date': datetime.now().isoformat(' '), 'classname': classname, 'instr': instr}

   f = open(filename, 'w')
   f.write(txt)
   f.close()
