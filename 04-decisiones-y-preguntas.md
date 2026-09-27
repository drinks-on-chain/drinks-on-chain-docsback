# 04 · Decisiones, contradicciones y preguntas abiertas

> **BORRADOR** · versión 0.3 · 28 de septiembre de 2026. Sustituye a la v0.1 (en `antiguo/`). La v0.3 añade las decisiones del 28-09-2026 (§1.3). Registra las respuestas del cliente y del equipo del 27-09-2026, las contradicciones que aparecen al leer la documentación del backend (subida el 27-09), lo que sigue abierto y la explicación ampliada que se pidió de D7. C3, C7 y D1 se explican a fondo en `06-tokens-billeteras-y-cadena.md`.

Estados: **Acordada** (la respondió el cliente o el equipo) · **Propuesta** (recomendación a la espera de acuerdo) · **Abierta** (falta información o decisión).

## 1. Decisiones

### 1.1 Acordadas el 27-09-2026

| ID | Decisión | Antes |
|---|---|---|
| A-01 | **Un NFT por botella** | D2 |
| A-02 | **Emisor por bodega**: la bodega aparece como origen de sus NFT | D3 |
| A-03 | **Preventa**: la bodega autoriza, por lote y con una cantidad, la tokenización desde el ERP, lo antes posible en el proceso; los NFT se emiten entonces y el comprador sigue el avance casi en tiempo real | D4 |
| A-04 | **El backend crea y gestiona las billeteras** de los consumidores; el usuario nunca ve cripto ni paga comisiones | C1 |
| A-05 | Nada de **Dynamic** ni **Privy**. Si se usan cuentas inteligentes, con `smart-account-kit` y *relayer* propio. El tipo de billetera concreto sigue en D1 | C2 |
| A-06 | **Solo bolivianos**; nada de cripto como medio de pago | C4, P8 |
| A-07 | **Pase de canje** (no "de retiro") con caducidad **en horas**, configurable desde el back office, **solo a nivel general**; al caducar se genera otro | C5, D10 |
| A-08 | **Alta de bodegas por dos caminos**: formulario + aprobación (con reunión opcional) o alta directa desde el back office | C6, C8 |
| A-09 | El **back office** puede añadir colaboradores a una bodega, cambiar su rol y **bloquearlos**; todo queda en la **bitácora** | C9 |
| A-10 | El **dueño invita** a su equipo; hay que definir el proceso (definido en doc 07 §2) | — |
| A-11 | **Custodio de claves** y firmante aislado según lo recomendado | D5 |
| A-12 | **Indexador propio y mínimo** según lo recomendado | D6 |
| A-13 | **Solo correo** para verificación y notificaciones; sin SMS | D8 |
| A-14 | La **pasarela del banco se integra al final**; hasta entonces, infraestructura lista con adaptador de prueba | D9 |
| A-15 | El equipo que construyó el backend participa en este análisis | D11 |
| A-16 | **Sin facturación** ni notas de venta por ahora; **sin liquidación** a bodegas ni temas de pagos todavía | P1, P2 |
| A-17 | La **bodega gestiona la logística** de botellas a sus puntos de canje; los puntos son autorizados por las bodegas (o por la plataforma con autorización de la bodega) | P3 |
| A-18 | **Mayoría de edad por declaración**, como en las landings | P4 |
| A-19 | **Ventana de canje en días** (30 por defecto) y **máximo de botellas por compra** (10 por defecto, admite ilimitado), ambos configurables desde el back office | P5, P6 |
| A-20 | Textos legales y privacidad: al final, pero se tienen presentes | P7 |
| A-21 | **Escaneo de la botella público**, sin cuenta; la cuenta solo es necesaria para dejar una **reseña** | — |
| A-22 | **Anclaje al final**: la trazabilidad se registra en la base de datos y el hash del expediente se envía a la red **al terminar el proceso** del lote (no etapa por etapa) | — |
| A-23 | **Aviso de "pago recibido"** explícito antes de mostrar los NFT en la cava | — |
| A-24 | **Reglas de trazabilidad, precios y límites configurables** con estándar general y ajuste por bodega, aplicables a todas o a una selección de bodegas | — |
| A-25 | Puntos de canje por tres caminos: la bodega (si está habilitada), soporte, o postulación del punto; máximos de puntos y de cajeros configurables | — |
| A-26 | Código único por botella registrado en el canje para enlazar botella y comprador (propuesta del cliente; diseño en doc 07 §8) | — |
| A-27 | Campañas post-canje (agradecimiento, recordatorio de reseña, promociones) activables desde el back office | — |

