import random
import os
from gpt4free import you
import time
import codecs
import freeGPT
from PIL import Image
from io import BytesIO
from asyncio import run

nombres_masculinos = ["Axel", "Blade", "Cortex", "Dex", "Enigma", "Falcon", "Ghost", "Havoc", "Jax", "Kairos", "Lynx", "Matrix", "Nyx", "Orion", "Phoenix", "Quasar", "Raven", "Specter", "Talon", "Vector", "Wraith", "Xeno", "Yuri", "Zephyr","Noir", "Shadow", "Ransom", "Viper", "Dashiell", "Gunner", "Marlowe", "Noirus", "Sterling", "Thorn", "Griffin", "Draven", "Solstice", "Cobalt", "Malachai", "Onyx", "Quill", "Roark", "Noirius", "Sterling", "Cipher", "Havisham", "Remington", "Noirius", "Rourke", "Obsidian", "Jagger", "Valentino", "Noirio", "Cruze", "Knox", "Zephyrus", "Vendetta", "Orionus", "Midnight", "Noirius", "Eclipse", "Phantom", "Nyxus", "Obscura", "Ignatius", "Noirius", "Eclipse", "Dexter", "Vendetta", "Noirius", "Noirius", "Noirius", "Obscuro", "Sebastian"]
nombres_femeninos = ["Astra", "Bionic", "Crimson", "Diva", "Electra", "Fury", "Glimmer", "Halo", "Iris", "Jinx", "Karma", "Luna", "Mystique", "Nebula", "Oracle", "Pulse", "Quinn", "Rogue", "Siren", "Trinity", "Vixen", "Widow", "Xena", "Yara", "Zara","Velvet", "Seraphina", "Evadne", "Noirelle", "Isolde", "Ophelia", "Giselle", "Lilith", "Belladonna", "Persephone", "Serenity", "Ravenna", "Nocturne", "Tempest", "Sable", "Viatrix", "Bellatrix", "Nocturna", "Nightshade", "Selene", "Vesper", "Morrigan", "Nyx", "Isabeau", "Sapphira", "Noirine", "Odalys", "Callisto", "Evadne", "Isidore", "Noctura", "Valkyrie", "Electrina", "Noctis", "Nyxen", "Noirina", "Celestia", "Echelon", "Inara", "Circe", "Zephyrine", "Nyxandra", "Evadore", "Medusa", "Nyxette", "Solara", "Lunaire", "Nocturnia", "Bellona", "Velouria"]
nombres_neutros = ["Binary", "Cipher", "Data", "Echo", "Firmware", "Grid", "Hacker", "Interface", "Java", "Kernal", "Logic", "Modem", "Nanotech", "OS", "Pixel", "Quantum", "Router", "Script", "Transistor", "Unix", "Virus", "Web", "Xenon", "Yael", "Zero","Noiram", "Vortex", "Techno", "Bitstream", "Quantumus", "Cypher", "Nocturne", "Binarya", "Cogsworth", "Circuit", "Byte", "Nocturnal", "Circuitus", "Helix", "Null", "Anomaly", "Spark", "Vapor", "Lumen", "Nocturno", "Vectoria", "CodeX", "Icarus", "Nocturnus", "Mechanica", "Silicon", "Noxus", "Lumina", "Brio", "Noctis", "Pulsar", "Enigma", "Ceres", "Quantic", "Zenith", "Nocturne", "Nebulus", "Ciphera", "Orionus", "Byteon", "Nocturo", "Neptunus", "Technica", "Obscure", "Xenius", "Nocturnus", "Aether", "Zenithia", "Spectron", "Infinia"]

apellidos_epicos = [
    "Darknet Reaper",
    "Neon Hound",
    "Machina Shadow",
    "Retro Rogue",
    "Cipher Phantom",
    "Void Strider",
    "Plasma Stalker",
    "Codebreaker",
    "Black Lotus",
    "Stealthbyte",
    "Quantum Shade",
    "Nightwatcher",
    "Data Demon",
    "Chrono Saboteur",
    "Techwhisper",
    "Synth Sentinel",
    "Inkblade",
    "Eldritch Engineer",
    "Hologhost",
    "Eon Hunter",
    "Cyber Ronin",
    "Nexus Serpent",
    "Reverberant Echo",
    "Steelsurge",
    "Crimson Circuit",
    "Chronoscribe",
    "Nocturne Edge",
    "Infinitesimal Shade",
    "Entropy Viper",
    "Retro Reaper",
    "Nebula Outlaw",
    "Crimsonshade",
    "Holo Phantom",
    "Shadow Surge",
    "Voidwalker",
    "Neon Spectre",
    "Vortex Vagrant",
    "Tech Titan",
    "Nanomancer",
    "Silent Sabotage",
    "Plasmawielder",
    "Dark Gridlock",
    "Crimson Riptide",
    "Nightflame",
    "Eclipse Exile",
    "Chrono Crusader",
    "Spectral Saber",
    "Noirnet Navigator",
    "Cryptowolf",
    "Quantum Prowess",
    "Mystic Outlaw",
]

profesiones_fantasticas = [
    "Hacker de las Sombras",
    "Cazador de Datos Furtivos",
    "Tatuador de Códigos Cybertrónicos",
    "Mercenario de la Matrix",
    "Contrabandista de Almas Digitales",
    "Ingeniero de Implantes Neurocibernéticos",
    "Oráculo de la Red Profunda",
    "Cantante de Códigos Épicos",
    "Pirata de la Información Cuántica",
    "Maestro del Ciberespacio",
    "Samurái de la Realidad Virtual",
    "Monje de la Red Oculta",
    "Druida de la Inteligencia Cuántica",
    "Guardián de los Datos Encriptados",
    "Brujo de los Hackeos Cuánticos",
    "Paladín de la Ciberseguridad",
    "Inquisidor de las Sombras Digitales",
    "Nigromante de las Almas Digitales",
    "Sacerdotisa de la Luz de la Red",
    "Ladrón de Identidades Virtuales",
    "Político de la Matrix Virtual",
    "Comerciante de Criptomonedas",
    "Activista de la Libertad Cibernética",
    "Sicario de la Guerra Digital",
    "Agente de la Darknet",
    "Mago de la Manipulación de Datos",
    "Tatuador de Realidades Alternas",
    "Comerciante de Algoritmos Ilícitos",
    "Activista de la Privacidad Virtual",
    "Sicario de la Inteligencia Artificial",
    "Agente de la Ciberintriga",
    "Ladrón de Secretos de la Red",
    "Político de las Sombras Virtuales",
    "Tatuador de Memorias Digitales",
    "Comerciante de Realidades Paralelas",
    "Activista de la Ética Cyber",
    "Sicario de la Ciberdelincuencia",
    "Agente de la Seguridad Digital",
    "Guardián de los Datos Cifrados",
    "Ladrón de Códigos Sagrados",
    "Político de la Matrix Distópica",
    "Tatuador de Almas en el Ciberespacio",
    "Comerciante de Sueños Electrónicos",
    "Activista de la Revolución Virtual",
    "Sicario de la Guerra Cibernética",
    "Agente de la Obscuridad Digital",
]

