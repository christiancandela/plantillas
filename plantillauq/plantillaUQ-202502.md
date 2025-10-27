---
marp: true
header: <div class="encabezado"><img src='franjaSuperior.png'  /></div>
footer: '![image](franjaInferior.png)' 
_header: '' 
_footer: '' 
paginate: true
_paginate: false
_backgroundImage: url('fondo.png')
style: |

  .encabezado {
    position: relative; left: 0; top:0;display: inline-block; text-align: center;
  }
  .titulo {
    position: absolute; top: 40%; left: 50%; transform: translate(0%, -50%); color: gray;
  }
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  
  h1 { 
    color: black; 
    position: absolute;
    left: 0;
    top: 40%;
    background-color: rgb(212, 231, 205);
    width: 100%;
    display: table-cell;
    text-align: center;
    padding: 30px 0;
    font-weight: bold; 
  }

  h2 {
    position: absolute; top: 40px; left: 653px; color: black;
    font-size: 22pt
  }

---

<div style="position: absolute; left: 45%; top:20%; background-color: rgb(212, 231, 205); width: 550px; display:table-cell; text-align: center; padding: 30px 0;">
<b>
<h3>OTRO TITULO</h3>
</b>
</div>

<div style="position: absolute; left: 30%; top:45%; width: 70%; text-align: left"><h3 style="color: gray">TITULO PRESENTACION</h3></div>
<div style="position: absolute; left: 30%; top:55%; width: 70%; text-align: left"><h5 style="color: gray">Autor</h5></div>

<div style="position: absolute; left: 93%; top:10px; ">

![width:80](licencia.png)
</div>

---

<!-- 
_header: ''
_footer: ''
-->

![bg](fondo.png)

<div style="position: absolute; left: 45%; top:20%; background-color: rgb(212, 231, 205); width: 550px; display:table-cell; text-align: center; padding: 30px 0;">
<b>
<h3>OTRO TITULO</h3>
</b>
</div>

<div style="position: absolute; left: 30%; top:45%; width: 70%; text-align: left"><h3 style="color: gray">TITULO PRESENTACION</h3></div>
<div style="position: absolute; left: 30%; top:55%; width: 70%; text-align: left"><h5 style="color: gray">Autor</h5></div>

<div style="position: absolute; left: 93%; top:10px; ">

![width:80](licencia.png)
</div>

---


<!-- 
_header: ''
_footer: ''
-->

![bg](fondo.png)

<div style="position: absolute; left: 45%; top:20%; background-color: rgb(212, 231, 205); width: 550px; display:table-cell; text-align: center; padding: 30px 0;">
<b><h3>OTRO TITULO</h3></b>
</div>

<div style="position: absolute; left: 30%; top:45%; width: 70%; text-align: left"><h3 style="color: gray">TITULO PRESENTACION</h3></div>
<div style="position: absolute; left: 30%; top:55%; width: 70%; text-align: left"><h5 style="color: gray">Autor</h5></div>

<div style="position: absolute; left: 93%; top:10px; ">

![width:80](licencia.png)
</div>

---


## Titulo temporal

### Prueba

---

## Fijanfo un Titulo

### Prueba

---



## Imagen flotante

- uno
- dos
- tres
- cuatro
- cinco
- seis
- ocho

<div style="position: absolute; left: 50%; top:140px; ">

![](imagen.png)
</div>

---

<style scoped>
img[alt~="center"] {
  display: block;
  margin: 0 auto;
}
</style>

## Imagen centrada

- uno




![Alt center width:400px](imagen.png)

---

## Dos columnas con texto a la derecha

<div class="columns">
  <div>

  ![](imagen.png)
  </div>
  <div>

  ### Dos columnas con texto a la derecha

  - 1
  - 2

  </div>
</div>

---

<style scoped>
  section{
    font-size: 30pt
  }
</style>

## Dos columnas con texto a la izquierda

<div class="columns">
  <div>

  ### Dos columnas con texto a la izquierda

  - Es posible cambiar el tamaño de la fuente 
  - 2

  </div>
  <div>

  ![](imagen.png)

  </div>
</div>

---


# Sub titulo


---

## Dos filas, tres columnas

<div class="rows">
  <div class="columns" style="grid-template-columns: repeat(3, minmax(0, 1fr));">
  <div>
  
   - Col 1
  </div>
  <div>
  
   - Col 2
  </div>
  <div>
  
   - Col 3
  </div>
  </div>
  <div class="columns" style="grid-template-columns: repeat(3, minmax(0, 1fr));">
  <div>

  ![height:200](imagen.png)
  </div>
  <div>

  ![height:200](imagen.png)
  </div>
  <div>

  ![height:200](imagen.png)
  </div>
  </div>
</div>

---

<!-- 
_header: ''
_footer: '' 
_paginate: false
-->
![bg](gracias.png)


---

<!-- 
_header: ''
_footer: '' 
_paginate: false
_backgroundImage: url('gracias.png')
-->
