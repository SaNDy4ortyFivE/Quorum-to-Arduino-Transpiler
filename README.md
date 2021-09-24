### Quorum to Arduino Transpiler(v2.0)
#### Supported Componenets
1. Ultrasonic sensor (HC-SR04)
2. Temperature sensor(LM-35)
3. Simple Push Button
4. Infrared Sensor
5. LED

#### Supported Datatypes
1. Integer
2. Number

#### Supported Conditionals
1. If _(with one condition)_
2. if _(with one condition)_ with else
3. Nested if _(with one condition)_ else

#### Comparison Operators
1. Equal _(=)_
2. Less than _(<)_
3. Greater than _(>)_

**_Support for underscores and numerals for variable names is not added_**  
**_No blank lines are allowed in the code_**  
**_Quroum supports variable initialization. Declaration is not yet supoorted but the feature is available in transpiler_**  

#### Component  Methods
##### Ultrasonic HC-SR04
```
use USONIC
class MyClass
		/*create an instance*/
		USONIC usona
		action Main()
			/*set trig pin*/
			usona:trigpin(10)
			usona:echopin(11)
			/*read distance*/
			integer a = usona:GETDISTANCE()
		end
end
```

##### Temperature Sensor(LM-35)
```
use LMTEMP
class MyClass
	/*creating an instance*/
	LMTEMP lmtp
	action Main()
		/*setting up its pin number*/
		lmtp:pinLMTP(10)
		/*variable with data type as number*/
		number a
		/*read value from sensor*/
		a = lmtp:READTEMP()
	end
end
```

##### Simple Push Button
```
use BUTTON
class MyClass
	/*creating instance*/
	BUTTON btn
	action Main()
		/*setting up a pin*/
		btn:pinBTN(10)
		integer a
		/*read button state*/
		a = btn:STATE()
		end
end

```
##### Infrared Sensor
```
use IRED
class MyClass
	/*creating instance*/
	IRED ired
	action Main()
		/*setting up the pin*/
		ired:pinIR(10)
		integer a
		/*reading the value*/
		a = ired:READVAL()
        end
end
```

##### LED
```
use LED
class MyClass
	/*creating instance*/
	LED ledred
	action Main()
		/*set the pin*/
		ledred:pin(10)
		ledred:ON()
		/*ledred:OFF()*/
	end
end
```

###### More Examples in examples folder

#### Libraries
1. ANTLR4 _(v4.8)_
- Generates lexer, parser and listener based on grammar file provided.
2. Anytree
- Library to help handling tree data structure in python.