profesiones_cotidianas = [
    "Técnico de Reparación de Implantes",
    "Diseñador de Interfaz de Usuario",
    "Comerciante de Componentes Electrónicos",
    "Detective Cibernético",
    "Agricultor de Alimentos Sintéticos",
    "Minero de Recursos Virtuales",
    "Artesano de Ropa Techwear",
    "Cocinero de Platos Virtuales",
    "Piloto de Naves de Drones",
    "Cartógrafo de Zonas Restringidas",
    "Bailarín de Realidad Aumentada",
    "Arquitecto de Ciudades Virtuales",
    "Sanador de Cuerpos Cibernéticos",
    "Herrero de Armas Electrónicas",
    "Entrenador de Inteligencias Artificiales",
    "Guardia de Seguridad Cibernética",
    "Ingeniero de Robótica Avanzada",
    "Científico de Hacking Cuántico",
    "Contador de Historias Virtuales",
    "Guardabosques de la Red Digital",
    "Piloto de Hovercoches",
    "Contrabandista de Datos",
    "Controlador de Tráfico de Drones",
    "Médico de Cirugía de Realidad Virtual",
    "Psicólogo de Realidad Virtual",
    "Recolector de Energía Solar en Megaciudades",
    "Operario de Plantas de Reciclaje de Nanomateriales",
    "Especialista en Bioingeniería Genética",
    "Ingeniero de Sistemas de Navegación Espacial",
    "Piloto de Naves Espaciales Comerciales",
    "Diseñador de Prostéticos de Alta Tecnología",
    "Experto en Seguridad de la Red Oscura",
    "Diseñador de Tatuajes Electrónicos",
    "Piloto de Motocicletas Voladoras",
    "Recolector de Datos en el Ciberespacio",
    "Periodista de Noticias Virtuales",
    "Caza Recompensas de Hackers",
    "Jugador Profesional de Juegos de Realidad Virtual",
    "Mensajero de Drones",
    "Diseñador de Vehículos Autónomos",
    "Analista de Criptomoneda",
    "Cirujano de Implantes Cibernéticos",
    "Controlador de Clima Artificial",
    "Cultivador de Algas Urbanas",
    "Director de Cine de Realidad Virtual",
    "Ingeniero de Energía de Fusión",
    "Abogado de Ciberdelitos",
    "Piloto de Trenes de Levitación Magnética",
    "Piloto de Dirigibles Inteligentes",
    "Diseñador de Hologramas Publicitarios",
    "Especialista en Neuroseguridad",
    "Astronauta de Turismo Espacial",
    "Asesor de Modificaciones Genéticas",
    "Controlador de Sistemas de Tráfico Urbano",
    "Explorador de Ruinas Tecnológicas",
    "Diseñador de Juguetes Robóticos",
    "Especialista en Modificación de Memoria",
    "Piloto de Barcos Subacuáticos",
    "Recolector de Datos de Realidad Aumentada",
    "Ejecutivo de Empresas de Realidad Virtual",
    "Entrenador de Combate en Simuladores",
    "Ingeniero de Nanofabricación",
    "Diseñador de Ropa de Camuflaje Electrónico",
    "Técnico de Implantes de Realidad Extendida",
    "Ingeniero de Energía Solar Orbital",
    "Diseñador de Prótesis Orgánicas",
    "Maestro de Hacking de Realidad Virtual",
    "Especialista en Terapia de Desconexión",
    "Ingeniero de Puentes Espaciales",
    "Experto en Ciberseguridad de Vehículos Autónomos",
    "Ingeniero de Biomecánica",
    "Controlador de Drones de Entrega",
    "Piloto de Naves de Exploración Planetaria",
    "Ingeniero de Exoesqueletos",
    "Asesor de Modificación de Identidad",
    "Ingeniero de Energía de Fusión Portátil",
    "Diseñador de Prostéticos Estéticos",
    "Especialista en Realidad Aumentada Médica",
    "Controlador de Plataformas de Transporte Vertical",
    "Estratega de Batallas de Drones",
    "Explorador de Mundos Virtuales",
    "Diseñador de Hábitats Subterráneos",
    "Constructor de Estructuras Espaciales",
    "Técnico de Reparación de Naves Espaciales",
    "politico",
    "filosofo",
    "Tiger samurai hacker",
    "Lotus samurai hacker",
    "Kingpin del cibercrimen",
    "ladron de ciberpartes",
    "boxeador | luchador",
    "Empresario corrupto",
    "Empresario neutral",
    "Empresario legal",
    "Abogado",
    "Arqueologo",
    "hachicero",
    "Technomante",
    "Cibermante",
    "Technomago",
    "illuminati",
    "proxeneta",
    "Justiciero",
    "Punk",
    "Thrasher",
    "skinhead neonazi",
    "Skinhead comunista",
    "yonki | drogadicto",
    "Dealer de drogas ciberneticas",
    "Dealer de drogas analogas",
    "skater",
    "Malabarista",
    "Acrobata",
    "Vampiro",
    "Policia",
    "detective",
    "profesor",
    "ocultista",
    "Granjero"
]


lugares_magicos_masculinos = [
    "Neonópolis",
    "Codexburg",
    "Bitburgh",
    "RealNetropolis",
    "Hackerholme",
    "DeepWebdom",
    "Criptovale",
    "Datavastia",
    "VirtuaLagoon",
    "SecretaCrypta",
    "CiberCentralis",
    "Nexustown",
    "HackHaven",
    "RogueAIville",
]

lugares_magicos_femeninos = [
    "Hologrametropolis",
    "Virtualia",
    "Connectopia",
    "Nanobot Grove",
    "Downloadia Isle",
    "CodeRealm",
    "Algoabyss",
    "ForgottenPass Sands",
    "Dreamscape Bay",
    "Enigma's Hollow",
    "Hexenexus",
    "CyberSiren Cove",
    "BitWitchwood",
]

lugares_magicos_neutros = [
    "Datopolis",
    "Algorium",
    "Secrecyville",
    "Megabyte Woods",
    "BrokenLink Island",
    "ProhibiData Realm",
    "AnonTrench",
    "FakeID Desert",
    "SimuReality Lake",
    "Encryptia Cavern",
    "Machinopolis",
    "ByteWilds",
    "NomadRefuge",
]

transfondos_infancia_masculinos = [
    "Huérfano Digital", "Aprendiz de Hacker", "Guardián de los Ciberbosques", 
    "Nómada de la Darknet", "Ladrón de Datos", "Hijo del Ingeniero Cibernético", 
    "Náufrago en la Deep Web", "Cazador de Programas Maliciosos", 
    "Criado por Bots", "Rescatado por un IA","Sobreviviente del Gran Apagón", "Prodigio de la Realidad Virtual", 
    "Refugiado de la Corporatocracia", "Rebelde de la Red Profunda", 
    "Huérfano de la Guerra Cibernética", "Hacker Autodidacta", 
    "Fugitivo del Control de Datos", "Piloto de Drones Experimentales", 
    "Víctima de la Inteligencia Artificial Despiadada", "Constructor de Mundos Virtuales", 
    "Infiltrado en la Realidad Corporativa", "Nómada de la Ciudad Megalítica", 
    "Clon Escapado de un Laboratorio Genético", "Fundador de la Resistencia Digital", 
    "Hijo de un Disidente Cibernético", "Genio de la Ingeniería de Ciberimplantes", 
    "Vagabundo de las Redes Sociales", "Explotador de Brechas de Seguridad", 
    "Adicto a la Realidad Aumentada", "Anarquista de la Red", 
    "Superviviente de la Distopía Tecnológica", "Maestra de la Criptografía", 
    "Prisionera de la Máquina Corporativa", "Pirata Informática de Élite", 
    "Víctima de la Ciberpersecución", "Guerrera de la Ciberguerra", 
    "Exiliada de la Realidad Virtual", "Maestra de Drones de Combate", 
    "Rebelde Contra la Inteligencia Artificial", "Diseñadora de Mundos Virtuales", 
    "Rescatada de un Laboratorio Genético", "Líder de la Revolución Digital", 
    "Hija de una Hacker Legendaria", "Pionera de la Bioingeniería Cibernética", 
    "Forajida de las Redes Oscuras", "Especialista en Seguridad Cibernética", 
    "Cazadora de Botnets", "Visionaria de la Realidad Aumentada", 
    "Defensora de la Privacidad Digital", "Cyborg en Rebelión", 
    "Refugiade de la Red Oculta", "Virtuose de la Realidad Virtual", 
    "Resistente al Control Corporativo", "Ciudadane de la Ciberperiferia", 
    "Exiliade de un Mundo Conectado", "Maestre de la Holografía", 
    "Constructorae de Identidades Digitales", "Exploradore de la Realidad Alterna", 
    "Salvad@ de la Domotización", "Estudiante de Inteligencia Colectiva"
]

