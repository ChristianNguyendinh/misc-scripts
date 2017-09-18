package main

import (
    "fmt"
    "io/ioutil"
    "os"
    "strconv"
)

func shiftup(input []byte, shift int) {
    for i, v := range(input) {
        if v != 10 && v != 32 && v != 42 {
            if int(v) + shift > 126 {
                input[i] = byte(33 + ((int(v) + shift) % 126))
            } else {
                input[i] = byte(int(v) + shift)
            }
        }
    }
}

func shiftdown(input []byte, shift int) {
    for i, v := range(input) {
        if v != 10 && v != 32 && v != 42 {
            if int(v) - shift < 33 {
                input[i] = byte(126 - (33 - (int(v) - shift)))
            } else {
                input[i] = byte(int(v) - shift)
            }
        }
    }
}

func main() {
    if len(os.Args) != 4 {
        panic("Needs 3 arguments - file name, -u or -d to shift up or down, and number of bytes to shift by")
    }

    file := os.Args[1]
    shift, err := strconv.Atoi(os.Args[3])
    if err != nil {
        panic(err)
    }

    // input file
    fin, err := ioutil.ReadFile(file)
    if err != nil {
        panic(err)
    }

    var outname string

    // Shift up or down
    if os.Args[2] == "-d" {
        shiftdown(fin, shift)
        outname = "unshift_" + file
    } else if os.Args[2] == "-u" {
        shiftup(fin, shift)
        outname = "un-shift_" + file
    } else {
        panic("Invalid shift option")
    }

    // output file
    err = ioutil.WriteFile(outname, fin, 0644)
    if err != nil {
       panic(err)
    }

    fmt.Println(fin)
}
