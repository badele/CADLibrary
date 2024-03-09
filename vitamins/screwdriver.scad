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
//! Screwdriver
//
include <NopSCADlib/utils/core/core.scad>

// screwdriver(270, 150, 37.5, 25, 17, 8);

module screwdriver(total_height, tool_height, max_diam, min_diam, washer_diam, tool_diam) //! Draw a screwdriver
{
    vitamin(str("screwdriver(", total_height, ",", tool_height, ",", max_diam, ",", min_diam, ",", washer_diam, ",",
                tool_diam, ",", "): Screwdriver ", total_height, "x", tool_height));

    // Vars
    handle_color = "#395F8A";
    handle_color1 = "#FC7D16";
    whasher_color = "#222";
    whasher_height = 2;
    cut_diam = 10;
    cut_nb = 6;
    cut_rot = 360 / cut_nb;

    fn = 64;

    // Computes
    handle_height = total_height - tool_height;

    module handle()
    {
        difference()
        {
            difference()
            {
                // handle
                translate([ 0, 0, whasher_height ]) union()
                {
                    // Top handle
                    color(handle_color) translate([ 0, 0, handle_height - whasher_height - max_diam / 2 ])
                        sphere(d = max_diam, $fn = fn);
                    // Main handle
                    color(handle_color)
                        cylinder(h = handle_height - whasher_height - max_diam / 2, d = max_diam, $fn = fn);
                    // Whasher handle
                    color("#222") translate([ 0, 0, -whasher_height ])
                        cylinder(h = whasher_height, d = washer_diam, $fn = fn);
                }
                // Cut bottom handle
                color(handle_color1) rotate_extrude(convexity = 10) translate([ max_diam / 1.6, max_diam / 3, 0 ])
                    circle(max_diam / 5, $fn = fn);
            }
            // Cut main handle
            for (i = [0:cut_nb - 1])
            {
                {
                    color(handle_color1) rotate(i * cut_rot, [ 0, 0, 1 ]) translate([ max_diam / 2, 0, -1 ])
                        cylinder(h = handle_height, d = cut_diam, $fn = fn);
                }
            }
        }
    }

    module tool()
    {
        screw_height = 5;
        paint_height = 10;
        real_tool_height = tool_height - screw_height - paint_height;
        color("#aaa") translate([ 0, 0, -real_tool_height ]) cylinder(h = real_tool_height, d = tool_diam, $fn = 32);
        color("#222") translate([ 0, 0, -real_tool_height - paint_height ])
            cylinder(h = paint_height, d = tool_diam, $fn = 32);
        color("#222") translate([ 0, 0, -tool_height ]) cylinder(h = screw_height, d1 = 0.5, d2 = tool_diam, $fn = 32);
    }

    module object()
    {
        union()
        {
            handle();
            tool();
        }
    }

    object();
}
