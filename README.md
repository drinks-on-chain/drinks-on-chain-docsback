# Drinks on Chain — Documentación del backend

> **BORRADOR** · versión 0.1 · 26 de septiembre de 2026. Nada de lo escrito aquí es oficial hasta que se revise y se marque como aceptado.

Análisis, arquitectura, decisiones y roadmap del **backend** del ecosistema Drinks on Chain: la API y los procesos que dan servicio al ERP de trazabilidad (S1), al Marketplace con visor y cava (S2), al Backoffice (S3) y a la aplicación de retiro en los puntos de recojo (S4), más la integración con la red Stellar y con la pasarela de pago del banco.

Es la contraparte de [`drinks-on-chain-docsfront`](https://github.com/BrianKGR01/drinks-on-chain-docsfront) (carpeta `docs-front`), que documenta el frontend. Ambas se leen juntas: aquí se cita "doc NN de frontend" para referirse a aquella.

## Documentos

| Documento | Qué contiene |
|---|---|
| [01-estado-actual-backend.md](01-estado-actual-backend.md) | Estado real de `drinks-on-chain-back`: arquitectura, módulos, modelo de datos, qué es real y qué es simulado, calidad, **hallazgos priorizados** y cobertura frente al producto |
| [02-vision-funcional.md](02-vision-funcional.md) | Qué hace el ecosistema de punta a punta: actores, sistemas, capacidades, **ciclo de vida de una botella**, flujos entre sistemas, reglas de negocio y glosario |
| [03-vision-backend.md](03-vision-backend.md) | Arquitectura propuesta: **un repositorio o varios**, contenedores, módulos, datos, Stellar, pagos, identidad, API, seguridad, operación, entornos y pruebas |
| [04-decisiones-y-preguntas.md](04-decisiones-y-preguntas.md) | Decisiones propuestas (ADR), **contradicciones entre documentos**, decisiones abiertas y preguntas para el cliente y para el equipo del backend actual |

Pendiente, tras la revisión de estos cuatro: **05 · Roadmap del backend** por etapas y con casillas de avance, alineado con el roadmap del frontend.

## Cómo leerlo

1. Si solo hay diez minutos: el **resumen ejecutivo** del 01 (§0), la **propuesta en diez puntos** del 03 (§0) y las **decisiones abiertas** del 04 (§3).
2. Para entender el producto: el 02 completo; sus diagramas de secuencia muestran cada flujo entre sistemas.
3. Para revisar la arquitectura: el 03, empezando por §2 (repositorios) y §7 (Stellar).

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

Última actualización: 26 de septiembre de 2026.
