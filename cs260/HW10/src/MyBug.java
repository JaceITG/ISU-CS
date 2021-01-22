/* Jace Williams
 * cs26017
 * Class for a bug to be placed and moved on a grid
 * 
 */

import info.gridworld.actor.Bug;
import java.awt.Color;
import java.util.Random;

public class MyBug extends Bug{
	private Random rand = new Random();
    /**
     * Constructs a bug which runs through a maze
     * @param color of the bug
     */
    public MyBug(Color color)
    {
    	setColor(color);
    }

    /**
     * moves to the next location of the square.
     */
    public void act()
    {
        if (canMove())
        {	
            move();
        }
        else
        {
        	//Find which direction is open
        	boolean rightClear;
        	boolean leftClear;
        	
        	//Check right hand side
        	turn();
        	turn();
        	rightClear = canMove();
        	
        	//Turn around and check left side
        	for(int i = 0; i<4; i++) {
        		turn();
        	}
        	leftClear = canMove();
        	//Reorient
        	turn();
        	turn();
        	
        	if(rightClear && leftClear) {
        		//Choose randomly which direction to go in
        		if(rand.nextBoolean()) {
        			//Turn left (270 degree turn)
        			for(int i = 0; i<6; i++) {
                		turn();
                	}
        		}else {
        			//Turn right
        			turn();
        			turn();
        		}
        	}else if(rightClear) {
        		turn();
        		turn();
        	}else if(leftClear) {
        		for(int i = 0; i<6; i++) {
            		turn();
            	}
        	}else {
        		//No path clear, turn around
        		for(int i = 0; i<4; i++) {
            		turn();
            	}
        	}
        	
        }
    }
}
