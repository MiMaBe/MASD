
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

