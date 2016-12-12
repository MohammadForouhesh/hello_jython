def classes( Class, pad = '' ) :
    print pad + str( Class )
    for base in Class.__bases__ :
        classes( base, pad + '| ' )
