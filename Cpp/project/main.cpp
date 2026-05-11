#include <iostream>
#include <string>
#include <termios.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/time.h>
#include "myMacros.h"

using namespace std;

#define ESC 27
unsigned long delay = 5000000;

int kbhit(void)
{
      struct timeval tv;
      fd_set rdfs;

      tv.tv_sec = 0;
      tv.tv_usec = 0;

      FD_ZERO(&rdfs);
      FD_SET (STDIN_FILENO, &rdfs);

      select(STDIN_FILENO+1, &rdfs, NULL, NULL, &tv);
      return FD_ISSET(STDIN_FILENO, &rdfs);

}

int main
(){
   int x = 2, y = 2, dx = 1, speed = 0;
   bool end = false;
   string floor(80,'-'),
          header = "**** BOUNCING BALL ****",
          commands = "[ESC] = Terminate"
                     "[+] = Speedup [-] = Slowdown";
   COLOR(WHITE,BLUE); CLS;
   LOCATE(1,25); cout<< header;
   LOCATE(24,1); cout<< floor;
   LOCATE(25,10); cout<< commands;

   while(!end)
   {
      LOCATE(y,x); cout<< 'o';
      for(long wait = 0; wait < delay; ++wait);
      if(x == 1 || x == 79) dx = -dx;
      if(y == 23)
      {
         speed = -speed;
         if(speed == 0) speed = -7;
      }
      speed += 1;
      LOCATE(y,x); cout<< ' ';
      y += speed; x += dx;
      if(kbhit() != 0)
      {
          switch(getchar())
          {
              case 107: delay -= delay/5;
                        break;
              case 109: delay += delay/5;
                        break;
              case ESC: end = true;
          }
      }
   }
   NORMAL; CLS;
   return 0;
}

