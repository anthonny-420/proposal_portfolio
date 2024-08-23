sections = ('Libros Clasicos y Modernos.',
            'Ciencia Ficción y Fantasia.',
            'Literatura Contemporanea y Otras Obras Destacadas.'
            )

list_sections = list(sections)
print('Hola bienvenido a libropolis, encontraras tu libro favorito en alguno de estos apartados:\n')

for item in list_sections:
    print(f'- {item}')
print()
print('¿en que apartado literario deseas navegar?')

tuple_sections = tuple(list_sections)
answer = input()

if answer == 'Libros Clasicos y Modernos' or answer == 'libros clasicos y modernos':
    print('se ha encontrado la sección asignada, ¡sigamos!')
    print()

    libros_clasicos_y_modernos = [
        'Don Quijote de la Mancha - Miguel de Cervantes',
        'Cien Años de Soledad - Gabriel García Márquez',
        'Orgullo y Prejuicio - Jane Austen', '1984 - George Orwell',
        'Matar a un Ruiseñor - Harper Lee',
        'El Gran Gatsby - F. Scott Fitzgerald',
        'Ulises - James Joyce',
        'Anna Karenina - León Tolstói',
        'La Metamorfosis - Franz Kafka',
        'En el Camino - Jack Kerouac'
    ]
    for item in libros_clasicos_y_modernos:
        print(f'- {item}')

elif answer == 'Ciencia Ficción y Fantasia' or answer == 'ciencia ficción y fantasia':
    print('se ha encontrado la sección asignada, ¡sigamos!')
    print()

    ciencia_ficción_y_fantasia = [
        'Dune - Frank Herbert',
        'El Señor de los Anillos - J.R.R. Tolkien',
        'Fundación - Isaac Asimov', 'Neuromante - William Gibson',
        'Harry Potter y la Piedra Filosofal - J.K. Rowling',
        'Canción de Hielo y Fuego (Saga Juego de Tronos) - George R.R. Martin',
        'La Guía del Autoestopista Galáctico - Douglas Adams',
        'Crónicas Marcianas - Ray Bradbury',
        'El Fin de la Infancia - Arthur C. Clarke',
        'El Ciclo de la Puerta de la Muerte - Margaret Weis y Tracy Hickman'
    ]
    for item in ciencia_ficción_y_fantasia:
        print(f'- {item}')

elif answer == 'Literatura Contemporanea y Otras Obras Destacadas' or answer == 'literatura contemporanea y otras obras destacadas':
    print('se ha encontrado la sección asignada, ¡sigamos!')
    print()

    literatura_c_y_d = [
        'Los Juegos del Hambre - Suzanne Collins',
        'La Sombra del Viento - Carlos Ruiz Zafón',
        'El Niño con el Pijama de Rayas - John Boyne',
        'La Ladrona de Libros - Markus Zusak',
        'El Alquimista - Paulo Coelho',
        'Tokio Blues - Haruki Murakami',
        'El Código Da Vinci - Dan Brown',
        'Las Ventajas de Ser Invisible - Stephen Chbosky',
        'La Casa de los Espíritus - Isabel Allende',
        'Los Pilares de la Tierra - Ken Follett'
    ]
    for item in literatura_c_y_d:
        print(f'- {item}')

else:
    print(f'el valor {answer} no fue encontrado')

book = input('¿que libro vas a leer?')
print()
if book in libros_clasicos_y_modernos or book in ciencia_ficción_y_fantasia or book in literatura_c_y_d:
    print(f'El libro {book} es una gran obra literaria')
