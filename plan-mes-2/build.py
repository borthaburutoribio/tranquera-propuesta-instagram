# Genera plan-mes-2/index.html (plan 15/11 -> 15/12/2026) a partir del estilo de plan-30-dias.
import json, pathlib, re
here = pathlib.Path(__file__).parent
base = (here.parent / "plan-30-dias" / "index.html").read_text(encoding="utf8")
head = base[:base.find("<body")]
head = head.replace("<title>Plan 30 días · Tranquera Digital</title>", "<title>Plan del mes · Tranquera Digital</title>")
head = re.sub(r"<!-- Calendario.*?-->", "<!-- Plan 15/11 -> 15/12/2026 de @tranquera_digital. EN REVISION: nada producido. Fuente: plan-mes-2/build.py -->", head, flags=re.S)
extra_css = """<style>
.day dl dt.v{color:#5B2330}
.day .serie{display:inline-block;font-size:12px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;background:#F3E7A2;border:1.5px solid #1D1B1A;padding:2px 7px;margin:6px 0 2px}
.day .serie.s-fru{background:#E9B8C0}.day .serie.s-inv{background:#B7CCE5}.day .serie.s-err{background:#F3E7A2}.day .serie.s-rubro{background:#F6F1E7}
.cast{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-top:14px}
.cast .box h4{margin:0 0 4px;font-size:18px}
.flow{counter-reset:p;list-style:none;padding:0;margin:14px 0 0}
.flow li{counter-increment:p;position:relative;padding:10px 12px 10px 46px;border:2px solid #1D1B1A;background:#fff;margin-bottom:8px;box-shadow:5px 5px 0 #1D1B1A}
.flow li:before{content:counter(p);position:absolute;left:10px;top:9px;width:26px;height:26px;border-radius:50%;background:#5B2330;color:#F6F1E7;font-weight:800;display:grid;place-items:center;font-size:14px}
.no{background:#1D1B1A;color:#F6F1E7;padding:14px 16px;margin-top:14px;border-left:8px solid #C8E783}
</style>
"""
head = head.replace("</head>", extra_css + "</head>")

