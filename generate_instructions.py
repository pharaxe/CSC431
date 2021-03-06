#!/usr/bin/env python
#
# Instruction generator.
# @author Nat Welch
#
# This would be so much easier if I actually knew python or perl.

from datetime import datetime, date, time

instructions = [

# Arithmetic (MATHS)

   {
      'name': 'add',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
      'sparc': [ 'add' ],
   },
   {
      'name': 'addi',
      'sources': [ 'Immediate', 'Register' ],
      'dest': [ 'Register' ],
      'sparc': [ 'add' ],
   },
   {
      'name': 'div',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
      'sparc': [ 'mov', 'mov','call', 'nop', 'mov' ],
      'modified': 1
   },
   {
      'name': 'mult',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
      'sparc': [ 'mov', 'mov','call', 'nop', 'mov' ],
      'modified': 1
   },
   {
      'name': 'sub',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
      'sparc': [ 'sub' ],
   },

# Boolean (Yes? or No?)

   {
      'name': 'and',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
      'sparc': [ 'and' ],
   },
   {
      'name': 'or',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
      'sparc': [ 'or' ],
   },
   {
      'name': 'xori',
      'sources': [ 'Register', 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': [ 'xor' ],
   },

# Comparison and Branching (Forks in the road)

   {
      'name': 'compi',
      'sources': [ 'Register', 'Immediate'],
      'dest': [ 'ConditionCodeRegister' ],
      'sparc': [ 'cmp' ],
   },
   {
      'name': 'comp',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'ConditionCodeRegister' ],
      'sparc': [ 'cmp' ],
   },
   {
      'name': 'cbreq',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
      'sparc': [ 'be', 'nop', 'ba', 'nop' ],
   },
   {
      'name': 'cbrge',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
      'sparc': [ 'bge', 'nop', 'ba', 'nop' ],
   },
   {
      'name': 'cbrgt',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
      'sparc': [ 'bg', 'nop', 'ba', 'nop' ],
   },
   {
      'name': 'cbrle',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
      'sparc': [ 'ble', 'nop', 'ba', 'nop' ],
   },
   {
      'name': 'cbrlt',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
      'sparc': [ 'bl', 'nop', 'ba', 'nop' ],
   },
   {
      'name': 'cbrne',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
      'sparc': [ 'bne', 'nop', 'ba', 'nop' ],
   },
   {
      'name': 'jumpi',
      'sources': [ 'Label' ],
      'dest': [ ],
      'sparc': [ 'ba', 'nop' ],
   },

# Loads (Not the kind for her face)

   {
      'name': 'loadi',
      'sources': [ 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': [ 'set', 'sub' ],
      'modified': 1
   },
   {
      'name': 'loadai',
      'sources': [ 'Register', 'Field' ],
      'dest': [ 'Register' ],
      'sparc': [ 'ldsw' ],
      'modified': 1
   },
   {
      'name': 'loadglobal',
      'sources': [ 'ID' ],
      'dest': [ 'Register' ],
      'sparc': [ 'set', 'ldsw' ],
   },
   {
      'name': 'loadinargument',
      'sources': [ 'ID', 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': ['mov'],
      'modified': 1
   },
   {
      'name': 'loadret',
      'sources': [ ],
      'dest': [ 'Register' ],
      'sparc': [ 'mov' ],
      'modified': 1
   },
   {
      'name': 'computeformaladdress',
      'sources': [ 'ID', 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': [ ],
   },
   {
      'name': 'restoreformal',
      'sources': [ 'ID', 'Immediate' ],
      'dest': [ ],
      'sparc': [ ],
   },
   {
      'name': 'computeglobaladdress',
      'sources': [ 'ID' ],
      'dest': [ 'Register' ],
      'sparc': [ ],
   },

# Stores (Target, 7-11, etc.)

   {
      'name': 'storeai',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Field' ],
      'sparc': ['st'],
      'modified': 1
   },
   {
      'name': 'storeglobal',
      'sources': [ 'Register' ],
      'dest': [ 'ID' ],
      'sparc': [ 'set', 'st' ],
   },
   {
      'name': 'storeoutargument',
      'sources': [ 'Register' ],
      'dest': [ 'Immediate' ],
      'sparc': [ 'mov' ],
      'modified': 1
   },
   {
      'name': 'storeret',
      'sources': [ 'Register' ],
      'dest': [ ],
      'sparc': [ 'mov' ],
      'modified': 1
   },

# Invocation (Casting spells, raising demons)

   {
      'name': 'call',
      'sources': [ 'Label' ],
      'dest': [ ],
      'sparc': [ 'call', 'nop' ],
   },
   {
      'name': 'ret',
      'sources': [ ],
      'dest': [ ],
      'sparc': [ 'ret', 'restore' ],
   },

# Allocation (Too serious to joke about)

   {
      'name': 'new',
      'sources': [ 'StructIdentifier' ],
      'dest': [ 'Register' ],
      'sparc': ['mov', 'call', 'nop', 'mov'],
      'modified': 1
   },
   {
      'name': 'del',
      'sources': [ 'Register' ],
      'dest': [ ],
      'sparc': [ 'mov', 'call', 'nop' ],
      'modified': 1
   },

# I/0 (That's a planet right?)

   {
      'name': 'print',
      'sources': [ 'Register' ],
      'dest': [ ],
      'sparc': [ 'set', 'mov', 'call', 'nop' ],
      'modified': 1,
   },
   {
      'name': 'println',
      'sources': [ 'Register' ],
      'dest': [ ],
      'sparc': [ 'set', 'mov', 'call', 'nop' ],
      'modified': 1,
   },
   {
      'name': 'read',
      'sources': [ ],
      'dest': ['Register'],
      'sparc': [ 'set', 'or', 'mov', 'call', 'nop' ],
      'modified': 1,
   },

# Moves (for the dance floor)

   {
      'name': 'mov',
      'sources': [ 'Register' ],
      'dest': [ 'Register' ],
      'sparc': [ 'mov' ],
   },
   {
      'name': 'moveq',
      'sources': [ 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': [ 'move' ],
   },
   {
      'name': 'movge',
      'sources': [ 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': [ 'movge' ],
   },
   {
      'name': 'movgt',
      'sources': [ 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': [ 'movg' ],
   },
   {
      'name': 'movle',
      'sources': [ 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': [ 'movle' ],
   },
   {
      'name': 'movlt',
      'sources': [ 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': [ 'movl' ],
   },
   {
      'name': 'movne',
      'sources': [ 'Immediate' ],
      'dest': [ 'Register' ],
      'sparc': [ 'movne' ],
   },
]

# Templates
iloc_txt = """import java.util.*;
import java.lang.*;

/**
 * Generated automatically by generate_instructions.py.
 */
public class %(classname)s extends Instruction {
   public static Integer operandCount = %(count)d;
   public %(classname)s() {
      super();%(sparc)s
   }

   public String toString() { return this.toILOC(); }

   public String toILOC() {
      String classPattern = new String("%(pattern)s");
      String[] pattern = classPattern.split(" ");
      String ret = "%(instr)s ";
      int operandCount = this.getOperands().size();

      if ((operandCount != 0) && (operandCount != pattern.length)) {
         Evil.error(ret + ": Found " + operandCount + " operands, ILOC expecting " + pattern.length);
      }

      for (Operand r : this.getOperands()) {
         if (!r.toString().equals(""))
            ret = ret + r.toILOC() + ", ";
      }

      ret = ret.trim();
      if (ret.lastIndexOf(",") == ret.length()-1)
         ret = ret.substring(0, ret.length()-1);

      for (int i = 0; i < this.getOperands().size(); i++) {
         Operand o = this.getOperands().get(i);
         String oper = "null";

         if (o != null) { oper = o.getClass().getName(); }

         if (!oper.equals(pattern[i])) {
            Evil.error(ret + ": ILOC expecting " + classPattern + ". Found " + oper);
         }
      }

      return ret;
   }
}
"""

sparc_txt = """import java.util.*;
import java.lang.*;

/**
 * Generated automatically by generate_instructions.py.
 */
public class %(classname)s extends Sparc {
   public String toString() {
      String ret = "%(instr)s ";

      for (Operand r : this.getOperands()) {
         if (!r.toString().equals(""))
            ret = ret + r.toSparc() + ", ";
      }

      ret = ret.trim();
      if (ret.lastIndexOf(",") == ret.length()-1)
         ret = ret.substring(0, ret.length()-1);

      return ret;
   }
}
"""

# Now that the instructions are defined, apply them to the template.
for instr in instructions:
   classname = instr['name'].capitalize() + "Instruction"
   filename = "src/" + classname + ".java"
   data = instr['sources'] + instr['dest']

   def s(x): return "sparcs.add(\"" + x+ "\");"
   def f(x,y): return x + y

   data = {
      'date': datetime.now().isoformat(' '),
      'classname': classname,
      'instr': instr['name'],
      'pattern': ' '.join(data),
      'count': len(data),
      'sparc': reduce(f, map(s, instr['sparc']), ""),
   }

   # Take the data we built, and apply it to the template.
   txt = iloc_txt % data

   # Writing disabled if data["modified"]
   if "modified" not in instr:
      f = open(filename, 'w')
      f.write(txt)
      f.close()

   for sparc in instr['sparc']:
      classname = sparc.capitalize() + "Sparc"
      filename = "src/" + classname + ".java"

      sparc_data = {
         'date': datetime.now().isoformat(' '),
         'classname': classname,
         'instr': sparc
      }

      txt = sparc_txt % sparc_data

      f = open(filename, 'w')
      f.write(txt)
      f.close()
