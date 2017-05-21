
shortestPath(X,Y,P,L) :- shortest(X,Y,P,L).

shortestPath(X,Y,P,L) :- 
	shortest(Y,X,Pr,L), 
	reverse(Pr,P).

shortestPathToRC(Init,Path,Length) :-
	setof([P,L],pathToRC(Init,P,L),Set),
	Set = [_|_], % fail if empty
	minimal(Set,[Path,Length]).

pathToRC(Init,Path,Length) :- 
	recyclingCenter(X),
	accessTo(Dest,X),
	shortestPath(Init,Dest,Path,Length).

minimal([F|R],M) :- min(R,F,M).

% minimal path
min([],M,M).
min([[P,L]|R],[_,M],Min) :- L < M, !, min(R,[P,L],Min). 
min([_|R],M,Min) :- min(R,M,Min).

