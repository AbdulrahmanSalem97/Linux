#include "STD_TYPES.h"
#include"BIT_MATH.h"

#include "DIO_interface.h"

#include "LED_interface.h"
#include "LED_private.h"
#include "LED_config.h"

void LED_voidInit( LED_Type LED_Configuration ){
	
	DIO_voidSetPinDirection( LED_Configuration.Port , LED_Configuration.Pin , OUTPUT );
	
}

void LED_voidOn  ( LED_Type LED_Configuration ){
	
	if( LED_Configuration.Active_State == ACTIVE_HIGH ){
		
		DIO_voidSetPinValue( LED_Configuration.Port , LED_Configuration.Pin , HIGH );
		
	}else if( LED_Configuration.Active_State == ACTIVE_LOW ){
		
		DIO_voidSetPinValue( LED_Configuration.Port , LED_Configuration.Pin , LOW  );
		
	}
	
}

void LED_voidOff ( LED_Type LED_Configuration ){
	
	if( LED_Configuration.Active_State == ACTIVE_HIGH ){
		
		DIO_voidSetPinValue( LED_Configuration.Port , LED_Configuration.Pin , LOW  );
		
	}else if( LED_Configuration.Active_State == ACTIVE_LOW ){
		
		DIO_voidSetPinValue( LED_Configuration.Port , LED_Configuration.Pin , HIGH  );
		
	}
	
}
