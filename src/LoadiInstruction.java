
import java.util.*;
import java.lang.*;

/**
 * Generated automatically by generate_instructions.py
 */
public class LoadiInstruction extends Instruction {
   public LoadiInstruction() { }

   public String toString() {
      return this.toILOC();
   }

   public String toILOC() {
      String ret = "loadi ";
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
