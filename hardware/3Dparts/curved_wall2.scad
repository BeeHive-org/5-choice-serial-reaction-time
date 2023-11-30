use<nose_poke.scad>


tol = 0.1;


h = 2;      // height of rectangle
l = 143;      // length of chord of the curve
dh = 10;      // delta height of the curve

ledDx = 8; // main LED
ledD = 5;
ledH = 6;


noseHoleD = 12;
noseHoleH = 11;
noseHoleZ = noseHoleD+ledH/2; //location on z plane(offset)


nHole = 5;
yOffsetHole = 13;

  // for the sides to slide

slideWallx = 2.5;
slideWally = 9;
slideWallz = noseHoleD*2+ledH+2*tol;


//metal grid
gridD = 3;
gridH = 110;



$fn=200;


gridOffset = 20;

module curve(width, height, length, dh,holes=1) {

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
 if (holes==1){
    for ( i = [0:nHole-1]){
    translate([0,l/2-yOffsetHole-i*((l-2*yOffsetHole)/(nHole-1)),noseHoleZ]) {
        rotate([0,90,0]) {
        cylinder(d=noseHoleD+tol, h=15);
    }//end rotate
    }//end translate
    }// end for loop 
}//end if

}//end difference


 if (holes==1){
angles = [-12,-6,0,6,12];
offsets = [3.8,8.8,10.5,8.8,3.8];
for ( i = [0:nHole-1]){
    translate([offsets[i],l/2-yOffsetHole-i*((l-2*yOffsetHole)/(nHole-1)),noseHoleZ]) {
        rotate([angles[i],90,0]) {           
        nosePoke();
    }//end rotate
    }//end translate
    }// end for loop 
}//end if
    translate([gridOffset-1,l/2-1,0]) {
        rotate([0,0,90]){
        cube([slideWallx,gridOffset, width]);
        }
        cube([slideWallx, slideWally, width]);
    }//end translate
    rotate([180,0,0]){
        translate([gridOffset-1,l/2-1,-width]) {
        rotate([0,0,90]){
        cube([slideWallx, gridOffset, width]);
        }
        cube([slideWallx, slideWally, width]);
    }//end translate
}//end rotate

    /*
    translate([-1.5,-l/2-7,0]) {
        rotate([0,0,90]){
        cube([slideWallx, 10, slideWallz]);
        }
        cube([slideWallx, slideWally, slideWallz]);
    }//end translate
*/
}// end module

curve(slideWallz, h, l, dh,holes=1);


translate([50,0,0]){
curve(90, h, l, dh,holes=0);
}//end translate

//curve(width, height, length, dh);





    
    
    
