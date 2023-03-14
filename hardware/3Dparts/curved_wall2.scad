use<nose_poke.scad>

  // for the sides to slide

slideWallx = 2.3;
slideWally = 9;
slideWallz = 60;


tol = 0.1;

w = 60;      // width of rectangle
h = 2;      // height of rectangle
l = 143;      // length of chord of the curve
dh = 10;      // delta height of the curve

noseHoleD = 12;
noseHoleH = 11;
noseHoleZ = 45; //location on z plane(offset)


nHole = 5;
yOffsetHole = 13;

//metal grid
gridD = 3;
gridH = 110;


ledDx = 8; // main LED
ledD = 5;
ledH = 6;
wallT = 2;
$fn=60;


gridOffset = 10;

module curve(width, height, length, dh) {

    r = (pow(length/2, 2) + pow(dh, 2))/(2*dh);
    a = 2*asin((length/2)/r);
    difference(){
    /*

    rotate_extrude( angle=a)
    translate([r,0,0])
    square([height,width], center=true);
*/
    translate([-(r -dh), 0, width/2]){
       rotate([0, 0, -a/2]){
           rotate_extrude(angle = a){
               translate([r, 0, 0]){
                   square(size = [height, width], center = true);
               }//end translate
           }//end rotate_extrude
       }//end rotate
   }//end translate
        
    for ( i = [0:nHole-1]){
    translate([0,l/2-yOffsetHole-i*((l-2*yOffsetHole)/(nHole-1)),noseHoleZ]) {
        rotate([0,90,0]) {
        cylinder(d=noseHoleD+tol, h=15);
    }//end rotate
    }//end translate
    }// end for loop 


}//end difference




    translate([gridOffset-1,l/2-1,0]) {
        rotate([0,0,90]){
        cube([slideWallx,gridOffset, slideWallz]);
        }
        cube([slideWallx, slideWally, slideWallz]);
    }//end translate
    rotate([180,0,0]){
        translate([gridOffset-1,l/2-1,-slideWallz]) {
        rotate([0,0,90]){
        cube([slideWallx, gridOffset, slideWallz]);
        }
        cube([slideWallx, slideWally, slideWallz]);
    }//end translate
}
    /*
    translate([-1.5,-l/2-7,0]) {
        rotate([0,0,90]){
        cube([slideWallx, 10, slideWallz]);
        }
        cube([slideWallx, slideWally, slideWallz]);
    }//end translate
*/
}// end module

curve(w, h, l, dh);



//curve(width, height, length, dh);




angles = [-12,-6,0,6,12];
offsets = [3.8,8.8,10.5,8.8,3.8];
for ( i = [0:nHole-1]){
    translate([offsets[i],l/2-yOffsetHole-i*((l-2*yOffsetHole)/(nHole-1)),noseHoleZ]) {
        rotate([angles[i],90,0]) {           
        nosePoke();
    }//end rotate
    }//end translate
    }// end for loop 
    
    
    
