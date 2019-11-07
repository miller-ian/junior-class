#include <U8g2lib.h>
#include <SPI.h>

//Some Screen setup declarations
//#define SCREEN U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI
#define SPI_CLK 14
#define NUM_PTS 100

//create an

//SCREEN oled(U8G2_R2, 10, 15,16);  
//create the correct object to interface with the OLED display.
U8G2_SH1106_128X64_NONAME_F_4W_HW_SPI oled(U8G2_R2, 10, 15,16);  

// Constants
const uint8_t DAC_RESOLUTION = 4;                     // DAC # bits
const int FULL_SCALE = pow(2,DAC_RESOLUTION)-1;   // DAC max value
const uint8_t V[] = {3,4,5,6};   // GPIO pins for DAC from MSB to LSB

//Songs to Play:
//(SPM is sixteenth notes per minute (4*times BPM)
// Comment/uncomment different songs.
//Adjust SPM Below

// SMURF Song: SPM around 300 
const char SONG[] = "ggggCCCgAAffddddgggcaaccbbbbbbbbggggCCCgAAffddddggeeffddcccccccc"; // Smurf's Song? i need sheet music to verify this doesn't sound like the right.

// Scale...Do Re Mi...
//const char SONG[] = "ccccddddeeeeffffggggAAAABBBBCCCCCCCCCC";

//Bodak Yellow, Cardi B (SPM: 500) (BPM 125) Cardi Cardi Cardi
//const char SONG[] = "BBBBCCCCEEEEBBBBCCCCEEEEBBBBCCCCBBBBCCCCEEEEBBBBCCCCEEEEBBBBEEEE"; 

//Just a regular note...set the SPM to whatever:
//const char SONG[] = "ggggggg"; // song notes

const int SPM = 300;               // Sixteenth Notes per min (adjust as needed)
const int SINE_LENGTH = 128;        // number of samples in sine wave
const float VOLUME = 1.0;


//Change to 1 for ramp up of voltages!
const int STEP_THROUGH =0;       // set to 0 or 1

float phase_count;  //accumulator of "normalized" Phase (kept pinned 0 through SINE_LENGTH)
float phase_step;   //amount of normalized phase to step each sampling_time time step.

// Global variables
elapsedMicros time = 0;               // overall timer
elapsedMicros time_since_last_note=0; // for playing song
unsigned long sampling_time;          // time between samples
unsigned long note_duration;          // length of notes
float SINE[SINE_LENGTH];              // vector for sine wave values
int num_of_samples;                   // number of values before repeating
int sine_counter = 0;                 // two counter variables
int counter = 0;

int dac[DAC_RESOLUTION];    // vector of dac bits
int final_sample;
uint8_t test_val;

struct note_freq_pair {
  char note;
  float freq;
};


//Note table
const note_freq_pair NOTE_TABLE[] = {
  {'a', 220},
  {'b', 246.94},
  {'c', 261.63},
  {'d', 293.66},
  {'e', 329.63},
  {'f', 349.23},
  {'g', 392.0},
  {'A', 440},
  {'B', 493.88},
  {'C', 523.25},
  {'D', 587.33},
  {'E', 659.25},
  {'F', 698.46},
  {'G', 783.99},
};

void setup() {
  Serial.begin(115200);
  SPI.setSCK(SPI_CLK);
  SPI.begin();   
  oled.begin();
  for (int i = 0; i < DAC_RESOLUTION; i++){
    pinMode(V[i], OUTPUT);    // Initialize DAC pins
  }
  pinMode(13,OUTPUT);
  test_val = false;
  if (STEP_THROUGH) {
    num_of_samples = FULL_SCALE + 1;
    sampling_time = 5E4;      // hold values for 0.5 sec
  } else {
    num_of_samples = strlen(SONG);
    note_duration = float(60E6) / SPM;    //microseconds
    float note_frequency = get_note_frequency(SONG[0]);
    //sampling_time = 1E6 / (float(SINE_LENGTH)*note_frequency);    // microsec
    sampling_time = 150; // (microseconds) 10 kHz about
    phase_count = 0;
    phase_step = SINE_LENGTH*sampling_time*note_frequency/1E6;

  }

  // Create array of values to output from sine wave
  for (int i = 0; i < SINE_LENGTH; i++) {
    SINE[i] = 0.5 + 0.5*sin(2*PI/SINE_LENGTH*i);
  }
  oled.setFont(u8g2_font_profont15_mf);


}  

void loop() {

  if (time >= sampling_time) {
    time = 0;
    //test_val = ~test_val;
    //digitalWriteFast(13,test_val);
    digitalWrite(13,1);
    digitalWrite(13,0);
    if (STEP_THROUGH){    // going from 0..FS-1
      final_sample = counter; 
      counter = (counter + 1) % num_of_samples;    // increment to next sample
    }
    else {               // play song is more complicated
      if (time_since_last_note >= note_duration) {
        counter = (counter + 1) % num_of_samples;
        oled.clearBuffer();
        oled.setCursor(0,10);
        //oled.setFont(u8g2_font_profont15_mf);
        oled.print(SONG[counter]);
        oled.sendBuffer();
        float note_frequency = get_note_frequency(SONG[counter]);
        //sampling_time = 1E6 / (float(SINE_LENGTH)*note_frequency);    // microsec
        //phase_count = 0;
        phase_step = SINE_LENGTH*sampling_time*note_frequency/1E6;
        //Serial.print(note_frequency); Serial.print(" ");
        //Serial.println(phase_step);
        time_since_last_note = 0;
      }
      phase_count+=phase_step;
      while (phase_count > SINE_LENGTH){
        phase_count -= SINE_LENGTH;
      }
      float sample = SINE[int(phase_count)];
      float sample_FS = sample * VOLUME * FULL_SCALE;        // scale to full scale      
      float rounded_sample_FS = round(sample_FS * 100)/100; // round to 2 digits
      final_sample = ceil(rounded_sample_FS);   // round up

    }
    for (int i = 0; i < DAC_RESOLUTION; i++) {
      dac[i] = ((int)pow(2,i) & final_sample) != 0; // get value of each bit
      digitalWriteFast(V[i],dac[i]);    // write bit value to corresponding digital out
    }

    // report values to OLED
    if (STEP_THROUGH) {
      oled.clearBuffer();
      oled.setCursor(0,10);
      oled.print("value: "+ String(final_sample));
      oled.setCursor(0,30);
      String bits_to_print = "";
      for (int i = DAC_RESOLUTION-1; i >= 0; i--) {
        bits_to_print += String(dac[i]);
      } 
      oled.print("setting bits: "+bits_to_print);
      oled.sendBuffer();
    }
  }
}


float get_note_frequency(char note) {   // lookup frequency for each note
  int index = 0;
  while(1) {
    if (NOTE_TABLE[index].note == note) {
      //Serial.println(NOTE_TABLE[index].note);
      return NOTE_TABLE[index].freq;
    }
    else {
      index++;
    }
  }
}
