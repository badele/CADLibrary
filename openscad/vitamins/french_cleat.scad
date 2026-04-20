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
//! French Cleat
//

include <./plywood.scad>
include <NopSCADlib/utils/core/core.scad>

module french_cleat(type, width, height, depth, bottom = true, nb_ply = 7) //! Draw a french cleat
{
    booleanerror = 0.02;
    direction = bottom ? "Bottom" : "Top";

    vitamin(str("french_cleat(", type[0], ",", width, ",", height, ",", depth, ",", bottom, "): ", direction,
                " french cleat ", type[1], " ", width, "x", height, "x", depth));

    module fc_shape()
    {

        isoptimised = type[0] == "opt";
        rotatez = bottom ? 0 : -180;

        virtualwidth = width + booleanerror;
        virtualheight = height + booleanerror;
        virtualdepth = depth + booleanerror;

        rotate([ rotatez, 0, rotatez ]) difference() difference()
        {
            plywood_plank(nb_ply, height, width, depth);

            color("#ead2aa") rotate([ 0, 90, -90 ])
                translate([ -virtualdepth / 2, -virtualdepth / 2 - height / 2 + depth / 2, 0 ])
                    right_triangle(virtualdepth, virtualdepth, virtualwidth);

            // Easier to design, as there's no need to recut at right angles.
            if (isoptimised)
            {
                color("#ead2aa") rotate([ 90, 0, 180 ]) translate([ -virtualheight / 2, -virtualdepth / 2, 0 ])
                    right_triangle(virtualdepth, virtualdepth, virtualwidth);
            }
        }
    }

    module object()
    {
        fc_shape();
    }

    object();
}
