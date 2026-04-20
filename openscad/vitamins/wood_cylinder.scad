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
//! Wood cylinder
//
include <NopSCADlib/utils/core/core.scad>

function nb_1th(nb_ply) = ceil(nb_ply / 2);
function nb_2nd(nb_ply) = 7 - nb_1th(nb_ply);
function realstep(nb_ply) = nb_ply + nb_2nd(nb_ply);
function posz(idx, ply1th, ply2nd) = ceil(idx * 0.5) * ply1th + ceil(max(0, idx * 0.5 - 0.5)) * ply2nd;

module wood_cylinder(nb_ply, height, diameter) //! Draw a wood cylinder
{
    vitamin(str("wood_cylinder(", nb_ply, ",", height, ",", diameter, "):", nb_ply, " Plies wood cylinder ", height, "x", diameter," mm"));

    ply1th = diameter / realstep(nb_ply); // tickness (shortest)
    ply2nd = ply1th * 2;           // tickness (biggest)

    color1th = "#ead2aa";
    color2nd = "#c0a680";

    module slice_cylinder(h, d,thickness, color)
    {
        difference()
        {
            color(color) cylinder(h, d=d,center=true);
            color(color) cylinder(h+2, d=d-thickness,center=true);
        }
    }

    module wcylinder()
    {
        for (i = [0:nb_ply - 1])
        {
            if (i % 2 == 0)
            {
                color(color1th) slice_cylinder(height,diameter-posz(i, ply1th, ply2nd),ply1th);
            }
            else
            {
                color(color2nd) slice_cylinder(height,diameter-posz(i, ply1th, ply2nd),ply2nd);
            }
        }
    }

    module object()
    {
        wcylinder();
    }

    object();
}
