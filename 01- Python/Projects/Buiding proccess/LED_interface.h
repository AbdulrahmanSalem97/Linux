#ifndef LED_INTERFACE_H
#define LED_INTERFACE_H


#define ACTIVE_HIGH    1
#define ACTIVE_LOW     0

typedef struct{
	
	u8 Port         ;
	u8 Pin          ;
	u8 Active_State ;
	
}LED_Type;

  
void LED_voidInit( LED_Type LED_Configuration );

void LED_voidOn  ( LED_Type LED_Configuration );

void LED_voidOff ( LED_Type LED_Configuration );

#endif