body = """<body><div class="wrap">

<div class="k">Tranquera Digital · plan de Instagram · mes 2</div>
<h1>Del 15/11 al 15/12, <em>todo animado.</em></h1>
<p class="lead">Sigue el esquema de siempre: números, objetivos, mezcla y el calendario día por día. Lo nuevo: <b>se acabaron las ilustraciones quietas con zoom.</b> Cada plano es video animado de verdad, hecho con IA (los personajes caminan, hablan, se espantan), y <b>nada es serie</b>: cada reel es una pieza suelta que se entiende sola. El pilar del mes son las <b>frutinovelas</b>: telenovelas de plastilina con frutas y verduras que tienen cara, celos y traiciones, y cada una termina en un problema real de comercio. Una historia completa por reel, sin continuación.</p>

<h2>1. Lo que dicen <em>los números</em></h2>
<p class="lead">32 publicaciones desde el 14/10 (24 reels, 8 carruseles), medidas el 13/11. Desde el 12/11 no salió nada nuevo, así que siguen valiendo.</p>
<div class="tablewrap" style="margin-top:14px"><table>
<tr><th>Lo que pasó</th><th>Qué hacemos este mes</th></tr>
<tr><td><b>Curiosidad argentina con "??"</b> (el hacker argentino): 214 reproducciones y 6 comentarios. El único que hizo hablar a la gente.</td><td>Formato suelto <b>"Inventos argentinos"</b> los miércoles (cada uno se entiende solo), cada uno con una pregunta fácil para comentar.</td></tr>
<tr><td><b>Mundo ilustrado con gente</b> (ladrillo, consultorios, sobrino, panaderías): 130 a 173, parejo.</td><td><b>Frutinovelas</b>: 9 dramas de culebrón con frutas y verduras de plastilina, cada uno suelto, con un problema real de comercio y un remate con humor. Siguen la tensión del ladrillo y los dos locales en la misma cuadra.</td></tr>
<tr><td><b>Celular con texto o explicación</b>: 11 a 32.</td><td>Se deja de hacer. Si aparece un celu, lo tiene en la mano un personaje animado.</td></tr>
<tr><td><b>Carruseles</b>: 0 a 2 me gusta.</td><td>3 en el mes, solo para guardar, y con placas que se mueven (los carruseles aceptan video).</td></tr>
<tr><td><b>Seguidores: 9.</b> El alcance está, la gente no vuelve.</td><td>Reels que se compartan por mensaje y cierren con una razón concreta para seguir (la palabra clave, el próximo tema en la caja de preguntas).</td></tr>
</table></div>

<h2>2. Objetivos <em>con número</em></h2>
<div class="grid3">
<div class="box"><b class="n">9 → 80</b><p><b>Seguidores.</b> Frutinovelas que se mandan por mensaje ("mandáselo a alguien que…"), palabras clave y respuestas a comentarios con reel. Cada reel se entiende solo, sin ver el anterior.</p></div>
<div class="box"><b class="n">83 → 250</b><p><b>Reproducciones promedio por reel.</b> Animación que frena el dedo + ganchos con el checklist de 8.</p></div>
<div class="box"><b class="n">6 → 50</b><p><b>Comentarios en el mes</b> y <b>3 consultas</b> que vengan de Instagram. Juegos para comentar ("encontrá el error"), palabras clave (FICHA, QR, BOT).</p></div>
</div>

<h2>3. Cómo se anima <em>(ya no son fotos)</em></h2>
<ol class="flow">
<li><b>Fichas de estilo en Gemini</b> (Nano Banana): el look de plastilina (materiales, luz, paleta de la marca) y una hoja de caras para frutas y verduras (traición, llanto, desmayo, mirada de culebrón). Sirven para que todos los reels se vean de la misma mano; cada frutinovela estrena su elenco.</li>
<li><b>Cuadros clave</b> de cada plano en Gemini, con las fichas de estilo.</li>
<li><b>Video en Google Flow (Veo 3.1)</b> con primer y último cuadro: el personaje se mueve, gesticula, la cámara viaja. Planos de 4 a 8 segundos. Pruebas en calidad Lite, la final en Fast.</li>
<li><b>Montaje en HyperFrames:</b> cortes al ritmo, subtítulos que son la voz palabra por palabra, carteles de Google y WhatsApp encima, la T al final, música propia.</li>
<li><b>Voz de Valeria</b> (ElevenLabs): en las frutinovelas, narra como locutora de telenovela; sumamos una o dos voces dramáticas para los personajes cuando ayudan. Subtítulos palabra por palabra y música de suspenso.</li>
<li><b>"Info de IA"</b> activado en cada reel (lo pide Instagram para video hecho con IA).</li>
</ol>
<div class="no"><b>Presupuesto de video:</b> la cuenta de Flow con la que trabajamos (flow.google.com/u/2) <b>no tiene Pro</b>: trae 50 créditos gratis por día. Un plano Fast de 8 segundos sale 20 créditos (uno Lite, 10), o sea 2 o 3 planos por día. Dos caminos: repartimos la producción en varios días (un reel de 6 planos son dos días de créditos, así que se arranca antes de cada fecha) o activás Pro y se produce de corrido. Con el plan actual, la primera tanda se reparte hasta fin de mes.</div>

<h2>4. Los sistemas virales <em>del mes</em></h2>
<div class="tablewrap" style="margin-top:14px"><table>
<tr><th>Sistema</th><th>Qué empuja</th><th>Dónde</th></tr>
<tr><td><b>Frutinovelas</b> (pilar del mes): culebrón con frutas y verduras, frase de telenovela en los primeros 2 segundos ("¡Me engañaste con la verdulería de enfrente!")</td><td>Que lo vean entero y lo manden: drama exagerado que termina en un problema real de comercio</td><td>9 reels sueltos, cada uno con su remate</td></tr>
<tr><td><b>Tensión que no se entiende</b> y remate al final (el ladrillo, 173 reproducciones)</td><td>Que lo vean hasta el final</td><td>Los ganchos de las frutinovelas</td></tr>
<tr><td><b>Orgullo argentino + "??"</b></td><td>Comentarios y compartidos ("¿sabías esto?")</td><td>Inventos argentinos, miércoles</td></tr>
<tr><td><b>Encontrá el error</b>: escena animada con 3 errores, "pausá el video"</td><td>Lo vuelven a mirar (cuenta doble) y comentan el número</td><td>Martes 24/11 y 1/12</td></tr>
<tr><td><b>"Mandáselo a…"</b> con un rubro con nombre (tu peluquera, tu médico, el de la rotisería)</td><td>Envíos por mensaje: lo que más mide Instagram para mostrarle el reel a gente nueva</td><td>Serie "Tu rubro"</td></tr>
<tr><td><b>Palabra clave</b> (FICHA, QR, BOT): comentan y les escribimos por privado</td><td>Comentarios + consultas reales</td><td>Carruseles y reels útiles</td></tr>
<tr><td><b>Loop:</b> el último cuadro empalma con el primero</td><td>Repeticiones sin que se den cuenta</td><td>Todos los reels</td></tr>
<tr><td><b>Portadas con la cara del personaje</b> espantado + 2 a 4 palabras, misma grilla</td><td>Clics desde el perfil y la pestaña de reels</td><td>Todos los reels</td></tr>
<tr><td><b>Fechas calientes</b> (feriados, Black Friday, Navidad)</td><td>Ganchos con urgencia del día</td><td>20/11, 27/11, 8/12, 12/12 (Navidad en frutinovela)</td></tr>
<tr><td><b>Responder comentarios con un reel</b> (desde la app)</td><td>Más comentarios: la gente ve que contestamos</td><td>Lun 7/12</td></tr>
</table></div>

<h2>5. La mezcla</h2>
<div class="grid3">
<div class="box"><p><span class="tag t-reel">22 reels</span> <span class="tag t-car">3 carruseles</span> <span class="tag t-post">1 posteo</span> <span class="tag t-hist">historias</span></p><p style="margin-top:10px">Reels a las 19 hs (lun, mar, mié, vie y sáb). Carrusel o posteo los jueves a las 12:30. Domingos: historia con encuesta o pregunta que alimenta los reels de la semana.</p></div>
<div class="box"><p><b>Series</b></p><ul class="dots"><li><b>Frutinovelas</b> (pilar, cada una suelta): 9</li><li><b>Inventos argentinos</b>: 4</li><li><b>Encontrá el error</b>: 2</li><li><b>Tu rubro en 30 segundos</b>: 1</li><li>Fechas, comodines y detrás de escena: 6</li></ul></div>
<div class="box"><p><b>Esfuerzo</b></p><ul class="dots"><li><b>Liviano</b>: 2 o 3 planos animados.</li><li><b>Medio</b>: 4 o 5 planos.</li><li><b>Pesado</b>: 6 a 8 planos, frutinovela con elenco y escenario nuevos. Uno por semana.</li></ul></div>
</div>

<h2>6. El calendario, <em>día por día</em></h2>
<div class="legend"><span class="tag t-reel">Reel</span><span class="tag t-car">Carrusel</span><span class="tag t-post">Posteo</span><span class="tag t-hist">Historia</span><span class="hand" style="font-size:20px;margin-left:6px">los datos y los feriados se chequean con fuente antes de producir</span></div>
<div id="cal"></div>

<div class="ok">
<b>Cómo seguimos.</b> Revisalo y decime qué cambiar: podés tachar días o traer tus ideas (mandan sobre las mías). La prueba de estilo de plastilina ya está hecha. Con tu OK: me decís si activás Pro en Flow o repartimos los créditos gratis por día, armo las fichas de estilo y produzco la primera tanda (17/11 → 29/11), te la paso entera y con tu OK la programo en Business Suite y cargo las historias en tu calendario. Después, la segunda tanda (30/11 → 15/12), con el mismo ritmo de créditos.
</div>
</div>
"""

