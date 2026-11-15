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
.day .serie.s-cuadra{background:#C8E783}.day .serie.s-inv{background:#B7CCE5}.day .serie.s-err{background:#F3E7A2}.day .serie.s-rubro{background:#F6F1E7}
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
<p class="lead">Sigue el esquema de siempre: números, objetivos, mezcla y el calendario día por día. Lo nuevo: <b>se acabaron las ilustraciones quietas con zoom.</b> Cada plano es video animado de verdad, hecho con IA (los personajes caminan, hablan, se espantan), y el mes gira alrededor de una serie con personajes fijos para que la gente vuelva y siga la cuenta.</p>

<h2>1. Lo que dicen <em>los números</em></h2>
<p class="lead">32 publicaciones desde el 14/10 (24 reels, 8 carruseles), medidas el 13/11. Desde el 12/11 no salió nada nuevo, así que siguen valiendo.</p>
<div class="tablewrap" style="margin-top:14px"><table>
<tr><th>Lo que pasó</th><th>Qué hacemos este mes</th></tr>
<tr><td><b>Curiosidad argentina con "??"</b> (el hacker argentino): 214 reproducciones y 6 comentarios. El único que hizo hablar a la gente.</td><td>Serie semanal <b>"Inventos argentinos"</b> los miércoles, cada uno con una pregunta fácil para comentar.</td></tr>
<tr><td><b>Mundo ilustrado con gente</b> (ladrillo, consultorios, sobrino, panaderías): 130 a 173, parejo.</td><td>Pasa a ser <b>una serie con personajes fijos</b>, "La Cuadra", y ahora animada en serio.</td></tr>
<tr><td><b>Celular con texto o explicación</b>: 11 a 32.</td><td>Se deja de hacer. Si aparece un celu, lo tiene en la mano un personaje animado.</td></tr>
<tr><td><b>Carruseles</b>: 0 a 2 me gusta.</td><td>3 en el mes, solo para guardar, y con placas que se mueven (los carruseles aceptan video).</td></tr>
<tr><td><b>Seguidores: 9.</b> El alcance está, la gente no vuelve.</td><td>Episodios con "sigue el sábado": la razón para seguir la cuenta.</td></tr>
</table></div>

<h2>2. Objetivos <em>con número</em></h2>
<div class="grid3">
<div class="box"><b class="n">9 → 80</b><p><b>Seguidores.</b> La Cuadra en 5 episodios con final abierto, temporada que cierra el 12/12.</p></div>
<div class="box"><b class="n">83 → 250</b><p><b>Reproducciones promedio por reel.</b> Animación que frena el dedo + ganchos con el checklist de 8.</p></div>
<div class="box"><b class="n">6 → 50</b><p><b>Comentarios en el mes</b> y <b>3 consultas</b> que vengan de Instagram. Juegos para comentar ("encontrá el error"), palabras clave (FICHA, QR, BOT).</p></div>
</div>

<h2>3. La serie: <em>La Cuadra</em></h2>
<p class="lead">Una cuadra de Buenos Aires, siempre la misma, con sus locales y sus vecinos. Cada episodio es un problema real de un comercio y termina en suspenso. Personajes ilustrados en 3D tipo maqueta (nunca gente realista), con cara de dibujo animado para las portadas.</p>
<div class="cast">
<div class="box"><h4>Rubén</h4><p>Verdulero, 58. La mejor fruta de la cuadra y nadie lo encuentra en Google. Se resiste a todo ("yo toda la vida con la libreta").</p></div>
<div class="box"><h4>Marta</h4><p>La de la panadería de enfrente. Se entera de todo antes que nadie. Ya tiene página y bot, y se lo cuenta a Rubén.</p></div>
<div class="box"><h4>La doctora Paz</h4><p>Consultorio en el primer piso. Pacientes que la llaman al fijo a las 22 hs. Llega en el episodio 4.</p></div>
<div class="box"><h4>Lucas, el sobrino</h4><p>"Yo te hago la página, tío." En 2015. Vuelve con un contador de visitas.</p></div>
</div>
<p class="hand" style="font-size:20px;margin-top:10px">Episodios: mar 17/11 · sáb 21/11 · sáb 28/11 · sáb 5/12 · sáb 12/12 (final de temporada de Navidad)</p>

<h2>4. Cómo se anima <em>(ya no son fotos)</em></h2>
<ol class="flow">
<li><b>Biblia de La Cuadra en Gemini</b> (Nano Banana, cuenta Pro): ficha de cada personaje de frente, perfil y 3 caras (sorpresa, bronca, risa) y la cuadra en 4 horarios. Así salen iguales en todos los episodios.</li>
<li><b>Cuadros clave</b> de cada plano en Gemini, con los personajes de la biblia.</li>
<li><b>Video en Google Flow (Veo 3.1)</b> con primer y último cuadro: el personaje se mueve, gesticula, la cámara viaja. Planos de 4 a 8 segundos. Pruebas en calidad Lite, la final en Fast.</li>
<li><b>Montaje en HyperFrames:</b> cortes al ritmo, subtítulos que son la voz palabra por palabra, carteles de Google y WhatsApp encima, la T al final, música propia.</li>
<li><b>Voz de Valeria</b> (ElevenLabs), contada como a un amigo. Los personajes con voces distintas cuando hablan.</li>
<li><b>"Info de IA"</b> activado en cada reel (lo pide Instagram para video hecho con IA).</li>
</ol>
<div class="no"><b>Presupuesto de video:</b> el plan Pro trae 1.000 créditos por mes en Flow más 50 por día. Un plano Fast sale 20 créditos y uno Lite 10. El mes completo usa unos 1.300, con margen para repetir planos que salgan mal. <b>Hay que confirmar que tu Google AI Pro esté activo en Flow</b> (labs.google/flow con la cuenta donde tenés Gemini Pro): es lo primero que miro con tu OK.</div>

<h2>5. Los sistemas virales <em>del mes</em></h2>
<div class="tablewrap" style="margin-top:14px"><table>
<tr><th>Sistema</th><th>Qué empuja</th><th>Dónde</th></tr>
<tr><td><b>Serie con final abierto</b> ("¿Rubén vuelve a aparecer? El sábado.")</td><td>Seguidores: la única forma de ver la parte 2</td><td>La Cuadra, 5 episodios</td></tr>
<tr><td><b>Orgullo argentino + "??"</b></td><td>Comentarios y compartidos ("¿sabías esto?")</td><td>Inventos argentinos, miércoles</td></tr>
<tr><td><b>Encontrá el error</b>: escena animada con 3 errores, "pausá el video"</td><td>Lo vuelven a mirar (cuenta doble) y comentan el número</td><td>Martes 24/11 y 1/12</td></tr>
<tr><td><b>"Mandáselo a…"</b> con un rubro con nombre (tu peluquera, tu médico, el de la rotisería)</td><td>Envíos por mensaje: lo que más mide Instagram para mostrarle el reel a gente nueva</td><td>Serie "Tu rubro"</td></tr>
<tr><td><b>Palabra clave</b> (FICHA, QR, BOT): comentan y les escribimos por privado</td><td>Comentarios + consultas reales</td><td>Carruseles y reels útiles</td></tr>
<tr><td><b>Loop:</b> el último cuadro empalma con el primero</td><td>Repeticiones sin que se den cuenta</td><td>Todos los reels</td></tr>
<tr><td><b>Portadas con la cara del personaje</b> espantado + 2 a 4 palabras, misma grilla</td><td>Clics desde el perfil y la pestaña de reels</td><td>Todos los reels</td></tr>
<tr><td><b>Fechas calientes</b> (feriados, Black Friday, Navidad)</td><td>Ganchos con urgencia del día</td><td>20/11, 27/11, 8/12, 12/12</td></tr>
<tr><td><b>Responder comentarios con un reel</b> (desde la app)</td><td>Más comentarios: la gente ve que contestamos</td><td>Lun 7/12</td></tr>
</table></div>

<h2>6. La mezcla</h2>
<div class="grid3">
<div class="box"><p><span class="tag t-reel">21 reels</span> <span class="tag t-car">3 carruseles</span> <span class="tag t-post">1 posteo</span> <span class="tag t-hist">historias</span></p><p style="margin-top:10px">Reels a las 19 hs (lun, mar, mié, vie y sáb). Carrusel o posteo los jueves a las 12:30. Domingos: historia con encuesta o pregunta que alimenta los reels de la semana.</p></div>
<div class="box"><p><b>Series</b></p><ul class="dots"><li><b>La Cuadra</b>: 5 episodios</li><li><b>Inventos argentinos</b>: 4</li><li><b>Encontrá el error</b>: 2</li><li><b>Tu rubro en 30 segundos</b>: 3</li><li>Fechas, comodines y detrás de escena: 7</li></ul></div>
<div class="box"><p><b>Esfuerzo</b></p><ul class="dots"><li><b>Liviano</b>: 2 o 3 planos animados.</li><li><b>Medio</b>: 4 o 5 planos.</li><li><b>Pesado</b>: 6 a 8 planos, episodio de La Cuadra. Uno por semana.</li></ul></div>
</div>

<h2>7. El calendario, <em>día por día</em></h2>
<div class="legend"><span class="tag t-reel">Reel</span><span class="tag t-car">Carrusel</span><span class="tag t-post">Posteo</span><span class="tag t-hist">Historia</span><span class="hand" style="font-size:20px;margin-left:6px">los datos y los feriados se chequean con fuente antes de producir</span></div>
<div id="cal"></div>

<div class="ok">
<b>Cómo seguimos.</b> Revisalo y decime qué cambiar: podés tachar días, cambiar personajes o traer tus ideas (mandan sobre las mías). Con tu OK: confirmo Flow, armo la biblia de La Cuadra y te paso una prueba de 8 segundos para que apruebes el estilo. Después produzco la primera tanda (17/11 → 29/11), te la paso entera y con tu OK la programo en Business Suite y cargo las historias en tu calendario. Después, la segunda tanda (30/11 → 15/12).
</div>
</div>
"""

# fecha, tipo, esfuerzo, serie, tema, gancho, idea, animacion, sistema, cta
D = [
["Dom 15/11","hist","liviano","","Encuesta para arrancar","¿Qué te da más bronca de tu local?","Encuesta con 3 opciones: “que no me encuentren”, “contestar WhatsApp todo el día”, “que pregunten el precio y se vayan”. Lo que gane va primero en La Cuadra.","Placa con Rubén animado (sale de la prueba de estilo)","La gente elige el tema: después quiere ver el resultado","Votar."],
["Lun 16/11","hist","liviano","cuadra","Adelanto de la serie","Mañana, 19 hs. Episodio 1.","La cuadra de noche, una sola persiana se ilumina. Sticker de cuenta regresiva para que se anoten.","1 plano corto (la persiana)","Cuenta regresiva: Instagram les avisa cuando sale","Tocar “Recordarme”."],
["Mar 17/11","reel","pesado","cuadra","La Cuadra · Ep. 1 “Rubén no existe”","Rubén está adentro de su verdulería. Y su verdulería está desapareciendo.","Una clienta busca “verdulería cerca”. Cada vez que el mapa no lo muestra, el local de Rubén se borra un poco más, como un fantasma, con él adentro acomodando tomates. Marta lo mira desde enfrente.","7 planos Veo: la cuadra, la clienta, el local que se desvanece, la cara de Rubén","Final abierto: “¿Rubén vuelve a aparecer? El sábado.”","Seguinos para ver el episodio 2."],
["Mié 18/11","reel","medio","inv","Inventos argentinos #1: El Apóstol","La primera película animada larga del mundo es argentina. ¿Y por qué nadie la vio?","Quirino Cristiani, Buenos Aires, 1917. No quedó ninguna copia. Lo hizo primero y el mundo se lo adjudica a otros: lo que no queda a la vista, no existe. Remate: “este video también es animado, y este sí lo vas a encontrar”.","4 planos: un taller de 1917 en blanco y negro que se colorea, dibujos recortados que cobran vida","Orgullo argentino + pregunta: comentan y comparten","Comentá si lo sabías."],
["Jue 19/11","car","liviano","","Checklist: tu ficha de Google","Tu ficha de Google tiene 7 casilleros. ¿Cuántos llenaste?","Una placa por casillero (nombre, rubro, horario, teléfono, fotos, web, reseñas), cada una con Rubén haciéndolo mal y Marta bien, en loop de 3 segundos.","Placas con video corto (el carrusel acepta video)","Para guardar + palabra clave","Comentá FICHA y te la revisamos gratis."],
["Vie 20/11","reel","liviano","","Feriado (a confirmar si es el 20 o se pasa al 23)","Hoy es feriado. Tu ficha de Google dice “Abierto”.","Un cliente camina contento con el mapa en la mano, llega y la persiana está baja. Se da vuelta despacio a cámara. Cómo se carga un horario especial en 30 segundos.","3 planos Veo","Urgencia del día: sirve hoy mismo","Actualizalo ahora y mandáselo a alguien que se olvida."],
["Sáb 21/11","reel","pesado","cuadra","La Cuadra · Ep. 2 “Rubén vuelve”","Marta cruzó la calle. Y le dijo a Rubén lo que nadie se animaba.","Marta le arma la ficha y la página. Un pin gigante de Google cae del cielo sobre la verdulería, el local vuelve a tener color y entra gente. Final: el celu de Rubén empieza a vibrar. Y no para.","7 planos: el pin que cae, la cuadra que se colorea, el celu vibrando","Final abierto: “200 mensajes a las 2 de la mañana. El sábado.”","Seguinos para el episodio 3."],
["Dom 22/11","hist","liviano","","Caja de preguntas","¿Qué rubro tenés?","Caja de preguntas. Con las respuestas elegimos los rubros de “Tu rubro en 30 segundos”.","Placa animada","Les prometemos un reel de su rubro: vuelven a mirar","Responder la caja."],
["Lun 23/11","reel","medio","rubro","Tu rubro #1: peluquerías","Si tenés una peluquería, esto te está costando clientas.","Una peluquera animada con el celu explotando de “¿tenés turno?”, cero fotos de trabajos en Google, reseñas sin responder. Arreglo de cada una, rápido.","5 planos Veo en una peluquería ilustrada","“Mandáselo a” con nombre: se reenvía por mensaje","Mandáselo a tu peluquera."],
["Mar 24/11","reel","medio","err","Encontrá el error #1: el consultorio","Esta ficha tiene 3 errores. Casi nadie encuentra el tercero.","La cámara recorre la puerta de un consultorio y su ficha: horario viejo, teléfono fijo que nadie atiende, cero fotos. Pausa, cuenta regresiva y la respuesta al final.","4 planos + marcas que aparecen","Lo miran dos veces + comentan el número","Comentá cuántos encontraste antes de la respuesta."],
["Mié 25/11","reel","liviano","inv","Inventos argentinos #2: la birome","La birome es argentina. ¿Y por qué el mundo dice Bic?","László Bíró la patentó en Argentina en 1943; la que la hizo famosa en todo el mundo fue la marca que la puso en cada kiosco. Hoy el kiosco donde te ven es Google.","3 planos: una birome que dibuja sola la historia en el aire","Pregunta fácil para comentar","Comentá otro invento argentino que conozcas."],
["Jue 26/11","post","liviano","","Para comentar","¿1.000 seguidores o 10 reseñas de 5 estrellas?","Una placa partida en dos que se mueve en loop: de un lado un celu con likes, del otro Rubén con la verdulería llena. En el texto, por qué para un local la respuesta no es tan obvia.","Posteo de video corto en loop (6 s)","Dos opciones: comentar cuesta una palabra","Comentá 1.000 o 10."],
["Vie 27/11","reel","medio","","Black Friday","Black Friday: todos buscan ofertas cerca. ¿Aparece la tuya?","Una multitud animada con el celu en la mano camina por la cuadra; solo entran al local que tiene la oferta publicada en Google. Google deja publicar ofertas en la ficha y casi nadie lo usa.","4 planos Veo","Urgencia del día","Guardalo y publicá tu oferta hoy."],
["Sáb 28/11","reel","pesado","cuadra","La Cuadra · Ep. 3 “Las 2 AM”","Son las 2 de la mañana. Rubén tiene 200 mensajes. Y todos dicen lo mismo.","Los globitos de WhatsApp llenan la verdulería como agua hasta el techo; Rubén flota con el celu. Marta, en pijama desde la ventana: “Poné un bot.” Final: el bot le contestó a una clienta algo que nadie esperaba.","8 planos: la inundación de mensajes es el plano estrella","Final abierto: “¿Qué le contestó el bot? El sábado.”","Comentá qué creés que le contestó."],
["Dom 29/11","hist","liviano","","Encuesta + respuesta","¿Le pondrías un bot a tu WhatsApp?","Encuesta “Sí, ya” / “Ni loco”. En otra historia, la respuesta del Encontrá el error del martes.","Placas animadas","Cierra el juego del martes: confianza","Votar."],
["Lun 30/11","reel","medio","rubro","Tu rubro #2: consultorios","Antes de llamarte, tu paciente hace esto.","Un paciente animado busca tu nombre, mira reseñas, se fija si atendés su obra social y si hay turnos online. Si no encuentra nada, llama al siguiente.","5 planos en sala de espera y casa del paciente","“Mandáselo a” con nombre","Mandáselo a tu médico (en serio)."],
["Mar 1/12","reel","medio","err","Encontrá el error #2: la tienda en diciembre","Esta vidriera vende el doble en diciembre. Tiene 3 errores igual.","Un local de regalos lleno de luces: el horario de fiestas sin cargar, el WhatsApp que dice “escribime” y no contesta, ningún link para ver los regalos. Pausa y respuesta.","4 planos + marcas","Lo miran dos veces + comentan","Comentá cuántos encontraste."],
["Mié 2/12","reel","medio","inv","Inventos argentinos #3: las huellas","Las huellas digitales para identificar gente son un invento argentino.","Juan Vucetich, La Plata, 1891: un sistema para que cada persona sea inconfundible. Tu negocio también necesita que lo reconozcan al toque: mismo nombre, mismo logo y los mismos datos en todos lados.","4 planos: una huella gigante que se vuelve mapa de la ciudad","Orgullo argentino + pregunta","Comentá el próximo invento que querés ver."],
["Jue 3/12","car","liviano","","Checklist de fiestas","6 cosas para dejar listas antes del 20 de diciembre.","Horario especial en Google, respuesta automática de WhatsApp, link de regalos o catálogo, foto nueva en la ficha, pedir reseñas a los de siempre, avisar fechas de entrega. Una por placa, con Marta tachando.","Placas con video corto","Para guardar","Guardalo y tachá lo que ya hiciste."],
["Vie 4/12","reel","medio","","Comodín (o tu tendencia)","Lo que vos creés que ve tu cliente. Lo que ve de verdad.","Pantalla partida: de un lado tu local lindo y ordenado; del otro, lo que ve el cliente en el celu (una ficha sin fotos, un WhatsApp que no contesta). Si traés una tendencia, va esa.","4 planos","Identificación: “me pasa”","Mandáselo a alguien que se cree muy digital."],
["Sáb 5/12","reel","pesado","cuadra","La Cuadra · Ep. 4 “El bot de Rubén”","El bot de Rubén le contestó a una clienta a las 2:14. Rubén no lo puede creer.","Se resuelve el suspenso: el bot le pasó el precio del tomate, el horario y le reservó un cajón, y Rubén se entera a la mañana con el mate. Final: la doctora Paz, desde el primer piso, escuchó todo.","7 planos, entra la doctora Paz","Final abierto: “La doctora Paz tiene un problema peor. El sábado.”","Seguinos para el final de temporada."],
["Dom 6/12","hist","liviano","","Caja de preguntas","Preguntanos lo que quieras de Google, WhatsApp o tu página.","Caja de preguntas. Las mejores van al reel del lunes.","Placa animada","Pregunta que se contesta con video","Preguntar."],
["Lun 7/12","reel","liviano","","Respuesta real (contestada con reel)","Me preguntaron: “¿Cuánto sale una página?”","Rubén hace la pregunta a cámara. La voz responde honesto: de qué depende, qué no puede faltar y por qué una página barata que nadie encuentra sale cara. Precios solo si nos pasás los reales.","3 planos + el comentario en pantalla","Responder comentarios con reel","Comentá tu pregunta para el próximo."],
["Mar 8/12","reel","liviano","","Feriado del 8","Hoy es feriado. ¿Tu ficha lo sabe?","Rubén llega a la verdulería, cerrada como corresponde, y ve en el celu que Google dice “Abierto”. Cara de espanto. 30 segundos para arreglarlo.","2 planos Veo","Urgencia del día","Revisalo ahora (son 30 segundos)."],
["Mié 9/12","reel","medio","inv","Inventos argentinos #4: el dulce de leche","Dicen que el dulce de leche nació de un descuido. En 1829. ¿Argentino o uruguayo?","La leyenda de Cañuelas: una olla de leche con azúcar que se olvidó en el fuego. Se pelean dos países por quién lo inventó; se lo queda el que todos tienen a la vista. Se cuenta como leyenda, no como dato.","4 planos: la olla, la estancia, dos banderas que tiran del frasco","Debate: el que más comentarios trae","Comentá: ¿argentino o uruguayo?"],
["Jue 10/12","car","liviano","","Plantillas de WhatsApp","5 mensajes de WhatsApp para fiestas, listos para copiar.","Horario de fiestas, “tu pedido está listo”, demora en envíos, saludo, pedir reseña. Uno por placa, para copiar y pegar.","Placas con video corto","Para guardar y mandar","Guardalo y copiá el que te sirva."],
["Vie 11/12","reel","medio","","Reseñas: cómo pedirlas","Casi todos leen reseñas antes de elegir. Así se piden sin dar vergüenza.","Un QR en el mostrador que lleva directo a dejar la reseña y la frase justa para pedirla, actuada por Marta con un cliente. (Dato con fuente antes de producir.)","4 planos","Palabra clave","Comentá QR y te armamos el tuyo gratis."],
["Sáb 12/12","reel","pesado","cuadra","La Cuadra · Ep. 5 “24 de diciembre” (final)","24 de diciembre, 18 hs. Toda la cuadra busca el último regalo.","Final de temporada con luces de Navidad: los locales que tienen todo cargado se llenan, la doctora Paz atiende con turnos online, Rubén vende su último cajón y brinda con Marta. Cierre: “Temporada 2 en enero”.","8 planos, el más grande del mes","Final de temporada: siguen para la 2","Seguinos: en enero vuelve La Cuadra."],
["Dom 13/12","hist","liviano","","Encuesta de la serie","¿Qué personaje de La Cuadra querés que vuelva?","Encuesta Rubén / Marta / la doctora Paz / Lucas. Gracias a los que se sumaron este mes.","Placa con los 4 personajes","Los hace parte de la temporada 2","Votar."],
["Lun 14/12","reel","medio","","Detrás de escena","Así hacemos La Cuadra. Sin cámaras ni actores.","Del dibujo al video: el boceto de Rubén, la ficha del personaje, el plano que se mueve, el episodio terminado. Cierre: lo mismo hacemos para el Instagram de tu local.","4 planos + capturas del proceso","Curiosidad por el cómo: se comparte entre emprendedores","Escribinos y te mostramos tu página antes de pagar."],
["Mar 15/12","reel","medio","rubro","Tu rubro #3: gastronomía en fiestas","Si tenés una rotisería, el 24 te van a escribir 300 personas. ¿Quién les contesta?","Una cocina animada a full: pedidos por WhatsApp, la carta que cambió, el horario del 24 y 31. La carta online y el bot lo ordenan todo.","5 planos en una cocina ilustrada","“Mandáselo a” con nombre","Mandáselo al de la rotisería."],
]
T = {"reel":["Reel","t-reel",""],"car":["Carrusel","t-car","car"],"post":["Posteo","t-post","post"],"hist":["Historia","t-hist","hist"]}
S = {"cuadra":["La Cuadra","s-cuadra"],"inv":["Inventos argentinos","s-inv"],"err":["Encontrá el error","s-err"],"rubro":["Tu rubro","s-rubro"]}
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
