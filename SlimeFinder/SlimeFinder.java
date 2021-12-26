import java.util.Random; 

public class SlimeFinder{
	long seed;

	// Constructor #0 (Random Seed)
	public SlimeFinder(){
		Random random = new Random();
		this.seed = random.nextLong();
		System.out.printf("Random seed assigned: %d %n",seed);
	}

	// Constructor #1 (Given Seed)
	public SlimeFinder(long myseed){ 
		this.seed = myseed;
	} 

	// Update seed after initialization
	public void setSeed(long seed) {
		this.seed = seed;
	}

	// Check for slimes
	public boolean search(Coordinates in){
		int xPosition = in.x;
		int zPosition = in.z;
		Random rnd = new Random(
			this.seed +
			(int) (xPosition * xPosition * 0x4c1906) +
			(int) (xPosition * 0x5ac0db) +
			(int) (zPosition * zPosition) * 0x4307a7L +
			(int) (zPosition * 0x5f24f) ^ 0x3ad8025fL
		);
		return (rnd.nextInt(10) == 0);
	}
}

