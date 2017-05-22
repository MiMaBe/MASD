:- dynamic newGarbage/1.

nCols(12).
colsXrows(180).
roadCell(101).
roadCell(102).
roadCell(105).
roadCell(106).
roadCell(109).
roadCell(110).
roadCell(113).
roadCell(114).
roadCell(117).
roadCell(118).
roadCell(121).
roadCell(122).
roadCell(125).
roadCell(126).
roadCell(129).
roadCell(13).
roadCell(130).
roadCell(133).
roadCell(134).
roadCell(137).
roadCell(138).
roadCell(14).
roadCell(141).
roadCell(142).
roadCell(145).
roadCell(146).
roadCell(147).
roadCell(148).
roadCell(149).
roadCell(15).
roadCell(150).
roadCell(153).
roadCell(154).
roadCell(157).
roadCell(158).
roadCell(159).
roadCell(16).
roadCell(160).
roadCell(161).
roadCell(162).
roadCell(165).
roadCell(166).
roadCell(17).
roadCell(18).
roadCell(19).
roadCell(20).
roadCell(21).
roadCell(22).
roadCell(25).
roadCell(26).
roadCell(27).
roadCell(28).
roadCell(29).
roadCell(30).
roadCell(31).
roadCell(32).
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
roadCell(67).
roadCell(68).
roadCell(69).
roadCell(70).
roadCell(73).
roadCell(74).
roadCell(77).
roadCell(78).
roadCell(79).
roadCell(80).
roadCell(81).
roadCell(82).
roadCell(85).
roadCell(86).
roadCell(89).
roadCell(90).
roadCell(93).
roadCell(94).
roadCell(97).
roadCell(98).

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

