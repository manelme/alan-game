# Al-Ándalus Programación y Computación 2 - Alan-game

## Intalación y cosas que hacer primero

Lo ideal es que una vez tengas instalado Python3 y Pip3 instales virtualenv, porque sino todas las dependencias que instalemos con pip se instalan de manera global y eso es un carajo, por lo que te dejo las ordenes para instalar y usar virtualenv :P

### Toda la pesca que hacer si estás con Ubuntu

```sh
sudo apt-get install python3-pip
sudo pip3 install virtualenv 

virtualenv venv #Asi se crea por primera vez el virtualenv, en este caso se llama venv, pero le puedes llamar como te de la gana.
```

Veras que cuando ejecutas la orden se te crea una varpeta llamada venv, todas las dependencias se trasladarán hay, para entrar y salir en el virtualenv tienes que usar estas ordenes

```sh
venv/bin/activate #Esto para activarlo estando dentro de la carpeta principal del proyecto

deactivate #Para salir del venv y volver a tu terminal normal :P
```

Todo esto debería de ser igual para Windows o cualquier sistema operativo excepto la parte del apt-get que es de Ubuntu :).

## Scaffolding

Habrá una carpeta con las src y con otra con los test. Ya te contaré :P

## Hacer funcionar test

Para que los test funcionen hay que lanzar la siguiente orden con la clase que se va a testear y el test en la misma carpeta. Es importante que tengamos activado el venv primero

```sh
python -m unittest -v instituto_test.py
```

## Modelo a implementar

Meto un diagrama UML para tenerlo como referencia para implementar, pongo una versión preliminar.

![Diagrama de Clases](./out/DiagramaClases/DiagramaClases.png)