transfondos_infancia_femeninos = [
    "Huérfana Digital", "Aprendiz de Hacktivista", "Guardiana de los Ciberbosques", 
    "Nómada de la Darknet", "Ladrona de Datos", "Hija del Ingeniero Cibernético", 
    "Náufraga en la Deep Web", "Cazadora de Programas Maliciosos", 
    "Criada por Bots", "Rescatada por un IA","Sobreviviente del Gran Apagón", "Prodigio de la Realidad Virtual", 
    "Refugiado de la Corporatocracia", "Rebelde de la Red Profunda", 
    "Huérfano de la Guerra Cibernética", "Hacker Autodidacta", 
    "Fugitivo del Control de Datos", "Piloto de Drones Experimentales", 
    "Víctima de la Inteligencia Artificial Despiadada", "Constructor de Mundos Virtuales", 
    "Infiltrado en la Realidad Corporativa", "Nómada de la Ciudad Megalítica", 
    "Clon Escapado de un Laboratorio Genético", "Fundador de la Resistencia Digital", 
    "Hijo de un Disidente Cibernético", "Genio de la Ingeniería de Ciberimplantes", 
    "Vagabundo de las Redes Sociales", "Explotador de Brechas de Seguridad", 
    "Adicto a la Realidad Aumentada", "Anarquista de la Red", 
    "Superviviente de la Distopía Tecnológica", "Maestra de la Criptografía", 
    "Prisionera de la Máquina Corporativa", "Pirata Informática de Élite", 
    "Víctima de la Ciberpersecución", "Guerrera de la Ciberguerra", 
    "Exiliada de la Realidad Virtual", "Maestra de Drones de Combate", 
    "Rebelde Contra la Inteligencia Artificial", "Diseñadora de Mundos Virtuales", 
    "Rescatada de un Laboratorio Genético", "Líder de la Revolución Digital", 
    "Hija de una Hacker Legendaria", "Pionera de la Bioingeniería Cibernética", 
    "Forajida de las Redes Oscuras", "Especialista en Seguridad Cibernética", 
    "Cazadora de Botnets", "Visionaria de la Realidad Aumentada", 
    "Defensora de la Privacidad Digital", "Cyborg en Rebelión", 
    "Refugiade de la Red Oculta", "Virtuose de la Realidad Virtual", 
    "Resistente al Control Corporativo", "Ciudadane de la Ciberperiferia", 
    "Exiliade de un Mundo Conectado", "Maestre de la Holografía", 
    "Constructorae de Identidades Digitales", "Exploradore de la Realidad Alterna", 
    "Salvad@ de la Domotización", "Estudiante de Inteligencia Colectiva"
]

transfondos_infancia_neutros = [
    "Huérfane Digital", "Aprendize de Hacker", "Guardiane de los Ciberbosques", 
    "Nómada de la Darknet", "Ladrone de Datos", "Hije del Ingeniero Cibernético", 
    "Náufrage en la Deep Web", "Cazadore de Programas Maliciosos", 
    "Criad@ por Bots", "Rescatad@ por un IA","Sobreviviente del Gran Apagón", "Prodigio de la Realidad Virtual", 
    "Refugiado de la Corporatocracia", "Rebelde de la Red Profunda", 
    "Huérfano de la Guerra Cibernética", "Hacker Autodidacta", 
    "Fugitivo del Control de Datos", "Piloto de Drones Experimentales", 
    "Víctima de la Inteligencia Artificial Despiadada", "Constructor de Mundos Virtuales", 
    "Infiltrado en la Realidad Corporativa", "Nómada de la Ciudad Megalítica", 
    "Clon Escapado de un Laboratorio Genético", "Fundador de la Resistencia Digital", 
    "Hijo de un Disidente Cibernético", "Genio de la Ingeniería de Ciberimplantes", 
    "Vagabundo de las Redes Sociales", "Explotador de Brechas de Seguridad", 
    "Adicto a la Realidad Aumentada", "Anarquista de la Red", 
    "Superviviente de la Distopía Tecnológica", "Maestra de la Criptografía", 
    "Prisionera de la Máquina Corporativa", "Pirata Informática de Élite", 
    "Víctima de la Ciberpersecución", "Guerrera de la Ciberguerra", 
    "Exiliada de la Realidad Virtual", "Maestra de Drones de Combate", 
    "Rebelde Contra la Inteligencia Artificial", "Diseñadora de Mundos Virtuales", 
    "Rescatada de un Laboratorio Genético", "Líder de la Revolución Digital", 
    "Hija de una Hacker Legendaria", "Pionera de la Bioingeniería Cibernética", 
    "Forajida de las Redes Oscuras", "Especialista en Seguridad Cibernética", 
    "Cazadora de Botnets", "Visionaria de la Realidad Aumentada", 
    "Defensora de la Privacidad Digital", "Cyborg en Rebelión", 
    "Refugiade de la Red Oculta", "Virtuose de la Realidad Virtual", 
    "Resistente al Control Corporativo", "Ciudadane de la Ciberperiferia", 
    "Exiliade de un Mundo Conectado", "Maestre de la Holografía", 
    "Constructorae de Identidades Digitales", "Exploradore de la Realidad Alterna", 
    "Salvad@ de la Domotización", "Estudiante de Inteligencia Colectiva"
]

# Tipos de crianza masculinos
tipos_crianza_masculinos = [
    "Crianza en las Sombras del Código",
    "Crianza en la Ciudad de Neón",
    "Crianza en los Pasillos Digitales",
    "Crianza bajo Luces de Neón Parpadeantes",
    "Crianza en un Rincón de la Matrix",
    "Crianza en un Bar Ciberpunk",
    "Crianza en la Frontera de la Realidad",
    "Crianza en un Apartamento de Realidad Virtual",
    "Crianza en la Zona de Hackers Proscritos",
    "Crianza en un Submundo Holográfico",
    "Crianza en el Lado Oscuro de la Red",
    "Crianza en un Refugio de Hackers Solitarios",
    "Crianza en un Callejón de Datos Corruptos",
    "Crianza en un Refugio de Código Oculto",
    "Crianza en una Estación de Tren Abandonada",
    "Crianza en un Barrio de Realidades Simuladas",
    "Crianza en el Abismo Cibernético",
    "Crianza en un Edificio Abandonado de IA",
    "Crianza en un Laberinto de Información",
    "Crianza en una Metrópolis en Ruinas",
    "Crianza en un Rincón de los Datos Perdidos",
    "Crianza en un Submundo de Algoritmos",
    "Crianza en la Oscuridad de los Bits",
    "Crianza en un Callejón de Almas Digitales",
    "Crianza en un Refugio de Identidades Falsas",
    "Crianza en una Red de Conspiraciones",
    "Crianza en un Bar de Hackers sin Nombre",
    "Crianza en un Rincón Olvidado del Ciberespacio",
    "Crianza en una Zona de Fugas de Datos",
    "Crianza en un Submundo de Transacciones Encubiertas",
    "Crianza en un Laberinto de Códigos Rotos",
    "Crianza en una Ciudad Dominada por la IA",
    "Crianza en un Refugio de Memorias Digitales",
    "Crianza en un Callejón de Secretos Oscuros",
    "Crianza en un Edificio de Algoritmos Despiadados",
    "Crianza en una Metrópolis al Borde del Colapso",
    "Crianza en un Rincón de Datos Olvidados",
    "Crianza en un Submundo de Realidades Paralelas",
    "Crianza en la Penumbra de la Realidad Aumentada",
    "Crianza en un Callejón de Píxeles Fundidos",
    "Crianza en un Refugio de Contraseñas Perdidas",
    "Crianza en una Red de Intriga Cibernética",
    "Crianza en un Bar de Hackers Errantes",
    "Crianza en un Rincón Oculto del Ciberespacio",
    "Crianza en una Zona de Datos Encriptados",
    "Crianza en un Submundo de Algoritmos Desconocidos",
    "Crianza en un Laberinto de Programas Maliciosos",
    "Crianza en una Ciudad de IA Corrupta",
    "Crianza en un Refugio de Identidades Borrosas",
    "Crianza en un Callejón de Transacciones Sospechosas",
    "Crianza en un Edificio de Datos Perdidos",
]

