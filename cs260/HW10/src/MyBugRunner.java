/* Jace Williams
 * cs26017
 * This class runs a world with 
 * 
 */

import java.awt.Color;
import info.gridworld.actor.ActorWorld;

import info.gridworld.actor.Rock;
import info.gridworld.grid.*;
import java.util.Scanner;

public class MyBugRunner {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		
		ActorWorld world = new ActorWorld();
		MyBug bug1 = new MyBug(Color.BLUE);
        world.add(new Location(0,0), bug1);
        
        System.out.println("Would you like to create a maze world (true) or generate randomly (false)? ");
        boolean mazeGen = s.nextBoolean();
        
        if(mazeGen) {
	       
	        //Create maze in the world
	        boolean gapToRight = true;
	        //Loop over rows
	        for(int i = 0; i<10; i++) {
	        	//Get range of j values we can put rocks in to leave correct gaps
	        	int[] jRange;
	        	if(gapToRight) {
	        		jRange = new int[] {0,1,2,3,4,5,6,7,8};
	        	}else {
	        		jRange = new int[] {1,2,3,4,5,6,7,8,9};
	        	}
	        	
	        	boolean rocksPlaced = false;
	        	//Loop over columns
	        	for(int j = 0; j<10; j++) {
	        		
	        		//If row is odd and j is in range
	        		if(i%2==1 && inArray(jRange,j)) {
	        			rocksPlaced = true;
	        			//Add rock
	        			world.add(new Location(i,j), new Rock());
	        		}
	        	}
	        	if(rocksPlaced) {
	        		rocksPlaced = false;
	        		gapToRight = !gapToRight;
	        	}
	        }
        }else {
        	for(int i=0; i<15;i++) {
	        	world.add(new Rock());
	        }
        }
        
        
        world.show();
		s.close();
	}
	
	//Return if the passed array contains the passed integer
	private static boolean inArray(int[] arr, int integer) {
		for(int elem: arr) {
			if(elem==integer) {
				return true;
			}
		}
		return false;
	}

}
