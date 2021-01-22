/*	Jace, Ben, Kevin
 * 	cs26017, cs26009, cs26011
 *
 *  Remove all zeros in file and add them to end
 */

import java.io.*;
import java.util.Scanner;
public class Compact {

	public static void main(String[] args) {
		Scanner init = new Scanner(System.in);
		System.out.println("\"1\" for Array, \"2\" for ArrayList");
		//Get choice of method to use
		String choice = init.nextLine();

		//Parse chosen method
		switch (choice){
			case "1":{
				withArray();
				break;
			}
			case "2":{
				withArrList();
				break;
			}
			default:{
				System.out.println("Invalid choice");
			}
		}
		init.close();
	}

	//Compact the array with normal Array
	private static void withArray(){
		try {
			File f = new File("/u1/class/cs26017/Downloads/arrays.txt");
			Scanner s = new Scanner(f);

			//Find how many ints in file
			int arraySize = 0;
			while(s.hasNext()) {
				s.nextInt();
				arraySize +=1;
			}
			s.close();
			Scanner myscan = new Scanner(f);

			//Create Array the size of num of ints in file
			int[] arr = new int[arraySize];

			//Scan file and add ints to array
			int index = 0;
			while(myscan.hasNext()) {
				int num = myscan.nextInt();
				arr[index]  = num;
				index++;
			}
			myscan.close();

			//Loop over each index in Array
			int count = 0;
			for(int i =0; i<arr.length-count;i++) {
				//If encounter zero
				if(arr[i] == 0) {
					//Move all the indices down to overwrite 0 here
					move(arr,i,count);
					count++;
				}
			}

			//Print array values
			for(int i =0; i<arr.length;i++) {
				System.out.println(arr[i]);
			}

			System.out.println("Zeros compacted: "+count);
		}
		catch(Exception e) {
			System.out.println(e.getMessage());
		}
	}

	//Compact the array using an ArrayList
	private static void withArrList(){
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
	//Loop past this index replacing i with i+1, until hit zeros stored at end
	private static void move(int[] arr, int index, int zerosAtEnd) {
		for(int i = index; i<arr.length-zerosAtEnd; i++) {
			if(i == arr.length-zerosAtEnd-1) {
				arr[i] = 0;
			}else {
				arr[i] = arr[i+1];
			}
		}
	}

}
