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
        [1,1,1,0]
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

Plantillas = [
    [
        [1,1,1,1,0], #plantilla 1
        [1,1,1,0,0],
        [0,1,1,1,1]
    ],
    [
        [0,0,1,1], #plantilla 2
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