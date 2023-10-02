# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:47:02 2023

@author: jumaf
"""

import torch
from transformers import BertTokenizerFast, EncoderDecoderModel

MODEL_SUMMARIZATION = 'mrm8488/bert2bert_shared-spanish-finetuned-summarization'

def generate_summary(text, model):
    """
    Genera el resumen de un texto en función de un modelo pre-entrenado
    Parameters:
        text (str): El texto a resumir
        model (str): El nombre del modelo pre-entrenado que se utilizará
    Returns: str: el texto resumido.
    """

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    tokenizer = BertTokenizerFast.from_pretrained(model)
    model = EncoderDecoderModel.from_pretrained(model).to(device)
    
    inputs = tokenizer(text, padding="max_length", truncation=True, max_length=512, return_tensors="pt")
    input_ids = inputs.input_ids.to(device)
    attention_mask = inputs.attention_mask.to(device)
    output = model.generate(input_ids, attention_mask=attention_mask)
    
    return [tokenizer.decode(output[i], skip_special_tokens=True) for i in range(len(output))]

texts = ["Junio de 2008 13 L a reduccion de los recursos naturales la degradacion del suelo la sobreexplotacion de los acuiferos y la acelerada perdida de la biodiversidad son algunos de los efectos del creciente deterioro ambiental que se viven hoy en dia en el mundo Los cambios sociales y econo micos experimentados en las ulti mas decadas suelen considerarse como los factores causantes de la degradacion ambiental El impacto del desarrollo economico del creci miento demografi co y de la explota cion de los recursos naturales en el medio ambiente propicio que el 15 de diciembre de 1972 la Asamblea General de las Naciones Unidas de signara el 5 de junio como el Dia Internacional del Medio Ambiente con el fi n de insistir en la necesidad de mejorar y conservar nuestro en torno Se eligio esa fecha porque se habia iniciado la Conferencia de las Naciones Unidas sobre el Medio Humano celebrada en Estocolmo en 1972 a raiz de la cual se creo el Programa de las Naciones Unidas sobre el Medio Ambiente y el Desarrollo se reunieron los pai ses para adoptar las decisiones que permitieran reavivar las esperanzas que habia infundido la Conferencia de 1972 y hacer frente al desafio de lograr un equilibrio viable y equi tativo entre medio ambiente y de sarrollo Principalmente esta fecha pre tende fomentar la sensibilizacion Dia Mundial mundial sobre el medio ambiente y promover la atencion y accion po litica al respecto Asimismo busca incentivar a las personas para que del Medio Ambiente se conviertan en agentes activos del desarrollo sostenible y equitati vo promover el papel fundamental de las comunidades en el cambio de actitud hacia temas ambientales y fomentar la cooperacion la cual ga rantizara que todas las naciones y personas disfruten de un futuro mas prospero y seguro14 Junio de 2008 La Conferencia sobre Medio Ambiente y Desarrollo de las Naciones Unidas conocida tam bien como la Cumbre de la Tierra celebrada en las cercanias de Rio de Janeiro Brasil en junio de 1992 constituye el mayor antecedente de la lucha contra el deterioro ambien tal En dicha cumbre se acordaron medidas para la proteccion del me dio ambiente Los temas principales que se trataron fueron el cambio del clima la biodiversidad la protec cion forestal la Agenda 21 un pro yecto de desarrollo medioambiental de 900 paginas y la Declaracion de Rio documento compuesto por seis paginas en el cual se demanda la integracion del medio ambiente y el desarrollo economico Este ano las principales celebra ciones se llevaran a cabo en Nueva Zelanda el tema seleccionado fue repercusiones del cambio climatico materia ecologica los principales Deje el habito Hacia una econo plantean el potencial de problemas problemas que enfrenta hoy en dia mia baja en carbono el cual alude a escala mundial que requiere que el pais son la disminucion y degra a los efectos del cambio climatico las naciones colaboren para conse dacion de la cubierta vegetal natural en nuestra era El Programa de guir soluciones Todos los paises del y del suelo la acelerada perdida de las Naciones Unidas para el Medio mundo estan reconociendo sus fun biodiversidad y la sobreexplotacion Ambiente PNUMA esta pidiendo a ciones para encontrar vias creativas de los acuiferos los paises las empresas y las comu con que hacer frente a los retos sin Al igual que en muchas naciones nidades que se concentren en bus precedentes del mundo el medio ambiente en Mexico no fue objeto de la atencion gubernamental sino hasta hace poco tiempo cuando los efectos del dete rioro ambiental se hicieron eviden El detrimento ambiental y la reduccion de los recursos tes y pusieron en riesgo el desarrollo naturales en las ultimas decadas han sido notorios futuro de muchos paises Aunque el desarrollo economico es indispen sable para garantizar el bienestar humano de cualquier Estado son muy altos los costos que implica el car el modo de reducir las emisiones En 2007 El deshielo Un tema lograrlo sin considerar el medio am de gases invernadero Hara hinca caliente fue el lema del Dia biente pie en los recursos e iniciativas que Internacional del Medio Ambiente En marzo de 2005 la Organizacion promuevan estilos de vida y econo y se enfoco en los efectos que el de las Naciones Unidas emitio el in mias con bajas emisiones de carbo cambio climatico esta teniendo en forme Evaluacion de los ecosistemas no como la mejora de la efi ciencia los ecosistemas y comunidades po del milenio en el que diagnostico el energetica las fuentes alternativas lares y las ulteriores consecuencias estado del planeta y de sus ecosiste de energia la conservacion de los alrededor del mundo mas ademas de ofrecer las acciones bosques y el consumo ecologico En Mexico la situacion no dista necesarias para mejorar la conserva Sequias e inundaciones niveles del mucho de la realidad mundial El cion y el uso sostenible de los mis mar en elevacion fusion de hielos detrimento ambiental y la reduccion mos degradacion de ecosistemas perdi de los recursos naturales en las ulti En la evaluacion la ONU senalo da de diversidad biologica y otras mas decadas han sido notorios En que la estructura y el funcionaJunio de 2008 15 miento de los ecosistemas del pla neta han cambiado en la segunda mitad del siglo XX mas rapida y ex tensamente que en ningun otro pe riodo de tiempo comparable de la historia humana en gran parte para resolver rapidamente las demandas crecientes de alimento agua dulce madera fi bra y combustible Esto ha generado una perdida conside rable y en gran medida irreversible de la diversidad de la vida sobre la Tierra Asimismo el informe resalto que la degradacion de los ecosistemas es una de las principales causales de pobreza Aproximadamente 17 millones de personas mueren al ano por escasez de agua e higiene y la mitad de la poblacion pobre que habita en las urbes ve afectada su salud por dicha escasez La desertifi cacion por su parte afecta a los me dios de sobrevivencia de millones de personas los sistemas de tierras se cas abarcan un 41 de la superfi cie terrestre y en ellas habitan mas de 2000 millones de personas de las cuales mas del 90 viven en paises en desarrollo de los ecosistemas y satisfacer a la sustanciales en las politicas institu El mayor reto que enfrenta el vez las demandas de sus servicios ciones e iniciativas existentes La planeta es revertir la degradacion Para lograrlo se requieren cambios Evaluacion examino 78 opciones de respuestas para los servicios y la gestion integral de los ecosistemas la conservacion y utilizacion soste nible de la biodiversidad y el cam bio climatico Pueden agruparse en cambios sustanciales en las institu ciones y gobiernos en las politicas economicas e incentivos en los fac tores sociales y de comportamien to y en la tecnologia y los conoci mientos Formular estrategias y politicas de gobierno que conjunten el desa rrollo economico y la conservacion del ambiente es fundamental para revertir el deterioro que se vive ac tualmente para ello es necesario contar con informacion sufi ciente y confi able sobre la situacion del medio ambiente y sobre los facto res que presionan su integridad y su efectividad",
        "CAMARA EMPRESARIA DE MEDIO AMBIENTERepresentacion de la Camara Empresaria de Medio Ambiente La CEMA ejerce un espacio de Representacion Gremial Empresaria desde hace veintitres anos y aspira a encarnar los genuinos intereses del Sector Ambiental Empresario a los que entiende alineados con los de la Comunidad el Ambiente y el Interes Nacional en la materiaLa Camara Empresaria de Medio Ambiente CEMA es una organizacion integrada por companias que proveen bienes y servicios para la preservacion del ambiente y la mejora de la calidad de vida Tiene 24 anos de vida y nuclea a 65 empresas lideres en distintos campos ambientalesLa Camara Empresaria de Medio Ambiente mantiene una estrecha relacion con camaras y organismos similares del pais y del exterior Cuenta con Comisiones Tecnicas para el estudio de cuestiones de relevancia Ademas ofrece a sus asociados Asistencia en Consultas puntuales relativas a aspectos tecnicos normativos o comerciales Fomenta la relacion entre sus integrantes a traves de las Reuniones de Seguimiento de Temas RST que se realizan semanalmente Organiza Eventos tecnicos y un Evento anual de Estrategias Ambientales con autoridades y destacados invitados especiales Participa u organiza Misiones Comerciales y Tecnologicas al Exterior y recibe Delegaciones Extranjeras interesadas en estrechar vinculos con empresas del sector ambiental en nuestro paisANALISIS FODA AMBIENTAL ARGENTINA Fortalezas Debilidades Capacidades cientificas y tecnicas Superposicion jurisdiccional Marco regulatorio profuso Inexistente informacion de base Acompanamiento judicial Deficit de planificacion e implementacion de politicas Debilidad de las autoridades de aplicacion Oportunidades Amenazas Innovacion tecnologica Temas explotan Generacion de puestos de trabajo Discontinuidad en la de calidad implementacion de politicas Generar herramientas con base al Problemas presupuestarios analisis de riesgo y de aplicabilidad progresiva Fuente CEMATEMAS DIAGNOSTICO RESIDUOS Niveles Enviados a CEAMSE 2004 100 4160 tndia Los rellenos sanitarios se estan agotando A la espera de la aprobacion de Ley residuos peligrosos SANEAMIENTO DE SITIOS Cuenca Matanza Riachuelo Reconquista y Sali Dulce Necesidad de identificar las CONTAMINADOS fuentes de contaminacion GESTION DEL AGUA Contaminacion de los recursos hidricos Bajo porcentaje 12 de tratamiento de aguas residuales EMISIONES GASEOSAS Control de emisiones muy poco regulado en Fuente Documento la mayoria del territorio nacional propuestas Ambientales CEMA RECURSOS NATURALES Recursos sobre explotados no valorizados ni ambiental ni economicamente Las politicas se instruyen de manera desarticulada y con organismos de control deficientes AGROINDUSTRIA Tratamiento inadecuado de efluentes y residuos Alta dependencia respecto a plaguicidas con impacto en la salud y el ambiente ENERGIA Necesidad de reacondicionar la matriz energeticaHacia donde deberia ir la Argentina en materia ambiental Actualizacion en la normativa ambiental con un marco regulatorio actualizado moderno y progresivo Actualizar el marco regulatorio para evaluar adecuadamente los impactos y controlar distintas etapas de los proyectos de la actividad no convencional de extraccion de gas Alcanzar el 100 de plantas de tratamiento de efluentes en Argentina Armado y ejecucion de un Plan Ambiental para sectores claves con el objetivo de aumentar las exportaciones nacionales Fortalecer mediante creditos verdes la inversion en las mejores tecnologias ambientales disponibles Impulsar fuertemente la Valorizacion del biogas cogeneracion electrica biometano para inyeccion en red de gas natural y combustible para vehiculos La Camara desarrolla actividades tecnicas y de divulgacion afines a diferentes sectores con el objeto de brindar a la comunidad y sobre todo a los decisores del ambito publico y privado las herramientas adecuadas para pensar las diversas actividades productivas desde una perspectiva ambiental Desde el ano 2010 se vienen desarrollando los Eventos anuales sobre Estrategias Ambientales donde participan representantes del sector publico empresarial academico y otras institucionesPRENSA Presentaron soluciones para el cuidado del medio ambiente NUlOtimTIaC mIoAdSif icacion 20 septiembre 2018 Twitter Facebook G Plus SUSCRIBITE ACTUALIDAD 17092018 C o n c lu s io n e s d e l 9E deg Home Actualidad Pedoja El medio ambiente debe ponerse a disposicion de los objetivos de la nacionP C0 o m1 p5 a rtir n c u e n tr o s o b r e e d o j a E l m e d io a m b ie n t e d e b e p o n e r s e B ajo el lema Hacia el Ambiente 40 se desarrollo el 9deg Encuentro sobre Estrategias E s tr a te g ia s A m b ie n ta le s a d is p o s ic io n d e lo s o b j e t iv o s d e la n a c io n Ambientales organizado por la Camara Empresaria de Medio Ambiente CEMA con el objetivo principal de brindar a la comunidad y a los decisores del ambito publico y privado las herramientas Posted on 24 septiembre 2018 by redaccion in Actualidad Entrevistas M edioambiente adecuadas para pensar diversas actividades productivas desde una perspectiva ambiental En la edicion 2018 que se llevo a cabo el pasado 13 de septiembre el compromiso asumido por la CEMA radico en darle tratamiento a tres grandes temas vinculados con la toma de conciencia ambiental la Sustentabilidad Agropecuaria la Evolucion de la normativa ambiental y las Tecnologias ambientales para acompanar al Ambiente 40 Durante el primer panel coordinado por el Ing Jose Mazzitelli de CEMA e integrado por la Ing Agr Amanda Fuxman del Area de Gestion de Proyectos Agroindustriales de la Subsecretaria de Alimentos y Bebidas de la Secretaria de Agregado de Valor el Ing Agr Marcelo Regunaga Analista de la Bolsa de Cereales y representante de la Red de Buenas Practicas Agropecuarias y el Dr Med Veterinario Claudio Glauber Especialista en Lecheria y Docente de la Facultad de Veterinaria de la UBA se expuso con profusion de detalles la situacion actual del sector agroindustrial con especial tratamiento al aspecto ambiental en cultivos intensivos como la horticultura y en la produccion primaria de la leche Bajo el lema Hacia el Ambiente 40 la Camara Empresaria de M edio Ambiente CEM A acaba de celebrar su noveno Encuentro sobre Estrategias Ambientales Al respecto conversamos con Guillermo Pedoja titular de la entidad quien destaco la disposicion del medio ambiente al servicio de los objetivos de la nacion Tenemos que ayudar al pais a salir de la mejor manera posible de su ajustada situacion actual expreso N O VE D AD ES Como puede brindar su aporte la CEM A en esta problematica preguntamos a Pedoja Podemos colaborar a traves del diseno y la implementacion de planes de apoyo a sectores clave exportadores en materia Ambiente 40 el primer evento sobre soluciones sustentables a las industrias que 9 deg E n c u e n tr o s o b r e E s tr a te g ia s ambiental Por nuestra parte no sabemos como nos afectara el cambio de rango de la cartera de Ambiente que paso de acompanen las nuevas tecnologias M inisterio a Secretaria Pero creo que la etapa del gradualismo se acabo y que tambien le llego al medio ambiente la etapa Detalles del realismo Categoria La region Visto 57 A m b ie n ta le s o r g a n iz a d o p o r C E M A Cual es tu vision del actual escenario ambiental en la Argentina Se habla mucho de medio ambiente pero la sociedad parece mas dispuesta a reclamar por sus derechos que a cumplir con A m b i e n t e 4 0 E n el m arco del 9deg E ncuentro sobre E strategias A m bientales y bajo el lem a H acia el A m biente 40 la C am ara E m presaria de M edio sus obligaciones M uchas veces por ejemplo el consumidor prefiere pagar un poco menos por un tomate que no es seguro por lo que no premia la produccion sustentable Hay que corregir este problema cultural con trabajo sistematico y con el aporte de medios de comunicacion serios como Futuro Sustentable de una Camara como la muestra y de empresarios que apuesten por las nuevas tecnologias y la competitividad E l n u e v o p a ra d ig m a q u e a c o m p a n a a la In d u s tria A m biente C E M A llevo a cabo el pasado jueves 13 de septiem bre una 4 0 nueva edicion de su tradicional evento de actualizacion profesional con el objetivo de difundir las ultim as soluciones para preservar el M edio A m biente y plantear la necesidad de actualizar las norm as en funcion Lic W itold Roman Kopytynski Ambiente 40 el primer evento sobre soluciones sustentables a las industrias que Fundador de Servicio Integral de Medio Ambiente SIM Integrante Comision Directiva de la Camara Empresaria de de los avances tecnologicos actuales acompanen las nuevas tecnologias Medio Ambiente CEMA AMBIENTE NACIONALES oH rga ac ni ia z ae l l a A Cm ambi ae rn at e E m4 p0 r e sae rs i a u dn e n Mue ev do io e An mcu be in et nr to e s Cob Er Me AE s t r Eat ne g si ua s n oA vm enb ai e en dta icle ios nq u see llevara a cabo el 13 de septiembre en el 725 Continental Hotel Ciudad A de Buenos Aires Ya estamos inmersos en la cuarta revolucion industrial que esta cambiando los paradigmas productivos y sin duda alguna cambiara forzosamente el paradigma ambiental Primero llego la maquina de vapor luego la La Camara Empresaria de Medio Ambiente CEMA institucion que lleva mas de 22 anos electricidad y la produccion masiva y en serie y finalmente la informatizacion y la automatizacion Con la cuarta fase las promoviendo la concientizacion y las buenas practicas industriales para el cuidado y computadoras trabajan directamente con la automatizacion de modo que no es siempre nueva tecnologia es un nuevo abordaje preservacion ambiental organiza su 9deg Encuentro sobre Estrategias Ambientales bajo el lemaHacia el Ambiente 40 que se llevara a cabo el jueves 13 de septiembre de 830 a industrial innovativo y enfocado a procesos La maquina de vapor causo la primera revolucion industrial La aplicacion de distintos avances tecnologicos fue configurando nuevas revoluciones hasta alcanzar el estadio actual en el que la incorporacion de las mas recientes tecnologias informaticas en todo tipo de elementos productivos herramientas y dispositivos da forma a la cuarta 1330 horas en 725 Continental Hotel ubicado en Av Roque Saenz Pena 725 Ciudad revolucion industrial la Industria 40 Autonoma de Buenos Aires El evento es gratuito y requiere inscripcion previa Portada Agenda Nota S u s te n ta b ilid a d 130918 Hacia el ambiente 40 En este momento es que cabe entonces introducir la pregunta y los conceptos de sustentabilidad que venimos desarrollando O a sonr bog rsa e pn Eriz o sa tm rd aoa tv ep i geo inr ad sla o A C l maa c bm o iena ncr tia ae n lE etm si z bp a ar c je i oos na er ly i la el a md se a b M u Hee nd aai co s i a pA erm la Acb ti mie cn a bt s ie e i nnC td eE u 4sM t 0rA ia l e i sn s tt ei ntu dc ri ao n lu q gu ae r l el le v 9a deg Em na cs u d ee n t2 r2 o L A Ta em rrba itp ie oe n rr itt aeu l r y ya CDes oet osa a rr r da r io na l al o cc i a oSr nug so dt ee d n Oe ta bbI rn l aeg P R uG a bb lu i c il aSl e e Fr rm eg rio no a BP nde ed orgo Amja la vnd a e ry e zC e dlE eSM CeA c er le istj a u yrn i o eto l d Pea r l e P sM l ia dni en i nfi ts ic etr a do c e io d ln ae Agencia de Proteccion Ambiental APRA Juan Bautista Filgueira Risso donde se situan en este proceso La respuesta no es simple ni directa y es mucho menos evidente cual sera el rumbo que la sustentabilidad debera tomar para acompanar a la Industria 40 Acerca de la Sustentabilidad sabemos y hemos aprendido acompanando a la Industria 30 ya casi introduciendonos en la cuarta fase del cambio El Ambiente la Economia y lo Social debidamente asociados equilibrados y complementados es lo que denominamos Sustentabilidad En el encuentro se abordaran los nuevos escenarios con los que se encuentran las empresas surgidos a partir de la utilizacion de tecnologias de ultima generacion de la mano de la Ambiente 40 el cuidado del ambienteI ndustria 40 o tambien llamada Cuarta Revolucion Industrial como son la incorporacion de la roboticala internet de las cosas el uso del Big Data o el Cloud Computing almacenamiento en la nube entre otros y como dichas empresas podrian en la produccion agroindustrial son una sed ca tp ot ra r as me ba i ela n td ai l g di ata nl diz oa c soio lun c d ioe n l eo ss ap r ocesos y a la aplicacion de esas nuevas tecnologias al factor determinante para el desarrollo Instituto Ciencia e Investigacion Se abordaran los nuevos escenarios con los que se encuentran las empresas surgidos a partir de la u Ctil uiz aa rtc ai o Rn e d voe lt ue cc in oo nl o Ing dia us s td re ia u llt i m ca o mge on se ora nc li ao n in c od re p ola r am cia on no d d ee l ala r I on bd ou tis ctr ai a l a4 i0 n to e rt na em t b di ee n la l sla cm osa ad sa el uso economico y social de las empresas Uruguay 260818 del Big Data o el Cloud Computing almacenamiento en la nube entre otros y como dichas empresas podrian adaptarse a la digitalizacion de los procesos y a la aplicacion de esas nuevas tecnologias al sector ambiental dando soluciones a Modelizar las emisiones gaseosas de parques o conglomerados industriales multiplicidad de Twitter c ontaminantes y fuentes de emision y controlar el impacto sobre poblaciones cercanas Facebook Monitorear la calidad de aire en puntos criticos Monitorear de ruido y contaminacion en grandes ciudades debido al transito urbano SEPTIEMBRE 19 2018 313 PM Monitorear zonas con alta frecuencia de incendios altas temperaturas sequias Monitorear cuerpos de agua superficiales y subterraneos RELACIONADASPresencia de funcionariosSponsorsAuspiciantesCantidad de participantes NUMERO DE INSCRIPTOS EVENTOS CEMA 800 700 600 500 400 300 200 100 2016 2017 2018 0Tipo de participantes Caracterizacion de Participantes Eventos CEMA 17 Empresas 38 Independientes Instituciones Camaras 24 Organismos Estado Universidades 9 12Luego de 9 anos de exitosos Eventos Anuales sobre Estrategias AmbientalesObjetivos Proponer objetivos y metas ambientales para un futuro cercano situado en el ano 2030 Nutrir el proceso de reflexion y estimular el debate entre los actores de mayor gravitacion de la economia que ayude a delinear una gestion ambiental y social sustentable para la Argentina del 2030 Entregable Presentar la actualizacion 2019 de nuestro documento Pautas ambientales para la Argentina que se viene elaborado en 2015 como una contribucion a los actores politicos en plena campana electoral En el 2019 se suman los aportes de las camaras y organismos representativos de cada sectorEn esta mirada hacia el 2030 son tenidos en cuenta el futuro de la sociedad el abastecimiento de recursos el marco economico y la calidad medioambiental La perspectiva de los escenarios a considerar tendran en cuenta lo deseable lo posible y lo probable a fin de proponer politicas de estado y el marco regulatorio pertinente aprovechando las oportunidades en materia de tecnologias ambientalesMedia Partner Categoria ORO Categoria PLATALugar y fecha Horario 9 a 18 horasModalidad Salon Plenario Panel de disertantes 400 PAX PANELES Produccion agropecuaria Empresa Gobierno Industria manufacturera Empresa Moderador Mineria Energias renovables No convencionales Construccion e infraestructura Periodistas moderadores Silvia Naishtat Marina Aizen Laura Rocha CEMA Camara sectorial Hector Huergo Daniel Bosque Gustavo Di CostaModalidad Taller en Aula Magna 120 pax Produccion desarrollo e innovacion para la competitividad Mejores tecnologias disponibles MTD Empresas presentan logros destacados en materia ambientalComo llegar UbicacionSector acreditacionSala plenaria Salon Juan Pablo IISala plenariaSala plenaria Sala Plenaria Juan Pablo II 400 personas Foyer de 400m2 GuardarropasSector Stands y NetworkSector Stands y NetworkSala Talleres Aula magna Sala en simultaneo para 120 personas Foyer de 100 m2 Aula MagnaPlano 2do piso Salon Juan Pablo IIPlano 1er Piso Aula MagnaMuchas gracias"]

summarys = []

for doc in texts:
    summarys.append(generate_summary(doc, MODEL_SUMMARIZATION))
    