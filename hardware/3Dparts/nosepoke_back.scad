
///////////////////////////////////////////
// Design for a magazine entry to be used//
// in the behaviour box                  //
// Andre Maia Chagas - Cansu Demirbatir  //
// 16082021                              //
///////////////////////////////////////////

// all dimensions in mm.

//needs the ring.scad file (saved on the same folder)
use <ring.scad>

//// variables /////////////


//back plate dimensions 
//(the plate that slides on the metal railings)
backpanelx = 52.5*2;
backpanely = 60;
backpanelz = 2.8;

supportw=5;

//dimensions for the headport 

noseHoleD = 12;
noseHoleH = 11;

//wall thickness
headportwall = 2;

screwD = 4;


tolerance = 0.1;

ledDx = 8; // main LED
ledD = 5;
ledH = 6;
wallT = 2;

/* change this depending on the printer and printer settings
   it is a "tolerance" variable, so holes and fittings can be 
   adjusted.
*/
tol = 0.1;

$fn=30;

module backwall_np(){
//backpanel
difference(){
    translate([-(backpanely)/2,-0.1,(-backpanelx)/2]){
        cube([backpanely,backpanelz,backpanelx]);
}//end translate      


//negative

//central hole
translate([headportwall-3,headportwall+5,headportwall]){
rotate([90,0,0])
    cylinder(d= 12,h= 11 - headportwall*2+5);
}//end translate
}//end difference
}//end module

translate([1,0,4]){
backwall_np();
}//end translate


module nosePoke(){
    $fn=30;
difference(){
union(){
cylinder(d=noseHoleD+wallT,h=noseHoleH+wallT);
//cylinder(d=noseHoleD+2*screwD+7,h=wallT);
translate([0,0,noseHoleH+wallT]){
cylinder(d=ledDx+2,h=ledH-1);
}//end translate

translate([(noseHoleD+1)/2,0,ledD-1]){
rotate([0,90,0]){
    cylinder(d=ledD+wallT,h=ledH);
}//end rotate
}//end translate

translate([-(noseHoleD+1)/2,0,ledD-1]){
rotate([0,-90,0]){
    cylinder(d=ledD+wallT,h=ledH);
}//end rotate
}//end translate
}//end union


translate([0,0,-1]){
cylinder(d=noseHoleD,h=noseHoleH);
cylinder(d=ledDx+2*tolerance,h=ledH+noseHoleH+wallT+5);
}//end translate

translate([(noseHoleD+1)/2-wallT,0,ledD-1]){
rotate([0,90,0]){
    cylinder(d=ledD+2*tolerance,h=ledH+3);
}//end rotate
}//end translate

translate([-(noseHoleD+1)/2+wallT,0,ledD-1]){
rotate([0,-90,0]){
    cylinder(d=ledD+2*tolerance,h=ledH+3);
}//end rotate
}//end translate

translate([0,(noseHoleD)/2+screwD,-1]){
cylinder(d=screwD+2*tolerance,h=10);
}//end translate

translate([0,-(noseHoleD)/2-screwD,-1]){
cylinder(d=screwD+2*tolerance,h=10);
}//end translate
}//end difference
}//end module
translate([0,0,6]){
rotate([90,0,0]){
nosePoke();
}//end rotate
}//end translate

