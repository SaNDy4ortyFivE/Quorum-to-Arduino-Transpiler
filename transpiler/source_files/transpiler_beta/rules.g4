grammar rules;

/*
Parser rules
*/

stmt  : (line (EOF | '\n'))+;

line  : (v_init | conditional | output | other | END);

v_init  : (decl | assign | both);

decl  : d_type VARIABLE;

assign  : VARIABLE EQUAL ( NUMB | FLOAT );

both  : d_type VARIABLE EQUAL ( NUMB | FLOAT );

d_type  : (INTEGER|NUMBER);

conditional   : (r_if | r_elif | ELSE);

r_if  :  IF (VARIABLE | NUMB | FLOAT) relation (VARIABLE | NUMB | FLOAT);

r_elif  : ELSEIF (VARIABLE | NUMB | FLOAT) relation (VARIABLE | NUMB | FLOAT);

relation  : (GREATER | LESS | EQUAL);

output  : OUTPUT (VARIABLE)+;

other   : (use | class_ | action | inst | funcall);

use   : USE lib;

inst   : lib VARIABLE;

lib   : LED;

class_   : CLASS_KEY VARIABLE;

action  : ACTION ACTION_MAIN '(' ')';

funcall : VARIABLE ':' funs;

funs    : (led_related);

led_related     : (LED_ON | LED_OFF | LED_PIN);

/*
Lexer rules
*/

fragment A  : 'a';

fragment AA : 'A';

fragment B  : 'b';

fragment BB : 'B';

fragment C  : 'c';

fragment CC : 'C';

fragment D  : 'd';

fragment DD : 'D';

fragment E  : 'e';

fragment EE : 'E';

fragment F  : 'f';

fragment FF : 'F';

fragment G  : 'g';

fragment GG : 'G';

fragment H  : 'h';

fragment HH : 'H';

fragment I  : 'i';

fragment II : 'I';

fragment J  : 'j';

fragment JJ : 'J';

fragment K  : 'k';

fragment KK : 'K';

fragment L  : 'l';

fragment LL : 'L';

fragment M  : 'm';

fragment MM : 'M';

fragment N  : 'n';

fragment NN : 'N';

fragment O  : 'o';

fragment OO : 'O';

fragment P  : 'p';

fragment PP : 'P';

fragment Q  : 'q';

fragment QQ : 'Q';

fragment R  : 'r';

fragment RR : 'R';

fragment S  : 's';

fragment SS : 'S';

fragment T  : 't';

fragment TT : 'T';

fragment U  : 'u';

fragment UU : 'U';

fragment V  : 'v';

fragment VV : 'V';

fragment W  : 'w';

fragment WW : 'W';

fragment X  : 'x';

fragment XX : 'X';

fragment Y  : 'y';

fragment YY : 'Y';

fragment Z  : 'z';

fragment ZZ : 'Z';

fragment LOWER  : [a-z];

fragment UPPER  : [A-Z];

fragment NUM  : [0-9];

INTEGER   : I N T E G E R;

NUMBER  : N U M B E R;

OUTPUT  : O U T P U T;

/*
conditional keywords
*/

IF  : I F;

ELSE  : E L S E;

ELSEIF : E L S E I F;

END   : E N D;

/*
relational operators
*/

EQUAL   : '=';

GREATER   : '>';

LESS   : '<';

/*
datatypes keywords
*/

NUMB   : (NUM)+;

FLOAT   : (NUM)+ '.' (NUM)+;

/*
OOP keywords
*/

USE     : U S E;

ACTION  : A C T I O N;

CLASS_KEY      : C L A S S;

ACTION_MAIN     : MM A I N;

/*
led related keywords
*/

LED   : LL EE DD;

LED_ON : OO NN '(' ')';

LED_OFF : OO FF FF '(' ')';

LED_PIN : P I N '(' (NUM)+ ')';

VARIABLE  : (LOWER | UPPER)+;

TEXT  : {self._input.LA(-1) == ord('[') or self._input.LA(-1) == ord('(')}? ~[\])]+ ;

WHITESPACE  : (' ' | '\t')+ -> skip;

NEWLINE  : ('\r'? '\n' | '\r')+ ;
