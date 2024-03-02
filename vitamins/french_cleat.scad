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

include <NopSCADlib/utils/core/core.scad>
use <NopSCADlib/utils/round.scad>

module french_cleat(type, height, depth, width, bottom = true) //! Draw a french cleat
{
    direction = bottom ? "Bottom" : "Top";

    vitamin(str("french_cleat(", type[0], ",", height, ",", depth, ",", width, ",", bottom, "): ", direction,
                " french cleat ", type[1], " ", height, "x", depth, "x", width));

    module fc_shape()
    {
        bottomright = type[0] == "std" ? 0 : depth;
        rotatez = bottom ? 0 : 180;

        color("#C49769") rotate([ 0, 0, rotatez ]) translate([ -depth / 2, -height / 2 ])
            linear_extrude(width, center = true)
                polygon([ [ 0, 0 ], [ depth, bottomright ], [ depth, height ], [ 0, height - depth ] ]);
    }

    module object()
    {
        fc_shape();
    }

    object();
}
