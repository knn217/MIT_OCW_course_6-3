#include <iostream>

using namespace std;

class Tool {
protected:
	int strength;
	char type;
public:
	void setStrength(int s){
		strength = s;
	}
	int getStrength(){
		return strength;
	}
	char getType(){
		return type;
	}
};

class Scissors : public Tool {
public:
	Scissors(int s){
		strength = s;
		type = 's';
	}

	bool fight(Tool op){
		if (op.getType() == 'r') return (strength > (op.getStrength()*2));
		else if (op.getType() == 'p') return ((strength*2) > op.getStrength());
		else return (strength > op.getStrength());
	}
};

class Paper : public Tool {
public:
	Paper(int s){
		strength = s;
		type = 'p';
	}

	bool fight(Tool op){
		if (op.getType() == 's') return (strength > (op.getStrength()*2));
		else if (op.getType() == 'r') return ((strength*2) > op.getStrength());
		else return (strength > op.getStrength());
	}
};

class Rock : public Tool {
public:
	Rock(int s){
		strength = s;
		type = 'r';
	}

	bool fight(Tool op){
		if (op.getType() == 'p') return (strength > (op.getStrength()*2));
		else if (op.getType() == 's') return ((strength*2) > op.getStrength());
		else return (strength > op.getStrength());
	}
};

int main() {
	// Example main function
	// You may add your own testing code if you like

	Scissors s1(5);
	Paper p1(7);
	Rock r1(15);
	cout << s1.fight(p1) << p1.fight(s1) << endl;
	cout << p1.fight(r1) << r1.fight(p1) << endl;
	cout << r1.fight(s1) << s1.fight(r1) << endl;

	return 0;
}
