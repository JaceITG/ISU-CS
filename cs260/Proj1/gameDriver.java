/* Jace Williams
 * cs26017
 * Driver for 4 games
 */

import java.util.Scanner;
public class gameDriver {

	public static void main(String[] args) {
		
		Scanner s = new Scanner(System.in);
		boolean playing = true;
		while (playing) {	

			System.out.println("Enter 1 to play HiLo.");
			System.out.println("Enter 2 to play Three Card Monte.");
			System.out.println("Enter 3 to practice Addition facts between 0-20.");
			System.out.println("Enter 4 to play The Game of Nim.");
			System.out.println("Enter -1 to exit the game player.");
			String choice = s.nextLine();
	
			parseGameChoice(choice);
			System.out.println("Play again? (true/false): ");
			playing = s.nextBoolean();
			
		}
		s.close();
	}
	
	private static void parseGameChoice(String choice) {
		switch (choice) {
			case "1":{
				//Play HiLo
				Games.hilo();
				break;
			}
			case "2":{
				//Play 3 Card Monte
				break;
			}
			case "3":{
				//Addition facts
				break;
			}
			case "4":{
				//Play Nim
				break;
			}
			case "-1":{
				//Exit menu
				System.out.println("Exiting");
				break;
			}
			default:{
				break;
			}
		}
	}

}
