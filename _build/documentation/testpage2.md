[3d printer]:Parts/3dprinter.md ""
[Laser cutter]:Parts/Lasercutter.md ""
[PLA filament]:Parts/PLAfilament.md ""
[clear plastic sheet]:Parts/ClearSheet.md ""
[maker beam XL]:Parts/MakerBeamXL.md ""
[150mm mini hacksaw]:Parts/Hacksaw.md ""
[M3 tap set]:Parts/M3tapset.md ""
[tap wrench]:Parts/Tapwrench.md ""
[2mm Hex key]:Parts/2mmHexkey.md ""
[Pozidriv PZ1 screw driver]:Parts/PozidrivPZ1.md ""
[M3x8 Pozi pan machine screw]:Parts/M3X12mmPozipanscrews.md ""
[M3 hex Nut]:Parts/M3hexnut.md ""
[Liquid Adhesive]:Parts/Adhesive.md ""


# Reaction chamber
![](images/Ass_full.PNG "")

The chamber is used to track mice reaction time using light as a training cue. We will cover the step by step process of making the chamber in this section. 
> [3d printer] and  [Laser cutter]  are OPTIONAL. If you dont have them you can outsource the services from your local supplier. 



### Parts 

* 1 [3d printer]{: Class="bom"} 
* 1 [clear plastic sheet]{: Class="bom"} 
* 1 [Laser cutter]{: Class="bom"} 
* 1 [Liquid Adhesive]{: Class="bom"} 
* 14 [M3 hex Nut]{: Class="bom"} 
* 38 [M3x8 Pozi pan machine screw]{: Class="bom"} 
* 1 [maker beam XL]{: Class="bom"} 
* 400 g of [PLA filament]{: Class="bom"} 


### Tools 

* 1 [150mm mini hacksaw]{: Class="bom"} 
* 1 [M3 tap set]{: Class="bom"} 
* 1 [Pozidriv PZ1 screw driver]{: Class="bom"} 
* 1 [tap wrench]{: Class="bom"} 




> If you have outsourced the printed and laser cut parts.  You migth need to inform your supplier to have  [PLA filament] for printing and [clear plastic sheet] for laser cutting.


## Step 1: Electronics box {:id="electronics-box" class="page-step"}
 + Using a laser cutter, cut the following parts:
     + 1 pc of [Ecase_Back](models/Ecase_Back.svg "")
     + 1 pc of [Ecase_Base](models/Ecase_Base.svg "")
     + 1 pc of [Ecase_Front](models/Ecase_Front.svg "")
     +  2 pcs of [Ecase_R&L](models/Ecase_RnL.svg "")

   + Assemble the Electronics box with the laser cut parts to form a box then fasten the box with [M3 hex Nut] and  [M3x8 Pozi pan machine screw] using [Pozidriv PZ1 screw driver] to tighten the nuts.

![](images/Electronics_base.PNG "")

## Step 2: Electronics board {:id="electronics-board" class="page-step"}

   + Position the Pcb board in line with the holes on the side of the box assembly. Then using  [M3x8 Pozi pan machine screw]fasten the board using  [Pozidriv PZ1 screw driver] to tighten the screws.

![](images/Electronics_base1.PNG "")

## Step 3: Electronics cover {:id="electronics-cover" class="page-step"}

  + Print the two models below
[](models/Latch_handle.stl "") 

[](models/Latch_base.stl "")

> Do not print the latch_assembly.stl as one part 

   + Snap fit the latch_handle.svg on to the latch_base.svg part to from the [Latch_assembly](models/Latch_assembly.stl "").


 + Locate the holes on the side of the box and using [M3 hex Nut] and [M3x8 Pozi pan machine screw] fasten the assembled latch to the box uisng [Pozidriv PZ1 screw driver].   

   ![](images/Electronics_base2.PNG "")

 + Place the [Electronics top](models/Electronics_top.stl "") on top of the box and fasten it using the latch assembly.

![](images/Electronics_base3.PNG "")

## Step 4: Maker beam frame {:id="maker-beam-frame" class="page-step"}

 + Using [150mm mini hacksaw] cut 2 pcs 200mm long and 6 pcs 150mm long from the [maker beam XL]
 
  + From the [M3 tap set] place the taping screw on the [tap wrench] then make threads on the holes at the end of the maker beam xl pieces that you had cut ealier. 

  + Place 2 makerbeam xl 200mm and 150 mm end to end at their meeting point joing them together using [corner](models/corner.stl ""). to make a square frame. Using [M3x8 Pozi pan machine screw] fasten the corners to the maker beam xl uisng [Pozidriv PZ1 screw driver]. Repeat the process for all the corners to make a rectangle.

  ![](images/Maker_base.PNG "")

  + At the corners of the square frame fasten horizontally 4 more maker beam xl using [M3x8 Pozi pan machine screw].  

![](images/Maker_base1.PNG "")

## Step 5: Adding the enclosure {:id="adding-the-enclosure" class="page-step"}

 + Slide the [platform support](models/Platform_support.svg "") parts on opposite sides of the pillars and on top of them place the [Platform base](models/Platform_base.svg "").

![](images/Maker_base2.PNG "")

 + Slide the [feeding wall](models/Feeding_wall.stl "") making sure it goes all the way to the bottom. Then for the [led series wall](models/Led_series_wall.stl "") will slide up to the platform and on top of it slide the [curved wall](models/Curved_wall.stl "").
.
![](images/Maker_base3.PNG "")

+ With the [side entry wall](models/Side_entry_wall.svg "") press fit the [tunnel connector](models/Tunnel_connector.stl "") and the [tunnel clamp](models/Tunnel_clamp.stl "") on either side of the plasric sheet.

![](images/Side_entry_wall.PNG "")

+ Slide the [side entry wall](models/Side_entry_wall.svg "") and the [side plain wall](models/Side_plain_wall.svg "") through the pillars of the box.

![](images/Maker_base4.PNG "")

+ With the [lid](models/Lid.svg "") pieces, [hinge](models/Hinge.stl ""), [trap latch](models/Trap_latch.stl "") and [groove pins](models/Grooved_pin.stl ""). Locate the holes on the lid and allign the hinge and latch then press fit the groove pins on the holes to fasten the latch and hinge on the clear sheet.

![](images/Lid_assembly.PNG "")

+ Place the assembled lid on the box assembly. Then using [M3x8 Pozi pan machine screw] fasten the lid tightening the screws using [Pozidriv PZ1 screw driver].  

![](images/Maker_base5.PNG "")

+ On the bottom of the box along the makerbeam xl groove slide the [guide rail](models/Guide_rail.svg "") and make sure it is at the middle and fits tightly.

![](images/Maker_base6.PNG "")

## Step 6: Excrete panel {:id="excrete-panel" class="page-step"}

+ Using the Excrete box case parts [case back](models/Excrete_panel_RnL.svg ""), [case base](models/Excrete_panel_base.svg ""),[case front](models/Excrete_panel_RnL.svg ""), [case right](models/Excrete_panel_FnB.svg ""), [case left](models/Excrete_panel_FnB.svg "") and [Liquid Adhesive] stick the parts together and waith for them to dry.

![](images/Excrete_panel.PNG "")

## Step 7: Putting things together {:id="putting-things-together" class="page-step"}

+ Place the box assembly on top of the electronics case and close the latches to make the assembly stable.

![](images/Ass1.PNG "")




+ The assembled tray in should slid on the assembly in the assembly to make a collector for the animal excretion during experiment.

![](images/Ass_full.PNG "")

<!-- GitBuilding Nav -->
---

[Previous page](testpage1.md)