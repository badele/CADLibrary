//
// CADLibrary Copyright Bruno Adelé 2024
// brunoadele@gmail.com
// blog.jesuislibre.org
//
// This file is part of CADLibrary.
//
// CADLibrary is free software: you can redistribute it and/or modify it under the terms of the
// GNU General Public License as published by the Free Software Foundation, either version 3 of
// the License, or (at your option) any later version.
//
// CADLibrary is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
// without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
// See the GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License along with CADLibrary.
// If not, see <https://www.gnu.org/licenses/>.
//
//! Parkside Magnetic bar
//
include <NopSCADlib/utils/core/core.scad>
include<../logo/parkside.scad>
use <NopSCADlib/utils/round.scad>

function mth_width(type) = type[2];         //! magnetbar width
function mth_depth(type) = type[3];         //! magnetbar depth
function mth_height(type) = type[4];        //! magnetbar height
function mth_padding(type) = type[5];       //! magnetbar padding
function mth_metaltickness(type) = type[6]; //! magnetbar metaltickness

// Source: https://www.lidl.be/p/fr-BE/porte-outils-magnetique-parkside/p100370664
module magnet_bar(type) //! Draw a parkside magnet bar
{
    vitamin(str("magnet_bar(", type[0], "): Magnetbar ", type[1]));

    width = mth_width(type);
    height = mth_height(type);
    depth = mth_depth(type);
    padding = mth_padding(type);
    metaltickness = mth_metaltickness(type);

    radius_hole = 4;
    logo_size = 24;
    metal_color = "#222222";
    hole_color = "#aaaaaa";

    module mth_shape_support()
    {
        color(metal_color) rotate([ -90, 0, 90 ]) linear_extrude(width, center = true, convexity = 4)
            round(metaltickness / 4) difference()
        {
            square([ depth, mth_height(type) ], center = true);
            translate([ 0, -metaltickness, 0 ]) square([ depth - 2 * metaltickness, height ], center = true);
        }
    }

    module mth_magnet()
    {

        color(metal_color) rotate([ -90, 0, 0 ]) linear_extrude(depth - 2 * metaltickness, center = true)
            round(metaltickness) square([ width - 2 * padding, height - 1 ], center = true);
    }

    module object()
    {

        difference()
        {
            union()
            {
                mth_shape_support();
                mth_magnet();
            }

            for (dir = [ -1, 1 ])
                translate([ dir * (width / 2 - radius_hole - 2.5), 0, (-height + metaltickness) / 2 ]) color(hole_color)
                    cylinder(h = 2 * metaltickness, r = radius_hole, center = true);
        }

        // logo
        translate([ width / 2 - 2 * padding - logo_size, -depth / 2 + metaltickness, height / 2 ]) parkside_logo();
    }

    object();
}
