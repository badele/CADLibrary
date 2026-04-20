include <BOSL2/std.scad>

// Create parkside logo
module parkside_logo()
{
    booleanError = 0.01;

    // Create a parkside parallelogram
    module parallelogram(diag = 1, horiz = 1)
    {
        path = turtle([ "turn", 70, "move", diag, "turn", -70, "move", horiz, "turn", -110, "move", diag ]);
        polygon(path);
    };

    union()
    {
        // Background parallelogram
        color("#222222") linear_extrude(2 * booleanError) parallelogram(12.5, 41.6);

        // 3 bars
        translate([ 7.6, 4, booleanError ]) for (i = [0:2])
        {
            translate([ i * 1.6, 0, 0 ])
            {
                color("red") linear_extrude(2 * booleanError) parallelogram(4.1, 1);
            }
        }

        // Text logo
        color("white") translate([ 7.6 + 4 * 1.6, 4, booleanError ]) linear_extrude(2 * booleanError)
            text("PARKSIDE", size = 3.8, font = "ARIAL");
    }
}
