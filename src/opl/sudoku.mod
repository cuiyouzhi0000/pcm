/*********************************************
 * OPL 12.4 Model
 * Author: jcui
 * Creation Date: 2012-3-11 at ����10:51:30
 *********************************************/
using CP;

dvar int+ s[1..9][1..9] in 1..9;

subject to
{
	s[1][2] == 6;
	s[1][5] == 5;
	s[1][8] == 2;
	
	s[2][4] == 3;
	s[2][8] == 9;
	
	s[3][1] == 7;
	s[3][4] == 6;
	s[3][8] == 1;
	
	s[4][3] == 6;
	s[4][5] == 3;
	s[4][7] == 4;
	
	s[5][3] == 4;
	s[5][5] == 7;
	s[5][7] == 1;
	
	s[6][3] == 5;
	s[6][5] == 9;
	s[6][7] == 8;
	
	s[7][2] == 4;
	s[7][6] == 1;
	s[7][9] == 6;
	
	s[8][2] == 3;
	s[8][6] == 8;
	
	s[9][2] == 2;
	s[9][5] == 4;
	s[9][8] == 5;
	
	forall(i in 1..9)
		allDifferent(all(j in 1..9) s[i][j]);
		
	forall(j in 1..9)
		allDifferent(all(i in 1..9) s[i][j]);
		
	forall(i in 1..3, j in 1..3)
	    allDifferent(all(m in 3*(i-1)+1..3*(i-1)+3, n in 3*(j-1)+1..3*(j-1)+3) s[m][n]);
}