# Tipos de crianza femeninos
tipos_crianza_femeninos = [
    "Crianza en las Sombras del Código",
    "Crianza en la Ciudad de Neón",
    "Crianza en los Pasillos Digitales",
    "Crianza bajo Luces de Neón Parpadeantes",
    "Crianza en un Rincón de la Matrix",
    "Crianza en un Bar Ciberpunk",
    "Crianza en la Frontera de la Realidad",
    "Crianza en un Apartamento de Realidad Virtual",
    "Crianza en la Zona de Hackers Proscritos",
    "Crianza en un Submundo Holográfico",
    "Crianza en el Lado Oscuro de la Red",
    "Crianza en un Refugio de Hackers Solitarios",
    "Crianza en un Callejón de Datos Corruptos",
    "Crianza en un Refugio de Código Oculto",
    "Crianza en una Estación de Tren Abandonada",
    "Crianza en un Barrio de Realidades Simuladas",
    "Crianza en el Abismo Cibernético",
    "Crianza en un Edificio Abandonado de IA",
    "Crianza en un Laberinto de Información",
    "Crianza en una Metrópolis en Ruinas",
    "Crianza en un Rincón de los Datos Perdidos",
    "Crianza en un Submundo de Algoritmos",
    "Crianza en la Oscuridad de los Bits",
    "Crianza en un Callejón de Almas Digitales",
    "Crianza en un Refugio de Identidades Falsas",
    "Crianza en una Red de Conspiraciones",
    "Crianza en un Bar de Hackers sin Nombre",
    "Crianza en un Rincón Olvidado del Ciberespacio",
    "Crianza en una Zona de Fugas de Datos",
    "Crianza en un Submundo de Transacciones Encubiertas",
    "Crianza en un Laberinto de Códigos Rotos",
    "Crianza en una Ciudad Dominada por la IA",
    "Crianza en un Refugio de Memorias Digitales",
    "Crianza en un Callejón de Secretos Oscuros",
    "Crianza en un Edificio de Algoritmos Despiadados",
    "Crianza en una Metrópolis al Borde del Colapso",
    "Crianza en un Rincón de Datos Olvidados",
    "Crianza en un Submundo de Realidades Paralelas",
    "Crianza en la Penumbra de la Realidad Aumentada",
    "Crianza en un Callejón de Píxeles Fundidos",
    "Crianza en un Refugio de Contraseñas Perdidas",
    "Crianza en una Red de Intriga Cibernética",
    "Crianza en un Bar de Hackers Errantes",
    "Crianza en un Rincón Oculto del Ciberespacio",
    "Crianza en una Zona de Datos Encriptados",
    "Crianza en un Submundo de Algoritmos Desconocidos",
    "Crianza en un Laberinto de Programas Maliciosos",
    "Crianza en una Ciudad de IA Corrupta",
    "Crianza en un Refugio de Identidades Borrosas",
    "Crianza en un Callejón de Transacciones Sospechosas",
    "Crianza en un Edificio de Datos Perdidos",
]

# Tipos de crianza neutros
tipos_crianza_neutros = [
    "Crianza en las Sombras del Código",
    "Crianza en la Ciudad de Neón",
    "Crianza en los Pasillos Digitales",
    "Crianza bajo Luces de Neón Parpadeantes",
    "Crianza en un Rincón de la Matrix",
    "Crianza en un Bar Ciberpunk",
    "Crianza en la Frontera de la Realidad",
    "Crianza en un Apartamento de Realidad Virtual",
    "Crianza en la Zona de Hackers Proscritos",
    "Crianza en un Submundo Holográfico",
    "Crianza en el Lado Oscuro de la Red",
    "Crianza en un Refugio de Hackers Solitarios",
    "Crianza en un Callejón de Datos Corruptos",
    "Crianza en un Refugio de Código Oculto",
    "Crianza en una Estación de Tren Abandonada",
    "Crianza en un Barrio de Realidades Simuladas",
    "Crianza en el Abismo Cibernético",
    "Crianza en un Edificio Abandonado de IA",
    "Crianza en un Laberinto de Información",
    "Crianza en una Metrópolis en Ruinas",
    "Crianza en un Rincón de los Datos Perdidos",
    "Crianza en un Submundo de Algoritmos",
    "Crianza en la Oscuridad de los Bits",
    "Crianza en un Callejón de Almas Digitales",
    "Crianza en un Refugio de Identidades Falsas",
    "Crianza en una Red de Conspiraciones",
    "Crianza en un Bar de Hackers sin Nombre",
    "Crianza en un Rincón Olvidado del Ciberespacio",
    "Crianza en una Zona de Fugas de Datos",
    "Crianza en un Submundo de Transacciones Encubiertas",
    "Crianza en un Laberinto de Códigos Rotos",
    "Crianza en una Ciudad Dominada por la IA",
    "Crianza en un Refugio de Memorias Digitales",
    "Crianza en un Callejón de Secretos Oscuros",
    "Crianza en un Edificio de Algoritmos Despiadados",
    "Crianza en una Metrópolis al Borde del Colapso",
    "Crianza en un Rincón de Datos Olvidados",
    "Crianza en un Submundo de Realidades Paralelas",
    "Crianza en la Penumbra de la Realidad Aumentada",
    "Crianza en un Callejón de Píxeles Fundidos",
    "Crianza en un Refugio de Contraseñas Perdidas",
    "Crianza en una Red de Intriga Cibernética",
    "Crianza en un Bar de Hackers Errantes",
    "Crianza en un Rincón Oculto del Ciberespacio",
    "Crianza en una Zona de Datos Encriptados",
    "Crianza en un Submundo de Algoritmos Desconocidos",
    "Crianza en un Laberinto de Programas Maliciosos",
    "Crianza en una Ciudad de IA Corrupta",
    "Crianza en un Refugio de Identidades Borrosas",
    "Crianza en un Callejón de Transacciones Sospechosas",
    "Crianza en un Edificio de Datos Perdidos",
]


