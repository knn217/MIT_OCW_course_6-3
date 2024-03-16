#include <stdio.h>

char GRADE_MAP[] = { 'F', 'F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'A'};

class Grade
{
private:
    char letter;
    int percent;
public:
    void setByPercent(int p);
    void setByLetter(char l);
    void print();
};

void Grade::setByPercent(int p)
{
    percent = p;
    letter = GRADE_MAP[p / 10];
}

void Grade::setByLetter(char l){
    letter = l;
    percent = 100 - (l - 'A') * 10 - 5;
}

void Grade::print(){
    printf("Grade: %d: %c\n", percent, letter);
}

int main() {
	Grade g;
	int percent;
	
	printf("Enter two grades separated by a space. Use a percentage for the first and letter for the second: ");
	scanf("%d", &percent);
	scanf("\n");
	
	g.setByPercent(percent);
	g.print();
	
	g.setByLetter(getchar());
	g.print();

	return 0;
}