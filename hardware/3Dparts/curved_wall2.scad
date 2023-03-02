// for the sides to slide

slideWallx = 2.3;
slideWally = 9;
slideWallz = 60;

$fn= 360;
tol = 0.1;

w = 60;      // width of rectangle
h = 2;      // height of rectangle
l = 143;      // length of chord of the curve
dh = 10;      // delta height of the curve

noseHoleD = 12;
//noseHoleH = 20;
noseHoleZ = 45; //location on z plane(offset)
n_Hole = 5;

y_offset_Hole = 13;


//metal grid
gridD = 3;
gridH = 110;


module curve(width, height, length, dh) {
    $fn=360;
    
    difference(){
    
    r = (pow(length/2, 2) + pow(dh, 2))/(2*dh);
    a = 2*asin((length/2)/r);
    translate([-(r -dh), 0, width/2]) rotate([0, 0, -a/2])         rotate_extrude(angle = a) translate([r, 0, 0]) square(size = [height, width], center = true);
        
    for ( i = [0:n_Hole-1]){
    translate([0,l/2-y_offset_Hole-i*((l-2*y_offset_Hole)/(n_Hole-1)),noseHoleZ]) {
        rotate([0,90,0]) {
        cylinder(d=noseHoleD+2*tol, h=15);
    }//end rotate
    }//end translate
    }// end for loop 
            
translate([6,55,29]){
        rotate([90,0,0]){
        cylinder(d= gridD, h= gridH);
        }//end rotate
    }//end translate

translate([1,80,29]){
        rotate([90,0,0]){
        cylinder(d= gridD, h= gridH+50);
        }//end rotate
    }//end translate

}//end difference



union(){ // slide panels
    translate([-1.5,l/2-1,0]) {
        cube([slideWallx, slideWally, slideWallz]);
    }//end translate
    
    translate([-1.5,-l/2-7,0]) {
        cube([slideWallx, slideWally, slideWallz]);
    }//end translate
}// end union
}// end module

curve(w, h, l, dh);
//grid();
//nosepoke2();
module grid(){
translate([7,50,29]){
        rotate([90,0,0]){
        %cylinder(d= gridD, h= gridH);
        }//end rotate
    }//end translate

translate([2,70,29]){
        rotate([90,0,0]){
        %cylinder(d= gridD, h= gridH+40);
        }//end rotate
    }//end translate
}//end module
curve(width, height, length, dh);
screwD = 4;

noseHoleD = 12;
noseHoleH = 11;
tolerance = 0.1;

ledDx = 8; // main LED
ledD = 5;
ledH = 6;
wallT = 2;

module nosePoke(){
    $fn=30;
difference(){
union(){
cylinder(d=noseHoleD+wallT,h=noseHoleH+wallT);
//cylinder(d=noseHoleD+2*screwD+7,h=wallT);
translate([0,0,noseHoleH+wallT]){
cylinder(d=ledDx+2,h=ledH-1);
}//end translate

translate([(noseHoleD+1)/2,0,ledD]){
rotate([0,90,0]){
    cylinder(d=ledD+wallT,h=ledH);
}//end rotate
}//end translate

translate([-(noseHoleD+1)/2,0,ledD]){
rotate([0,-90,0]){
    cylinder(d=ledD+wallT,h=ledH);
}//end rotate
}//end translate
}//end union


translate([0,0,-1]){
cylinder(d=noseHoleD,h=noseHoleH);
cylinder(d=ledDx+2*tolerance,h=ledH+noseHoleH+wallT+5);
}//end translate

translate([(noseHoleD+1)/2-wallT,0,ledD]){
rotate([0,90,0]){
    cylinder(d=ledD+2*tolerance,h=ledH+3);
}//end rotate
}//end translate

translate([-(noseHoleD+1)/2+wallT,0,ledD]){
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

  
//nosePoke();

for ( i = [0:n_Hole-1]){
    translate([0,l/2-y_offset_Hole-i*((l-2*y_offset_Hole)/(n_Hole-1)),noseHoleZ]) {
        rotate([0,90,0]) {
        nosePoke();
    }//end rotate
    }//end translate
    }// end for loop 