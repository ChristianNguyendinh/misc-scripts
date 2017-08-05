/*

Simple Go program for future reference

go build go_skeleton.go
./go_skeleton

Makes a custom type that implements the stringer interface which allows the type to
work with fmt printing functions such as println. Then uses goroutines to concurrently
convert 2 strings into this custom type, wait a random amount of seconds between 1 - 10,
and then print the custom type. After, each goroutine will send through the channel a 
boolean value signifying that it is done, which is caught and read in main()

*/

package main

import (
	"fmt"
	"time"
	"math/rand"
)

type MyString struct {
	str string
	age int
}

// Implement interface Stringer for MyString
func (ms MyString) String() string {
	return fmt.Sprintf("%s (%d)", ms.str, ms.age)
}

// Wait random duration (0-10 sec) then print MyString
func DoThing(str string, c chan bool) {
	wait := rand.Int() % 10
	time.Sleep(time.Duration(wait) * time.Second)

	mystr := MyString{str, len(str)}
	fmt.Printf("Waited %d seconds... Now Println'ing: \n", wait)
	fmt.Println(mystr)

	// Just pipe something through the channel to say we are done with this goroutine
	c <- true
}

func main() {
	rand.Seed(time.Now().Unix())

	var str1 string = "Hello World"
	var str2 string = "Jello is good"

	// make a channel for communication back
	c := make(chan bool)

	// Concurrently run the function twice using goroutines
	go DoThing(str1, c)
	go DoThing(str2, c)

	// not using sync.WaitGroup so i can throw a for loop in here for future ref
	for i := 0; i < 2; i++ {
		// block until something writes to c
		<- c
	}

}