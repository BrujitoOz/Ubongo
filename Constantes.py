from Figura import CFigura
# Cualquier constante como los colores van aqui
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
PURPLE = (128,0,128)

YTABLERO = 100
YFIGURAS = 300
YPLANTILLA = 400

Figuras = [
    [
        [1,1,0,0], #cuadrado 0
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,0,0,0], #palote(4) 1
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0]
    ],
    [
        [1,0,0,0], #palo(3) 2
        [1,0,0,0],
        [1,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,0,0,0], #palito(2) 3
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,1,0,0], # L grande(4) 4
        [0,1,0,0],
        [0,1,0,0],
        [1,1,0,0]
    ],
    [
        [0,1,0,0], # L(3) 5
        [0,1,0,0],
        [1,1,0,0],
        [0,0,0,0]
    ],
    [
        [0,1,0,0], # L chiquita(2) 6
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,1,0,0], # Tetris1 7
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,0,1,0], # Tetris2 8
        [1,1,1,1],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,1,1,0], # gusano1 9
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,1,1,0], # gusano2 10
        [0,1,0,0],
        [1,1,0,0],
        [0,0,0,0]
    ],
    [
        [0,1,1,0], # P 11
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
]

FigCuadrado = [
    [
        Figuras[0]
    ]
]
FigPalote = [
    [
        Figuras[1]
    ],
    [
        [1,1,1,1], #rotado
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
]
FigPalo = [
    [
        Figuras[2]
    ],
    [
        [1,1,1,0], #rotado
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
]
FigPalito = [
    [
        Figuras[3]
    ],
    [
        [1,1,0,0], #rotado
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
]
FigLGrande = [
    [
        Figuras[4]
    ],
    [
        [1,0,0,0], #rotado
        [1,1,1,1],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,0,0], #rotado
        [1,0,0,0],
        [1,0,0,0],
        [1,0,0,0]
    ],
    [
        [1,1,1,1], #rotado
        [0,0,0,1],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,0,0,0], #invertido
        [1,0,0,0],
        [1,0,0,0],
        [1,1,0,0]
    ],
    [
        [1,1,1,1], #invertido rotado
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,0,0], #invertido rotado
        [0,1,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ],
    [
        [0,0,0,1], #invertido rotado
        [1,1,1,1],
        [0,0,0,0],
        [0,0,0,0]
    ]
]
FigL = [
    [
        Figuras[5]
    ],
    [
        [1,0,0,0], #rotado
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,0,0], # rotado
        [1,0,0,0],
        [1,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,1,0], # rotado
        [0,0,1,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,0,0,0], #invertido
        [1,0,0,0],
        [1,1,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,1,0], #invertido rotado
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,0,0], #invertido
        [0,1,0,0],
        [0,1,0,0],
        [0,0,0,0]
    ],
    [
        [0,0,1,0], #invertido
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
]
FigLChiquita = [
    [
        Figuras[6]
    ],
    [
        [1,0,0,0], # rotada
        [1,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,0,0], # rotada
        [1,0,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,0,0], # rotada
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
]
FigTetris1 = [
    [
        [0,1,0,0],
        [1,1,1,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,0,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,1,1,0],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,1,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,0,0,0]
    ]
]
FigTetris2 = [
    [
        [0,0,1,0],
        [1,1,1,1],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,0,0,0],
        [1,0,0,0],
        [1,1,0,0],
        [1,0,0,0]
    ],
    [
        [1,1,1,1],
        [0,1,0,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,1,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ],
    [
        [0,1,0,0],
        [1,1,1,1],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [1,0,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [1,0,0,0]
    ],
    [
        [1,1,1,1],
        [0,0,1,0],
        [0,0,0,0],
        [0,0,0,0]
    ],
    [
        [0,1,0,0],
        [0,1,0,0],
        [1,1,0,0],
        [0,1,0,0]
    ]
]
F0 = CFigura(FigCuadrado, 1) # cuadrado
F1 = CFigura(FigPalote, 2) # palote
F2 = CFigura(FigPalo, 2) # palo
F3 = CFigura(FigPalito, 2) # palito
F4 = CFigura(FigLGrande, 8) # L grande
F5 = CFigura(FigL, 8) # L
F6 = CFigura(FigLChiquita, 4)
F7 = CFigura(FigTetris1, 4)
F8 = CFigura(FigTetris2, 8)


Plantillas = [
    [
        [1,1,1,1,0], #plantilla 0
        [1,1,1,0,0],
        [0,1,1,1,1]
    ],
    [
        [0,0,1,1], #plantilla 1
        [1,1,1,1],
        [1,1,1,1],
        [0,1,1,0]
    ]
]
Opciones = [
    # para la plantilla 0
    [
        [Figuras[3], Figuras[11], Figuras[5]],#opcion 0: palito, P, L
        [Figuras[5], Figuras[1], Figuras[2]],#opcion 1: L, palote, palo
        [Figuras[8], Figuras[9], Figuras[3]],#opcion 2: tetris2, gusano, palito
        [Figuras[9], Figuras[2], Figuras[7]],#opcion 3: gusano1, palo, tetris1
        [Figuras[4], Figuras[7], Figuras[3]],#opcion 4: L grande, tetris1, palito
        [Figuras[2], Figuras[5], Figuras[9]]#opcion 5: palo, L, gusano1
    ],
    # para la plantilla 1
    [
        [Figuras[9], Figuras[2], Figuras[8]],#opcion 0: gusano1, palo, tetris2
        [Figuras[5], Figuras[11], Figuras[2]],#opcion 1: L, P, palo
        [Figuras[9], Figuras[6], Figuras[11]],#opcion 2: gusano1, L chiquita, P
        [Figuras[0], Figuras[2], Figuras[4]],#opcion 3: cuadrado, palo, L grande
        [Figuras[6], Figuras[10], Figuras[5]],#opcion 4: L chiquita, gusnano2, L
        [Figuras[7], Figuras[11], Figuras[6]]#opcion 5: tetris1, P, L chiquita
    ]
]