
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "serialport_read.h"


int main(void)
{
	char message_received[100]="";
	char *commands;
	int fd = connect_serial_port();
	while(1){
		receive_serial_message(fd, message_received);
		//printf("%s",message_received);
		strtok_r(message_received, "|", &commands);
		int n_uavs = atoi(message_received);		
		printf("N_UAVS: %s Commands: %s", message_received, commands);
	    char *token = strtok(commands, "_");
		while (token != NULL) 
		{ 
			printf("%s\n", token); 
			token = strtok(NULL, "_"); 
		} 
		
	}
	
	printf("\n +----------------------------------+\n\n\n");
		
	close(fd); /* Close the serial port */
	return 0;
}
