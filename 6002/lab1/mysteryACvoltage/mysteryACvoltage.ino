#include <U8g2lib.h>
#include <SPI.h>

#define SCREEN U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI
#define SPI_CLK 14
#define NUM_PTS 100

// VARIABLE AND CONSTANT DECLARATIONS
long seed1;
long seed2;
float twopi = 3.14159 * 2;
elapsedMicros t = 0;
int general_sin[NUM_PTS];
int ind = 0;
float vo;
float ff;
float scale = 4096/3.3;
unsigned long dt;

// d = 15; e = 47; N = 391

// Objects
SCREEN oled(U8G2_R2, 10, 15,16);  


void setup()                    
{
  SPI.setSCK(SPI_CLK);
  SPI.begin();   
  oled.begin();
  

  randomSeed(analogRead(A9));
  seed1 = random(5,15);
  vo = seed1/10.0;
  seed2 = random(10,300);
  ff = seed2/100.0;
  dt = 1e3/(NUM_PTS*ff);    // in microseconds

  analogWriteResolution(12);
  update_display();   

  // precalculate sine
  for (int i=0;i<NUM_PTS;i++) {
    general_sin[i] = (int)(vo * (sin(twopi/(NUM_PTS) * i) + 1)*scale); 
  }


}

void loop() {

  analogWrite(A14, general_sin[ind]);
  while (t<=dt);
  t = 0;
  ind += 1;
  if (ind==99) ind = 0;
}

void update_display()
{  
  oled.clearBuffer();
  oled.setCursor(0,10);
  oled.setFont(u8g2_font_profont15_mf);
  oled.print("AC voltage");
  oled.setCursor(0,30);
  oled.setFont(u8g2_font_profont15_mf);
  oled.print("CODE1: ");
  oled.print(modulo(seed1,15,391));
  oled.setCursor(0,50);
  oled.print("CODE2: ");
  oled.print(modulo(seed2,15,391));
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