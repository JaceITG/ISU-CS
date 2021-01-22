/* Jace Williams
 * cs26017
 * methods to run 4 games
 */
import java.util.Random;
import java.util.Scanner;
public class Games {
	static Scanner s = new Scanner(System.in);
	
	/* Play Hi/Lo game
	 * Get a random number between 1-100
	 * User has 7 guesses to get the number right
	 * On each guess, tell if it was too high or too low
	 */
	public static void hilo() {
		Random rand = new Random();
		int number = rand.nextInt(100) + 1;
		int guesses = 0;
		
		System.out.println("I'm thinking of a number between 1-100. " +
		                   "You have 7 guesses.");
		
		while (guesses<7){
			System.out.print("Guess #"+(guesses+1)+": ");
			int guess = s.nextInt();
			
			if(guess == number) {
				System.out.println("You guessed it!");
				return;
			}else if (guess<number) {
				System.out.println("Too low");
			}else if (guess>number) {
				System.out.println("Too high");
			}
			guesses++;
		}
		System.out.println("You didn't guess it in 7 tries! The number was "+number);
	}
	
	public static void threeCardMonty() {
		
	}
	
	public static void additionFacts() {
		
	}
	
	public static void gameOfNim() {
		
	}
}
