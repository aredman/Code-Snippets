import java.util.ArrayList;

public class main{
	public static void main(String[] args){
		System.out.println("Searcing for slimes");

		// Main world seed
		SlimeFinder mySlimeFinder = new SlimeFinder(-7612515974354822130L);
		Coordinates pos = new Coordinates(6, 1, -8);
		ArrayList<Coordinates> slimeList = new ArrayList<Coordinates>();

		System.out.println(" -----------");
		for(int i = pos.z-3;i<=pos.z+3;i++){
			System.out.printf("|");
			for(int j = pos.x-3;j<=pos.x+3;j++){
				boolean slimeCheck = mySlimeFinder.search(new Coordinates(j,0,i));
				if(slimeCheck){
					slimeList.add(new Coordinates(j,0,i));
					System.out.printf("S");
				}else{
					System.out.printf(" ");
				}
			}
			System.out.printf("|");
			System.out.println();
		}
		System.out.println(" -----------");

		System.out.println(slimeList);
	}
}
