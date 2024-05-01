import java.util.Scanner;

public class Circumfrence_Circle {

	public static void main(String[] args) {

		int radius, diameter;
		double circumference;

		Scanner keyboard = new Scanner(System.in);

		System.out.print("Enter the radius of the circle: ");
		radius = keyboard.nextInt(); // input

		diameter = radius * 2;
		System.out.println("The Diameter is " + diameter);

		System.out.printf( "Area is %f\n", ( Math.PI * radius * radius ) );

		circumference = Math.PI * 2 * radius;
		System.out.println("Circumference of the circle is " + circumference);
	}

}