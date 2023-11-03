
package main

import (
	"fmt"
	"math"
	"time"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n <= 3 {
		return true
	}
	if n%2 == 0 || n%3 == 0 {
		return false
	}
	for i := 5; i <= int(math.Sqrt(float64(n))); i += 6 {
		if n%i == 0 || n%(i+2) == 0 {
			return false
		}
	}
	return true
}

func main() {
	start := time.Now()

	for i := 1; i <= 1000000; i++ {
		if isPrime(i) {
			fmt.Printf("%d is prime\n", i)
		}
	}

	elapsed := time.Since(start)
	fmt.Printf("Time elapsed: %s\n", elapsed)
}
