#include"STD_TYPES.h"
#include"BIT_MATH.h"
#include"DIO_interface.h"

#include"LED_interface.h"
#include<util/delay.h>

int main(void){


	LED_Type LED0 = { PORTA , PIN0 , ACTIVE_HIGH};
	LED_Type LED1 = { PORTA , PIN1 , ACTIVE_HIGH};
	LED_Type LED2 = { PORTA , PIN2 , ACTIVE_HIGH};

	LED_voidInit(LED0);	LED_voidInit(LED1);	LED_voidInit(LED2);

	while(1){
		LED_voidOn(LED2);
		_delay_ms(1000);
		LED_voidOn(LED1);
		_delay_ms(1000);
		LED_voidOn(LED0);
		_delay_ms(1000);
		LED_voidOff(LED0);
		LED_voidOff(LED1);
		LED_voidOff(LED2);

	}


	return 0 ;
}
