#include "SpaceCraft.h"

// Constructor
SpaceCraft::SpaceCraft(float mass, float fuelcapacity, float thrust){
	Mass = mass;			//kg
	FuelCapacity = fuelcapacity;	//kg
	Thrust = thrust;		//kg/N
}

float SpaceCraft::Burn(float time){
	float delta_v;
	float accel;

	accel = Mass/Thrust;
	delta_v = accel * time;

	return delta_v;
}
