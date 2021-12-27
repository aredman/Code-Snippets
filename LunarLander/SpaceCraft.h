#ifndef SpaceCraft_H
#define SpaceCraft_H

class SpaceCraft
{
protected:
	float Mass;
	float FuelCapacity;
	float Thrust;

	float velocity;
	float height;

public:
	// Constructor
	SpaceCraft(float mass, float fuelcapacity, float thrust);

	// Setters/Getters
	float setHeight(float h);
	float getHeight(){ return height; }

	float setVelocity(float v);
	float getVelocity(){ return velocity; }

	float Burn(float time);
};

#endif