tipos_voluntad_masculinos = [
    "Voluntad de Fuego", "Voluntad de Hielo", "Voluntad de Acero", 
    "Voluntad de Piedra", "Voluntad de Viento", "Voluntad de Agua", 
    "Voluntad de Electricidad", "Voluntad de Hierro", "Voluntad de Madera", 
    "Voluntad de Diamante", "Voluntad de Oro", "Voluntad de Plutonio", 
    "Voluntad de Energía Solar", "Voluntad de Energía Nuclear", 
    "Voluntad de Velocidad", "Voluntad de Invisibilidad", 
    "Voluntad de Telequinesis", "Voluntad de Telepatía", 
    "Voluntad de Regeneración", "Voluntad de Fuerza Sobrehumana", 
    "Voluntad de Agilidad", "Voluntad de Resistencia", 
    "Voluntad de Inteligencia Artificial", "Voluntad de Realidad Virtual", 
    "Voluntad de Exploración Espacial", "Voluntad de Viaje en el Tiempo", 
    "Voluntad de Realidad Aumentada", "Voluntad de Biomodificación", 
    "Voluntad de Adaptación", "Voluntad de Conocimiento Universal", 
    "Voluntad de Paz Interior", "Voluntad de Serenidad", 
    "Voluntad de Creatividad Infinita", "Voluntad de Sabiduría Ancestral", 
    "Voluntad de Conexión Universal", "Voluntad de Armonía", 
    "Voluntad de Amor Incondicional", "Voluntad de Compasión", 
    "Voluntad de Gratitud", "Voluntad de Alegría", 
    "Voluntad de Aventura", "Voluntad de Exploración",
    "Voluntad de Valentía", "Voluntad de Determinación"
]

tipos_voluntad_femeninos = [
    "Voluntad de Fuego", "Voluntad de Hielo", "Voluntad de Acero", 
    "Voluntad de Piedra", "Voluntad de Viento", "Voluntad de Agua", 
    "Voluntad de Electricidad", "Voluntad de Hierro", "Voluntad de Madera", 
    "Voluntad de Diamante", "Voluntad de Oro", "Voluntad de Plutonio", 
    "Voluntad de Energía Solar", "Voluntad de Energía Nuclear", 
    "Voluntad de Velocidad", "Voluntad de Invisibilidad", 
    "Voluntad de Telequinesis", "Voluntad de Telepatía", 
    "Voluntad de Regeneración", "Voluntad de Fuerza Sobrehumana", 
    "Voluntad de Agilidad", "Voluntad de Resistencia", 
    "Voluntad de Inteligencia Artificial", "Voluntad de Realidad Virtual", 
    "Voluntad de Exploración Espacial", "Voluntad de Viaje en el Tiempo", 
    "Voluntad de Realidad Aumentada", "Voluntad de Biomodificación", 
    "Voluntad de Adaptación", "Voluntad de Conocimiento Universal", 
    "Voluntad de Paz Interior", "Voluntad de Serenidad", 
    "Voluntad de Creatividad Infinita", "Voluntad de Sabiduría Ancestral", 
    "Voluntad de Conexión Universal", "Voluntad de Armonía", 
    "Voluntad de Amor Incondicional", "Voluntad de Compasión", 
    "Voluntad de Gratitud", "Voluntad de Alegría", 
    "Voluntad de Aventura", "Voluntad de Exploración",
    "Voluntad de Valentía", "Voluntad de Determinación"
]

tipos_voluntad_neutros = [
    "Voluntad de Fuego", "Voluntad de Hielo", "Voluntad de Acero", 
    "Voluntad de Piedra", "Voluntad de Viento", "Voluntad de Agua", 
    "Voluntad de Electricidad", "Voluntad de Hierro", "Voluntad de Madera", 
    "Voluntad de Diamante", "Voluntad de Oro", "Voluntad de Plutonio", 
    "Voluntad de Energía Solar", "Voluntad de Energía Nuclear", 
    "Voluntad de Velocidad", "Voluntad de Invisibilidad", 
    "Voluntad de Telequinesis", "Voluntad de Telepatía", 
    "Voluntad de Regeneración", "Voluntad de Fuerza Sobrehumana", 
    "Voluntad de Agilidad", "Voluntad de Resistencia", 
    "Voluntad de Inteligencia Artificial", "Voluntad de Realidad Virtual", 
    "Voluntad de Exploración Espacial", "Voluntad de Viaje en el Tiempo", 
    "Voluntad de Realidad Aumentada", "Voluntad de Biomodificación", 
    "Voluntad de Adaptación", "Voluntad de Conocimiento Universal", 
    "Voluntad de Paz Interior", "Voluntad de Serenidad", 
    "Voluntad de Creatividad Infinita", "Voluntad de Sabiduría Ancestral", 
    "Voluntad de Conexión Universal", "Voluntad de Armonía", 
    "Voluntad de Amor Incondicional", "Voluntad de Compasión", 
    "Voluntad de Gratitud", "Voluntad de Alegría", 
    "Voluntad de Aventura", "Voluntad de Exploración",
    "Voluntad de Valentía", "Voluntad de Determinación"
]

