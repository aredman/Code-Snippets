import random

class suitPower:
    def __init__(self):
        self.power = 100        # Initial power
        self.underpower = 5     # Roll below which no power is used for a critical success
        self.overpower = 96     # "Overpower" situation where power is consumed for a critical failure
        self.burn = 10          # Power usage for an overpower situation
        
        # Counters for number of actions, hits, misses, free usage and failures
        self.actions = 0
        self.hit = 0
        self.free = 0
        self.miss = 0
        self.fail = 0

    # Function to simulate a die roll, defaults to d100
    def die(self, side=100):
        return int(random.random() * side) +1
        
    # Attempt an attack using the stored power level
    def attack(self):
        self.actions +=1
        d = self.die()
        # If the roll is lower power, get a free action
        if(d<=self.underpower):
            self.free +=1
            return "Hit", d, self.power
        # If the roll is high power, burn power with no success
        elif(d>=self.overpower):
            self.power -= self.burn
            self.fail +=1
            return "Miss", d, self.power
        # If the roll is less than your current power level, then succeed and use power
        elif(d<=self.power):
            self.hit +=1
            self.power -= self.burn
            return "Hit", d, self.power
        # If the roll is above your current power level, then fail with no power use
        else:
            self.miss +=1
            return "Miss", d, self.power  
    
    # Return stats 
    def stats(self):
        #print(f"You ran out of power after {self.actions} Actions\nIn that time you received.\nHITS:\t{self.hit}\nMISS:\t{self.miss}\nFREE:\t{self.free}\nFAIL:\t{self.fail}")
        return self.actions, self.hit,self.miss,self.free,self.fail
        
        
if __name__ == "__main__":
    count = 0
    actions = []
    hits = []
    misses = []
    frees = []
    fails = []
    
    # Run test with 100 suits
    while(count < 1e6):
        count += 1
        
        suit1 = suitPower()
        pwr = 1
        while(pwr>0):
            res, rol, pwr = suit1.attack()
            #print(f"[{pwr}%] {res} on {rol}")
        action, hit, miss, free, fail = suit1.stats()
        actions.append(action)
        hits.append(hit)
        misses.append(miss)
        frees.append(free)
        fails.append(fail)
        
    action  = sum(actions)/count
    hit = sum(hits)/count
    miss = sum(misses)/count
    free = sum(frees)/count
    fail = sum(fails)/count
    print(f"After destroying {count} suits, on average you ran out of power after {action} Actions\nIn that time you received.\nHITS:\t{hit}\nMISS:\t{miss}\nFREE:\t{free}\nFAIL:\t{fail}")

        
    
    