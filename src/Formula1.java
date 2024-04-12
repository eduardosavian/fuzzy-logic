import net.sourceforge.jFuzzyLogic.FIS;
import net.sourceforge.jFuzzyLogic.FunctionBlock;

public class Formula1 {

    public static void main(String[] args) {
        // Check if the correct number of arguments is provided
        if (args.length != 5) {
            System.err.println("Usage: java Formula1 <file> <fuel_level> <race_position> <race_progress> <tire_condition>");
            System.exit(1);
        }

        // Load the FCL file
        String filename = args[0];
        FIS fis = FIS.load(filename, true);
        if (fis == null) {
            System.err.println("Cannot load file: '" + filename + "'");
            System.exit(1);
        }

        // Get default function block
        FunctionBlock fb = fis.getFunctionBlock("formula1");

        // Set input variables
        fb.setVariable("fuel_level", Double.parseDouble(args[1]));
        fb.setVariable("race_position", Double.parseDouble(args[2]));
        fb.setVariable("race_progress", Double.parseDouble(args[3]));
        fb.setVariable("tire_condition", Double.parseDouble(args[4]));

        // Evaluate
        fb.evaluate();

        // Get output variable
        double pitstop_necessity = fb.getVariable("pitstop_necessity").getValue();

        // Output the result
        System.out.println("\nPitstop necessity: " + pitstop_necessity);
    }
}
