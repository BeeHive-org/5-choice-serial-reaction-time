[3d printer]:Parts.yaml#3dprinter
[Servo motor]:Parts.yaml#ServoMotor
[Machine Screws DIN 965]:Parts.yaml#MachineScrewsDIN965
[Pz2 Pozidriv screwdriver]:Parts.yaml#PozidrivScrewdriver
[Laser cutter]:Parts.yaml#Lasercutter
[PLA filament]:Parts.yaml#PLAfilament
[clear plastic sheet]:Parts.yaml#ClearSheet
[M3x8 counter sunk screw]:Parts.yaml#M3X8mmCountersunk
[2mm Hex key]:Parts.yaml#2mmHexkey
[M2x6 counter sunk screw]:Parts.yaml#M2X6mmCountersunk
[Pozidriv PZ1 screw driver]:Parts.yaml#PozidrivPZ1
[M3x8 socket cap screw]:Parts.yaml#M3X8mmSocketcap
[Flexible Tube]: Parts.yaml#Flexibletube


# Food dispencer

An automated feeding and storage tank for small animals during lab test. In this project its being used to reward the animal under test. After testing is done the feeding tank should be filled and programed to auto feed mode to ensure the animal is feed as per the diatery requirements.

![](images/Food_dispencer.PNG)


{{BOM}} 
>i You can skip step 1 and 2, if you have purchased the parts.

##Printing parts{pagestep}

>? Please follow the information on your slicing software and remember to add a brim where necessary. 

*  To accomplish this section you will need a [3d printer]{qty: 1, cat:machine} and [PLA filament]{ qty:1, cat:material} to print the following parts:
![](models/Allparts.stl)

## Laser cut parts {pagestep}

* To accomplish this section you will need a [Laser cutter]{qty: 1, cat:machine} and [clear plastic sheet]{qty:1, cat: material} to cut the following parts:
     + [Outer Cover](food_dispencer/Outer_cover.svg)
     + [Inner Cover](food_dispencer/Inner_cover.svg)

##Assemble the parts{pagestep}
1. Push the [Servo motor]{qty: 1} on the 3d printed motor holder.

![](images/base_motor.PNG)

2.  Align the motor holder pillars with the tank base holes and fasten the assembly using [M3x8 counter sunk screw]{Qty:4} and use [2mm Hex key]{Qty:1, cat: tool} to tighten the screws. Make sure the through hole is at the oppsite side of the motor support hook.

![](images/base1.PNG)

3. Align the feed throat with the two holes and the feed throat hole on the base. Then fasten the feed throat with [M2x6 counter sunk screw]{qty:2} and tighten uisng [Pozidriv PZ1 screw driver]{Qty: 1, cat: tool}.

![](images/base2.PNG)

4. fit the rotor on the servo motor shaft and fasten it using the [M3x8 socket cap screw]{Qty:1}.

![](images/base3.PNG)

5. screw the tank on to the tank base. MAke sure the tabs fit in the slots.

![](images/base4.PNG)

6. place the outer cover and inner cover ontop of each other and align the holes with the cover handle. Then fasten them using the [M3x8 socket cap screw]{qty:1} on the cover handle hole.

![](images/lid.PNG)

7. The lid can be placed ontop of the tank to cover the food. The [Flexible Tube]{qty:1, cat: material} is then press fit on the fed throat.

![](images/base5.PNG)

You made it!




