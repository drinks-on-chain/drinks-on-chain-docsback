# docs-back · guía de trabajo

Documentación del backend de Drinks on Chain (repo `drinks-on-chain/drinks-on-chain-docsback`). Solo Markdown, más `diagramas/generar.py` para extraer los diagramas.

- Estado: **BORRADOR** hasta que el usuario lo declare oficial. No marques decisiones como aceptadas por tu cuenta.
- Español, marca única Drinks on Chain, nombres de código tal cual.
- Numeración `NN-tema.md`; versión y fecha al inicio de cada documento; lo sustituido va a `antiguo/`.
- Diagramas en Mermaid compatibles con GitHub (`flowchart`, `sequenceDiagram`, `erDiagram`, `stateDiagram-v2`); nada de `;` en mensajes de secuencia ni estados compuestos con alias; sin colores ni estilos. Tras tocar un diagrama, ejecuta `python diagramas/generar.py` (regenera `diagramas/*.mmd` y los enlaces a Mermaid Live) y valídalo con Mermaid 12.
- Cada hallazgo sobre `drinks-on-chain-back` cita `archivo:línea`; vuelve a comprobarlo contra el código antes de reutilizarlo, porque el backend cambia.
- La documentación de frontend está en `../docs-front`; cuando haya conflicto, anótalo en `04-decisiones-y-preguntas.md` §2 en vez de elegir en silencio.
- Git: commits directos a `main` (decisión del usuario, 26-09-2026), uno por cambio importante, Conventional Commits; push de los commits acumulados al terminar el trabajo. Push con la cuenta `BrianKGR01` de `gh`.
