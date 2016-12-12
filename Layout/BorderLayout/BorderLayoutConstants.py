from java.awt import BorderLayout

width = max( [ len( name ) for name in dir( BorderLayout ) ] )

values = {}

for name in dir( BorderLayout ) :
    if name == name.upper() :
        value = eval( 'BorderLayout.%s' % name )
        if values.has_key( value ) :
            values[ value ].append( name )
        else :
            values[ value ] = [ name ]

names = values.keys()
names.sort()

name_width = max( [ len( name ) for name in names ] )
for name in names :
    print '%*s :' % ( -name_width, name ),
    values[ name ].sort()
    print ', '.join( values[ name ] )
