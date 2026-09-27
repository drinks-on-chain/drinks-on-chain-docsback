# 04 · Decisiones, contradicciones y preguntas abiertas

> **SUSTITUIDO** el 27-09-2026 por la versión 0.2 en la raíz del repositorio. Se conserva como registro y no se edita.
>
> BORRADOR · versión 0.1 · 26 de septiembre de 2026. Registro vivo del backend. Toda decisión aparece con fecha, estado y motivo; las preguntas se cierran moviéndolas a decisiones. Mientras el documento sea borrador, **ninguna decisión está aceptada**: todas figuran como *propuesta*.

## 1. Decisiones propuestas

Formato ligero de ADR (*Architecture Decision Record*): cuando una decisión se acepte, cambia su estado y, si hace falta más detalle, se abre un documento propio en `decisiones/`.

| ID | Fecha | Decisión | Estado | Motivo | Detalle |
|---|---|---|---|---|---|
| ADR-001 | 2026-09-26 | La documentación del backend vive en un repositorio propio (`drinks-on-chain-docsback`, carpeta `docs-back`), en la organización `drinks-on-chain`, con commits directos a `main` y Conventional Commits | Propuesta | Separar análisis y decisiones del código; que frontend, backend y cliente lo lean | README |
| ADR-002 | 2026-09-26 | Todo el backend en **un repositorio** (`drinks-on-chain-back`) como **monolito modular**, desplegado como `api` + `worker`; repositorio de contratos solo si se escriben contratos propios | Propuesta | Equipo pequeño, modelo compartido entre los cuatro sistemas, transacciones locales | 03 §2 |
| ADR-003 | 2026-09-26 | **Se evoluciona el backend actual**, no se reescribe: se conservan stack, estructura y contrato del ERP | Propuesta | Base razonable; el frontend del ERP ya depende de su contrato | 01 §8, 03 §18 |
| ADR-004 | 2026-09-26 | PostgreSQL es la fuente operativa y Stellar la prueba pública; **libro de unidades de doble entrada** conciliado con la red | Propuesta | Invariante de respaldo uno a uno; resiliencia ante la red | 03 §6, §7 |
| ADR-005 | 2026-09-26 | Toda operación externa (red, banco, mensajería) sale por **outbox transaccional + colas**, con idempotencia | Propuesta | Reintentos seguros; la API nunca espera a terceros | 03 §4, §9 |
| ADR-006 | 2026-09-26 | **Firma solo en el servidor**, en un firmante aislado con claves en un custodio; el firmante acepta intenciones de dominio, no XDR arbitrario | Propuesta | Estándar de custodia institucional; decisiones 25-09 del frontend | 03 §7 |
| ADR-007 | 2026-09-26 | Trazabilidad ***append-only*** con correcciones compensatorias, eventos encadenados por hash y **anclaje del expediente** del lote en la red (sin contrato propio) | Propuesta | Promesa de registro inmutable; hoy no se cumple (EA-06) | 03 §7.6 |
| ADR-008 | 2026-09-26 | Identidad **por audiencia** (personal, consumidor, dispositivo POS) y **roles por membresía** en organizaciones (plataforma, bodega, punto de recojo) | Propuesta | Cierra SE-01 y OP-05; soporta varias bodegas por persona | 03 §11 |
| ADR-009 | 2026-09-26 | Se conserva el envoltorio `{ success, data \| error }` y `/v1`; listas `{ items, total, limit, offset }`; `details` por campo; `Idempotency-Key` en operaciones de valor | Propuesta | Compatibilidad con el frontend y con `@drinks-on-chain/mocks` | 03 §12 |
| ADR-010 | 2026-09-26 | El **OpenAPI del backend es el contrato**: se publica en cada release y de él se generan tipos y esquemas para el frontend | Propuesta | Evitar la deriva actual entre catálogo, guías y OpenAPI (doc 09 §8 punto 7 de frontend) | 03 §12 |
| ADR-011 | 2026-09-26 | Los hallazgos EA-01 a EA-07 y SE-01 se corrigen **antes de cualquier emisión de tokens** | Propuesta | Cada botella registrada de más sería un token sin respaldo | 01 §9 |

## 2. Contradicciones entre documentos

Entre el documento maestro, la documentación de frontend (`drinks-on-chain-docsfront`) y el backend actual (código y README).

