/*
Simple test of the OLED SH1106 display for 6.S08
Joel Voldman, January 2017
*/

#include <SPI.h>
#include <U8g2lib.h>

#define SPI_CLK 14
#define DELAY 1000
// Set up the oled object
//U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI(rotation, cs, dc [, reset])
U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI oled(U8G2_R2, 10, 15, 16);


void setup() {
  SPI.setSCK(SPI_CLK);   // move the SPI SCK pin from default of 13
  oled.begin();     // initialize the OLED
}

void loop() {
  oled.clearBuffer();    //clear the screen contents
  oled.setFont(u8g2_font_ncenB10_tr);    
  oled.drawStr(0,15,"I Love 6.002!");
  oled.sendBuffer();     // update the screen
  delay(DELAY);           //wait a bit

  oled.clearBuffer();    
  oled.drawBox(3,7,25,15);
  oled.sendBuffer();
  delay(DELAY);

  oled.clearBuffer();    //clear the screen contents 
  oled.drawFrame(3,7,25,15);
  oled.sendBuffer();
  delay(DELAY);

  oled.clearBuffer();    //clear the screen contents 
  oled.drawCircle(20, 25, 10, U8G2_DRAW_ALL);
  oled.sendBuffer();
  delay(DELAY);

  oled.clearBuffer();    //clear the screen contents 
  oled.setFont(u8g2_font_unifont_t_symbols);
  oled.drawGlyph(5, 20, 0x2603);  /* dec 9731/hex 2603 Snowman */
  oled.sendBuffer();
  delay(DELAY);

  oled.clearBuffer();    //clear the screen contents 
  oled.drawLine(20, 5, 5, 32);
  oled.sendBuffer();
  delay(DELAY);

  oled.clearBuffer();    //clear the screen contents 
  oled.drawRFrame(20,15,30,22,7);
  oled.sendBuffer();
  delay(DELAY);

  oled.clearBuffer();    //clear the screen contents 
  oled.drawRFrame(20,15,60,40,15);
  oled.sendBuffer();
  delay(DELAY);

  oled.clearBuffer();    //clear the screen contents 
  oled.drawTriangle(20,5, 27,50, 5,32);
  oled.sendBuffer();
  delay(DELAY);

  oled.clearBuffer();    //clear the screen contents 
  oled.setFont(u8g2_font_ncenB14_tf);
  oled.setFontDirection(0);
  oled.drawStr(15, 20, "Abc");
  oled.setFontDirection(1);
  oled.drawStr(15, 20, "Abc");
  oled.setFontDirection(0);  
  oled.sendBuffer();
  delay(DELAY);


}