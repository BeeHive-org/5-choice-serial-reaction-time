screwD = 4;

noseHoleD = 12;
noseHoleH = 20;
tolerance = 0.1;

ledD = 5;
ledH = 6;
wallT = 1;

backWallL = 240;
backWallD = 250;
pokeAreaH = 80;
module nosePoke(){
    $fn=30;
difference(){
union(){
cylinder(d=noseHoleD+wallT,h=noseHoleH+wallT);
cylinder(d=noseHoleD+2*screwD+7,h=wallT);
translate([0,0,noseHoleH+wallT]){
cylinder(d=ledD+2,h=ledH);
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
cylinder(d=ledD,h=ledH+noseHoleH+wallT+5);
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
cylinder(d=screwD,h=10);
}//end translate

translate([0,-(noseHoleD)/2-screwD,-1]){
cylinder(d=screwD,h=10);
}//end translate
}//end difference
}//end module



module backWall(){
    difference([]){
    %cylinder(d=backWallD,h=50,$fn=10);
    
    union(){
    translate([0,0,-1]){
    cylinder(d=backWallD-15,h=52,$fn=10);
        
    }//end transalte
    translate([-backWallD/2,0,-1]){
    %cube([backWallD+4,backWallD,52]);
    }//end translate
}//end union
}//end difference
    }//end module
backWall(); 
  translate([0,-(backWallD)/2+20,0]){ 
     rotate([90,0,0]){ 
    cylinder(d=noseHoleD+wallT,h=20);
     }//end rotate
  }//end translate