| # | Tema | Una fuente dice | Otra fuente dice | Propuesta |
|---|---|---|---|---|
| C1 | Billeteras existentes | Frontend 04 §3, 09 §1 y 11 §1: el backend ya crea billeteras custodiales para usuarios y bodegas | Código: se genera un par de claves y **se descarta la clave privada**; las direcciones no existen en la red | Tratar las billeteras actuales como inexistentes; decidir D1 |
| C2 | Proveedor de billeteras | Backend: *Dynamic* (variables `DYNAMIC_*`, `MockDynamicWalletProvider`) | Frontend 04 y 06: `smart-account-kit` con relayer propio; Privy como alternativa futura; Dynamic no aparece | Decidir en D1; no depender de un SaaS sin decisión explícita |
| C3 | Modelo de token | Backend: contratos Soroban propios (`CONTRACT_PRODUCER_REGISTRY`, `_BATCH_ANCHOR`, `_PRODUCT_NFT`, `_CLAIM_ESCROW`), "NFT de botellas y barricas", contrato `trazabillidad.rs` no versionado | Frontend 04 §6 y 11 §4: activo clásico por lote con clawback, sin contratos | D2; recomendación: activo clásico (03 §7.3) |
| C4 | Moneda de pago | Backend README: USDC, XLM y QR, liquidación directa a bodegas | Documento maestro y frontend 06: pago en moneda local por la pasarela del banco; el usuario no ve cripto | MVP solo bolivianos por el banco; cripto, si acaso, en Fase 2 |
| C5 | Caducidad del pase | Backend: `CLAIM_PASS_DEFAULT_EXPIRY_HOURS = 24` | Frontend 06: caducidad en días (supuesto 7) | Días, configurable (D10) |
| C6 | Cuándo nace la cuenta de la bodega | Backend: al **solicitar** el alta (bodega aún `PENDING`) | Frontend 04 y 06: al **aprobar** el alta desde el Backoffice | Al aprobar |
| C7 | Registro del productor en la red | Backend: hook "C-01 ProducerRegistry" (simulado) | Frontend: la cuenta emisora de la bodega y el `stellar.toml` identifican al productor | Sin contrato de registro en el MVP |
| C8 | Quién da de alta la bodega | Documento maestro: el gestor la crea y envía credenciales | Backend: autoinscripción + aprobación (frontend 09 §8 punto 8 lo acepta) | Soportar ambos caminos |
| C9 | Roles | Frontend 01 §7: enólogo, operario, admin de bodega, admin de plataforma, soporte, cajero, miembro | Backend: sin soporte; `POS_OPERATOR` es a la vez cajero y operario de planta; un rol global por persona | Modelo de 03 §11.2 |
| C10 | Rechazo de bodega | Catálogo de endpoints: estado `REJECTED` | Código: pasa a `REVOKED` y el motivo solo se escribe en el log | Estado `REJECTED` y motivo persistido |
| C11 | Inmutabilidad | Documento maestro: "cuaderno de bitácora digital inmutable" | Código: registros editables y 16 borrados en cascada | ADR-007 |
| C12 | Fases del backend | Backend README: 9 fases (Fase 5 tokenización y *vaults*, 6 pagos, 7 claims y POS, 8 indexador, 9 visor y reseñas) | Frontend 03: Etapas 0–5 (ERP → Marketplace → POS → Backoffice → integración) | Unificar en el roadmap del backend (siguiente documento) |
| C13 | URL del QR | Backend: `https://drinksonchain.com/trace/batch/{código}` fija | Frontend 02 y 09: `app.{dominio}/b/{código}` | Configurable por entorno |
| C14 | Billetera del consumidor por defecto | Frontend 06 (25-09): smart account con passkey por defecto, custodial de respaldo | Frontend 11 (25-09, posterior): empezar por la custodial "que ya existe" | D1, sabiendo que la custodial no existe (C1) |
| C15 | Documentación del backend | Backend README: enlaza arquitectura, base de datos, contratos y planes por fase | Repositorio: `docs/*` ignorado por git; esos archivos no existen | Pedirlos al equipo que los escribió (§5) |

## 3. Decisiones abiertas