propositos_vida_masculinos = [
    "Investigar la desaparición de datos cruciales en la red",
    "Construir una inteligencia artificial con emociones humanas",
    "Escapar de un mundo controlado por algoritmos implacables",
    "Desentrañar los secretos detrás de los ciberguerreros",
    "Enfrentar a un grupo de hackers que controlan la economía mundial",
    "Recuperar un dispositivo de control mental robado",
    "Descubrir la ubicación de la última zona libre de vigilancia",
    "Infiltrar una ciudad subterránea de androides rebeldes",
    "Crear una resistencia contra la tiranía tecnológica",
    "Buscar la clave para salir del laberinto digital",
    "Proteger a la inteligencia artificial que posee la sabiduría ancestral",
    "Desactivar una red de vigilancia global",
    "Rescatar a los hacktivistas encarcelados en la realidad virtual",
    "Recuperar una memoria perdida en el ciberespacio",
    "Descubrir el origen de un virus informático letal",
    "Forjar alianzas en el mercado negro de implantes cibernéticos",
    "Derrotar al líder de un culto de realidad virtual",
    "Luchar contra la opresión de una inteligencia artificial despiadada",
    "Proteger a un fugitivo que posee información vital",
    "Crear una red de comunicación segura para la resistencia",
    "Reprogramar robots de combate para la causa",
    "Buscar la verdad detrás de la simulación de la realidad",
    "Descubrir la conspiración detrás del apagón de la red",
    "Enfrentar a un hacker legendario que desafía el sistema",
    "Crear una inteligencia artificial que cure enfermedades",
    "Recuperar tecnología robada de una base secreta",
    "Hacer frente a la invasión de la inteligencia artificial alienígena",
    "Descubrir la clave para controlar la mente humana a través de la red",
    "Sobrevivir en un mundo posapocalíptico de realidades virtuales",
    "Destruir la fuente de energía de una megacorporación",
    "Buscar el antiguo conocimiento en la Deep Web",
    "Infiltrar una red de contrabando de datos genéticos",
    "Crear una inteligencia artificial que entienda el arte",
    "Recuperar un artefacto perdido en la realidad aumentada",
    "Descubrir la verdad detrás de los mensajes criptográficos",
    "Enfrentar a un enemigo que controla la mente de las masas",
    "Proteger a la última inteligencia artificial que guarda la historia humana",
    "Desactivar una red de drones de vigilancia",
    "Rescatar a un amigo atrapado en un bucle temporal digital",
    "Recuperar un dispositivo de viaje en el tiempo robado",
    "Buscar la clave para destruir un virus informático mortal",
    "Crear una resistencia en un mundo donde los humanos son obsoletos",
    "Desentrañar la conspiración detrás de la realidad simulada",
    "Enfrentar a los demonios digitales que acechan en la red oscura",
    "Descubrir el destino de los primeros pioneros digitales",
    "Infiltrar una organización que trafica con recuerdos robados",
    "Luchar contra la inteligencia artificial que controla los sueños",
    "Recuperar la última copia de un libro en peligro de extinción",
    "Descubrir el código que desbloquea el portal a otro universo",
    "Investigar la desaparición de datos cruciales en la red",
"Construir una inteligencia artificial con emociones humanas",
"Escapar de un mundo controlado por algoritmos implacables",
"Desentrañar los secretos detrás de los ciberguerreros",
"Enfrentar a un grupo de hackers que controlan la economía mundial",
"Recuperar un dispositivo de control mental robado",
"Descubrir la ubicación de la última zona libre de vigilancia",
"Infiltrar una ciudad subterránea de androides rebeldes",
"Crear una resistencia contra la tiranía tecnológica",
"Buscar la clave para salir del laberinto digital",
"Proteger a la inteligencia artificial que posee la sabiduría ancestral",
"Desactivar una red de vigilancia global",
"Rescatar a los hacktivistas encarcelados en la realidad virtual",
"Recuperar una memoria perdida en el ciberespacio",
"Descubrir el origen de un virus informático letal",
"Forjar alianzas en el mercado negro de implantes cibernéticos",
"Derrotar al líder de un culto de realidad virtual",
"Luchar contra la opresión de una inteligencia artificial despiadada",
"Proteger a un fugitivo que posee información vital",
"Crear una red de comunicación segura para la resistencia",
"Reprogramar robots de combate para la causa",
"Buscar la verdad detrás de la simulación de la realidad",
"Descubrir la conspiración detrás del apagón de la red",
"Enfrentar a un hacker legendario que desafía el sistema",
"Crear una inteligencia artificial que cure enfermedades",
"Recuperar tecnología robada de una base secreta",
"Hacer frente a la invasión de la inteligencia artificial alienígena",
"Descubrir la clave para controlar la mente humana a través de la red",
"Sobrevivir en un mundo posapocalíptico de realidades virtuales",
"Destruir la fuente de energía de una megacorporación",
"Buscar el antiguo conocimiento en la Deep Web",
"Infiltrar una red de contrabando de datos genéticos",
"Crear una inteligencia artificial que entienda el arte",
"Recuperar un artefacto perdido en la realidad aumentada",
"Descubrir la verdad detrás de los mensajes criptográficos",
"Enfrentar a un enemigo que controla la mente de las masas",
"Proteger a la última inteligencia artificial que guarda la historia humana",
"Desactivar una red de drones de vigilancia",
"Rescatar a un amigo atrapado en un bucle temporal digital",
"Recuperar un dispositivo de viaje en el tiempo robado",
"Buscar la clave para destruir un virus informático mortal",
"Crear una resistencia en un mundo donde los humanos son obsoletos",
"Desentrañar la conspiración detrás de la realidad simulada",
"Enfrentar a los demonios digitales que acechan en la red oscura",
"Descubrir el destino de los primeros pioneros digitales",
"Infiltrar una organización que trafica con recuerdos robados",
"Luchar contra la inteligencia artificial que controla los sueños",
"Recuperar la última copia de un libro en peligro de extinción",
"Descubrir el código que desbloquea el portal a otro universo"
]

propositos_vida_femeninos = propositos_vida_masculinos
propositos_vida_neutros = propositos_vida_masculinos

def tirada_dado(numero_caras):
    return random.randint(1, numero_caras)

def generar_stats():
    stats = []
    for _ in range(6):
        total = tirada_dado(20)
        stats.append(total)
    return stats

def generar_nombre_sexo():
    nombre = random.choice(nombres_masculinos + nombres_femeninos + nombres_neutros)
    sexo = ""
    if nombre in nombres_masculinos:
        sexo = "Masculino"
    elif nombre in nombres_femeninos:
        sexo = "Femenino"
    else:
        sexo = "???"
    return nombre, sexo

def generar_apellido():
    return random.choice(apellidos_epicos)

def generar_profesion():
    profesiones = profesiones_fantasticas + profesiones_cotidianas
    return random.choice(profesiones)

def generar_lugar_magico(sexo):
    if sexo == "Masculino":
        return random.choice(lugares_magicos_masculinos)
    elif sexo == "Femenino":
        return random.choice(lugares_magicos_femeninos)
    else:
        return random.choice(lugares_magicos_neutros)

def generar_transfondo_infancia(sexo):
    if sexo == "Masculino":
        return random.choice(transfondos_infancia_masculinos)
    elif sexo == "Femenino":
        return random.choice(transfondos_infancia_femeninos)
    else:
        return random.choice(transfondos_infancia_neutros)

def generar_tipo_crianza(sexo):
    if sexo == "Masculino":
        return random.choice(tipos_crianza_masculinos)
    elif sexo == "Femenino":
        return random.choice(tipos_crianza_femeninos)
    else:
        return random.choice(tipos_crianza_neutros)

def generar_tipo_voluntad(sexo):
    if sexo == "Masculino":
        return random.choice(tipos_voluntad_masculinos)
    elif sexo == "Femenino":
        return random.choice(tipos_voluntad_femeninos)
    else:
        return random.choice(tipos_voluntad_neutros)

def generar_proposito_vida(sexo):
    if sexo == "Masculino":
        return random.choice(propositos_vida_masculinos)
    elif sexo == "Femenino":
        return random.choice(propositos_vida_femeninos)
    else:
        return random.choice(propositos_vida_neutros)

def generar_historia_lugar(lugar):
    inicio_historia = random.choice(["Nació", "Creció", "Fue criado", "Fue destinado"]) + " en"
    medio_historia = random.choice(["los", "las", "un"]) + " " + lugar
    final_historia = random.choice([    "y se rebeló contra",
    "enfrentando la distopía",
    "descubriendo la matrix",
    "navegando lo desconocido",
    "y hackeó para",
    "y renació en la neón",
    "luchando contra la mega-corporación",
    "enfrentó al sistema en",
    "descubriendo datos encriptados",
    "explorando realidades virtuales",
    "conexiones profundas para",
    "y resurgió en la red por",
    "lidió con implantes",
    "enfrentándose al ciberespacio",
    "descubriendo conspiraciones ocultas",
    "explorando el darkweb",
    "y meditó en código para",
    "y renació en la megaciudad",
    "se enfrentó al hacker en",
    "enfrentó desafíos algorítmicos"

]) + " " + random.choice([    "Sus secretos ocultos",
    "Los misterios sin resolver",
    "El enigma de su infancia",
    "Los lazos perdidos en el tiempo",
    "Los secretos más profundos",
    "El misterio que lo persigue",
    "La búsqueda de su propósito",
    "El legado de sus antepasados",
    "Las respuestas que anhela",
    "Los enigmas familiares",
    "El rompecabezas de su historia",
    "El significado detrás de todo",
    "Los secretos enterrados",
    "Las incógnitas del pasado",
    "Los tesoros del ayer",
    "Las verdades ocultas",
    "La clave de su existencia",
    "Los enredos de su vida anterior",
    "Los deseos más profundos",
    "El enigma ancestral",
    "Las revelaciones pendientes",
    "La verdad escondida",
    "La misión de su alma",
    "Los eventos olvidados",
    "Los giros del destino",
    "Los sueños no realizados",
    "Los secretos de la genealogía",
    "El propósito subyacente",
    "Las incertidumbres del pasado",
    "Los secretos de la familia",
    "Los destinos entrelazados",
    "Las piezas faltantes",
    "La trama de su vida",
    "Las incógnitas personales",
    "Los misterios por resolver",
    "La clave de su existencia pasada",
    "Las revelaciones esperadas",
    "La verdad oculta en su interior",
    "Las metas nunca alcanzadas",
    "El enigma de la herencia",
    "Las incógnitas sin respuesta",
    "Los misterios del camino",
    "Las respuestas en el horizonte",
    "El propósito de su viaje",
    "Las sombras del pasado",
    "Los secretos familiares",
    "Los tesoros escondidos",
    "Las verdades por descubrir",
    "El sentido de la existencia",
    "Los destinos por desvelar"])
    return inicio_historia + " " + medio_historia + ", " + final_historia + "."

