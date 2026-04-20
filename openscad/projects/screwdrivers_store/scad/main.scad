//!
//! screwdrivers support
//!
//! The screwdrivers store with french cleat support
//!
include <../../../vitamins/french_cleats.scad>
include <../../../vitamins/plywood.scad>
include <../../../vitamins/screwdriver.scad>
include <NopSCADlib/lib.scad>

sd_support_height = 70;
fc_height = 50;
plank_nbply = 7;
plank_depth = 15;
posx_hole = 50;

// TODO: create utils function
function cumsum(v) = [for (a = v[0] - v[0], i = 0; i < len(v); a = a + v[i], i = i + 1) a + v[i]];

//!
//! 1. cut the plywood and external cut at 45°
//!
module wall_frenchcleat_assembly() assembly("wall_frenchcleat")
{
    rotate([ 0, 90, 90 ]) translate([ -fc_height / 2, 0, sd_support_height / 2 + 3 * plank_depth / 2 ])
        french_cleat(frenchcleat_opt, sd_support_width, 50, plank_depth, bottom = true, nb_ply = 7);
}

module wall_support_assembly() assembly("wall_support", ngb = true)
{
    translate([ 0, sd_support_height / 2 + plank_depth / 2, 0 ]) rotate([ 90, 0, 0 ])
        plywood_plank(plank_nbply, sd_support_width, 100, plank_depth);
}

//!
//! 1. cut the plywood
//! 1. drill holes
//!
module screwdriver_support_assembly() assembly("screwdriver_support")
{
    holespos = [ 20, 40, 35, 35, 35, 35, 35, 35 ];
    holesdiam = [ 12, 8, 8, 8, 8, 8, 8, 8 ];

    difference()
    {
        plywood_plank(plank_nbply, sd_support_width, sd_support_height, plank_depth);

        // Holes
        sumpos = cumsum(holespos);
        for (i = [0:len(holespos) - 1])
        {
            translate([ -sd_support_width / 2 + sumpos[i], 0, 0 ]) cylinder(h = 16, d = holesdiam[i], center = true);
        }
    }
}

//!
//! 1. Center the screwdriver support on the wall support
//! 1. Tighten screws
//!
module support_assembly() pose([ 95, 0, 125 ]) assembly("support")
{
    explode([ 0, 60, 0 ], true) wall_support_assembly();
    screwdriver_support_assembly();

    explode([ 0, 100, 0 ], true)
    {
        translate([ sd_support_width / 2 - posx_hole, sd_support_height / 2 + plank_depth, 0 ]) rotate([ -90, 0, 0 ])
            screw(No632_pan_screw, 40);
        translate([ -sd_support_width / 2 + posx_hole, sd_support_height / 2 + plank_depth, 0 ]) rotate([ -90, 0, 0 ])
            screw(No632_pan_screw, 40);
    }
}

//!
//! 1. Attach french cleat to the wall
//!
module frenchcleat_assembly() pose([ 95, 0, 125 ], exploded = true) assembly("frenchcleat")
{
    support_assembly();
    explode([ 0, 60, 0 ], true) wall_frenchcleat_assembly();

    explode([ 0, 100, 0 ], true)
    {
        translate([ sd_support_width / 2 - posx_hole, sd_support_height / 2 + 2 * plank_depth, fc_height / 2 ])
            rotate([ -90, 0, 0 ]) screw(No632_pan_screw, 25);
        translate([ -sd_support_width / 2 + posx_hole, sd_support_height / 2 + 2 * plank_depth, fc_height / 2 ])
            rotate([ -90, 0, 0 ]) screw(No632_pan_screw, 25);
    }
}

module screwdrivers()
{
    translate([ -sd_support_width / 2 + 20, 0, 0 ]) screwdriver(270, 150, 37.5, 25, 17, 8);
    translate([ -sd_support_width / 2 + 60, 0, 0 ]) screwdriver(240, 125, 34.5, 23, 15.5, 5.5);
    translate([ -sd_support_width / 2 + 95, 0, 0 ]) screwdriver(210, 100, 28.5, 19, 14.2, 4.5);
    translate([ -sd_support_width / 2 + 130, 0, 0 ]) screwdriver(210, 100, 28.5, 19, 13.5, 4.5);
    translate([ -sd_support_width / 2 + 200, 0, 0 ]) screwdriver(210, 100, 28.5, 19, 13.5, 4.5);
}

//!
//! Assembly instructions
//!
module main_assembly() assembly("main")
{
    frenchcleat_assembly();
    screwdrivers();
}

if ($preview)
    main_assembly();
