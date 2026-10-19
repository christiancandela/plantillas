---
marp: true
theme: uq
paginate: true
_paginate: false

---

<!-- _class: lead -->

# TITULO DE LA PRESENTACIÓN <br/> Subtitulo
##
##
##
##
## Arquitectura Basada en Microservicios
**Área de infraestructura
Programa de Ingeniería de Sistemas y Computación
Facultad de Ingeniería**

<div style="position: absolute; left: 93%; top:10px; ">

![width:80](https://raw.githubusercontent.com/christiancandela/plantillas/main/plantillauq/licencia.png)
</div>

---

# Otro elemento

![center small](https://raw.githubusercontent.com/christiancandela/plantillas/main/plantillauq/licencia.png)

---

<!-- _class: titulo -->

# Prueba

---

<!-- _class: titulo h1-left -->

# Prueba

---

<!-- _class: titulo h1-right -->

# Prueba

---

<!-- _class: columns-2 -->
# columns-2

## Titulo 
- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc

---

<!-- _class: columns-2 h2-center -->

# columns-2 h2-center

## Titulo 
- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc


---

<!-- _class: columns-2-grid -->
# columns-2-grid 

## Titulo 

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

---

<!-- _class: columns-2-grid h2-center -->
# columns-2-grid h2-center

## Titulo 

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

---

<!-- _class: columns-3 -->
# columns-3

## Titulo 
- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc

---

<!-- _class: columns-3 h2-center -->

# columns-3 h2-center

## Titulo 
- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc


---

<!-- _class: columns-3-grid -->
# columns-3-grid 

## Titulo 

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

---

<!-- _class: columns-3-grid h2-center -->
# columns-3-grid h2-center

## Titulo 

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

---


<!-- _class: columns-4 -->
# columns-4

## Titulo 
- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc

---

<!-- _class: columns-4 h2-center -->

# columns-4 h2-center

## Titulo 
- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc


---

<!-- _class: columns-4-grid -->
# columns-4-grid 

## Titulo 

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

---

<!-- _class: columns-4-grid h2-center -->
# columns-4-grid h2-center

## Titulo 

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

---

<!-- _class: columns-flex  -->

# columns-flex

## prueba 

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

---



<!-- _class: columns-flex h2-center -->

# columns-flex h2-center

## prueba 

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

<div>

- una opcion 
- dos opciones
- tres opciones
- cuatro opciones
- cinco opciones
- etc
</div>

---

# Stack de Observabilidad Completo

<div class="mermaid" style="text-align: center; max-width: 400px; margin: 0 auto;">
graph TB
    subgraph SERVICIOS["Microservicios"]
        EMP["👥 empleados\n/metrics + logs + trazas"]
        DEP["🏢 departamentos\n/metrics + logs + trazas"]
        AUTH["🔐 auth\n/metrics + logs + trazas"]
    end
    PROM["📊 Prometheus\nMétricas (Pull)"] -->|Scraping| SERVICIOS
    LOKI["🗂️ Loki\nLogs (Push)"]
    PROMTAIL["📋 Promtail"] -->|Recolecta| SERVICIOS
    PROMTAIL -->|Push| LOKI
    ZIPKIN["🔍 Zipkin / Jaeger\nTrazas (Push)"]
    SERVICIOS -->|OTel SDK| ZIPKIN
    GRAFANA["📈 Grafana\nVisualiza y alerta"] -->|PromQL| PROM
    GRAFANA -->|LogQL| LOKI
    GRAFANA -->|Alerta| NOTIF["🔔 Discord / Telegram"]
</div>

---

# Stack de Observabilidad Completo

<div class="mermaid" style="text-align: center; --diagrama-alto: 500px;">
graph TB
    subgraph SERVICIOS["Microservicios"]
        EMP["👥 empleados\n/metrics + logs + trazas"]
        DEP["🏢 departamentos\n/metrics + logs + trazas"]
        AUTH["🔐 auth\n/metrics + logs + trazas"]
    end
    PROM["📊 Prometheus\nMétricas (Pull)"] -->|Scraping| SERVICIOS
    LOKI["🗂️ Loki\nLogs (Push)"]
    PROMTAIL["📋 Promtail"] -->|Recolecta| SERVICIOS
    PROMTAIL -->|Push| LOKI
    ZIPKIN["🔍 Zipkin / Jaeger\nTrazas (Push)"]
    SERVICIOS -->|OTel SDK| ZIPKIN
    GRAFANA["📈 Grafana\nVisualiza y alerta"] -->|PromQL| PROM
    GRAFANA -->|LogQL| LOKI
    GRAFANA -->|Alerta| NOTIF["🔔 Discord / Telegram"]
</div>

---

# Event Storming: Proceso de Onboarding

<div class="mermaid" style="text-align: center; transform: scale(1.1) translateY(-30px);">
graph LR
    C1["🔵 RegistrarEmpleado"]
    E1["🟠 EmpleadoCreado"]
    P1["🟣 Política:\ncuando EmpleadoCreado\n→ CrearUsuario"]
    E2["🟠 UsuarioCreado"]
    P2["🟣 Política:\ncuando UsuarioCreado\n→ CrearPerfil"]
    E3["🟠 PerfilCreado"]
    E4["🟠 BienvenidaEnviada"]
    E5["🟠 OnboardingCompletado"]

    C1 --> E1 --> P1 --> E2 --> P2 --> E3 --> E4 --> E5
</div>

---

<!-- _class: end -->

<div style="position:absolute;  left:565px; top: 540px">

**Arquitectura Orientada a Microservicios**  
Ingeniería de Sistemas y Computación
Universidad del Quindío  

![width:80](https://raw.githubusercontent.com/christiancandela/plantillas/main/plantillauq/licencia.png) 2025 [**Christian Andrés Candela Uribe**](mailto:christiancandela@uniquindio.edu.co)

</div>