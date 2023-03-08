////////////////////////////////////////////
// Curved wall at the back of box 
// containing holes so that nosepoke 
// ports can be attached
//
// CC BY SA 4.0
////////////////////////////////////////////


// for the sides to slide

slideWallx = 2.8;
slideWally = 14;
slideWallz = 60;

$fn= 360;
tol = 0.1;

w = 60;      // width of rectangle
h = 2.6;      // height of rectangle
l = 130;      // length of chord of the curve
dh = 10;      // delta height of the curve

noseHoleD = 12;
noseHoleH = 20;
noseHoleZ = 40; //location on z plane(offset)
n_Hole = 5;

y_offset_Hole = 17;

screwD = 4;




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
    

}//end difference

union(){ // slide panels
    translate([-1.5,l/2-1,0]) {
        cube([slideWallx, slideWally, slideWallz]);
    }//end translate
    
    translate([-1.5,-l/2-12,0]) {
        cube([slideWallx, slideWally, slideWallz]);
    }//end translate
}// end union
}// end module

curve(w, h, l, dh);

//for ( i = [0:n_Hole]){
        //translate([x_Hole/2-x_offset_Hole ,-y_Hole/2+y_offset_Hole+i*((y_Hole-2*y_offset_Hole)/n_Hole),-tol])cylinder(r=r_Hole, h=z_Hole+2*tol+50, $fn=Smoothness);
    //}
