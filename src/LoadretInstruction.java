import java.util.*;
import java.lang.*;

/**
 * Generated automatically by generate_instructions.py.
 */
public class LoadretInstruction extends Instruction {
   public static Integer operandCount = 1;
   public LoadretInstruction() {
      super();sparcs.add("mov");
   }

   public String toString() { return this.toILOC(); }

   public ArrayList<Sparc> toSparc() {
      ArrayList<Sparc> instructions = new ArrayList<Sparc>();
      Sparc i;

      i = new MovSparc();
      i.addOp(new Register("%o0"));
      i.addOp(this.getOperands().get(0));

      instructions.add(i);
      return instructions;
   }

   public String toILOC() {
      String classPattern = new String("Register");
      String[] pattern = classPattern.split(" ");
      String ret = "loadret ";
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