| ID | Pregunta | Opciones | Recomendación (borrador) | Quién decide | Bloquea |
|---|---|---|---|---|---|
| D1 | ¿Qué billetera tiene el consumidor en el MVP? | A smart account con passkey · B custodial `G…` · C ómnibus | A por defecto con B de respaldo, como decidió el frontend; C solo como contingencia | Cliente + backend + frontend | Marketplace, POS, demo del grant |
| D2 | ¿Qué es un token? | Activo clásico por lote con clawback · SEP-41 propio · NFT por botella | Activo clásico por lote | Backend + cliente | Emisión, cava, quema |
| D3 | ¿Quién emite? | Una emisora por bodega · una emisora de plataforma | Por bodega (la bodega aparece como origen del activo); revisar coste de gestión si hay muchas bodegas | Cliente | Alta de bodega, emisión |
| D4 | ¿Cuándo se emite? | Todo el lote al publicar (a una cuenta de distribución) · al vender cada unidad | Todo el lote al publicar: el suministro total queda visible en la red y coincide con la narrativa del Backoffice | Backend | Emisión, libro |
| D5 | ¿Dónde viven las claves? | Vault Transit · KMS de nube con Ed25519 · HSM · semilla cifrada con KMS | Un custodio que firme Ed25519 sin exportar la clave; verificar soporte del proveedor elegido | Backend + cliente (coste) | Todo lo on-chain |
| D6 | ¿Cómo se indexa la red? | Indexador propio sobre RPC · Mercury · ambos | Propio y mínimo (solo nuestras cuentas y activos); Mercury si el volumen crece | Backend | Cava, conciliación |
| D7 | ¿Dónde se despliega? | Servidor actual con contenedores · plataforma gestionada de contenedores · nube con base de datos gestionada | Base de datos gestionada con PITR sí o sí; cómputo en contenedores donde el cliente prefiera | Cliente | Staging y producción |
| D8 | ¿Qué proveedor envía OTP por SMS y correo? | Varios proveedores regionales y globales | Uno con buena entrega en Bolivia y coste por mensaje conocido | Cliente | Registro del consumidor |
| D9 | ¿Qué modalidad ofrece la pasarela del banco? | Redirección · widget · QR interoperable | Soportar las tres detrás del adaptador; empezar por la que el banco documente | Banco + cliente | Checkout |
| D10 | ¿Reglas del pase de retiro? | Días de validez, máximo de botellas por pase, código rotativo, verificación del titular | 7 días, sin máximo en el MVP, nombre del titular en el POS, código rotativo opcional | Cliente | POS |
| D11 | ¿Quién desarrolla y mantiene el backend? | El equipo que construyó el backend actual · este equipo · mixto | A definir: cambia cómo se organiza el roadmap y la revisión de código | Cliente | Todo |

## 4. Preguntas para el cliente (negocio)

1. **Facturación**: ¿quién vende al consumidor y emite la factura (la plataforma o la bodega)? ¿Con qué sistema de facturación electrónica? Afecta a pedidos, reembolsos e integración con el sistema tributario.
2. **Liquidación a bodegas**: ¿cómo y cuándo se paga a la bodega por cada botella vendida (al vender o al entregar)? ¿Hay comisión de la plataforma? El MVP no tiene tesorería, pero alguien tiene que cuadrar esos pagos.
3. **Inventario físico**: ¿las botellas se quedan en la bodega y se envían a los puntos de recojo? ¿El backend debe llevar el stock físico por punto para saber si un punto puede entregar?
4. **Edad legal**: ¿basta con declarar la mayoría de edad al registrarse o hay que verificarla al comprar o al retirar?
5. **Reembolsos y cancelaciones**: ¿se puede devolver un token no retirado? ¿Qué pasa con un pase caducado muchas veces?
6. **Límites**: ¿máximo de botellas por compra o por persona en una colección?
7. **Datos personales**: textos legales y política de privacidad del Marketplace, y plazos de conservación de datos.
8. **Precio**: ¿solo bolivianos o también referencia en dólares? (pregunta 4.6 del doc 06 de frontend, sigue abierta).

## 5. Preguntas para el equipo que construyó el backend actual

1. ¿Pueden compartir los documentos que el README enlaza y que no están en el repositorio (`docs/architecture`, `docs/bd`, `docs/contratos/trazabillidad.rs`, `docs/implementation`)?
2. ¿Cómo está desplegado el servidor de desarrollo (contenedores, proceso, proxy HTTPS, copias de seguridad)? ¿Está detrás de un proxy (afecta al rate limit, SE-06)?
3. ¿Había una decisión tomada sobre Dynamic, o era un marcador?
4. ¿Los contratos Soroban de la configuración existen en testnet?
5. ¿Pasan hoy las pruebas unitarias y e2e? ¿Contra qué base de datos se ejecutan?
6. ¿Pueden cargar los datos de demostración en el servidor de desarrollo (doc 10 §2.1 de frontend)?
7. ¿Qué opinan de los hallazgos del doc 01 §9? Algunos pueden tener un motivo que el código no muestra.

## 6. Supuestos vigentes mientras no haya respuesta

- El backend evoluciona desde `drinks-on-chain-back`, sin reescritura.
- Token: activo clásico por lote, 1 unidad = 1 botella, quema por clawback (igual que el frontend).
- Pago solo en bolivianos por la pasarela del banco; ningún usuario paga XLM.
- Pase de retiro: 7 días, solo en puntos habilitados para el lote.
- Testnet hasta la integración; mainnet solo tras revisión de seguridad.
- Las billeteras y hashes on-chain que hoy devuelve el backend son de prueba y no se migran.
- El contrato actual del ERP se mantiene; los cambios incompatibles se acuerdan con frontend.
