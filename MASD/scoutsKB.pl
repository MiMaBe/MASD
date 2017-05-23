:- dynamic followingPath/1,
	currentLocation/1,
	allowedToMove/2,
	newGarbage/1,
	notifyNewGarbage/1,
	scoutId/1,
	ready/1,
	checkedSurroundings/1.
edge(10,11).
edge(10,18).
edge(10,9).
edge(100,101).
edge(100,92).
edge(100,99).
edge(101,100).
edge(101,102).
edge(101,93).
edge(102,101).
edge(102,94).
edge(11,10).
edge(11,12).
edge(11,19).
edge(12,11).
edge(12,13).
edge(12,20).
edge(13,12).
edge(13,14).
edge(13,21).
edge(14,13).
edge(14,22).
edge(17,18).
edge(17,25).
edge(17,9).
edge(18,10).
edge(18,17).
edge(18,19).
edge(18,26).
edge(19,11).
edge(19,18).
edge(19,20).
edge(20,12).
edge(20,19).
edge(20,21).
edge(21,13).
edge(21,20).
edge(21,22).
edge(21,29).
edge(22,14).
edge(22,21).
edge(22,30).
edge(25,17).
edge(25,26).
edge(25,33).
edge(26,18).
edge(26,25).
edge(26,34).
edge(29,21).
edge(29,30).
edge(29,37).
edge(30,22).
edge(30,29).
edge(30,38).
edge(33,25).
edge(33,34).
edge(33,41).
edge(34,26).
edge(34,33).
edge(34,42).
edge(37,29).
edge(37,38).
edge(37,45).
edge(38,30).
edge(38,37).
edge(38,46).
edge(41,33).
edge(41,42).
edge(41,49).
edge(42,34).
edge(42,41).
edge(42,50).
edge(45,37).
edge(45,46).
edge(45,53).
edge(46,38).
edge(46,45).
edge(46,54).
edge(49,41).
edge(49,50).
edge(49,57).
edge(50,42).
edge(50,49).
edge(50,58).
edge(53,45).
edge(53,54).
edge(53,61).
edge(54,46).
edge(54,53).
edge(54,62).
edge(57,49).
edge(57,58).
edge(57,65).
edge(58,50).
edge(58,57).
edge(58,66).
edge(61,53).
edge(61,62).
edge(61,69).
edge(62,54).
edge(62,61).
edge(62,70).
edge(65,57).
edge(65,66).
edge(65,73).
edge(66,58).
edge(66,65).
edge(66,74).
edge(69,61).
edge(69,70).
edge(69,77).
edge(70,62).
edge(70,69).
edge(70,78).
edge(73,65).
edge(73,74).
edge(73,81).
edge(74,66).
edge(74,73).
edge(74,82).
edge(77,69).
edge(77,78).
edge(77,85).
edge(78,70).
edge(78,77).
edge(78,86).
edge(81,73).
edge(81,82).
edge(81,89).
edge(82,74).
edge(82,81).
edge(82,90).
edge(85,77).
edge(85,86).
edge(85,93).
edge(86,78).
edge(86,85).
edge(86,94).
edge(89,81).
edge(89,90).
edge(89,97).
edge(9,10).
edge(9,17).
edge(90,82).
edge(90,89).
edge(90,91).
edge(90,98).
edge(91,90).
edge(91,92).
edge(91,99).
edge(92,100).
edge(92,91).
edge(92,93).
edge(93,101).
edge(93,85).
edge(93,92).
edge(93,94).
edge(94,102).
edge(94,86).
edge(94,93).
edge(97,89).
edge(97,98).
edge(98,90).
edge(98,97).
edge(98,99).
edge(99,100).
edge(99,91).
edge(99,98).
path(9,17,1).
path(17,25,1).
path(25,33,1).
path(33,41,1).
path(41,49,1).
path(49,57,1).
path(57,65,1).
path(65,73,1).
path(73,81,1).
path(81,89,1).
path(89,97,1).
path(97,98,1).
path(98,99,1).
path(99,100,1).
path(100,92,1).
path(92,91,1).
path(91,90,1).
path(90,82,1).
path(82,74,1).
path(74,66,1).
path(66,58,1).
path(58,50,1).
path(50,42,1).
path(42,34,1).
path(34,26,1).
path(26,18,1).
path(18,10,1).
path(10,9,1).
path(11,12,2).
path(12,13,2).
path(13,14,2).
path(14,22,2).
path(22,30,2).
path(30,38,2).
path(38,46,2).
path(46,54,2).
path(54,62,2).
path(62,70,2).
path(70,78,2).
path(78,86,2).
path(86,94,2).
path(94,102,2).
path(102,101,2).
path(101,93,2).
path(93,85,2).
path(85,77,2).
path(77,69,2).
path(69,61,2).
path(61,53,2).
path(53,45,2).
path(45,37,2).
path(37,29,2).
path(29,21,2).
path(21,20,2).
path(20,19,2).
