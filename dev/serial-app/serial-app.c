#include <stdio.h>
#include <termios.h>
#include <sys/stat.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/fcntl.h>
#include <string.h>
#include <errno.h>

static int fd = 0;
char psResponse[10];
int iIn = 0;
int iOut = 0;

int main(void) {
fd = open("/dev/ttyUSB0", O_RDWR | O_NOCTTY | O_NONBLOCK);
	//iOut = write(fd, "o", 1);
	iIn = read(fd, psResponse, 1);
	printf("%d\n", iIn);
}