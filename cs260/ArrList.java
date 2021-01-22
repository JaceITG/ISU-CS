/*	Jace, Ben, Kevin
 * 	cs26017, cs26009, cs26011
 * 
 *  Remove all zeros in file and add them to end
 */

import java.io.*;
import java.util.Scanner;
import java.util.ArrayList;
public class ArrList {
	
	public static void main(String[] args) {
		try {
			File f = new File("/u1/class/cs26017/Downloads/arrays.txt");
			Scanner s = new Scanner(f);
			
			//Add integers in file to ArrayList
			ArrayList<Integer> numbers = new ArrayList<Integer>();
			while(s.hasNext()) {
				numbers.add(s.nextInt());
			}
			
			s.close();
			
			int numZeros = 0;
			int zeroIndex = numbers.indexOf(0);
			//While there is still a zero in arraylist
			while (zeroIndex > -1) {
				//Remove zero at this index and increment number of zeros removed
				numbers.remove(zeroIndex);
				numZeros++;
				zeroIndex = numbers.indexOf(0);	//Find next zero
			}
			
			//Append number of zeros removed to end of arraylist
			for(int i = 0; i<numZeros; i++) {
				numbers.add(0);
			}
			
			//Print arraylist
			for(Integer i:numbers) {
				System.out.println(i);
			}
			System.out.println("Zeros compacted: "+numZeros);
		}catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}

}
