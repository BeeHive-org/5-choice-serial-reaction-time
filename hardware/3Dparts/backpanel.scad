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

noseHoleD = 12;
noseHoleH = 11;
tolerance = 0.1;

ledDx = 8; // main LED
ledD = 5;
ledH = 6;
wallT = 2;

//magazine LED
magledD = 8; // magazine LED diameter

//dimensions for the headport 

headportx = 25;
headporty = 28;
headportz = 30;

//infrared led dimensions
irledd = 5;
irledh = 6;

//pellet dispenser tube
pelletD = 14;
/* change this depending on the printer and printer settings
   it is a "tolerance" variable, so holes and fittings can be 
   adjusted.
*/
tol = 0.1;

$fn=30;

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
translate([-60,0,2-6]){
rotate([90,0,0]){
nosePoke();
}//end rotate
}//end translate

module magazine(){

difference(){



union(){
    
    translate([-(backpanely-headporty)/2,-0.1,(-backpanelx+headportx)/2]){
cube([backpanely,backpanelz,backpanelx]);
}
cube([headportx,headporty,headportz]);


//well
translate([headportx/2,headporty/2,-(headporty-10)/2]){
cylinder(d1=headporty/2,d2=headporty/2+5,h=10);
}//end translate

//magazine led
translate([headportx/2,headporty/2,headportz]){
cylinder(d=magledD+headportwall,h=7);
}//end translate



//IR detector holes
translate([headportx+irledh,8,6]){
rotate([0,-90,0]){
cylinder(d=irledd+headportwall,h=headportx+irledh*2);
}//end rotate
}//end translate

//pellet shute
translate([headportx/2,headporty-2.5*headportwall,headportz/4+4]){
rotate([-45,0,0]){
cylinder(d=pelletD+headportwall,h=20);
}//end rotate
}//end translate


}//end union



//negative
union(){
//central hole
translate([headportwall,headportwall-5,headportwall]){
cube([headportx-headportwall*2,headporty-headportwall*2+5,headportz-headportwall*2]);
}//end translate
//well
translate([headportx/2,headporty/2,-(headporty-10)/2+1.1]){
cylinder(d1=headporty/2-1,d2=headporty/2+5-1,h=10);
}
//ir led holes
translate([headportx+irledh+1,8,6]){
rotate([0,-90,0]){
cylinder(d=irledd+2*tol,h=headportx+irledh*2+2);
}//end rotate
}//end translate

//pellet shute
translate([headportx/2,headporty-2.5*headportwall-2,headportz/4+2]){
rotate([-45,0,0]){
cylinder(d=pelletD,h=30);
}//end rotate
}//end translate


//magazine led
translate([headportx/2,headporty/2,headportz-headportwall-2]){
cylinder(d=magledD+2*tol,h=20);
}//end translate
}//end union
}//end difference
//headentry
}//end module

translate([-105,2.6,-12.5]){
rotate([0,0,180]){
magazine();
}//end rotate
}//end translate