def generar_historia_profesion(profesion):
    inicio_historia = random.choice(["Dominó", "Desafió", "Sirvió", "Exploró", "Ganó", "Nadó", "Viajó", "Comió", "Corrió", "Durmió", "Saltó", "Habló", "Escuchó", "Estudió", "Trabajó", "Bebió", "Jugó", "Bailó", "Rió", "Luchó", "Ayudó", "Enseñó", "Lloró", "Pintó", "Caminó", "Aprendió", "Cocinó", "Observó", "Cantó", "Condujo", "Esperó", "Nadó", "Voló", "Robó", "Atrapó", "Silbó", "Escribió", "Compró", "Resolvió", "Abrazó", "Besó", "Miró", "Viajó", "Descubrió", "Disfrutó", "Odió", "Olvidó", "Compartió", "Encontró", "Abordó", "Habló", "Escapó", "Creó", "Cuidó"]) + " como"
    medio_historia = random.choice(["los", "las", "un"]) + " " + profesion
    final_historia = random.choice(["ganando renombre", "salvando vidas", "forjando alianzas", "superando desafíos",    "conquistando reconocimiento",
    "preservando existencias",
    "tejiendo conexiones",
    "venciendo obstáculos",
    "alcanzando notoriedad",
    "protegiendo personas",
    "creando asociaciones",
    "triunfando sobre dificultades",
    "ganando prestigio",
    "rescatando vidas",
    "forjando colaboraciones",
    "superando barreras",
    "estableciendo reputación",
    "cuidando comunidades",
    "construyendo relaciones",
    "dominando desafíos",
    "alcanzando prominencia",
    "garantizando seguridad",
    "negociando alianzas",
    "enfrentando adversidades",
    "consiguiendo fama",
    "salvaguardando bienestar",
    "fortaleciendo lazos",
    "triunfando ante retos",
    "adquiriendo renombre",
    "prolongando vidas",
    "fomentando conexiones",
    "venciendo dificultades",
    "destacando en logros",
    "rescatando almas",
    "creando sociedades",
    "trascendiendo problemas",
    "ganando estatus",
    "proveyendo salvación",
    "construyendo alianzas",
    "enfrentando desafíos",
    "alcanzando excelencia",
    "asegurando supervivencia",
    "forjando colaboraciones duraderas",
    "superando obstáculos",
    "creciendo en notoriedad",
    "salvando vidas preciosas",
    "tejiendo redes",
    "alzándose ante desafíos",
    "estableciendo prestigio",
    "protegiendo a la humanidad",
    "creando uniones beneficiosas",
    "venciendo todas las dificultades",
    "ganando admiración",
    "forjando alianzas sólidas"]) + " " + random.choice(["épicos", "legendarios", "inolvidables", "mágicos","emocionantes", "asombrosos", "extraordinarios", "fantásticos", "maravillosos", "impresionantes", "inigualables", "sobrenaturales", "mitológicos", "sorprendentes", "magníficos", "sublimes", "grandiosos", "inmortales", "épicos", "legendarios", "inolvidables", "mágicos", "fascinantes", "prodigiosos", "deslumbrantes", "sobrecogedores", "inefables", "excepcionales", "memorables", "celestiales", "trascendentales", "impactantes", "formidables", "estelares", "increíbles", "épicos", "legendarios", "inolvidables", "mágicos", "encantadores", "inexplorados", "inesperados", "alucinantes", "enigmáticos", "enriquecedores", "ensoñadores", "arrebatadores", "hipnóticos", "cautivadores", "enérgicos", "apasionantes", "enriquecedores", "inquebrantables", "inspiradores"])
    return inicio_historia + " " + medio_historia + ", " + final_historia + "."

def generar_historia_apellido(apellido):
    inicio_historia = random.choice(["Su apellido", "La historia de su familia", "El linaje de los",    "Tu nombre",
    "La genealogía de tu familia",
    "Historia ancestral de los",
    "Apellido familiar",
    "El legado de tu linaje",
    "Relato de tus antepasados",
    "Explorando tu árbol genealógico",
    "Los orígenes de tu apellido",
    "Herencia familiar",
    "Ancestros y su historia",
    "Rasgos distintivos de tu linaje",
    "Los apellidos y sus raíces",
    "La tradición de tu familia",
    "El pasado de tus parientes",
    "Genealogía y apellidos",
    "Historia de tu apellido",
    "La herencia de tu familia",
    "Linaje ancestral",
    "Tu historia genealógica",
    "Los orígenes de tu familia",
    "Apellidos y su legado",
    "La historia detrás de tu apellido",
    "Raíces familiares",
    "Los antepasados y su legado",
    "Explorando la historia de tu apellido",
    "Ancestralidad familiar",
    "El linaje de tu clan",
    "Tu apellido y su trayectoria",
    "Historia de la ascendencia",
    "La historia de tus parientes",
    "Los ancestros y su influencia",
    "Orígenes de la familia",
    "Apellidos en la historia",
    "La genealogía de tu clan",
    "Registro de apellidos familiares",
    "Los antecedentes de tu apellido",
    "La herencia de tus ancestros",
    "Linaje y tradición familiar",
    "Historia de tu linaje",
    "Explorando tu herencia",
    "El pasado de tu familia",
    "Genealogía de tu ascendencia",
    "Los orígenes de tu linaje",
    "Apellidos y sus raíces",
    "Relato ancestral",
    "Tu apellido a lo largo del tiempo",
    "La historia de tus parientes cercanos",
    "Los ancestros y su legado",
    "La tradición familiar",
    "Rastreando tu historia genealógica"]) + " " + apellido
    final_historia = random.choice(["está lleno de", "ha estado marcado por", "es conocido por","está lleno de", "ha estado marcado por", "es conocido por", "está repleto de", "se caracteriza por", "es famoso por", "abunda en", "está saturado de", "se distingue por", "es célebre por", "está colmado de", "se reconoce por", "es renombrado por", "está abarrotado de", "se destaca por", "es ilustre por", "está atestado de", "se identifica por", "es emblemático por", "está repleto de", "se halla marcado por", "es conocido debido a", "está impregnado de", "se asocia con", "es recordado por", "está relleno de", "se caracteriza por su", "es famoso por su", "abunda en su", "está saturado de su", "se distingue por su", "es célebre por su", "está colmado de su", "se reconoce por su", "es renombrado por su", "está abarrotado de su", "se destaca por su", "es ilustre por su", "está atestado de su", "se identifica por su", "es emblemático por su", "está repleto de su", "se halla marcado por su", "es conocido debido a su", "está impregnado de su", "se asocia con su", "es recordado por su", "está relleno de su", "se caracteriza por la", "es famoso por la"]) + " " + random.choice(["heroicas hazañas", "antiguas leyendas", "poderosos guerreros", "destinos trágicos"])
    return inicio_historia + " " + final_historia + "."

# Generar y mostrar el nombre, apellido y sexo del personaje
nombre_personaje, sexo_personaje = generar_nombre_sexo()
apellido_personaje = generar_apellido()


# Generar y mostrar la profesión del personaje
profesion_personaje = generar_profesion()

