///////////////////////////////////////////
// Design for a magazine entry to be used//
// in the behaviour box                  //
// Andre Maia Chagas - Cansu Demirbatir  //
// 16082021                              //
///////////////////////////////////////////

// all dimensions in mm.

//needs the ring.scad file (saved on the same folder)

use <nose_poke.scad>
use <magazine.scad>
//// variables /////////////


//back plate dimensions 
//(the plate that slides on the metal railings)
backpanelx = 52.5*2;
backpanely = 60;
backpanelz = 2.8;
wally=160-17;

//dimensions for the headport 
noseHoleD = 12;


//dimensions for the headport 
headportx = 25;
headporty = 28;
headportz = 30;


/* change this depending on the printer and printer settings
   it is a "tolerance" variable, so holes and fittings can be 
   adjusted.
*/
tol = 0.1;

$fn=30;


module backwall_simple(){
offsetZ = 10;
difference(){


cube([backpanelx, wally,backpanelz]);

translate([headportx+10,45,-2]){
rotate([0,0,-90]){
cube([headportx,headporty+2,backpanelz+5]);
}//end rotate
}//end translate
translate([(backpanelx)/2+3.5,wally/2+noseHoleD-2,-2]){
cylinder(d=noseHoleD,h=20);
}//end translate
}//end difference

translate([backpanelx/2+headportx/2,45,0]){
rotate([90,0,-90]){
magazine(panel=0);
}//end rotate
}//end translate
translate([(backpanelx)/2+3.5,wally/2+noseHoleD-2,2.7]){
nosePoke();
}//end translate

cube([backpanelx, backpanelz,offsetZ]);
translate([0,backpanelz,offsetZ]){
rotate([90,0,0]){
cube([backpanelx, backpanelz,offsetZ]);
}
}//end translate
translate([backpanelx,wally,0]){
    rotate([0,0,180]){
cube([backpanelx, backpanelz,offsetZ]);
translate([0,backpanelz,offsetZ]){
rotate([90,0,0]){
cube([backpanelx, backpanelz,offsetZ]);
}
}//end translate
}
}//end rotate
}//end module

//rotate([0,90,-90]){
//translate([-52,-150,-4]){
backwall_simple();
//}
//}

/*
module backwall(){
//backpanel

translate([-(backpanely)/2,-0.1,(-backpanelx)/2]){
cube([backpanely-20,backpanelz,backpanelx]);
}//end translate      


//negative
}//end module
backwall();

module backwall_np(){
//backpanel
difference(){
    translate([-(backpanely)/2,-0.1,(-backpanelx)/2]){
        cube([backpanely,backpanelz,backpanelx]);
}//end translate      


//negative

//central hole
translate([headportwall-3,headportwall+5,headportwall-6]){
rotate([90,0,0])
    cylinder(d= 12,h= 11 - headportwall*2+5);
}//end translate
}//end difference
}//end module

translate([-59,0,0]){
backwall_np();
}//end translate



translate([-60,0,2-6]){
rotate([90,0,0]){
nosePoke();
}//end rotate
}//end translate



translate([-105,2.6,-12.5]){
rotate([0,0,180]){
magazine(panel=1);
}//end rotate
}//end translate
*/