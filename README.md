# 5-choice-serial-reaction-time

## Open source implementation of a behavioural system for freely moving rodents.

  
![](media/box_sketch.png)
  

It has holes with a light on one end and a feeding slot with a light in the opposite end. Depending on the behavoiur being experimented the animal needs to poke it's nose 
into the correct hole and feeding occurs in accordance to the experiemntal rules.

This system is the first implementation of a complete behavioural box using BeeHive, off the shelf components and 3D printed parts.
  
---
  
### Hardware:
- Beehive components:
- - central hub + ESP32
- - h-bridge
- - IR- emitter and detector
  
- other components:
- - Makerbeams for the box frame
- - perspex sheets for box wall
- - food pellet dispenser based on this [model](https://open-ephys.atlassian.net/wiki/spaces/OEW/pages/79069188/Food+Pellet+Dispenser)
- - 3D printed parts for the different parts
  
### Software:
- micropython on the ESP32
- python (or Bonsai) running data collection on PC.

--- 