//////////////////////////////////////////
//adapter to connect an acrylic tube that 
// connects the home box with the testing 
// box
// CC BY SA 4.0
//////////////////////////////////////////

//cylinder(10,10,25, $fn = 200);

/* **** Common parameters **** */

Smoothness = 200; 
ring_in_d = 51; // inner diameter of outer ring

/* **** Outer ring parameters **** */

out_ring_d = 72;  // diameter
out_ring_h = 12;  // height
out_ring_z_disp = -2; //z axis displacement

/* **** Inner ring parameters **** */

in_ring_h = 5.5;  // height
in_ring_in_d = 44; // inner diameter of inner ring



/*module doorhole(){
 translate([]){   
 cylinder(50,50,10, $fn = Smoothness);   
    
    
}}*/





module outerring(){
  translate([0,0,out_ring_z_disp]){
 cylinder(out_ring_h, d=out_ring_d, $fn = Smoothness);   
    
    
}}




module outerring2(){
      translate([0,0,out_ring_z_disp-1]){

     cylinder(out_ring_h+abs(out_ring_z_disp), d=ring_in_d, $fn = Smoothness);   
}
}




module innerring1(){
   translate([0,0,out_ring_h-abs(out_ring_z_disp)]){ 
 cylinder(in_ring_h, d=ring_in_d, $fn = Smoothness);   
    
   }
}

module innerring2(){
   translate([0,0,out_ring_h-abs(out_ring_z_disp)-1]){ 
 cylinder(out_ring_h, d=in_ring_in_d, $fn = Smoothness);   
    
   }
}

difference(){
    outerring();
    outerring2();
}

difference(){
    innerring1();
    innerring2();
}