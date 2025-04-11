```bash
 class MyClass {
	// Define the fields
	 var field1 : Int = __
	 var field2 : String = __
	 
	// Define the method
	def myMethod() = {
		// Implement your method logic here
	}
	 
	// Define the function
	def myFunction()= () => {
		// Implement your function logic here
	}
}
```

```bash
object Main {
	def main ( args : Array [ String ]) : Unit = {
		// Create an instance of MyClass
		val myInstance = new MyClass()
		
		// Use the method
		myInstance.myMethod()
		
		// Change the fields
		myInstance.field1 = 10
		myInstance.field2 = "Hello, Scala!"
		
		// Print the changed fields
		println (s"Field1: ${myInstance.field1}")
		println (s"Field2: ${myInstance.field2}")
	}
}
```
