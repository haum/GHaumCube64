/****************************************************************
** Distance entre deux tåls (sur l'arrête) : 35cm              **
** Distance entre deux tåls (sur leur fil) : √3 × 35cm ≃ 60 cm **
** Envergure : 171,5 ≃ 172 cm                                  **
** Distance entre deux tåls dans le plan XY: 28,6 cm           **
**                                                             **
** Distances des premiers tåls sur leur fil :                  **
** - rouges (×1)              :          20 cm                 **
** - bleus (×3)               :  40,2 ≃  40 cm                 **
** - vert (×3) & magenta (×3) :  60,4 ≃  60 cm                 **
** - jaunes (×6)              :  80.6 ≃  81 cm                 **
** - cyan (×3)                : 100,8 ≃ 101 cm                 **
** - blancs :                                                  **
**   ⋅ 80.6  ≃  81 cm (×3)                                     **
**   ⋅ 100,8 ≃ 101 cm (×6)                                     **
**   ⋅         121 cm (×6)                                     **
**   ⋅ 141,2 ≃ 141 cm (×3)                                     **
****************************************************************/

/** Verification **/
show_cable = true;
show_support = true;
show_color = true;
distance_cable = 600;
distance_support = 286;
sphere_size = 70;
cable_diameter = 3;

module cable(n, d) {
    // n: Number of tåls
    // d: Distance of the first tål
    h = d + (n - 1) * distance_cable;
    if (show_cable)
        translate([0, 0, -h])
            cylinder(h=h, r=cable_diameter);
    for (i = [0 : n-1]) {
        translate([0, 0, -d - distance_cable * i])
            sphere(d=sphere_size);
    }
}

module support_element() {
    translate([0,-50/2,0])
        cube([3*distance_support+100,50,30]);

    translate([3*distance_support,0,0])
        rotate([0,0,120])
            translate([0,-50/2,0])
                cube([3*distance_support,50,30]);

    translate([distance_support,0,0])
        rotate([0,0,60])
            translate([0,-50/2,0])
                cube([2*distance_support,50,30]);
}

color(show_color ? "red" : "grey")
    cable(4, 200);

color(show_color ? "green" : "grey")
    for (i = [0:2]) {
        rotate([0, 0, 120*i])
        translate([distance_support, 0, 0])
            cable(3, 600);
    }

color(show_color ? "blue" : "grey")
    for (i = [0:2]) {
        rotate([0, 0, 120*i+60])
        translate([distance_support, 0, 0])
            cable(3, 400);
    }

color(show_color ? "cyan" : "grey")
    for (i = [0:2]) {
        rotate([0, 0, 120*i])
        translate([distance_support*2, 0, 0])
            cable(2, 1010);
    }

color(show_color ? "magenta" : "grey")
    for (i = [0:2]) {
        rotate([0, 0, 120*i+60])
        translate([distance_support*2, 0, 0])
            cable(2, 600);
    }

color(show_color ? "yellow" : "grey")
    for (i = [0:5]) {
        rotate([0, 0, 60*i+30])
        translate([distance_support * sqrt(3), 0, 0])
            cable(2, 810);
    }

wd = [1410, 1210, 1010, 810, 1010, 1210];
color(show_color ? "white" : "grey")
    for (i = [0:2]) {
        for (d = [0:5]) {
           rotate([0, 0, i * 120 + d * 20])
              translate([distance_support * (d % 3 == 0 ? 3 : sqrt(7)), 0, 0])
                cable(1, wd[d]);
        }
    }

if (show_support)
    for (i = [0:5]) {
        rotate([0, 0, i * 60])
            color("black")
                support_element();
    }