### 1.3 Acordadas el 28-09-2026

| ID | Decisión | Antes |
|---|---|---|
| A-28 | **Billeteras del consumidor**: direcciones custodiales derivadas de una semilla maestra (SEP-0005), sin fondear; cuentas inteligentes con `smart-account-kit` en Fase 2. Se confirman todas las recomendaciones del doc 06 (contrato NFT por bodega sobre OpenZeppelin, quema por el operador, anclaje con transacción clásica, custodio) | D1, D-12 |
| A-29 | **Ventana de canje vencida**: las tres acciones (quemar, extender, compensar) configurables desde el back office, con estándar general y ajuste por bodega; **por defecto, quemar** al vencer, con aviso previo por correo | D-13 |
| A-30 | **Faltante** (menos botellas que NFT vendidos): prioridad por orden de compra; al resto, devolución o sustitución por un proceso manual en el MVP | D-14 |
| A-31 | **Mínimos legales como piso**: las reglas normativas (altitud y cepa D.O., reposo del singani) no bajan del mínimo legal por defecto; el back office puede autorizar excepciones si fuera necesario, solo con rol de administración, motivo obligatorio y registro en la bitácora | D-16 |
| A-32 | **Precios y pagos**: no se definen todavía. El backend deja la estructura lista (precio en la colección, política configurable, adaptador de pasarela) para implementarlos cuando el negocio lo tenga claro | D-17 |
| A-33 | **Reglas de código del equipo** con cinco ajustes: tokens de sesión cortos con renovación rotativa, roles por membresía, paginación `limit`/`offset`, cabecera `Idempotency-Key` permitida y patrón outbox en lugar de doble escritura | D-22 |
| A-34 | Se pasa al **roadmap** (`08-roadmap.md`) en el orden del ciclo del MVP: back office y bodegas → ERP → tokenización → Marketplace → POS | — |

### 1.2 Propuestas (de la v0.1, siguen vigentes)

| ID | Decisión | Estado |
|---|---|---|
| ADR-001 | Documentación del backend en `drinks-on-chain/drinks-on-chain-docsback`, commits directos a `main` | Acordada (26-09) |
| ADR-002 | Todo el backend en un repositorio, monolito modular con `api` + `worker`. **Cambio**: con A-01 hay contrato propio, así que se añade `drinks-on-chain-contracts` (doc 03 §2) | Propuesta |
| ADR-003 | Se evoluciona el backend actual, no se reescribe | Propuesta |
| ADR-004 | PostgreSQL como fuente operativa, la red como prueba pública, conciliación entre ambas | Propuesta |
| ADR-005 | Outbox transaccional + colas para toda operación externa | Propuesta |
| ADR-006 | Firma solo en el servidor, firmante aislado | Acordada (A-11) |
| ADR-007 | Trazabilidad append-only con correcciones compensatorias y anclaje al final | Acordada en lo del anclaje (A-22) |
| ADR-008 | Identidad por audiencia y roles por membresía | Propuesta (coherente con A-09) |
| ADR-009 | Envoltorio actual, `/v1`, `details` por campo, `Idempotency-Key` | Acordada (A-33) |
| ADR-010 | OpenAPI como contrato publicado | Propuesta |
| ADR-011 | Corregir EA-01 a EA-07 y SE-01 antes de emitir NFT | Propuesta |
| ADR-012 | Las reglas de código del equipo (`drinks-on-chain-back/docs/rules/`) son el estándar de implementación, con los ajustes de D-22 | Acordada (A-33) |

## 2. Contradicciones

### 2.1 De la v0.1: cómo quedan

| # | Tema | Resolución |
|---|---|---|
| C1 | Billeteras existentes (simuladas) | El backend crea billeteras reales (A-04); tipo en D1 |
| C2 | Proveedor de billeteras | Sin Dynamic ni Privy (A-05) |
| C3 | Modelo de token | NFT por botella (A-01). Explicación completa de qué era C3 en doc 06 §1 |
| C4 | Moneda | Solo bolivianos (A-06) |
| C5 | Caducidad del pase | Horas, configurable, general (A-07) |
| C6 | Cuándo nace la cuenta de la bodega | Al activarse la bodega (aprobación o alta directa) |
| C7 | Registro del productor en la red | Explicación completa en doc 06 §3; propuesta en D-12 |
| C8 | Quién da de alta la bodega | Ambos caminos (A-08) |
| C9 | Roles | Roles por membresía y gestión desde el back office (A-09, doc 05 §3) |
| C10 | Rechazo de bodega | Estado propio de la solicitud y motivo guardado (doc 07 §1) |
| C11 | Inmutabilidad | Append-only + anclaje al final (A-22) |
| C12 | Fases del backend | Se unifican en el roadmap que sale del catálogo (doc 05) |
| C13 | URL del QR | Configurable; QR por botella (doc 07 §8) |
| C14 | Billetera por defecto | D1 |
| C15 | Documentación del backend sin versionar | Resuelto: subida al repositorio el 27-09 |

