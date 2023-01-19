
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
backpanelz = 2.5;

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
pelletD = 7;

/* change this depending on the printer and printer settings
   it is a "tolerance" variable, so holes and fittings can be 
   adjusted.
*/
tol = 0.1;

$fn=30;

%cylinder(d1=headporty/2,d2=headporty/2+5,h=10);
translate([0,0,1]){
cylinder(d1=headporty/2-1,d2=headporty/2+5-1,h=10);
}

//backpanel
//difference(){
//cube([backpanelx,backpanely,backpanelz]);
//translate([45,(backpanely-headporty)/2,]){



cube([headportx,headporty,headportz]);
translate([0,0,-(headporty-10)/2]){
%cylinder(d1=headporty/2,d2=headporty/2+5,h=10);
}//end translate
translate([-irledh,(headporty+irledd)/4,(headportz+irledd)/4]){
rotate([0,90,0]){
cylinder(d=irledd+headportwall*2,h=headporty+irledh*2);
}//end rotate
}//end translate
//}//end translate




//}//end differnece
//headentry



//supporting modules
module irholes(){
    rotate([90,0,0]){
        translate([0,0,0]){
            cylinder(d=irledd+2*tol,h=irledh);
        }//end translate
        translate([0,0,-headporty]){    
            cylinder(d=irledd+2*tol,h=irledh+1);
        }//end translate
     }//end rotate
}//end module ir holes

module irsupports(){
rotate([90,0,0]){
    translate([0,0,headportwall+2]){
ring(irledd+2*tol,2,irledh);
    }//end translate
translate([0,0,-2-headporty+headportwall/2]){    
    ring(irledd+2*tol,2,irledh);
    }//end translate
}//end rotate
}//end module ir holes


/////////////////////////////
module magazine_entry(){
//head port
difference(){
cube([headportx,headporty,headportz]);
    
    
union(){    
translate([headportwall,headportwall,headportwall]){
cube([headportx-headportwall*2,headporty-headportwall*2,headportz]);
}//end translate


// magazine LED entry
translate([-1,14,15]){
    rotate([0,90,0])
    cylinder(d=magledD+2*tol,h=15);
    }//end translate

// pellet dispenser entry
translate([9,14,-6]){
   rotate([0,40,0])
   cylinder(h = 15, d = pelletD);
} //end translate 
    
    
//led side ports
translate([headportx/5+5,headportwall+2,4*headportz/5]){
    irholes();
    }//end translate
}//end union
}//end difference
///////////////////////

union(){
      //translate([4,0,10]){  
      translate([2.3,0,10]){
      pellet_dispenser();
  }// end translate     
}// end union
union(){
translate([headportx/5+5,headportwall+2,4*headportz/5]){
irsupports();
}// end translate
}// end union
union(){
      translate([0,0,0]){
      LED_support();
      }//end translate
  }//end union
}//end magazine_entry

module pellet_dispenser() {

   difference(){
   translate([5,14,-19]){
   rotate([0,38,0])
   cylinder(h = 15, d = pelletD+2);
       } //end translate
   translate([4,14,-20]){
   rotate([0,38,0])
   cylinder(h = 19, d = pelletD); 
     }//end translate 
   translate([7,7,-9.5]){
   rotate([0,0,0])
   cube([12, 12, 12]); 
     }//end translate
}// end difference
//}// end translate
}//end pellet_dispenser

module LED_support() {
    difference() {
        translate([-4,14,15]){
        rotate([0,90,0])
        cylinder(d=magledD+2,h=4);
        }//end translate
            
        translate([-7,14,15]) {
        rotate([0,90,0])
        cylinder(d=magledD+2*tol,h=8);   
        }//end translate
            
    }//end difference
}//end LED_support    
module backpanel(){
difference(){
translate([-(headportx+2*headportwall)/2-30,-backpanely/2+headporty/2,headportz-headportwall-0.90+0.4]){

cube([backpanelx,backpanely,backpanelz]);
    

}
translate([0,0,5]){
cube([headportx,headporty,headportz]);
}//end translate
}//end difference
}//end backpanel

///////////////////////////
//magazine_entry();
//translate([44.5,16,-27.5])
//backpanel();
//pellet_dispenser();
//LED_support();
///////////////////////////


