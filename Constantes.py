from Figura import Figura
from Plantilla import Plantilla
# Cualquier constante como los colores van aqui
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
ORANGE = (255,165,0)
YELLOW = (255,255,0)
PURPLE = (128,0,128)

TAMANIOFIGURA = 20
YTABLERO = 100
YFIGURAS = 300
YPLANTILLA = 400
XINICIAL = 30

figura0 = Figura("Cuadrado", [
    [
        [1,1],
        [1,1]
    ]
])
figura1 = Figura("palote",[
    [
        [1],
        [1],
        [1],
        [1]
    ],
    [
        [1,1,1,1]
    ]
])
figura2 = Figura("palo",[
    [
        [1],
        [1],
        [1]
    ],
    [
        [1,1,1]
    ]
])
figura3 = Figura("palito",[
    [
        [1],
        [1]
    ],
    [
        [1,1]
    ]
])
figura4 = Figura("L grande", [
    [
        [1,0],
        [1,0],
        [1,0],
        [1,1]
    ],
    [
        [1,1,1,1],
        [1,0,0,0]
    ],
    [
        [1,1],
        [0,1],
        [0,1],
        [0,1]
    ],
    [
        [0,0,0,1],
        [1,1,1,1]
    ],
    [
        [0,1],
        [0,1],
        [0,1],
        [1,1]
    ],
    [
        [1,0,0,0],
        [1,1,1,1],
    ],
    [
        [1,1],
        [1,0],
        [1,0],
        [1,0]
    ],
    [
        [1,1,1,1],
        [0,0,0,1]
    ]
])
figura5 = Figura("L",[
    [
        [0,1],
        [0,1],
        [1,1]
    ],
    [
        [1,0,0],
        [1,1,1]
    ],
    [
        [1,1],
        [1,0],
        [1,0]
    ],
    [
        [1,1,1],
        [0,0,1]
    ],
    [
        [1,0],
        [1,0],
        [1,1]
    ],
    [
        [1,1,1],
        [1,0,0]
    ],
    [
        [1,1],
        [0,1],
        [0,1]
    ],
    [
        [0,0,1],
        [1,1,1]
    ]
])
figura6 = Figura("L chiquita", [
    [
        [0,1],
        [1,1]
    ],
    [
        [1,0],
        [1,1]
    ],
    [
        [1,1],
        [1,0]
    ],
    [
        [1,1],
        [0,1]
    ]
])
figura7 = Figura("tetris1", [
    [
        [0,1,0],
        [1,1,1]
    ],
    [
        [1,0],
        [1,1],
        [1,0]
    ],
    [
        [1,1,1],
        [0,1,0]
    ],
    [
        [0,1],
        [1,1],
        [0,1]
    ]
])
figura8 = Figura("tetris2", [
    [
        [0,0,1,0],
        [1,1,1,1]
    ],
    [
        [1,0],
        [1,0],
        [1,1],
        [1,0]
    ],
    [
        [1,1,1,1],
        [0,1,0,0]
    ],
    [
        [0,1],
        [1,1],
        [0,1],
        [0,1]
    ],
    [
        [0,1,0,0],
        [1,1,1,1]
    ],
    [
        [1,0],
        [1,1],
        [1,0],
        [1,0]
    ],
    [
        [1,1,1,1],
        [0,0,1,0]
    ],
    [
        [0,1],
        [0,1],
        [1,1],
        [0,1]
    ]
])
figura9 = Figura("gusano1", [
    [
        [0,1,1],
        [1,1,0]
    ],
    [
        [1,0],
        [1,1],
        [0,1]
    ],
    [
        [0,1],
        [1,1],
        [1,0]
    ],
    [
        [1,1,0],
        [0,1,1]
    ]
])
figura10 = Figura("gusano2", [
    [
        [0,1,1],
        [0,1,0],
        [1,1,0]
    ],
    [
        [1,0,0],
        [1,1,1],
        [0,0,1]
    ],
    [
        [1,1,0],
        [0,1,0],
        [0,1,1]
    ],
    [
        [0,0,1],
        [1,1,1],
        [1,0,0]
    ]
])
figura11 = Figura("p", [
    [
        [0,1,1],
        [1,1,1]
    ],
    [
        [1,0],
        [1,1],
        [1,1]
    ],
    [
        [1,1,1],
        [1,1,0]
    ],
    [
        [1,1],
        [1,1],
        [0,1]
    ],
    [
        [1,1],
        [1,1],
        [1,0]
    ],
    [
        [1,1,1],
        [0,1,1]
    ],
    [
        [0,1],
        [1,1],
        [1,1]
    ],
    [
        [1,1,0],
        [1,1,1]
    ]
])

plantilla1 = Plantilla( [
    [0,0,0,0,1],
    [0,0,0,1,1],
    [1,0,0,0,0]
    ],
    [
        [figura5, figura1, figura2],
        [figura3, figura11, figura5],
        [figura8, figura9, figura3],
        [figura9, figura2, figura7],
        [figura4, figura7, figura3],
        [figura2, figura5, figura9]
    ]
)
plantilla2 = Plantilla( [
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [1,0,0,1]
    ],
    [
        [figura5, figura11, figura2],
        [figura9, figura2, figura8],
        [figura9, figura6, figura11],
        [figura0, figura2, figura4],
        [figura6, figura10, figura5],
        [figura7, figura11, figura6]
    ]
)
Plantillas = [plantilla1, plantilla2]