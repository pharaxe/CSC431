#!/usr/bin/env python
#
# Instruction generator.
# @author Nat Welch
#
# This would be so much easier if I actually knew python or perl.

from datetime import datetime, date, time

instructions = [
   {
      'name': 'add',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
   },
   {
      'name': 'addi',
      'sources': [ 'Immediate', 'Register' ],
      'dest': [ 'Register' ],
   },
   {
      'name': 'div',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
   },
   {
      'name': 'mult',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
   },
   {
      'name': 'sub',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
   },
   {
      'name': 'rsubi',
      'sources': [ 'Immediate', 'Register' ],
      'dest': [ 'Register' ],
   },
   {
      'name': 'and',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
   },
   {
      'name': 'or',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'Register' ],
   },
   {
      'name': 'xori',
      'sources': [ 'Immediate', 'Register' ],
      'dest': [ 'Register' ],
   },
   {
      'name': 'compi',
      'sources': [ 'Immediate', 'Register' ],
      'dest': [ 'ConditionCodeRegister' ],
   },
   {
      'name': 'comp',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'ConditionCodeRegister' ],
   },
   {
      'name': 'comp',
      'sources': [ 'Register', 'Register' ],
      'dest': [ 'ConditionCodeRegister' ],
   },
   {
      'name': 'cbreq',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
   },
   {
      'name': 'cbrge',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
   },
   {
      'name': 'cbrgt',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
   },
   {
      'name': 'cbrle',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
   },
   {
      'name': 'cbrlt',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
   },
   {
      'name': 'cbrne',
      'sources': [ 'ConditionCodeRegister', 'Label', 'Label' ],
      'dest': [ ],
   },
]

# Now that the instructions are defined, apply them to the template.
for instr in instructions:
   classname = instr['name'].capitalize() + "Instruction"
   filename = "src/" + classname + ".java"

   data = {
      'date': datetime.now().isoformat(' '),
      'classname': classname,
      'instr': instr['name'],
   }

   # Take the data we built, and apply it to the template below.
   txt = """
import java.util.*;
import java.lang.*;

/**
 * Generated automatically by generate_instructions.py
 */
public class %(classname)s extends Instruction {
   ArrayList<Operand> sources = new ArrayList<Operand>();
   ArrayList<Operand> dests   = new ArrayList<Operand>();

   public %(classname)s() {
   }

   public String toString() {
      return this.toILOC();
   }

   public void addSource(Operand in) {
      this.sources.add(in);
   }

   public void addDest(Operand in) {
      this.dests.add(in);
   }

   public String toILOC() {
      String ret = "%(instr)s ";
      for (Operand r : sources) {
         ret = ret + r + ", ";
      }

      for (Operand r : dests) {
         ret = ret + r + ", ";
      }

      ret = ret.trim();
      if (ret.lastIndexOf(",") == ret.length()-1)
         ret = ret.substring(0, ret.length()-2);

      return ret;
   }
}
""" % data

   f = open(filename, 'w')
   f.write(txt)
   f.close()
