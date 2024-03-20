//!
//! Phole holder
//!
// ! 1. Use a wooden curtain rod to make a telephone stand (to film a piano player)
//!
include <../../../vitamins/plywood.scad>
include <../../../vitamins/wood_cylinder.scad>
include <NopSCADlib/lib.scad>

b1_width = 300;
b2_width = 150;
rode_diameter = 28;
rode_height = 1500;
plank_nbply = 7;
plank_depth = 15;

//!
//! 1. Cut the plank to make a base
//!
module base1_assembly() assembly("base1")
{
    translate_z(plank_depth / 2) plywood_plank(plank_nbply, b1_width, b1_width, plank_depth);
}

//!
//! 1. Glue two planks to make a thicker base (150x150)
//!
module base2_assembly() assembly("base2")
{
    translate_z(plank_depth / 2 + plank_depth) plywood_plank(plank_nbply, b2_width, b2_width, plank_depth);
    translate_z(plank_depth / 2 + 2 * plank_depth) plywood_plank(plank_nbply, b2_width, b2_width, plank_depth);
}

//!
//! 1. Glue base1 and base2
//!
module base_assembly() assembly("base")
{
    difference()
    {
        union()
        {
            base2_assembly();
            base1_assembly();
        }
        translate_z(-1) cylinder(h = plank_depth * 3 + 2, d = rode_diameter);
    }
}

//!
//! 1. Create hole with the rod diameter
//! 1. Create two holes for the camera vision
//!
module support_assembly() assembly("support")
{
    difference()
    {
        plywood_plank(plank_nbply, b2_width, b1_width, plank_depth);
        // Camera hole
        hull()
        {
            translate([ b2_width / 2 - rode_diameter, b2_width - rode_diameter, -plank_depth / 2 - 1 ])
                cylinder(h = plank_depth + 2, d = rode_diameter);
            translate([ -b2_width / 2 + rode_diameter, b2_width - rode_diameter, -plank_depth / 2 - 1 ])
                cylinder(h = plank_depth + 2, d = rode_diameter);
            translate([ b2_width / 2 - rode_diameter, b2_width - 2 * rode_diameter, -plank_depth / 2 - 1 ])
                cylinder(h = plank_depth + 2, d = rode_diameter);
            translate([ -b2_width / 2 + rode_diameter, b2_width - 2 * rode_diameter, -plank_depth / 2 - 1 ])
                cylinder(h = plank_depth + 2, d = rode_diameter);
        }
        // support hole
        translate([ -b2_width / 2 + rode_diameter, -b2_width + rode_diameter, -plank_depth / 2 - 1 ])
            cylinder(h = plank_depth + 2, d = rode_diameter);
    }
}

//!
//! A wooden rod
//!
module rod_assembly() assembly("rod")
{
    wood_cylinder(nb_ply = 7, height = rode_height, diameter = rode_diameter);
}

//!
//! 1. Assemble all
//!
module main_assembly() assembly("main")
{
    base_assembly();
    translate_z(rode_height / 2) rod_assembly();
    translate([ b2_width / 2 - rode_diameter, b2_width - rode_diameter, rode_height - 2 * plank_depth ])
        support_assembly();
}

if ($preview)
    main_assembly();