# fecha, tipo, esfuerzo, serie, tema, gancho, idea, animacion, sistema, cta
D = [
["Dom 15/11","hist","liviano","","Encuesta para arrancar","¿Qué te da más bronca de tu local?","Encuesta con 3 opciones: “que no me encuentren”, “contestar WhatsApp todo el día”, “que pregunten el precio y se vayan”. Lo que gane define el tema de los reels de la semana.","Placa animada con un verdulero de plastilina","La gente elige el tema: después quiere ver el resultado","Votar."],
["Lun 16/11","reel","medio","fru","Frutinovela: la Banana y la verdulería de enfrente","¡Me engañaste con la verdulería de enfrente!","Culebrón de plastilina: la Banana, con lágrimas, le reprocha a un Cliente (una Pera con gorra) que se fue con la verdulería de enfrente. Él, de rodillas: “¡La encontré en Google!”. Zoom a la cara de la Banana. Remate: ella también quiere aparecer en el mapa.","5 planos Veo: la verdulería, el reproche a cámara, el zoom, la Banana mirando el celu","Frase de culebrón en los primeros 2 s + identificación (“nos pasó”)","Mandáselo a alguien que todavía no aparece en Google."],
["Mar 17/11","reel","pesado","fru","Frutinovela: el Tomate y la Lechuga","Me dijiste que abrías a las 9. ¡Y estaba cerrado!","El Tomate y la Lechuga se separan en medio de la verdulería: él cambió el horario y no avisó en la ficha. Ella lo esperó una hora en la puerta. Música dramática, lluvia de plastilina. Remate: el horario se cambia en 30 segundos y se salvan las parejas.","6 planos Veo: la pareja en la puerta cerrada, la lluvia, la cachetada, el celu con la ficha","Gancho de culebrón + comentarios: “¿a quién le pasó?”","Mandáselo a quien cambió el horario y no avisó."],
["Mié 18/11","reel","medio","inv","Inventos argentinos #1: El Apóstol","La primera película animada larga del mundo es argentina. ¿Y por qué nadie la vio?","Quirino Cristiani, Buenos Aires, 1917. No quedó ninguna copia. Lo hizo primero y el mundo se lo adjudica a otros: lo que no queda a la vista, no existe. Remate: “este video también es animado, y este sí lo vas a encontrar”.","4 planos: un taller de 1917 en blanco y negro que se colorea, dibujos recortados que cobran vida","Orgullo argentino + pregunta: comentan y comparten","Comentá si lo sabías."],
["Jue 19/11","car","liviano","","Checklist: tu ficha de Google","Tu ficha de Google tiene 7 casilleros. ¿Cuántos llenaste?","Una placa por casillero (nombre, rubro, horario, teléfono, fotos, web, reseñas), cada una con un local mal cargado y otro bien cargado, en loop de 3 segundos.","Placas con video corto (el carrusel acepta video)","Para guardar + palabra clave","Comentá FICHA y te la revisamos gratis."],
["Vie 20/11","reel","liviano","","Feriado (a confirmar si es el 20 o se pasa al 23)","Hoy es feriado. Tu ficha de Google dice “Abierto”.","Un cliente camina contento con el mapa en la mano, llega y la persiana está baja. Se da vuelta despacio a cámara. Cómo se carga un horario especial en 30 segundos.","3 planos Veo","Urgencia del día: sirve hoy mismo","Actualizalo ahora y mandáselo a alguien que se olvida."],
["Sáb 21/11","reel","pesado","fru","Frutinovela: el velorio de la Palta","¡¿Tenías página web desde 2015?! ¡¿Y nadie lo sabía?!","Velorio de plastilina: entre llantos, el Sobrino (un Pepino) confiesa que le hizo la página a la Palta en 2015 y nunca se la mostró. La Palta se incorpora del cajón. Remate: la página existía; faltaba que alguien la encontrara.","7 planos Veo: el velorio, el Pepino que confiesa, la Palta que se levanta, el mapa","Culebrón con remate absurdo: se comparte entre dueños","Mandáselo a quien tiene un sobrino que hace páginas."],
["Dom 22/11","hist","liviano","","Caja de preguntas","¿Qué rubro tenés?","Caja de preguntas. Con las respuestas elegimos los rubros de “Tu rubro en 30 segundos”.","Placa animada","Les prometemos un reel de su rubro: vuelven a mirar","Responder la caja."],
["Lun 23/11","reel","medio","fru","Frutinovela: el Durazno de la peluquería","¡Dijiste que me ibas a dar turno y me dejaste en visto!","Una Zanahoria llora frente al espejo de una peluquería de plastilina: le escribió al Durazno y nunca le dieron turno. El Durazno, con rulero, jura que no vio el mensaje. Remate: respuesta automática con los horarios.","5 planos Veo en una peluquería de fruta","“Mandáselo a” con nombre: se reenvía por mensaje","Mandáselo a tu peluquera."],
["Mar 24/11","reel","medio","err","Encontrá el error #1: el consultorio","Esta ficha tiene 3 errores. Casi nadie encuentra el tercero.","La cámara recorre la puerta de un consultorio y su ficha: horario viejo, teléfono fijo que nadie atiende, cero fotos. Pausa, cuenta regresiva y la respuesta al final.","4 planos + marcas que aparecen","Lo miran dos veces + comentan el número","Comentá cuántos encontraste antes de la respuesta."],
["Mié 25/11","reel","liviano","inv","Inventos argentinos #2: la birome","La birome es argentina. ¿Y por qué el mundo dice Bic?","László Bíró la patentó en Argentina en 1943; la que la hizo famosa en todo el mundo fue la marca que la puso en cada kiosco. Hoy el kiosco donde te ven es Google.","3 planos: una birome que dibuja sola la historia en el aire","Pregunta fácil para comentar","Comentá otro invento argentino que conozcas."],
["Jue 26/11","post","liviano","","Para comentar","¿1.000 seguidores o 10 reseñas de 5 estrellas?","Una placa partida en dos que se mueve en loop: de un lado un celu con likes, del otro una verdulería llena. En el texto, por qué para un local la respuesta no es tan obvia.","Posteo de video corto en loop (6 s)","Dos opciones: comentar cuesta una palabra","Comentá 1.000 o 10."],
["Vie 27/11","reel","medio","","Black Friday","Black Friday: todos buscan ofertas cerca. ¿Aparece la tuya?","Una multitud animada con el celu en la mano camina por la cuadra; solo entran al local que tiene la oferta publicada en Google. Google deja publicar ofertas en la ficha y casi nadie lo usa.","4 planos Veo","Urgencia del día","Guardalo y publicá tu oferta hoy."],
["Sáb 28/11","reel","pesado","fru","Frutinovela: los 40 mensajes de la Frutilla","¡Te escribí 40 veces y nunca me contestaste!","La Frutilla, en bata y llorando, entra a la verdulería con el celu: 40 mensajes de WhatsApp para la Manzana, ninguno respondido. La Manzana duerme; son las 2 de la mañana. Remate: el bot le contestó precio y horario a la primera. Se abrazan.","7 planos Veo: la inundación de mensajes es el plano estrella","Gancho de culebrón + remate que se comparte","Comentá BOT y te contamos cómo se arma."],
["Dom 29/11","hist","liviano","","Encuesta + respuesta","¿Le pondrías un bot a tu WhatsApp?","Encuesta “Sí, ya” / “Ni loco”. En otra historia, la respuesta del Encontrá el error del martes.","Placas animadas","Cierra el juego del martes: confianza","Votar."],
["Lun 30/11","reel","medio","rubro","Tu rubro #2: consultorios","Antes de llamarte, tu paciente hace esto.","Un paciente animado busca tu nombre, mira reseñas, se fija si atendés su obra social y si hay turnos online. Si no encuentra nada, llama al siguiente.","5 planos en sala de espera y casa del paciente","“Mandáselo a” con nombre","Mandáselo a tu médico (en serio)."],
["Mar 1/12","reel","medio","err","Encontrá el error #2: la tienda en diciembre","Esta vidriera vende el doble en diciembre. Tiene 3 errores igual.","Un local de regalos lleno de luces: el horario de fiestas sin cargar, el WhatsApp que dice “escribime” y no contesta, ningún link para ver los regalos. Pausa y respuesta.","4 planos + marcas","Lo miran dos veces + comentan","Comentá cuántos encontraste."],
["Mié 2/12","reel","medio","inv","Inventos argentinos #3: las huellas","Las huellas digitales para identificar gente son un invento argentino.","Juan Vucetich, La Plata, 1891: un sistema para que cada persona sea inconfundible. Tu negocio también necesita que lo reconozcan al toque: mismo nombre, mismo logo y los mismos datos en todos lados.","4 planos: una huella gigante que se vuelve mapa de la ciudad","Orgullo argentino + pregunta","Comentá el próximo invento que querés ver."],
["Jue 3/12","car","liviano","","Checklist de fiestas","6 cosas para dejar listas antes del 20 de diciembre.","Horario especial en Google, respuesta automática de WhatsApp, link de regalos o catálogo, foto nueva en la ficha, pedir reseñas a los de siempre, avisar fechas de entrega. Una por placa, con una mano tachando.","Placas con video corto","Para guardar","Guardalo y tachá lo que ya hiciste."],
["Vie 4/12","reel","medio","fru","Frutinovela: la Cebolla que se cree muy digital","¡Mi vidriera es perfecta, no entiendo por qué no entra nadie!","La Cebolla, vanidosa, se mira al espejo mientras el cliente, afuera, ve en el celu una ficha sin fotos y un WhatsApp mudo y sigue de largo. Llanto de la Cebolla (por la cebolla, claro). Remate: lo que ve el cliente es lo que cuenta.","5 planos Veo: el espejo, la vidriera, la pantalla del celu del cliente","Identificación: “me pasa”","Mandáselo a alguien que se cree muy digital."],
["Sáb 5/12","reel","pesado","fru","Frutinovela: el Zapallo doctor y el teléfono fijo","¡Doctor, lo llamé veinte veces y nunca atendió!","Consultorio de plastilina: la Calabaza paciente le reprocha al Zapallo doctor el fijo que suena a las 22 sin que nadie atienda. Zoom, música de suspenso, desmayo. Remate: turnos por WhatsApp y respuesta automática.","6 planos Veo: el consultorio, el fijo que suena, el desmayo","Gancho de culebrón + “mandáselo a tu médico”","Mandáselo a tu médico."],
["Dom 6/12","hist","liviano","","Caja de preguntas","Preguntanos lo que quieras de Google, WhatsApp o tu página.","Caja de preguntas. Las mejores van al reel del lunes.","Placa animada","Pregunta que se contesta con video","Preguntar."],
["Lun 7/12","reel","liviano","","Respuesta real (contestada con reel)","Me preguntaron: “¿Cuánto sale una página?”","Un verdulero de plastilina hace la pregunta a cámara. La voz responde honesto: de qué depende, qué no puede faltar y por qué una página barata que nadie encuentra sale cara. Precios solo si nos pasás los reales.","3 planos + el comentario en pantalla","Responder comentarios con reel","Comentá tu pregunta para el próximo."],
["Mar 8/12","reel","liviano","","Feriado del 8","Hoy es feriado. ¿Tu ficha lo sabe?","Un verdulero llega a su local, cerrado como corresponde, y ve en el celu que Google dice “Abierto”. Cara de espanto. 30 segundos para arreglarlo.","2 planos Veo","Urgencia del día","Revisalo ahora (son 30 segundos)."],
["Mié 9/12","reel","medio","inv","Inventos argentinos #4: el dulce de leche","Dicen que el dulce de leche nació de un descuido. En 1829. ¿Argentino o uruguayo?","La leyenda de Cañuelas: una olla de leche con azúcar que se olvidó en el fuego. Se pelean dos países por quién lo inventó; se lo queda el que todos tienen a la vista. Se cuenta como leyenda, no como dato.","4 planos: la olla, la estancia, dos banderas que tiran del frasco","Debate: el que más comentarios trae","Comentá: ¿argentino o uruguayo?"],
["Jue 10/12","car","liviano","","Plantillas de WhatsApp","5 mensajes de WhatsApp para fiestas, listos para copiar.","Horario de fiestas, “tu pedido está listo”, demora en envíos, saludo, pedir reseña. Uno por placa, para copiar y pegar.","Placas con video corto","Para guardar y mandar","Guardalo y copiá el que te sirva."],
["Vie 11/12","reel","medio","","Reseñas: cómo pedirlas","Casi todos leen reseñas antes de elegir. Así se piden sin dar vergüenza.","Un QR en el mostrador que lleva directo a dejar la reseña y la frase justa para pedirla, actuada por una panadera con un cliente. (Dato con fuente antes de producir.)","4 planos","Palabra clave","Comentá QR y te armamos el tuyo gratis."],
["Sáb 12/12","reel","pesado","fru","Frutinovela: Navidad, 24 de diciembre","24 de diciembre, 18 hs. ¡Y la verdulería de enfrente está llena!","Luces de Navidad de plastilina. El Ananá, con horario de fiestas cargado y WhatsApp activo, se llena de gente; el Limón, al lado, mira la puerta vacía con cara de traición. Remate: tres cosas que se arreglan en una tarde.","7 planos Veo: la cuadra iluminada, las dos verdulerías, la fila en una sola","Fecha caliente + identificación: se comparte entre dueños","Guardalo y arreglá las tres antes del 20."],
["Dom 13/12","hist","liviano","","Encuesta de cierre","¿Cuál de estos te pasó?","Encuesta con las escenas del mes: el ladrillo, el sobrino, las 2 AM, el teléfono fijo. Gracias a los que se sumaron este mes. Lo que gane vuelve en enero con una escena nueva.","Placa con 4 miniaturas de plastilina","Los hace elegir el próximo tema","Votar."],
["Lun 14/12","reel","medio","","Detrás de escena","Así hacemos estos videos. Sin cámaras ni actores.","Del boceto en plastilina al video terminado: el cuadro clave, el plano que se mueve, el montaje. Cierre: lo mismo hacemos para el Instagram de tu local.","4 planos + capturas del proceso","Curiosidad por el cómo: se comparte entre emprendedores","Escribinos y te mostramos tu página antes de pagar."],
["Mar 15/12","reel","medio","fru","Frutinovela: la Berenjena de la rotisería","¡Me prometiste el pollo para el 24 y no me avisaste que cerrabas!","Rotisería de plastilina a toda marcha: la Berenjena atiende 300 pedidos de WhatsApp, la carta cambió y el horario del 24 y 31 no está en ningún lado. El Pollo se desmaya. Remate: la carta online y el bot lo ordenan.","5 planos Veo en una cocina de plastilina","“Mandáselo a” con nombre","Mandáselo al de la rotisería."],
]
T = {"reel":["Reel","t-reel",""],"car":["Carrusel","t-car","car"],"post":["Posteo","t-post","post"],"hist":["Historia","t-hist","hist"]}
S = {"fru":["Frutinovela","s-fru"],"inv":["Inventos argentinos","s-inv"],"err":["Encontrá el error","s-err"],"rubro":["Tu rubro","s-rubro"]}
semanas = [["Arranque · 15 y 16/11",0,2],["Semana 1 · 17 al 22/11",2,8],["Semana 2 · 23 al 29/11",8,15],["Semana 3 · 30/11 al 6/12",15,22],["Semana 4 · 7 al 13/12",22,29],["Cierre · 14 y 15/12",29,31]]
assert len(D) == 31
js = "<script>\nconst D=%s;\nconst T=%s;const S=%s;const semanas=%s;\n" % (
    json.dumps(D, ensure_ascii=False, indent=0), json.dumps(T), json.dumps(S, ensure_ascii=False),
    json.dumps(semanas, ensure_ascii=False)) + r"""
const esc=s=>s.replace(/&/g,"&amp;").replace(/</g,"&lt;");
document.getElementById("cal").innerHTML=semanas.map(([t,a,b])=>`<div class="week"><h3>${t}</h3><div class="days">${D.slice(a,b).map(([f,ti,e,se,tema,g,idea,an,sis,cta])=>`<div class="day ${T[ti][2]}"><div class="top"><span class="d">${f}</span><span><span class="tag ${T[ti][1]}">${T[ti][0]}</span> <span class="e">${e}</span></span></div>${se?`<span class="serie ${S[se][1]}">${S[se][0]}</span>`:""}<div class="tema">${esc(tema)}</div><div class="gancho">“${esc(g)}”</div><dl><dt>Idea</dt><dd>${esc(idea)}</dd><dt>Animación</dt><dd>${esc(an)}</dd><dt class="v">Sistema viral</dt><dd>${esc(sis)}</dd><dt>Llamada a la acción</dt><dd>${esc(cta)}</dd></dl></div>`).join("")}</div></div>`).join("");
</script>
</body></html>"""
(here / "index.html").write_text(head + body + js, encoding="utf8")
print("ok", sum(1 for d in D if d[1] == "reel"), "reels")
