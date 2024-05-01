import java.util.Scanner;
import java.text.DecimalFormat;
import java.math.RoundingMode;


public class BMI_Pounds {
   private static DecimalFormat df = new DecimalFormat("0.00"); // Rounds double/float value to 2 decimal points

   public static void main(String[] args) {
	  double weight, height, BMI;

      Scanner keyboard = new Scanner(System.in); // Your keyboard inputs

      System.out.println("BMI Standards:");
      System.out.println("Underweight: less than 18.5");
      System.out.println("Normal: between 18.5 and 24.9");
      System.out.println("Overweight: between 25 and 29.9");
      System.out.println("Obese: 30 or greater \n");

      System.out.print("Input weight in pounds: ");
      weight = keyboard.nextDouble(); // input for weight

      System.out.print("Input height in inches: ");
      height = keyboard.nextDouble(); // input for height

      BMI = weight * 0.45359237 / (height *0.0254 * height * 0.0254); // Turns kilometers to pounds and meters to inches
      System.out.println("You weight is " + weight + " pounds and you are " + height + " inches tall");
      System.out.println("Your Body Mass Index (BMI) is " + df.format(BMI) + " " );


		// Statements checks the BMI total and chooses the correct statement to print

		if (BMI <= 18.5) {
			System.out.println("You are considered underweight");
		}
		else if (BMI <= 24.9) {
			System.out.println("You weight is normal");
		}
		else if (BMI <= 29.9) {
			System.out.println("You are considered overweight");
		}
		else {
			System.out.println("You are considered obese");
		}
  	}
}