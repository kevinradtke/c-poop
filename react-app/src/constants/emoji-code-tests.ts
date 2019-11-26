const EMOJI_CODE_TEST: string = `program cpoop💩

main() {
  var 🧶 hello ⬅️ 🔤C Poop Rocks!🔤💩
  🖨(hello)💩
}`;

const EMOJI_TRANSLATED_TEST: string = `program patito;
var  int  uno, dos=2, tres;  float cuatro= 4.0;  bool  cinco =  true , seis =  false ;

 def   void  test(){
   print("Hola"); 
}

 def   int  test2( int  number,  string  word,  bool  poop,  float haha){
  var  int  siete, ocho = 8;
  uno = uno + dos;

  if ( uno + dos < tres){
    dos = uno + uno;
  }
  else{
    uno = dos + dos;
  };

   print(uno, dos, tres);
  return uno;
}

 def   int  test3( int  iNumber){
  var  string  nueve;
   print(nueve);
  return nueve;
}

main() {
  var  string  loc = "uwu";
  test();
   print(5+5.0);
  test2();
  test3(10);
   repeat  4 {
     print(666);
  }
   print(dos);
   while  (dos+1 >= 0) {
     print(dos);
    dos = dos-1;
  }
   print("Last line!");
}`;

export { EMOJI_CODE_TEST, EMOJI_TRANSLATED_TEST };
