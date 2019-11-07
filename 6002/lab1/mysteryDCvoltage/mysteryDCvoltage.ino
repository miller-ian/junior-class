#include <U8g2lib.h>
#include <SPI.h>

#define SCREEN U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI
#define SPI_CLK 14

// VARIABLE AND CONSTANT DECLARATIONS
long seed;

// Objects
SCREEN oled(U8G2_R2, 10, 15,16);  


void setup()                    
{
  SPI.setSCK(SPI_CLK);
  SPI.begin();   
  oled.begin();
  

  randomSeed(analogRead(A9));
  seed = random(0,30);

  analogWriteResolution(12);
  analogWrite(A14, (int)(seed/3.3*1/10*4096));
  update_display();   
}

void loop() {}



void update_display()
{  
  oled.clearBuffer();
  oled.setCursor(0,10);
  oled.setFont(u8g2_font_profont15_mf);
  oled.print("DC voltage");

  oled.setCursor(0,40);
  oled.setFont(u8g2_font_profont17_mf);
  oled.print("CODE: ");
  oled.print(modulo(seed,37,77));
  oled.sendBuffer();
}


// Taken from the internet to avoid integer overflow
// See:
// https://stackoverflow.com/questions/8496182/calculating-powa-b-mod-n
int modulo(int a,int b,int n){
  long long x=1,y=a; 
  while(b > 0){
      if(b%2 == 1){
          x=(x*y)%n;
      }
      y = (y*y)%n; 
      b /= 2;
  }
  return x%n;
}