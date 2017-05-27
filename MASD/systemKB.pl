nCols(8).
colsXrows(112).
roadCell(10).
roadCell(100).
roadCell(101).
roadCell(102).
roadCell(11).
roadCell(12).
roadCell(13).
roadCell(14).
roadCell(17).
roadCell(18).
roadCell(19).
roadCell(20).
roadCell(21).
roadCell(22).
roadCell(25).
roadCell(26).
roadCell(29).
roadCell(30).
roadCell(33).
roadCell(34).
roadCell(37).
roadCell(38).
roadCell(41).
roadCell(42).
roadCell(45).
roadCell(46).
roadCell(49).
roadCell(50).
roadCell(53).
roadCell(54).
roadCell(57).
roadCell(58).
roadCell(61).
roadCell(62).
roadCell(65).
roadCell(66).
roadCell(69).
roadCell(70).
roadCell(73).
roadCell(74).
roadCell(77).
roadCell(78).
roadCell(81).
roadCell(82).
roadCell(85).
roadCell(86).
roadCell(89).
roadCell(9).
roadCell(90).
roadCell(91).
roadCell(92).
roadCell(93).
roadCell(94).
roadCell(97).
roadCell(98).
roadCell(99).
:- dynamic newGarbage/1,
	agentId/1,
	ready/1,
	allAgentsReady/1,
	scoutLocation/1.

generateNewGarbageLoc(Loc) :- 
	colsXrows(Max),
	random(0, Max, Loc),
	\+ roadCell(Loc).

garbageAtReachFrom(X,Y) :- 
	newGarbage(Y),
	surroundings(Y,Surr),
	member(X,Surr). 


foundGarbage(Loc) :- 
	newGarbage(X),
	surroundings(X,Surr),
	roadCell(Loc),
	member(Loc,Surr).

surroundings(X,Set) :- setof(S,surr(X,S),Set).

surr(X,Y) :- nCols(C), Y is X - C - 1, Y >= 0.
surr(X,Y) :- nCols(C), Y is X - C, Y >= 0.
surr(X,Y) :- nCols(C), Y is X - C + 1, Y >= 0.
surr(X,Y) :- Y is X - 1, Y >= 0.
surr(X,Y) :- colsXrows(M), Y is X + 1, Y < M.
surr(X,Y) :- nCols(C), colsXrows(M), Y is X + C - 1, Y < M.
surr(X,Y) :- nCols(C), colsXrows(M), Y is X + C, Y < M.
surr(X,Y) :- nCols(C), colsXrows(M), Y is X + C + 1, Y < M.