### 2.2 Nuevas, al leer la documentación del backend

| # | Tema | Documentación del backend | Decisión o propuesta |
|---|---|---|---|
| C16 | Plataforma | `01-alcance-mvp.md` y `modulos-sistema.md` describen un backend en Supabase (PostgREST, Edge Functions, RLS) | Ya superado por `05-decision-backend.md` (NestJS). Marcar esos documentos como históricos |
| C17 | Momento de la emisión | *Lazy minting* (al pagar) y preventa "en Fase 2" | Preventa en el MVP con emisión al autorizar el lote (A-03) |
| C18 | Moneda en el modelo | `collections.distributor_price_usd`, `orders.total_amount_usd`, métodos de pago `XLM` y `USDC_STELLAR` | Importes en bolivianos, en unidad mínima entera; sin cripto (A-06) |
| C19 | Fideicomiso en la red | El roadmap v4 propone `PreSaleEscrow` con stablecoins y liberación de capital por hitos con multifirma | Fuera del MVP: no hay pagos en cripto ni tesorería (A-06, A-16) |
| C20 | Anclaje | `trazabillidad.rs` registra **cada etapa** en la red con roles on-chain | Solo el hash final (A-22); el contrato se simplifica (doc 06 §6) |
| C21 | Contratos | Seis contratos (C-01 a C-06) con un `ClaimEscrow` que ancla cada pase en la red | Proponemos menos piezas en la red: NFT + anclaje; los pases viven en la base de datos (doc 06 §7) |
| C22 | QR de la botella | Un QR estático por lote | QR y código por botella (A-26) |
| C23 | Reseñas | Solo quien quemó un NFT de la colección | Cualquier persona con sesión (A-21), con marca de "verificada" si canjeó (doc 05 RES-02) |
| C24 | Suscripciones | El roadmap v4 incluye planes (`Básico`, `Premium`, `Corporativo`) con límites de acuñación | No mencionado por el cliente: D-18 |
| C25 | Precios por etapa | El roadmap v4 propone precio de preventa temprana y estándar según el hito | Encaja con la preventa: D-17 |
| C26 | Marca | Varios documentos del backend nombran a otra empresa como operador de la plataforma | Según la regla de marca, solo Drinks on Chain; corregir en esos documentos |
| C27 | Reglas de código frente a la propuesta | `docs/rules/` fija JWT de 7 días, rol único por usuario, paginación por `page`, sin `Idempotency-Key` y con doble escritura en vez de outbox | D-22 |
| C28 | Tenant ajeno | `docs/rules/01` responde 403; `04` y `08` exigen 404 | 404 (lo que hace el código hoy) |
| C29 | Webhook ya procesado | 409 en `03` y `04`; "siempre 200" en `08` | 200 idempotente al proveedor, registro interno del duplicado |

## 3. Decisiones abiertas

| ID | Pregunta | Recomendación | Bloquea |
|---|---|---|---|
| **D1** | ~~¿Qué billetera crea el backend?~~ | **Acordada: A-28** | — |
| **D7** | ¿Dónde y cómo se despliega? | Ver §4 de este documento | Staging y producción |
| D-12 | ~~¿Contrato por bodega o de plataforma?~~ | **Acordada: A-28** (uno por bodega) | — |
| D-13 | ~~Ventana de canje vencida~~ | **Acordada: A-29** | — |
| D-14 | ~~Faltante~~ | **Acordada: A-30** | — |
| D-15 | Caducidad por defecto del pase de canje | 24 horas | Canje |
| D-16 | ~~Reglas bajo el mínimo legal~~ | **Acordada: A-31** | — |
| D-17 | ~~Política de precio~~ | **Aplazada: A-32** (estructura lista) | — |
| D-18 | ¿Planes de suscripción para bodegas en el MVP (roadmap v4)? | No en el MVP; los límites por bodega ya cubren la necesidad | — |
| D-19 | ¿Reseña por lote o por botella? ¿Solo compradores? | Una por persona y lote, cualquiera con sesión, con marca de verificada | Reseñas |
| D-20 | ¿La bodega necesita aprobación del back office para tokenizar o basta su autorización? | Aprobación del back office (configurable) | Tokenización |
| D-21 | ¿Qué datos pide el formulario de postulación de un punto de canje y quién lo aprueba? | Datos del local y de contacto; operaciones enlaza y la bodega autoriza | Puntos de canje |
| D-22 | ~~Ajustes a las reglas de código~~ | **Acordada: A-33** | — |

