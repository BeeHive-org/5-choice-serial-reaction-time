$fn=90;
tol=0.1;

union(){
    difference(){
        union(){
            cylinder(d=50,h=1.5);//original value was 2.25
            //cylinder(d=10,h=5);
        }//end union
        translate([0,0,-1]){
            union(){
                cylinder(d=5+2*tol,h=10);
                for(angle = [0 : 45 : 365-45]){
                rotate([0,0,angle]){
                    translate([18.5,0,0]){
                        cylinder(d=3.8+2*tol,h=5);
                    }//end translate
                }//end rotate
                }//end for 
            }//end union
        }//end translate

    }//end difference
cylinder(d=10,h=5);
}//end union