### Normal Hepta
scad_template = """
module hepta_tubular_cylinder(outer_d, inner_d, length) {{
    difference() {{
        // Outer cylinder
        cylinder(d=outer_d, h=length, $fn=100);

        // Central hole
        translate([0, 0, -1]) cylinder(d=inner_d, h=length + 2, $fn=100);

        // Calculate the radius for the surrounding holes
        r_outer = outer_d / 2;
        r_holes = r_outer * 0.75;

        // Angle between each hole
        angle = 360 / 6;

        // Surrounding holes
        for (i = [0 : 5]) {{
            translate([r_holes * cos(i * angle), r_holes * sin(i * angle), -1])
                cylinder(d=inner_d, h=length + 2, $fn=100);
        }}
    }}
}}

hepta_tubular_cylinder(outer_d={outer_d}, inner_d={inner_d}, length={length});
"""