## 4. D7 · Dónde se despliega (explicación ampliada)

### 4.1 Qué hay que decidir
El backend necesita cuatro piezas en ejecución y tres servicios de apoyo:

| Pieza | Qué es | Requisito |
|---|---|---|
| `api` | La aplicación NestJS que atiende a los frontends | Siempre encendida, detrás de HTTPS |
| `worker` | El mismo código en modo colas: cadena, correos, tareas programadas | Siempre encendido |
| PostgreSQL | Base de datos | Copias automáticas y recuperación a un punto en el tiempo |
| Redis | Colas y límites de peticiones | Persistencia básica |
| Almacenamiento de objetos | Informes, etiquetas, fotos | Privado con URL firmadas |
| Correo | Envío transaccional | Dominio verificado (SPF, DKIM, DMARC) |
| Custodio de claves | Firma de la red | Aislado del resto |

Y tres entornos: **desarrollo** (testnet, datos de demostración), **staging** (testnet, copia de producción sin datos personales) y **producción** (mainnet).

### 4.2 Opciones

| Opción | Cómo | Coste mensual orientativo | A favor | En contra |
|---|---|---|---|---|
| A · Servidor propio (el actual u otro similar) | Docker Compose con `api`, `worker`, PostgreSQL, Redis y un proxy HTTPS; copias a almacenamiento externo | Bajo: el servidor más el almacenamiento de copias | Barato, control total, ya existe | La operación es nuestra: parches, copias, monitoreo, caídas |
| B · Plataforma gestionada de contenedores (Railway, Render, Fly…) | `api` y `worker` como servicios; PostgreSQL y Redis gestionados | Medio: pago por servicio y por base de datos | Despliegue desde Git, copias y certificados incluidos, poco mantenimiento | Coste que crece con el uso; menos control |
| C · Nube grande (AWS, GCP, Azure) | Contenedores gestionados + base de datos gestionada + KMS | Medio a alto | Escala, KMS nativo, cumplimiento | Más complejo de montar y de pagar |
| D · Mixta | Aplicación en el servidor propio, **base de datos gestionada** y copias externas | Bajo a medio | Lo más delicado (datos) queda gestionado; lo demás barato | Dos proveedores |

Los rangos de precio de cada proveedor cambian; se cotizan al decidir.

### 4.3 Recomendación
- **Ahora (desarrollo y demo)**: opción **A** en el servidor actual, pero **reproducible desde el repositorio** (Dockerfile, `docker-compose` por entorno, variables en un gestor de secretos), con copias diarias fuera del servidor y monitoreo básico.
- **Antes de producción con dinero real**: opción **D**, base de datos gestionada con recuperación a un punto en el tiempo, o **B** si el equipo prefiere no operar servidores.
- En cualquier caso: dominio propio, HTTPS, un entorno por rama (`dev` → desarrollo, etiquetas → staging, `main` → producción) y la clave del firmante fuera del servidor de la aplicación.

### 4.4 Acceso al servidor
El 28-09 se compartieron por chat la contraseña del usuario del servidor y la del superadministrador de la API. **No se usan**: el acceso debe ser por **llave SSH** (no contraseña), con un usuario que se pueda revocar, y **ambas contraseñas deben cambiarse** porque ya circularon fuera de un gestor de secretos. Es la tarea 0.1 del roadmap.

## 5. Preguntas pendientes

1. **D7**: acceso al servidor por llave SSH (§4.4) para revisarlo y cerrar la decisión de despliegue.
2. D-15, D-18 a D-21.
3. ¿Cuál es la caducidad de las invitaciones que prefieren (propuesta 72 horas) y los máximos por defecto de puntos por bodega y cajeros por punto (propuesta 3 y 5)?
4. ¿Las campañas de promociones necesitan segmentación más allá de "canjeó esta colección" (por bodega, por tipo de bebida)?

## 6. Supuestos vigentes mientras no haya respuesta

- Valores por defecto de la tabla de parámetros (doc 05 §4), incluida la caducidad del pase en 24 horas.
- NFT en un contrato basado en la implementación estándar auditada de OpenZeppelin para Stellar (doc 06).
- Testnet hasta la integración; mainnet tras revisión de seguridad.
- El contrato actual del ERP se mantiene y los cambios incompatibles se acuerdan con frontend.
- Pagos con adaptador de prueba hasta tener la documentación del banco.
