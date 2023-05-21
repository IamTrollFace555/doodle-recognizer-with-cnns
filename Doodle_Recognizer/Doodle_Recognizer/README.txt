Doodle Recognizer

Universidad del Rosario.
Aprendizaje Automático de Máquina 2023-I.
Juan Nicolás Sepúlveda y Juan Nicolás Quintero. 



# Alguna información aclaratoria:


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
IMPORTANTE: en el archivo predict.py, hay una función llamada setup(). Al final de esta función se carga el modelo desde un archivo "Model.pt"
Es necesario cambiar la ruta del archivo para que se pueda leer correctamente. Es recomendable poner la ruta completa del archivo "Model.pt" 
así esté en la misma carpeta, esto para evitar posibles errores.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



El modelo en esta carpeta está entrenado con 6 clases diferentes:

* 0: Cookie
* 1: Boomerang
* 2: Airplane
* 3: Snail
* 4: Parachute
* 5: Tree


Para interactuar el modelo se debe correr el archivo board.py Este automáticamente creará un tablero que cuenta con los siguientes botones:

* Clear: Borra todos los trazos del tablero
* Save: Guarda la imagen que está dibujada
* Predict: Usa la última imagen que se guardó para hacer una predicción. Luego es necesario presionar el botón "Save" antes de presionar el botón "Predict" para que la predicción funcione bien.



El modelo no es perfecto, así que probablemente se equivoque!

Hemos notado que la clase que le cuesta más predecir es Cookie, la cual confunde bastante con parachute. Las clases que mejor clasifica en nuestra experiencia son "Boomerang" y "Tree".

!!!
Una recomendación importante para darle a las personas que interactúen con el modelo es que hagan sus dibujos grandes. Como la imagen se convierte a formato 28x28, algunas características se pueden perder en la imagen más pequeña.
!!!

Cualquier comentario al respecto al funcionamiento, interfaz y accesibilidad del proyecto será bien recibido!

