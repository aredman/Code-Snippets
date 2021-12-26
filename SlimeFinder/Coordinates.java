public class Coordinates{
	int x;
	int y;
	int z;

	public Coordinates(int x, int y, int z){
		this.x = x;
		this.y = y;
		this.z = z;
	}
	public void setx(int x){
		this.x = x;
	}
	public void sety(int y){
		this.y = y;
	}

	public void setz(int z){
		this.z = z;
	}

	@Override
	public String toString(){
		return "("+x+","+y+","+z+")";
	}
}
