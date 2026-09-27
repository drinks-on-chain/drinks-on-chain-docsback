# Drinks on Chain — Documentación del backend

> **BORRADOR** · versión 0.2 · 27 de septiembre de 2026. Nada de lo escrito aquí es oficial hasta que se revise y se marque como aceptado.

Análisis, arquitectura, decisiones y roadmap del **backend** del ecosistema Drinks on Chain: la API y los procesos que dan servicio al ERP de trazabilidad (S1), al Marketplace con visor y cava (S2), al Backoffice (S3) y a la aplicación de retiro en los puntos de recojo (S4), más la integración con la red Stellar y con la pasarela de pago del banco.

Es la contraparte de [`drinks-on-chain-docsfront`](https://github.com/BrianKGR01/drinks-on-chain-docsfront) (carpeta `docs-front`), que documenta el frontend. Ambas se leen juntas: aquí se cita "doc NN de frontend" para referirse a aquella.

## Documentos

| Documento | Qué contiene |
|---|---|
| [01-estado-actual-backend.md](01-estado-actual-backend.md) | Estado real de `drinks-on-chain-back`: arquitectura, módulos, modelo de datos, qué es real y qué es simulado, **hallazgos priorizados** y cobertura frente al producto |
| [02-vision-funcional.md](02-vision-funcional.md) | El **ciclo completo del MVP** de punta a punta: actores y roles, ciclos de vida del lote y del NFT, flujos entre sistemas, configuración, reglas y glosario |
| [03-vision-backend.md](03-vision-backend.md) | Arquitectura propuesta: repositorios, contenedores, módulos, modelo de datos, pagos, procesos por dentro, identidad, API, seguridad y operación |
| [04-decisiones-y-preguntas.md](04-decisiones-y-preguntas.md) | **Decisiones acordadas el 27-09**, contradicciones, decisiones abiertas y la explicación de D7 (despliegue) |
| [05-catalogo-funcional-backend.md](05-catalogo-funcional-backend.md) | **Catálogo completo de funcionalidades** del backend con ID, estado y alcance; roles y permisos; **parámetros configurables** |
| [06-tokens-billeteras-y-cadena.md](06-tokens-billeteras-y-cadena.md) | Explicación de **C3, C7 y D1**; contrato NFT por bodega, billeteras, anclaje, custodia de claves y costes en la red |
| [07-procesos-detallados.md](07-procesos-detallados.md) | Alta de bodegas, **invitaciones**, gestión de colaboradores desde el back office, **bitácora**, configuración en dos niveles, preventa, puntos de canje, **código de botella**, soporte y entrega asistida, anti-bots |
| [antiguo/](antiguo/README.md) | Versiones sustituidas (v0.1 de 02, 03 y 04) |

Pendiente: **roadmap del backend**, que se armará sobre el catálogo del doc 05.

## Cómo leerlo

1. Si solo hay diez minutos: el **ciclo completo** del 02 (§3), las **decisiones** del 04 (§1 y §3) y el **resumen** del 06 (§0).
2. Para entender el producto: el 02 y, para cada proceso, el 07.
3. Para planificar: el catálogo del 05.
4. Para revisar la arquitectura: el 03 y, para la red, el 06.

Los diagramas están en [Mermaid](https://mermaid.js.org/). GitHub y la mayoría de editores los dibujan dentro del documento. Debajo de cada uno hay un enlace **Abrir en Mermaid Live** y otro a su código puro en [`diagramas/`](diagramas/README.md), listo para pegar en [mermaid.live](https://mermaid.live). No copies las líneas ```` ```mermaid ```` del documento: Mermaid Live no las reconoce. Si cambias un diagrama, ejecuta `python diagramas/generar.py` para regenerar los archivos y los enlaces.

## Repositorios relacionados

| Repositorio | Qué es |
|---|---|
| `drinks-on-chain-back` | Backend actual (NestJS + Prisma + PostgreSQL). Objeto del análisis del doc 01 |
| `drinks-on-chain-docsback` | Este repositorio (carpeta `docs-back`) |
| `drinks-on-chain-docsfront` | Documentación del frontend (carpeta `docs-front`) |
| `drinks-on-chain-mocks` | Esquemas y datos de prueba del frontend; hoy imita el contrato del ERP |
| `drinks-on-chain-erp` | Frontend del ERP, construido contra el contrato actual del backend |

## Convenciones

- **Idioma**: español. Los nombres de código (entidades, campos, enumeraciones, endpoints) se escriben como en el código.
- **Marca**: Drinks on Chain; ninguna otra razón social aparece en los documentos.
- **Versiones y fechas** al inicio de cada documento; los documentos sustituidos pasan a `antiguo/` y no se editan.
- **Decisiones** en el 04 con identificador (`ADR-NNN` las propuestas, `Dn` las abiertas) y estado; nada se da por aceptado mientras el documento sea borrador.
- **Evidencia**: cada hallazgo cita archivo y línea del repositorio analizado.
- **Git**: en este repositorio se trabaja directamente en `main` (decisión del 26-09-2026, para compartir el avance en línea con el equipo): un commit por cambio importante, [Conventional Commits](https://www.conventionalcommits.org/es/) (`docs(estado): …`, `docs(vision): …`) y push al terminar cada bloque de trabajo.

Última actualización: 27 de septiembre de 2026.
