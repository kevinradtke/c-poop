const test: string = `temp7
[21, 'GOTOF', 'temp8', '', '']
[21, 'GOTOF', 'temp8', '', '']
Compiling successful!

____ Input: tests/test1.txt ____

____ Function Table ____
{ 'global': { 'pos': 0,
              'temps': {},
              'type': 'void',
              'vars': { 'cinco': {'addr': 4000, 'type': 'bool', 'value': True},
                        'cuatro': {'addr': 2000, 'type': 'float', 'value': 4.0},
                        'dos': {'addr': 1001, 'type': 'int', 'value': 2},
                        'seis': {'addr': 4001, 'type': 'bool', 'value': False},
                        'tres': {'addr': 1002, 'type': 'int', 'value': 0},
                        'uno': {'addr': 1000, 'type': 'int', 'value': 0}}},
  'main': { 'pos': 17,
            'temps': { 'temp10': {'addr': 9997, 'type': 'int'},
                       'temp11': {'addr': 12998, 'type': 'bool'},
                       'temp12': {'addr': 9996, 'type': 'int'},
                       'temp6': {'addr': 10999, 'type': 'float'},
                       'temp7': {'addr': 9999, 'type': 'int'},
                       'temp8': {'addr': 12999, 'type': 'bool'},
                       'temp9': {'addr': 9998, 'type': 'int'}},
            'type': 'void',
            'vars': {'loc': {'addr': 11000, 'type': 'string', 'value': 'uwu'}}},
  'test': {'pos': 2, 'temps': {}, 'type': 'void', 'vars': {}},
  'test2': { 'pos': 3,
             'temps': { 'temp1': {'addr': 9999, 'type': 'int'},
                        'temp2': {'addr': 9998, 'type': 'int'},
                        'temp3': {'addr': 12999, 'type': 'bool'},
                        'temp4': {'addr': 9997, 'type': 'int'},
                        'temp5': {'addr': 9996, 'type': 'int'}},
             'type': 'int',
             'vars': { 'haha': {'addr': 10000, 'type': 'float', 'value': 0.0},
                       'number': {'addr': 9000, 'type': 'int', 'value': 0},
                       'ocho': {'addr': 9002, 'type': 'int', 'value': 8},
                       'poop': {'addr': 12000, 'type': 'bool', 'value': True},
                       'siete': {'addr': 9001, 'type': 'int', 'value': 0},
                       'word': {'addr': 11000, 'type': 'string', 'value': ''}}},
  'test3': { 'pos': 16,
             'temps': {},
             'type': 'int',
             'vars': { 'iNumber': {'addr': 9000, 'type': 'int', 'value': 0},
                       'nueve': { 'addr': 11000,
                                  'type': 'string',
                                  'value': ''}}}}

____ Quadruples Names ____
--  -------  ------  ----  ----------
 1  GOTO                   17
 2  PRINT                  Hola
 3  +        uno     dos   temp1
 4  EQUAL    temp1         uno
 5  +        uno     dos   temp2
 6  <        temp2   tres  temp3
 7  GOTOF    temp3         11
 8  +        uno     uno   temp4
 9  EQUAL    temp4         dos
10  GOTO                   13
11  +        dos     dos   temp5
12  EQUAL    temp5         uno
13  PRINT                  uno
14  PRINT                  dos
15  PRINT                  tres
16  PRINT                  nueve
17  +        5       5.0   temp6
18  PRINT                  temp6
19  EQUAL    4             temp7
20  >        temp7   0     temp8
21  GOTOF    temp8         26
22  PRINT                  666
23  -        temp7   1     temp9
24  EQUAL    temp9         temp7
25  GOTO                   20
26  PRINT                  dos
27  +        dos     1     temp10
28  >=       temp10  0     temp11
29  GOTOF    temp11        34
30  PRINT                  dos
31  -        dos     1     temp12
32  EQUAL    temp12        dos
33  GOTO                   27
34  PRINT                  Last line!
35  ENDPROG
--  -------  ------  ----  ----------

____ Quadruples Addresses ____
--  -------  -----  ----  -----
 1  GOTO                  17
 2  PRINT                 7000
 3  +        1000   1001  9999
 4  EQUAL    9999         1000
 5  +        1000   1001  9998
 6  <        9998   1002  12999
 7  GOTOF    12999        11
 8  +        1000   1000  9997
 9  EQUAL    9997         1001
10  GOTO                  13
11  +        1001   1001  9996
12  EQUAL    9996         1000
13  PRINT                 1000
14  PRINT                 1001
15  PRINT                 1002
16  PRINT                 11000
17  +        5002   6001  10999
18  PRINT                 10999
19  EQUAL    5004         9999
20  >        9999   5005  12999
21  GOTOF    12999        26
22  PRINT                 5006
23  -        9999   5007  9998
24  EQUAL    9998         9999
25  GOTO                  20
26  PRINT                 1001
27  +        1001   5008  9997
28  >=       9997   5009  12998
29  GOTOF    12998        34
30  PRINT                 1001
31  -        1001   5010  9996
32  EQUAL    9996         1001
33  GOTO                  27
34  PRINT                 7002
35  ENDPROG
--  -------  -----  ----  -----

____ Constant Table ____
----------  ------  ----
2           int     5000
4.0         float   6000
True        bool    8000
False       bool    8001
Hola        string  7000
8           int     5001
uwu         string  7001
5           int     5002
5.0         float   6001
10          int     5003
4           int     5004
0           int     5005
666         int     5006
1           int     5007
1           int     5008
0           int     5009
1           int     5010
Last line!  string  7002
----------  ------  ----

EXECUTION BEGIN

10.0
666
666
666
666
2
2
1
0
-1
Last line!

EXECUTION COMPLETE`;

export default test;
