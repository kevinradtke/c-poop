const EMOJI_CODE_TEST: string = `program patito💩
var 🔢 uno, dos=2, tres; 🎈 cuatro= 4.0; 💡 cinco = 👍, seis = 👎💩

🚀 📭 test(){
  🖨(🔤Hola🔤)💩
}

🚀 🔢 test2(🔢 number, 🧶 word, 💡 poop, 🎈 haha){
  var 🔢 siete, ocho = 8💩
  uno = uno + dos💩

  if ( uno + dos < tres){
    dos = uno + uno💩
  }
  else{
    uno = dos + dos💩
  }💩

  🖨(uno, dos, tres)💩
  return uno💩
}

🚀 🔢 test3(🔢 iNumber){
  var 🧶 nueve💩
  🖨(nueve)💩
  return nueve💩
}

main() {
  var 🧶 loc = 🔤uwu🔤💩
  test()💩
  🖨(5+5.0)💩
  test2()💩
  test3(10)💩
  🔂 4 {
    🖨(666)💩
  }
  🖨(dos)💩
  🔁 (dos+1 >= 0) {
    🖨(dos)💩
    dos = dos-1💩
  }
  🖨(🔤Last line!🔤)💩
}`;

const EMOJI_TRANSLATED_TEST: string = `program patito;
var  int  uno, dos=2, tres;  float cuatro= 4.0;  bool  cinco =  True , seis =  False ;

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
