# round-robin-generator
Round-Robin generator designed for FPV Racing. The script generates random heats every round with the given pilots, but makes sure every pilot encounters every other pilots close to the same amount of times. The algorithm is not perfect yet, but it's practically usable for FPV races using a round robin system.


To use it, fill in the pilot names in the file, then run it from the command line with some optional parameters

```python fpv-round-robin.py [rounds] [pilots_per_heat] [debug]```

With default settings, 15 heats of 4 pilots per heat will be generated.

```
Round 1
Heat 1,Pilot 8,Pilot 10,Pilot 6,Pilot 1
Heat 2,Pilot 9,Pilot 5,Pilot 7,Pilot 4
Heat 3,Pilot 11,Pilot 2,Pilot 12,Pilot 3
Round 2
Heat 1,Pilot 6,Pilot 2,Pilot 7,Pilot 10
Heat 2,Pilot 4,Pilot 5,Pilot 1,Pilot 3
Heat 3,Pilot 9,Pilot 8,Pilot 12,Pilot 11
Round 3
Heat 1,Pilot 7,Pilot 10,Pilot 1,Pilot 11
Heat 2,Pilot 6,Pilot 9,Pilot 4,Pilot 3
Heat 3,Pilot 2,Pilot 5,Pilot 12,Pilot 8
Round 4
Heat 1,Pilot 7,Pilot 5,Pilot 12,Pilot 6
Heat 2,Pilot 8,Pilot 2,Pilot 4,Pilot 11
Heat 3,Pilot 9,Pilot 10,Pilot 1,Pilot 3
Round 5
Heat 1,Pilot 6,Pilot 5,Pilot 3,Pilot 11
Heat 2,Pilot 1,Pilot 2,Pilot 12,Pilot 4
Heat 3,Pilot 7,Pilot 10,Pilot 8,Pilot 9
Round 6
Heat 1,Pilot 5,Pilot 10,Pilot 4,Pilot 11
Heat 2,Pilot 1,Pilot 2,Pilot 6,Pilot 9
Heat 3,Pilot 7,Pilot 8,Pilot 3,Pilot 12
Round 7
Heat 1,Pilot 10,Pilot 4,Pilot 6,Pilot 12
Heat 2,Pilot 8,Pilot 2,Pilot 3,Pilot 7
Heat 3,Pilot 1,Pilot 9,Pilot 5,Pilot 11
Round 8
Heat 1,Pilot 10,Pilot 2,Pilot 5,Pilot 3
Heat 2,Pilot 1,Pilot 4,Pilot 11,Pilot 7
Heat 3,Pilot 8,Pilot 9,Pilot 6,Pilot 12
Round 9
Heat 1,Pilot 8,Pilot 1,Pilot 5,Pilot 6
Heat 2,Pilot 2,Pilot 9,Pilot 11,Pilot 10
Heat 3,Pilot 3,Pilot 4,Pilot 7,Pilot 12
Round 10
Heat 1,Pilot 12,Pilot 9,Pilot 5,Pilot 10
Heat 2,Pilot 8,Pilot 4,Pilot 11,Pilot 6
Heat 3,Pilot 3,Pilot 1,Pilot 7,Pilot 2
Round 11
Heat 1,Pilot 12,Pilot 1,Pilot 11,Pilot 10
Heat 2,Pilot 3,Pilot 4,Pilot 9,Pilot 8
Heat 3,Pilot 5,Pilot 2,Pilot 7,Pilot 6
Round 12
Heat 1,Pilot 10,Pilot 4,Pilot 5,Pilot 8
Heat 2,Pilot 7,Pilot 11,Pilot 9,Pilot 6
Heat 3,Pilot 12,Pilot 2,Pilot 1,Pilot 3
Round 13
Heat 1,Pilot 10,Pilot 11,Pilot 6,Pilot 3
Heat 2,Pilot 7,Pilot 5,Pilot 1,Pilot 8
Heat 3,Pilot 2,Pilot 4,Pilot 9,Pilot 12
Round 14
Heat 1,Pilot 1,Pilot 4,Pilot 6,Pilot 12
Heat 2,Pilot 2,Pilot 5,Pilot 11,Pilot 8
Heat 3,Pilot 10,Pilot 7,Pilot 9,Pilot 3
Round 15
Heat 1,Pilot 4,Pilot 7,Pilot 2,Pilot 10
Heat 2,Pilot 1,Pilot 3,Pilot 9,Pilot 8
Heat 3,Pilot 11,Pilot 5,Pilot 6,Pilot 12
```
