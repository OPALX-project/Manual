
[[sec.control.field_output]]

There are two routines that can be used to write out the field used in _opal-cycl_

....
DUMPFIELDS: write out static magnetic field map on a Cartesian grid
DUMPEMFIELDS: write out electromagnetic field map on a 4D grid in space-time
....

==== DUMPFIELDS Command

The `DUMPFIELDS` statement causes _opal-cycl_ to write out static magnetic field data on a 3D cartesian grid.

....
WHAT;                   // Give help on the "WHAT" command
WHAT,NAME=label;        // Show definition of "label"
WHAT,label;             // Shortcut for the second format
....

`label` is an identifier see link:format#sec.format.label[Identifiers or Labels]. If it is non-blank, _OPAL_
displays the object `label` in a format similar to the input statement
that created the object. Entering `WHAT` alone displays help on the
`WHAT` command. Examples:

....
WHAT;
WHAT,NAME=QD;
WHAT,QD;
....




