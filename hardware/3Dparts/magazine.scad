
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

//magazine LED
magledD = 8; // magazine LED diameter

//back plate dimensions 
//(the plate that slides on the metal railings)
backpanelx = 52.5*2;
backpanely = 60;
backpanelz = 2.8;

supportw=5;

//dimensions for the headport 

headportx = 25;
headporty = 28;
headportz = 30;

//wall thickness
headportwall = 2;

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


//backpanel
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
}//end differnece
//headentry