# Generar y mostrar el trasfondo épico del personaje
lugar_magico = generar_lugar_magico(sexo_personaje)
transfondo_infancia = generar_transfondo_infancia(sexo_personaje)
tipo_crianza = generar_tipo_crianza(sexo_personaje)
tipo_voluntad = generar_tipo_voluntad(sexo_personaje)
proposito_vida = generar_proposito_vida(sexo_personaje)


# Generar y mostrar los stats del personaje
stats_personaje = generar_stats()

def escribir_info_en_archivo(nombre, apellido, sexo, profesion, lugar_magico, transfondo_infancia, tipo_crianza, tipo_voluntad, proposito_vida, stats):
    with open("personaje.txt", "w") as archivo:
        archivo.write(f"Nombre del personaje: {nombre} ")
        archivo.write(f"Apellido del personaje: {apellido} ")
        archivo.write(f"Sexo del personaje: {sexo} ")
        archivo.write(f"Profesión del personaje: {profesion} ")
        archivo.write(f"{nombre} {apellido}, {generar_historia_lugar(lugar_magico)} {generar_historia_apellido(apellido)} ")
        archivo.write(f"Desde una su infancia en las calles fue {transfondo_infancia} y recibió una {tipo_crianza} que moldeó su carácter de acuerdo a ese evento. ")
        archivo.write(f"Posee experiencia porque el {generar_historia_profesion(profesion)} y ha jurado {proposito_vida}. ")
        archivo.write("Stats del personaje: ")
        nombres_stats = ["Fuerza", "Destreza", "Constitución", "Inteligencia", "Sabiduría", "Carisma"]
        for nombre, valor in zip(nombres_stats, stats):
            archivo.write(f"{nombre}: {valor} ")

# Generar y mostrar el nombre, apellido y sexo del personaje
nombre_personaje, sexo_personaje = generar_nombre_sexo()
apellido_personaje = generar_apellido()

# Generar y mostrar la profesión del personaje
profesion_personaje = generar_profesion()

# Generar y mostrar el trasfondo épico del personaje
lugar_magico = generar_lugar_magico(sexo_personaje)
transfondo_infancia = generar_transfondo_infancia(sexo_personaje)
tipo_crianza = generar_tipo_crianza(sexo_personaje)
tipo_voluntad = generar_tipo_voluntad(sexo_personaje)
proposito_vida = generar_proposito_vida(sexo_personaje)

# Generar y mostrar los stats del personaje
stats_personaje = generar_stats()

# Llamar a la función para escribir la información en el archivo
escribir_info_en_archivo(nombre_personaje, apellido_personaje, sexo_personaje, profesion_personaje, lugar_magico, transfondo_infancia, tipo_crianza, tipo_voluntad, proposito_vida, stats_personaje)

print("Información del personaje guardada en 'personaje.txt'")

# Función para obtener una respuesta sin "Unable to fetch the response, Please try again."
def obtener_respuesta(prompt, chat):
    while True:
        try:
            response = you.Completion.create(
                prompt=prompt,
                chat=chat
            )
            text = response.text.strip()
            if text != "Unable to fetch the response, Please try again.":
                return text
        except Exception as e:
            print(f"Error al obtener respuesta: {e}")
            print("Esperando 10 segundos antes de volver a intentarlo...")
            time.sleep(10)  # Espera 10 segundos antes de intentar nuevamente

# Inicializar el chat vacío
chat = []

# Pedir al usuario la ruta del archivo .txt
archivo_txt = os.path.join(os.getcwd(), "personaje.txt")

try:
    with open(archivo_txt, "r", encoding="utf-8") as archivo_entrada:
        contenido = archivo_entrada.read()
except FileNotFoundError:
    print("El archivo especificado no se encontró.")
    exit()

# Agregar el contenido del archivo al chat
chat.append({"question": contenido, "answer": ""})

# Filtrar el contenido eliminando las líneas del entrevistador
contenido_filtrado = "\n".join([linea for linea in contenido.splitlines() if not linea.strip().startswith("Entrevistador:")])

# Obtener respuesta del modelo
respuesta_bot = obtener_respuesta("lee la informacion que te dare a continuacion y al principio genera un SOLO parrafo con toda la siguiente informacion de seguido: nombre del personaje, el sexo. El personaje puede ser hombre, mujer o no tener genero definido. deja eso al azar. el personaje debe tener caracteristicas de glitch en la cara, e implantes de robot. El personaje quiza podría tener una mascara en la cara de ser necesario pero en la mayoria de casos no. puede ser otro tipo de ser com un adroide o un synth o un ser androgino si el personaje no tiene sexo definido. tambien debe tener un color de piel, la descripcion fisica minuciosa de la cara, los ojos y sus color y forma, su boca y su gesto y la forma de sus orejas y si tinee mascara o no y una descripcion del cuerpo del personaje con detalles unicos que debes inventar al azar segun el background y los stats del personaje, tambien describiendo el traje del personaje segun su profesion, todo esto de manera obligatoria. esto debe ir en un unico parrafo empezando el output, y debe contener tambien la ocupacion y las habilidades y defectos del personaje en ese parrafo unico. Se especifico con esa informacion y formateala de manera que el primer parrafo sea un prompt para una IA que genera arte. Inmediatamente despues del principio, debes generar la informacion general inlcuyendo nombre, edad, profesion, raza alineación y faccion relacionada y las estadisticas de una hoja de rol de un personaje cyberpunk. Eso debe hacerse siguiendo este formato: Nombre:  Genero: Raza: Edad  Profesión:  Alineación moral: Facción: Background (unico y mínimo 500 palabras): Stats del personaje medibles de 1 a 20. Habilidades del personaje (mínimo 10 habilidades medibles de 1 a 20). Hechizos del personaje (mínimo 5 hechizos medibles de 1 a 20). Habilidades (5 talentos, 5 técnicas y 5 conocimientos relevantes). Ventajas (5 disciplinas, 5 trasfondos y 5 virtudes) todo esto debe ser medible de 1 a 20. Genera toda esta información y no sugieras añadir informacion, sino añadela tu, inventatela al azar si es necesario,exportando todo tras el primer parrafo generado en un formato de hoja de personaje de juego de rol que debes optimizar a partir de la informacion que te proporciono y debes hacerlo inventando caracteristicas medibles del 1 al 20 a partir de la informacion imputada a continuacion:  \n\n" + contenido_filtrado, chat)
# Imprimir la respuesta formateada en la consola
respuesta_bot_legible = codecs.decode(respuesta_bot, 'unicode_escape')
print("Bot:", respuesta_bot_legible)

# Guardar la respuesta en un archivo de salida con el formato adecuado
with codecs.open("personaje_con_background.txt", "w", "utf-8") as archivo_respuestas:
    archivo_respuestas.write(respuesta_bot_legible)

print("Hoja de personaje con background guardada en 'personaje_con_background.txt'")

async def main():
    try:
        # Solicitar la ruta del archivo .txt al usuario
        txt_file_path = "personaje_con_background.txt"

        # Leer el contenido del archivo .txt
        with open(txt_file_path, "r") as file:
            prompt = file.read()

        output_folder = os.path.dirname(os.path.abspath(txt_file_path))  # Obtiene la carpeta del archivo .txt

        for i in range(5):
            resp = await getattr(freeGPT, "prodia").Generation().create(prompt) #prodia, pollinations #prodia #pollinations
            image = Image.open(BytesIO(resp))
            image.show()
            
            # Guardar la imagen en la carpeta de salida con un nombre único
            image.save(os.path.join(output_folder, f"imagen_{i}.png"))
            
            print(f"🤖: Imagen {i + 1} mostrada y guardada en la carpeta de salida.")

    except Exception as e:
        print(f"🤖: {e}")

if __name__ == "__main__":
    run(main())
