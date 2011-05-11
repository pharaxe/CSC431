import java.util.*;
import java.lang.*;

public abstract class Instruction {
   public static Integer operandCount = 0;
   private ArrayList<Operand> operands = new ArrayList<Operand>();
   private ArrayList<Register> dests = new ArrayList<Register>();
   ArrayList<String> sparcs = new ArrayList<String>();

   public String toString() {
      return "NULL INSTRUCTION.";
   }

   public String toILOC() {
      return "noop";
   }

   public ArrayList<Register> getSources() {
      ArrayList<Register> ret = new ArrayList<Register>();

      for (Operand o : this.operands) {
         if (o instanceof Register)
            ret.add((Register)o);
      }

      return ret;
   }

   public ArrayList<Sparc> toSparc() {
      ArrayList<Sparc> instructions = new ArrayList<Sparc>();
      String ret = "";

      for (String instr : this.sparcs) {
         String cap = instr.toUpperCase();
         instr = cap.substring(0,1) + instr.substring(1) + "Sparc";

         try {
            Class cls = Class.forName(instr);
            Sparc i = (Sparc)cls.newInstance();
            instructions.add(i);
         } catch (Exception e) {
            Evil.error("You're doing it wrong: " + e.getMessage());
         }
      }

      return instructions;
   }

   public ArrayList<Register> getDestinations() {
      return new ArrayList<Register>(this.dests);
   }

   public ArrayList<Operand> getOperands() {
      ArrayList<Operand> ret = new ArrayList<Operand>();
      ret.addAll(this.operands);
      ret.addAll(this.dests);

      return ret;
   }

   void addSource(Operand in) {
      this.operands.add(in);
   }

   public void addLabel(Label in) {
      this.addSource(in);
   }

   public void addLabel(String in) {
      this.addLabel(new Label(in));
   }

   public void addID(String in) {
      this.addSource(new ID(in));
   }

   public void addField(Field in) {
      this.addSource(in);
   }

   public void addRegister(Register in) {
      this.addSource(in);
   }

   public void addDest(Register in) {
      this.dests.add(in);
   }

   public void addImmediate(Immediate in) {
      this.addSource(in);
   }

   public void addImmediate(Integer in) {
      this.addSource(new Immediate(in));
   }
}
