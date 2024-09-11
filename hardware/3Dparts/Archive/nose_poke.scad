screwD = 4;

noseHoleD = 12;
noseHoleH = 11;
tolerance = 0.1;

ledDx = 8; // main LED
ledD = 5;
ledH = 6;
wallT = 2;

module nosePokeAttachment(){
    $fn=30;
difference(){
union(){
cylinder(d=noseHoleD+wallT,h=noseHoleH+wallT);
cylinder(d=noseHoleD+2*screwD+7,h=wallT);
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

module nosePoke(){
    $fn=30;
difference(){
union(){
cylinder(d=noseHoleD+wallT,h=noseHoleH+wallT);

translate([0,0,noseHoleH+wallT]){
cylinder(d=ledDx+2,h=ledH-1);
}//end translate


translate([noseHoleD/2+ledH,0,3.5]){
rotate([0,-90,0]){
    cylinder(d=ledD+wallT,h=2*ledH+noseHoleD);
}//end rotate
}//end translate
}//end union


translate([0,0,-1]){
    cylinder(d=noseHoleD,h=noseHoleH);
    cylinder(d=ledDx+2*tolerance,h=ledH+noseHoleH+wallT+5);
}//end translate

translate([-25,0,3.5]){
    rotate([0,90,0]){
        cylinder(d=ledD+2*tolerance,h=50);
}//end rotate
}//end translate


}//end difference
}//end module

  
nosePoke();
 